#!/usr/bin/env python3
"""Check documentary candidate catalog and prevent leakage into future holdout."""
import json
import math
import pathlib
import sys

from reconstruction_gate import _IO_LEGIBLE

CATALOG_DIR = pathlib.Path(__file__).resolve().parents[1] / "data/output-candidates"


def _unique_json_properties(pairs):
    """Reject last-wins parsing, including escaped duplicate keys and nested objects."""
    result = {}
    for name, value in pairs:
        if name in result:
            raise ValueError(f"duplicate JSON property: {name!r}")
        result[name] = value
    return result


def _reject_non_json_constant(token):
    """Python's default JSON decoder accepts non-finite numbers; JSON does not."""
    raise ValueError(f"non-JSON numeric constant: {token}")


def _finite_json_float(token):
    """Reject valid JSON exponents whose Python float overflows to infinity."""
    value = float(token)
    if not math.isfinite(value):
        raise ValueError(f"non-finite JSON number: {token}")
    return value


def load_all():
    """Read every shard strictly before validating ID and partition leakage."""
    paths = sorted(CATALOG_DIR.glob("*.json"))
    if not paths:
        raise ValueError("no candidate catalogs")
    entries = []
    for path in paths:
        try:
            data = json.loads(
                path.read_text(encoding="utf-8"),
                object_pairs_hook=_unique_json_properties,
                parse_constant=_reject_non_json_constant,
                parse_float=_finite_json_float,
            )
        except ValueError as exc:
            raise ValueError(f"{path.name}: {exc}") from exc
        entries.extend(data["entries"])
    return {"entries": entries}

SPLITS = {"unassigned", "development", "holdout"}
KINDS = {
    "published_chart_candidate", "device_display_photo", "bibliography_only",
    "report_without_output", "unreadable_visual_lead", "device_session_output",
}


def _has_instrumental_evidence(entry):
    """Structural admission only; a reviewer must authenticate these claims."""
    record = entry.get("instrumental_evidence")
    if not isinstance(record, dict):
        return False
    strings = (
        "device_identifier", "session_locator",
        "independent_reviewer", "independent_review_reference",
    )
    if any(not isinstance(record.get(name), str) or not record[name].strip()
           for name in strings):
        return False
    if any(not isinstance(record.get(name), str)
           or _IO_LEGIBLE.search(record[name]) is None
           for name in ("input_as_entered", "output_literal")):
        return False
    if record.get("output_channel") not in {"display", "printer"}:
        return False
    if not (isinstance(record.get("key_sequence"), list)
            and record["key_sequence"]
            and all(isinstance(key, str) and _IO_LEGIBLE.search(key)
                    for key in record["key_sequence"])):
        return False
    fragments = entry.get("literal_fragments")
    return (
        entry.get("status") == "reviewed"
        and entry.get("attribution") == "device_native_session_output"
        and isinstance(fragments, list)
        and bool(fragments)
        and all(isinstance(fragment, str) and _IO_LEGIBLE.search(fragment)
                and fragment in record["output_literal"]
                for fragment in fragments)
    )


def validate(data):
    errors = []
    entries = data.get("entries")
    if not isinstance(entries, list):
        return ["entries must be a list"]
    ids = set()
    families = {}
    source_regions = {}
    instrument_sessions = {}
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
        if split in {"development", "holdout"}:
            if isinstance(family, str):
                families.setdefault(family, set()).add(split)
            source_url, locator = entry.get("source_url"), entry.get("locator")
            if isinstance(source_url, str) and isinstance(locator, str):
                if source_url.strip() and locator.strip():
                    region = (source_url.strip(), locator.strip())
                    source_regions.setdefault(region, set()).add(split)
            # The same instrument session cannot be both training and holdout,
            # even if a publisher uses another URL, locator, or family label.
            # This is a declared identity, not independent authentication.
            evidence = entry.get("instrumental_evidence")
            if isinstance(evidence, dict):
                device = evidence.get("device_identifier")
                session = evidence.get("session_locator")
                if (isinstance(device, str) and device.strip()
                        and isinstance(session, str) and session.strip()):
                    session_key = (device.strip(), session.strip())
                    instrument_sessions.setdefault(session_key, set()).add(split)
        if split == "holdout":
            required = ("replayable", "input_complete", "output_complete", "numeric_holdout_eligible")
            if any(entry.get(field) is not True for field in required):
                errors.append(f"{ident}: holdout without complete, reviewed replayable input/output")
            if entry.get("kind") != "device_session_output":
                errors.append(f"{ident}: holdout source must be actual device session")
            if not _has_instrumental_evidence(entry):
                errors.append(f"{ident}: holdout missing instrumental evidence and independent review")
        if entry.get("numeric_holdout_eligible") is True and (
            entry.get("kind") != "device_session_output"
            or entry.get("replayable") is not True
            or entry.get("input_complete") is not True
            or entry.get("output_complete") is not True
            or not _has_instrumental_evidence(entry)
        ):
            errors.append(f"{ident}: numeric holdout eligibility unsupported")
    for family, splits in families.items():
        if len(splits) > 1:
            errors.append(f"family leakage across development/holdout: {family}")
    for (url, locator), splits in source_regions.items():
        if len(splits) > 1:
            errors.append(f"source locator leakage across development/holdout: {url} @ {locator}")
    for (device, session), splits in instrument_sessions.items():
        if len(splits) > 1:
            errors.append(f"instrument session leakage across development/holdout: {device} @ {session}")
    return errors


if __name__ == "__main__":
    errors = validate(load_all())
    if errors:
        print("\n".join(errors), file=sys.stderr)
        raise SystemExit(1)
    print("PASS catalog structural/partition checks; NOT a fidelity or authenticity test")
