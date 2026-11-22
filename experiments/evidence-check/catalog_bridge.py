"""Traceability check: Carlson layout probe versus canonical documentary catalog.

This is NOT a second reading, ephemeris comparison, or a DR-70 fidelity test.
The catalog and the probe share a documentary source and can drift together.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "data/output-candidates/catalog.json"
PAIRS = ROOT / "experiments/evidence-check/published-pairs.tsv"
ID = "OUT-CARLSON-F83"
FAMILY = "CARLSON-FIG1-1983-1985"
SOURCE_URL = "https://escholarship.org/content/qt0b40b045/qt0b40b045.pdf"


class CatalogDrift(ValueError):
    """Candidate probe and canonical catalog no longer agree."""


def _require(condition: bool, detail: str) -> None:
    if not condition:
        raise CatalogDrift(detail)


def _unique_object(pairs: list[tuple[str, object]]) -> dict:
    result: dict = {}
    for key, value in pairs:
        _require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise CatalogDrift(f"non-JSON numeric constant: {value}")


def check(catalog_text: str, pairs_text: str) -> str:
    """Cross-check exact candidate groups, provenance and holdout boundaries."""
    try:
        catalog = json.loads(catalog_text, object_pairs_hook=_unique_object, parse_constant=_reject_constant)
    except (ValueError, TypeError) as error:
        raise CatalogDrift(f"invalid catalog JSON: {error}") from error
    _require(isinstance(catalog, dict) and catalog.get("format_version") == "0.1", "unsupported catalog schema")
    entries = catalog.get("entries")
    _require(isinstance(entries, list), "missing catalog entries")
    matches = [entry for entry in entries if isinstance(entry, dict) and entry.get("id") == ID]
    _require(len(matches) == 1, "exactly one F83 catalog record required")
    f83 = matches[0]
    _require(f83.get("family_id") == FAMILY, "F83 family drift")
    _require(f83.get("source_url") == SOURCE_URL, "F83 source URL drift")
    _require("printed p. -24-" in str(f83.get("locator", "")), "F83 printed-page locator drift")
    _require(f83.get("related_ledger") == "docs/carlson-fig1-token-ledger.md", "F83 ledger drift")
    _require(f83.get("raw_excerpt_status") == "secondary_transcription_pending_image_recheck", "unreviewed source status promotion")
    _require(f83.get("status") == "candidate" and f83.get("kind") == "published_chart_candidate", "F83 candidate status drift")
    _require(f83.get("attribution") == "attributed_calculations_not_native_output", "F83 instrument attribution promotion")
    for flag in ("input_complete", "output_complete", "replayable", "numeric_holdout_eligible"):
        _require(f83.get(flag) is False, f"F83 {flag} must remain false pending new evidence")
    _require(f83.get("sample_split") == "unassigned", "F83 cannot be promoted to a holdout by this probe")
    f85 = [entry for entry in entries if isinstance(entry, dict) and entry.get("id") == "OUT-CARLSON-F85"]
    _require(len(f85) == 1 and f85[0].get("family_id") == FAMILY, "F85 editorial family is not independent")
    _require(f85[0].get("numeric_holdout_eligible") is False, "F85 cannot be used as independent holdout")
    _require(f85[0].get("sample_split") == "unassigned", "F85 cannot be assigned a separate holdout split")
    _require(
        f85[0].get("attribution") == "attributed_calculations_not_native_output"
        and f85[0].get("kind") == "published_chart_candidate"
        and f85[0].get("status") == "candidate",
        "F85 remains an editorial candidate, not native DR-70 output",
    )
    for flag in ("input_complete", "output_complete", "replayable"):
        _require(f85[0].get(flag) is False, f"F85 {flag} must remain false pending independent evidence")

    reported = f83.get("reported_numeric_fragments")
    _require(isinstance(reported, list) and len(reported) == 6, "F83 catalog requires six candidate pairs")
    records: dict[str, list[str]] = {}
    for item in reported:
        _require(isinstance(item, dict), "invalid canonical pair item")
        key, groups = item.get("pair"), item.get("groups")
        _require(isinstance(key, str) and key not in records, "duplicate/invalid canonical pair")
        _require(
            isinstance(groups, list) and len(groups) == 2
            and all(isinstance(g, str) and len(g) == 2 and g.isascii() and g.isdigit() for g in groups),
            "invalid canonical digit groups",
        )
        records[key] = groups
    parsed = []
    for raw in pairs_text.splitlines():
        if not raw or raw.startswith("#"):
            continue
        fields = raw.split("\t")
        _require(len(fields) == 6, "six TSV columns required")
        parsed.append(fields)
    _require(len(parsed) == 6, "six TSV house pairs required")
    for i, fields in enumerate(parsed, start=1):
        left, right, l1, l2, r1, r2 = fields
        _require(left == f"H{i:02}" and right == f"H{i+6:02}", "TSV house-pair sequence drift")
        key = f"{left}/{right}"
        _require(key in records, f"missing canonical catalog pair {key}")
        _require([l1, l2] == records[key], f"left TSV groups differ from canonical catalog for {key}")
        _require(
            [r1, r2] == records[key],
            f"right TSV groups differ from canonical candidate for {key}; review source before updating baseline",
        )
    _require(len(records) == len(parsed), "canonical pair-set mismatch")
    return (
        "CATALOG_TRACEABILITY_NOT_INDEPENDENT_VALIDATION\n"
        f"catalog_id={ID}\n"
        f"documentary_family={FAMILY}\n"
        "candidate_pairs_crosschecked=6\n"
        "independent_transcriptions=0\n"
        "complete_published_angles=0\n"
        "device_fidelity=NOT_RUN_NO_GOLDEN\n"
    )


def main() -> None:
    print(check(CATALOG.read_text(encoding="utf-8"), PAIRS.read_text(encoding="utf-8")), end="")


if __name__ == "__main__":
    main()
