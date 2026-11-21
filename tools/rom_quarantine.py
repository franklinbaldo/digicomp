"""Offline, no-execution intake of candidate historical firmware.

Experimental custody helper, NOT a forensic write blocker, malware sandbox,
immutable store, or an authenticity/rights determination.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import secrets
import stat
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

_CHUNK = 1024 * 1024
_METADATA_MAX = 16384  # Allow up to 2048 multibyte origin characters in v1 JSON.
_V1_FIELDS = frozenset({
    "schema", "sha256", "sha512", "size", "origin_note",
    "original_basename", "ingested_at_utc",
    "provenance_verified", "rights_cleared", "executed",
})


class CustodyError(RuntimeError):
    pass


def _valid_utf8_text(value: str) -> bool:
    # json.loads accepts escaped lone surrogates, which cannot be written as UTF-8.
    try:
        value.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def _regular_fd(path: Path) -> int:
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NONBLOCK", 0)
    if path.is_symlink():
        raise CustodyError("symbolic links are not admitted")
    fd = os.open(path, flags)
    if not stat.S_ISREG(os.fstat(fd).st_mode):
        os.close(fd)
        raise CustodyError("source must be a regular file")
    return fd


def _digest_fd(fd: int) -> tuple[int, str, str]:
    sha256 = hashlib.sha256()
    sha512 = hashlib.sha512()
    size = 0
    while True:
        data = os.read(fd, _CHUNK)
        if not data:
            break
        sha256.update(data)
        sha512.update(data)
        size += len(data)
    return size, sha256.hexdigest(), sha512.hexdigest()


def _object_path(root: Path, digest: str) -> Path:
    if len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
        raise CustodyError("invalid SHA-256 object ID")
    return root / (digest + ".blob")


def _root(root: Path) -> Path:
    if root.is_symlink() or not root.is_dir():
        raise CustodyError("quarantine root must be an existing non-symlink directory")
    resolved = root.resolve(strict=True)
    if stat.S_IMODE(resolved.stat().st_mode) & 0o077:
        raise CustodyError("quarantine root must not be group/world accessible")
    return resolved


def _reject_duplicate_json_keys(pairs: list[tuple[str, object]]) -> dict:
    """Do not let JSON's last-wins semantics erase conflicting custody claims."""
    record = {}
    for key, value in pairs:
        if key in record:
            raise CustodyError(f"duplicate quarantine metadata key: {key}")
        record[key] = value
    return record


def _reject_nonfinite_metadata_constant(value: str) -> None:
    """The Python JSON decoder otherwise admits NaN/Infinity, unlike JSON."""
    raise CustodyError(f"non-finite quarantine metadata constant: {value}")


def _read_metadata(path: Path) -> dict:
    # Do not follow a swapped symlink or block on a FIFO/device. Bound the JSON
    # read even if a writer grows the file between fstat() and read().
    fd = _regular_fd(path)
    try:
        with os.fdopen(fd, "rb") as stream:
            fd = -1
            if os.fstat(stream.fileno()).st_size > _METADATA_MAX:
                raise CustodyError("quarantine metadata too large")
            data = stream.read(_METADATA_MAX + 1)
    finally:
        if fd != -1:
            os.close(fd)
    if len(data) > _METADATA_MAX:
        raise CustodyError("quarantine metadata too large")
    record = json.loads(
        data,
        object_pairs_hook=_reject_duplicate_json_keys,
        parse_constant=_reject_nonfinite_metadata_constant,
    )
    if not isinstance(record, dict):
        raise CustodyError("quarantine metadata must be a JSON object")
    return record


def _check_provenance_fields(record: dict) -> None:
    # V1 is a closed schema. Unknown fields must not carry unreviewed
    # assertions such as "authentic": true while verification returns PASS.
    if set(record) != _V1_FIELDS:
        raise CustodyError("invalid quarantine v1 metadata fields")
    origin = record["origin_note"]
    if (
        not isinstance(origin, str)
        or not origin.strip()
        or len(origin) > 2048
        or not _valid_utf8_text(origin)
    ):
        raise CustodyError("invalid quarantine provenance text: origin_note")
    basename = record["original_basename"]
    if (
        not isinstance(basename, str)
        or not basename
        or basename in (".", "..")
        or "/" in basename
        or chr(0) in basename
        or not _valid_utf8_text(basename)
    ):
        raise CustodyError("invalid quarantine provenance text: original_basename")
    stamp = record["ingested_at_utc"]
    if not isinstance(stamp, str):
        raise CustodyError("invalid quarantine UTC timestamp")
    try:
        parsed = datetime.fromisoformat(stamp)
    except ValueError as exc:
        raise CustodyError("invalid quarantine UTC timestamp") from exc
    if parsed.utcoffset() != timedelta(0):
        raise CustodyError("invalid quarantine UTC timestamp")


def verify(root: Path, sha256: str) -> dict:
    root = _root(root)
    path = _object_path(root, sha256)
    fd = _regular_fd(path)
    try:
        size, actual256, actual512 = _digest_fd(fd)
    finally:
        os.close(fd)
    if actual256 != sha256:
        raise CustodyError("stored content differs from its SHA-256 object ID")
    manifest_path = root / (sha256 + ".json")
    record = _read_metadata(manifest_path)
    if (
        record.get("sha256") != actual256
        or record.get("sha512") != actual512
        or type(record.get("size")) is not int
        or record.get("size") != size
    ):
        raise CustodyError("metadata and content disagree")
    # Hash fixity alone must not promote an unverified candidate to trusted.
    if record.get("schema") != "digicomp-quarantine-v1":
        raise CustodyError("invalid quarantine schema")
    for field in ("provenance_verified", "rights_cleared", "executed"):
        if record.get(field) is not False:
            raise CustodyError(f"invalid quarantine safety metadata: {field}")
    _check_provenance_fields(record)
    return record


def ingest(source: Path, root: Path, *, origin: str) -> dict:
    if not isinstance(origin, str) or not origin.strip() or not _valid_utf8_text(origin):
        raise CustodyError("origin/provenance must be valid nonempty UTF-8 text")
    if not _valid_utf8_text(source.name):
        raise CustodyError("invalid quarantine provenance text: original_basename")
    root = _root(root)
    if len(origin) > 2048:
        raise CustodyError("origin note too long")
    fd = _regular_fd(source)
    temp = root / (".ingest-" + secrets.token_hex(12))
    staged = False
    try:
        before = os.fstat(fd)
        sink_fd = os.open(temp, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        staged = True
        try:
            digest256, digest512 = hashlib.sha256(), hashlib.sha512()
            size = 0
            while True:
                chunk = os.read(fd, _CHUNK)
                if not chunk:
                    break
                digest256.update(chunk)
                digest512.update(chunk)
                size += len(chunk)
                view = memoryview(chunk)
                while view:
                    written = os.write(sink_fd, view)
                    if written == 0:
                        raise CustodyError("short write")
                    view = view[written:]
            os.fsync(sink_fd)
        finally:
            os.close(sink_fd)
        after = os.fstat(fd)
        if (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns, before.st_ctime_ns) != (
            after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns, after.st_ctime_ns
        ) or size != before.st_size:
            raise CustodyError("source changed during read; snapshot refused")
        checksum = digest256.hexdigest()
        target = _object_path(root, checksum)
        record = {
            "schema": "digicomp-quarantine-v1",
            "sha256": checksum,
            "sha512": digest512.hexdigest(),
            "size": size,
            "origin_note": origin,
            "original_basename": source.name,
            "ingested_at_utc": datetime.now(timezone.utc).isoformat(),
            "provenance_verified": False,
            "rights_cleared": False,
            "executed": False,
        }
        manifest = root / (checksum + ".json")
        # Hard-link publication is exclusive: a second writer cannot replace a blob.
        try:
            os.link(temp, target, follow_symlinks=False)
        except FileExistsError:
            if not manifest.is_file():
                raise CustodyError("object exists without complete metadata")
            existing = verify(root, checksum)
            if existing["sha512"] != record["sha512"]:
                raise CustodyError("hash mismatch with existing object")
            return existing
        # The staged name and final name reference the same bytes.
        os.chmod(target, 0o400)  # permission barrier only, NOT immutable
        metadata_tmp = root / (".metadata-" + secrets.token_hex(12))
        try:
            with metadata_tmp.open("x", encoding="utf-8") as stream:
                json.dump(record, stream, indent=2, ensure_ascii=False, sort_keys=True)
                stream.write("\n")
                stream.flush()
                os.fsync(stream.fileno())
            # Exclusive publish: never silently replace provenance metadata.
            os.link(metadata_tmp, manifest, follow_symlinks=False)
        finally:
            metadata_tmp.unlink(missing_ok=True)
        dirfd = os.open(root, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
        try:
            os.fsync(dirfd)
        finally:
            os.close(dirfd)
        return verify(root, checksum)
    finally:
        os.close(fd)
        if staged:
            temp.unlink(missing_ok=True)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    a = sub.add_parser("ingest", help="copy bytes into offline quarantine; never execute them")
    a.add_argument("--source", type=Path, required=True)
    a.add_argument("--root", type=Path, required=True)
    a.add_argument("--origin", required=True, help="who/where supplied the bytes; unknown is permitted")
    b = sub.add_parser("verify", help="recompute two hashes and compare to recorded values")
    b.add_argument("--root", type=Path, required=True)
    b.add_argument("--sha256", required=True)
    opts = parser.parse_args(argv)
    try:
        result = ingest(opts.source, opts.root, origin=opts.origin) if opts.command == "ingest" else verify(opts.root, opts.sha256)
    except (CustodyError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"QUARANTINE_REFUSED: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
