#!/usr/bin/env python3
"""Check documentary candidate catalog and prevent leakage into future holdout."""
import json
import pathlib
import sys

PATH = pathlib.Path(__file__).resolve().parents[1] / "data/output-candidates/catalog.json"
SPLITS = {"unassigned", "development", "holdout"}
KINDS = {
    "published_chart_candidate", "device_display_photo", "bibliography_only",
    "report_without_output", "unreadable_visual_lead", "device_session_output",
}


def validate(data):
    errors = []
    entries = data.get("entries")
    if not isinstance(entries, list):
        return ["entries must be a list"]
    ids = set()
    families = {}
    for i, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"entry {i} is not an object")
            continue
        ident = entry.get("id")
        family = entry.get("family_id")
        split = entry.get("sample_split")
        if not isinstance(ident, str) or not ident:
            errors.append(f"entry {i}: missing id")
        elif ident in ids:
            errors.append(f"duplicate id: {ident}")
        ids.add(ident)
        if not isinstance(family, str) or not family:
            errors.append(f"{ident}: missing provenance family")
        if split not in SPLITS:
            errors.append(f"{ident}: invalid split")
        if entry.get("kind") not in KINDS:
            errors.append(f"{ident}: invalid kind")
        if not isinstance(entry.get("source_url"), str) or not entry["source_url"].startswith("https://"):
            errors.append(f"{ident}: source needs HTTPS URL")
        if not isinstance(entry.get("locator"), str) or not entry["locator"].strip():
            errors.append(f"{ident}: missing exact locator")
        if not isinstance(entry.get("literal_fragments"), list):
            errors.append(f"{ident}: literals must be a list")
        if split in {"development", "holdout"} and isinstance(family, str):
            families.setdefault(family, set()).add(split)
        if split == "holdout":
            required = ("replayable", "input_complete", "output_complete", "numeric_holdout_eligible")
            if any(entry.get(field) is not True for field in required):
                errors.append(f"{ident}: holdout without complete, reviewed replayable input/output")
            if entry.get("kind") != "device_session_output":
                errors.append(f"{ident}: holdout source must be actual device session")
        if entry.get("numeric_holdout_eligible") is True and (
            entry.get("kind") != "device_session_output"
            or entry.get("replayable") is not True
            or entry.get("input_complete") is not True
            or entry.get("output_complete") is not True
        ):
            errors.append(f"{ident}: numeric holdout eligibility unsupported")
    for family, splits in families.items():
        if len(splits) > 1:
            errors.append(f"family leakage across development/holdout: {family}")
    return errors


if __name__ == "__main__":
    errors = validate(json.loads(PATH.read_text(encoding="utf-8")))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        raise SystemExit(1)
    print("PASS catalog structural/partition checks; NOT a fidelity or authenticity test")
