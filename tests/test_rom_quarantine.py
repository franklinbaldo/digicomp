"""Synthetic only: no unknown programs downloaded, executed, or stored."""
from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path

from tools.rom_quarantine import CustodyError, ingest, verify, main


class QuarantineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "quarentena"
        self.root.mkdir(mode=0o700)
        self.source = self.base / "rom_candidate.bin"
        self.source.write_bytes(b"SYNTHETIC-CONTENT-NOT-A-ROM\x00" * 7)

    def check(self, condition, message):
        if not condition:
            raise AssertionError(message)

    def test_roundtrip_and_metadata(self):
        record = ingest(self.source, self.root, origin="synthetic fixture")
        self.check(record == verify(self.root, record["sha256"]), "round-trip changed metadata")
        self.check(record["executed"] is False, "should not execute")
        self.check(record["provenance_verified"] is False, "should not assert provenance")
        self.check(len(record["sha512"]) == 128, "missing SHA-512")

    def test_repeat_same_bytes_preserves_first_provenance(self):
        first = ingest(self.source, self.root, origin="first receipt")
        second = ingest(self.source, self.root, origin="untrusted duplicate")
        self.check(first == second, "overwrote original receipt")
        self.check(len(list(self.root.glob("*.blob"))) == 1, "duplicate object")

    def test_same_name_different_bytes_distinct_object(self):
        first = ingest(self.source, self.root, origin="first")
        self.source.write_bytes(b"different bytes")
        second = ingest(self.source, self.root, origin="second")
        self.check(first["sha256"] != second["sha256"], "collision in fixture")

    def test_mutation_detected(self):
        record = ingest(self.source, self.root, origin="fixture")
        obj = self.root / (record["sha256"] + ".blob")
        os.chmod(obj, 0o600)
        obj.write_bytes(b"tampered")
        with self.assertRaisesRegex(CustodyError, "differs"):
            verify(self.root, record["sha256"])

    def test_metadata_mutation_detected(self):
        record = ingest(self.source, self.root, origin="fixture")
        meta = self.root / (record["sha256"] + ".json")
        meta.write_text('{"size": 0}', encoding="utf-8")
        with self.assertRaisesRegex(CustodyError, "disagree"):
            verify(self.root, record["sha256"])

    def test_metadata_schema_rejects_silent_upgrade(self):
        record = ingest(self.source, self.root, origin="fixture")
        path = self.root / (record["sha256"] + ".json")
        modified = {**record, "schema": "digicomp-quarantine-v2"}
        path.write_text(json.dumps(modified), encoding="utf-8")
        with self.assertRaisesRegex(CustodyError, "invalid quarantine schema"):
            verify(self.root, record["sha256"])

    def test_metadata_safety_flags_cannot_be_promoted(self):
        record = ingest(self.source, self.root, origin="fixture")
        path = self.root / (record["sha256"] + ".json")
        for field in ("rights_cleared", "provenance_verified", "executed"):
            for value in (True, "false", None):
                with self.subTest(field=field, value=value):
                    modified = dict(record)
                    if value is None:
                        modified.pop(field)
                    else:
                        modified[field] = value
                    path.write_text(json.dumps(modified), encoding="utf-8")
                    with self.assertRaisesRegex(CustodyError, "invalid quarantine safety metadata"):
                        verify(self.root, record["sha256"])
                    with self.assertRaisesRegex(CustodyError, "invalid quarantine safety metadata"):
                        ingest(self.source, self.root, origin="duplicate")
        path.write_text(json.dumps(record), encoding="utf-8")
        self.check(verify(self.root, record["sha256"]) == record, "restored record failed")

    def test_reject_input_symlink(self):
        link = self.base / "linked.bin"
        link.symlink_to(self.source)
        with self.assertRaisesRegex(CustodyError, "symbolic"):
            ingest(link, self.root, origin="fixture")
        self.check(len(list(self.root.iterdir())) == 0, "side effects after denied source")

    def test_reject_fifo(self):
        fifo = self.base / "fifo"
        os.mkfifo(fifo)
        with self.assertRaisesRegex(CustodyError, "regular file"):
            ingest(fifo, self.root, origin="fixture")

    def test_reject_unsafe_permissions(self):
        os.chmod(self.root, 0o755)
        with self.assertRaisesRegex(CustodyError, "group/world"):
            ingest(self.source, self.root, origin="fixture")

    def test_reject_missing_provenance(self):
        with self.assertRaisesRegex(CustodyError, "origin"):
            ingest(self.source, self.root, origin=" ")

    def test_reject_wrong_id(self):
        with self.assertRaisesRegex(CustodyError, "invalid SHA-256"):
            verify(self.root, "../../../etc/passwd")

    def test_cli_roundtrip(self):
        code = main(["ingest", "--source", str(self.source), "--root", str(self.root), "--origin", "fixture"])
        self.check(code == 0, "CLI failed")


    def test_multibyte_origin_at_limit_roundtrips(self):
        origin = "🦀" * 2048
        record = ingest(self.source, self.root, origin=origin)
        self.check(verify(self.root, record["sha256"])["origin_note"] == origin,
                   "valid multibyte origin rejected")

    def test_metadata_fifo_rejected_without_waiting_for_writer(self):
        record = ingest(self.source, self.root, origin="fixture")
        path = self.root / (record["sha256"] + ".json")
        path.unlink()
        os.mkfifo(path)
        with self.assertRaisesRegex(CustodyError, "regular file"):
            verify(self.root, record["sha256"])

    def test_metadata_oversize_rejected_on_verify_and_dedup(self):
        record = ingest(self.source, self.root, origin="fixture")
        path = self.root / (record["sha256"] + ".json")
        path.write_bytes(b" " * 16385)
        with self.assertRaisesRegex(CustodyError, "metadata too large"):
            verify(self.root, record["sha256"])
        with self.assertRaisesRegex(CustodyError, "metadata too large"):
            ingest(self.source, self.root, origin="another")

    def test_metadata_array_is_refused_cleanly(self):
        record = ingest(self.source, self.root, origin="fixture")
        path = self.root / (record["sha256"] + ".json")
        path.write_text('[]', encoding="utf-8")
        with self.assertRaisesRegex(CustodyError, "JSON object"):
            verify(self.root, record["sha256"])

    def test_metadata_size_bool_rejected_even_for_one_byte_object(self):
        self.source.write_bytes(b"x")
        record = ingest(self.source, self.root, origin="fixture")
        path = self.root / (record["sha256"] + ".json")
        path.write_text(json.dumps({**record, "size": True}), encoding="utf-8")
        with self.assertRaisesRegex(CustodyError, "disagree"):
            verify(self.root, record["sha256"])


if __name__ == "__main__":
    unittest.main()
