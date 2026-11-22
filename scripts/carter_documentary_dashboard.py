"""Two distinct Carter documentary comparisons, never a DR-70 golden.

2023: published modern angular positions versus modern Swiss/Moshier.
1980: four historical categorical house claims from one secondary text,
versus modern Campanus at the printed 13 UT and counterfactual 12 UT.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
import importlib
import json

from scripts.carter_historical_house_claims import HOUSE_CLAIMS, compare_houses
from scripts.carter_modern_table import FIELDS, load_control, report as modern_report, render as render_modern
from scripts.chart_input_candidates import load
from scripts.compute_chart_reference import calculate

HISTORICAL_STATUS = "INDEXED_SECONDARY_TEXT_NOT_CHECKED_AGAINST_1980_PAGE"
HISTORICAL_CLASS = "MODERN_CAMPANUS_VS_SECONDARY_HISTORICAL_HOUSE_PROSE"


def assemble(modern: dict, historical: dict, counterfactual: dict) -> dict:
    """Keep numerical modern checks distinct from categorical historical checks."""
    if (
        modern.get("case_id") != "RAEL1980-CARTER"
        or modern.get("historical") != "NOT_RUN_NO_INSPECTED_1980_NUMBERS"
        or modern.get("dr70") != "NOT_RUN_NO_GOLDEN"
        or modern.get("compared") != len(FIELDS)
        or len(modern.get("rows", [])) != len(FIELDS)
        or {r.get("field") for r in modern["rows"]} != set(FIELDS)
        or modern.get("within_tolerance") != sum(r.get("within_declared_tolerance") is True for r in modern["rows"])
    ):
        raise ValueError("Modern result must retain its nine-field 2023 scope")
    for record, variant, ut in (
        (historical, "DOCUMENTARY_TRANSCRIPTION_13_UT", "1924-10-01T13:00:00Z"),
        (counterfactual, "COUNTERFACTUAL_12_UT_NOT_THE_PUBLISHED_INPUT", "1924-10-01T12:00:00Z"),
    ):
        claims = record.get("claims", [])
        if (
            record.get("classification") != HISTORICAL_CLASS
            or record.get("historical_claim_status") != HISTORICAL_STATUS
            or record.get("historical_numeric_residuals") != "NOT_RUN_NO_INSPECTED_1980_CHART"
            or record.get("dr70_fidelity") != "NOT_RUN_NO_GOLDEN"
            or record.get("input_variant") != variant
            or record.get("utc_interpreted") != ut
            or record.get("total_claims_same_editorial_family") != len(HOUSE_CLAIMS)
            or len(claims) != len(HOUSE_CLAIMS)
            or {r.get("body") for r in claims} != set(HOUSE_CLAIMS)
            or record.get("matched_claims") != sum(r.get("qualitative_match") is True for r in claims)
            or any(r.get("historical_text_house") != HOUSE_CLAIMS[r["body"]][0] for r in claims)
            or any(r.get("modern_campanus_house") not in range(1, 13) for r in claims)
            or any(r.get("qualitative_match") is not (r["historical_text_house"] == r["modern_campanus_house"]) for r in claims)
        ):
            raise ValueError("Invalid historical house comparison classification or data")
    if historical.get("source") != counterfactual.get("source"):
        raise ValueError("Both historical variants must refer to one editorial source")
    by_body = {entry["body"]: entry for entry in counterfactual["claims"]}
    rows = []
    for entry in historical["claims"]:
        control = by_body[entry["body"]]
        if control["historical_text_house"] != entry["historical_text_house"]:
            raise ValueError("Counterfactual must compare the same published claim")
        rows.append({
            "body": entry["body"],
            "historical_prose_house": entry["historical_text_house"],
            "computed_13_ut": entry["modern_campanus_house"],
            "computed_12_ut": control["modern_campanus_house"],
            "match_13_ut": entry["qualitative_match"],
            "match_12_ut": control["qualitative_match"],
            "source_text_line_range_not_page": entry["source_text_line_range_not_printed_page"],
        })
    return {
        "classification": "DOCUMENTARY_TWO_TIER_RESEARCH_OUTPUT_NOT_DR70_FIDELITY",
        "case_id": "RAEL1980-CARTER",
        "modern_2023": modern,
        "historical_house_prose": {
            "source": historical["source"],
            "source_status": HISTORICAL_STATUS,
            "independent_editorial_families": 1,
            "rows": rows,
            "matches_13_ut": historical["matched_claims"],
            "matches_12_ut_counterfactual": counterfactual["matched_claims"],
            "total_claims": len(rows),
            "precision": "CATEGORIES_NOT_ANGULAR_RESIDUALS",
        },
        "historical_chart_numeric_comparison": "NOT_RUN_NO_INSPECTED_1980_CHART",
        "dr70_instrumental_comparison": "NOT_RUN_NO_GOLDEN",
    }


def render(data: dict) -> str:
    """Produce a human-readable output without implying independent goldens."""
    if data.get("classification") != "DOCUMENTARY_TWO_TIER_RESEARCH_OUTPUT_NOT_DR70_FIDELITY":
        raise ValueError("Not the documentary dashboard result")
    history = data["historical_house_prose"]
    lines = [render_modern(data["modern_2023"]), "", "=== 1980 EDITORIAL HOUSE PROSE (SECONDARY TEXT) ===",
             "One editorial family; no inspected 1980 chart or instrumental numbers",
             "13 UT is transcribed; 12 UT is a counterfactual, NOT a second historical source",
             "", f'{"Body":<10} {"Text house":>10} {"13 UT modern":>13} {"12 UT modern":>13}  13 UT status']
    for row in history["rows"]:
        status = "MATCH" if row["match_13_ut"] else "MISMATCH"
        lines.append(f'{row["body"]:<10} {row["historical_prose_house"]:>10} {row["computed_13_ut"]:>13} {row["computed_12_ut"]:>13}  {status}')
    lines.extend(["", f'Historical-category consistency at 13 UT: {history["matches_13_ut"]}/{history["total_claims"]}',
                  f'At 12 UT counterfactual: {history["matches_12_ut_counterfactual"]}/{history["total_claims"]}',
                  "Non-unique: four houses do not determine a single birth time",
                  f'Historical printed angular comparison: {data["historical_chart_numeric_comparison"]}',
                  f'DR-70 instrument fidelity: {data["dr70_instrumental_comparison"]}',
                  f'Secondary source: {history["source"]}'])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    swe = importlib.import_module("swisseph")
    cases = [c for c in load()["cases"] if c["id"] == "RAEL1980-CARTER"]
    if len(cases) != 1:
        raise ValueError("Missing or ambiguous Carter source input")
    original = cases[0]
    control = deepcopy(original)
    control["utc_time_as_printed"] = "12:00"
    control["time_interpretation"] = "COUNTERFACTUAL: not an observed 1980 input"
    combined = assemble(modern_report(load_control(), calculate(original, swe)),
                        compare_houses(original, swe), compare_houses(control, swe))
    print(json.dumps(combined, ensure_ascii=False, indent=2) if args.format == "json" else render(combined))


if __name__ == "__main__":
    main()
