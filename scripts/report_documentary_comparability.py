#!/usr/bin/env python3
"""Report documentary comparability, without inventing DR-70 fidelity scores.

The evidence unit is a documentary family, not its editions, URLs or house rows.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_DIR = ROOT / "data/output-candidates"
GOLDEN = ROOT / "data/fidelity/observations.json"


def _unique_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON property: {key}")
        result[key] = value
    return result


def _finite_float(value: str) -> float:
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"non-finite JSON number: {value}")
    return number


def _reject_constant(value: str) -> None:
    raise ValueError(f"non-JSON numeric constant: {value}")


def read_json(path: Path) -> dict:
    value = json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=_unique_object,
        parse_constant=_reject_constant,
        parse_float=_finite_float,
    )
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def summarize(entries: list[dict], golden: dict) -> dict:
    """Source accounting only. No candidate becomes a typed angle or measurement."""
    if not isinstance(entries, list) or not all(isinstance(e, dict) for e in entries):
        raise ValueError("catalog entries must be objects")
    observed = golden.get("observations")
    if not isinstance(observed, list):
        raise ValueError("golden observations must be a list")
    ids = set()
    families: dict[str, dict] = {}
    for entry in entries:
        ident, family = entry.get("id"), entry.get("family_id")
        if not isinstance(ident, str) or not ident or ident in ids:
            raise ValueError(f"missing/duplicate catalog id: {ident}")
        ids.add(ident)
        if not isinstance(family, str) or not family.strip():
            raise ValueError(f"missing family for {ident}")
        # Match the candidate/holdout guard's family.strip() identity rule.
        # Editorial aliases with accidental outer whitespace are one family,
        # not independent evidence or additional numeric candidates.
        family = family.strip()
        item = families.setdefault(family, {"catalog_ids": [], "candidate_pairs": {}})
        item["catalog_ids"].append(ident)
        fragments = entry.get("reported_numeric_fragments", [])
        if not isinstance(fragments, list):
            raise ValueError(f"invalid fragment list for {ident}")
        for fragment in fragments:
            if not isinstance(fragment, dict):
                raise ValueError(f"invalid fragment for {ident}")
            pair, groups = fragment.get("pair"), fragment.get("groups")
            if (
                not isinstance(pair, str) or not pair
                or not isinstance(groups, list) or len(groups) != 2
                or not all(isinstance(g, str) and len(g) == 2 and g.isascii()
                           and g.isdigit() for g in groups)
            ):
                raise ValueError(f"non-comparable fragment format for {ident}")
            value = tuple(groups)
            prior = item["candidate_pairs"].setdefault(pair, value)
            if prior != value:
                raise ValueError(
                    f"conflicting editorial readings within family {family}: {pair}"
                )
    by_family = [
        {
            "family_id": name,
            "catalog_ids": sorted(record["catalog_ids"]),
            "candidate_pair_keys": sorted(record["candidate_pairs"]),
            "candidate_pair_count": len(record["candidate_pairs"]),
        }
        for name, record in sorted(families.items())
    ]
    return {
        "classification": "DOCUMENTARY_COVERAGE_NOT_DR70_FIDELITY",
        "catalog_entries": len(entries),
        "distinct_documentary_families": len(by_family),
        "families_with_numeric_group_candidates": sum(
            bool(f["candidate_pair_count"]) for f in by_family
        ),
        "unique_candidate_pairs_within_families": sum(
            f["candidate_pair_count"] for f in by_family
        ),
        "complete_historical_angles_compared": 0,
        "angular_residuals_computed": 0,
        # The corpus list is not provenance-validated here; this is a raw count.
        "fidelity_corpus_records_unvalidated": len(observed),
        "independent_holdout_scores_computed": 0,
        "family_coverage": by_family,
    }


def main() -> int:
    try:
        catalogs = sorted(CATALOG_DIR.glob("*.json"))
        if not catalogs:
            raise ValueError("no catalog shards found")
        entries = []
        for path in catalogs:
            doc = read_json(path)
            if not isinstance(doc.get("entries"), list):
                raise ValueError(f"{path}: entries missing")
            entries.extend(doc["entries"])
        # The separate candidate guard validates eligibility and split leakage.
        # This is a coverage census, not an authorization to compare or publish.
        report = summarize(entries, read_json(GOLDEN))
    except (ValueError, OSError) as error:
        print(f"documentary coverage refused: {error}", file=sys.stderr)
        return 1
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
