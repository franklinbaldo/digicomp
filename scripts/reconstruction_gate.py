"""Conservative triage for future DR-70 reconstruction, not authentication.

Uses only caller-supplied evidence metadata and never reads or executes firmware.
All positive results remain hypotheses requiring independent human review.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

_SHA256 = re.compile(r"[0-9a-f]{64}\Z")


def _present(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _record(value: object, required: tuple[str, ...]) -> bool:
    return isinstance(value, dict) and all(_present(value.get(k)) for k in required)


def _firmware(value: object) -> bool:
    return (
        _record(value, ("evidence_id", "locator", "sha256"))
        and bool(_SHA256.fullmatch(value["sha256"]))
        and value.get("custody_reviewed") is True
        and value.get("analysis_permitted") is True
    )


def _architecture(value: object) -> bool:
    return (
        _record(value, ("evidence_id", "isa", "address_mapping", "byte_order", "peripheral_evidence_id"))
        and value.get("independently_corroborated") is True
    )


def _observed_io(value: object) -> bool:
    """A candidate is not proof; a source must be independently inspected."""
    return (
        _record(value, ("id", "evidence_id", "locator", "input_literal", "keys_literal", "output_literal"))
        and isinstance(value.get("directness"), str)
        and value.get("directness") in {"device_observation", "contemporaneous_report"}
        and value.get("source_reviewed") is True
        and value.get("synthetic") is False
    )


def _count_distinct_io_candidates(records: list[object]) -> int:
    """Reject duplicate candidate IDs and cited regions before counting.

    Identical source regions are not additional observations. Different regions
    can still belong to the same device session; this is only a literal guard.
    """
    seen_ids: set[str] = set()
    seen_regions: set[tuple[str, str]] = set()
    count = 0
    for item in records:
        if not _observed_io(item):
            continue
        identifier = item["id"]
        region = (item["evidence_id"], item["locator"])
        if identifier in seen_ids:
            raise ValueError(f"duplicate candidate IO id {identifier!r}")
        if region in seen_regions:
            raise ValueError(f"duplicate candidate IO evidence region {region!r}")
        seen_ids.add(identifier)
        seen_regions.add(region)
        count += 1
    return count


def evaluate(metadata: object) -> dict[str, object]:
    """Classify *research tracks*, never authorize release or use of an emulator."""
    if not isinstance(metadata, dict):
        raise ValueError("evidence metadata must be a JSON object")
    firmware_ok = _firmware(metadata.get("firmware"))
    architecture_ok = _architecture(metadata.get("architecture"))
    raw_observations = metadata.get("observations", [])
    if not isinstance(raw_observations, list):
        raise ValueError("observations must be a list")
    io_cases = _count_distinct_io_candidates(raw_observations)
    if firmware_ok and architecture_ok:
        track = "A_INSTRUCTION_STUDY"
    elif io_cases:
        track = "B_BEHAVIOR_STUDY"
    else:
        track = "C_DOCUMENTATION"
    return {
        "track": track,
        "firmware_metadata_complete": firmware_ok,
        "architecture_metadata_complete": architecture_ok,
        "candidate_io_cases": io_cases,
        "approved_for_emulation": False,
        "approved_as_authentic_dr70": False,
        "note": "Metadata triage only: verify artifact, rights, independence and actual hardware/replay externally.",
    }


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print("usage: python3 scripts/reconstruction_gate.py metadata.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(args[0]).read_text(encoding="utf-8"))
        result = evaluate(data)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
