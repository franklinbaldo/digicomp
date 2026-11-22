"""Compare four historical editorial house claims with MODERN Campanus.

The 1980 claims are visible in a secondary web transcription, not in a
verified facsimile. Swiss Ephemeris/Moshier is an OPTIONAL modern control.
Nothing here authenticates DR-70 computations, prints, or a golden oracle.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
import importlib
import json
import math

from scripts.chart_input_candidates import load
from scripts.compute_chart_reference import calculate

# All four claims come from ONE editorial family. Their agreement is not
# four independent historical witnesses. Lines are web-text, not page numbers.
HOUSE_CLAIMS = {
    "moon": (1, "3843-3848;6117-6121"),
    "mercury": (11, "3843-3849"),
    "pluto": (9, "6117-6121"),
    "uranus": (5, "6117-6121"),
}
TEXT_URL = (
    "https://www.scribd.com/document/633437269/"
    "Dane-Rudhyar-Leyla-Rael-Astrological-Aspects-A-Process-Oriented-"
    "Approach-Rudhyar-Series-Aurora-Press-Inc-2018-pdf"
)


def compare_houses(case: dict, swe) -> dict:
    """Return modern house memberships, with explicit source limitations."""
    if (
        case.get("id") != "RAEL1980-CARTER"
        or case.get("status") != "INPUT_TRANSCRIPTION_UNVERIFIED"
        or case.get("date_as_printed") != "1924-10-01"
        or case.get("latitude_as_printed") != "32N02"
        or case.get("longitude_as_printed") != "84W24"
        or case.get("utc_time_as_printed") not in {"12:00", "13:00"}
        or case.get("observed_chart_values") is not None
    ):
        raise ValueError("Expected Carter documentary input or explicit 12 UT control")

    model = calculate(case, swe)
    if (
        model["classification"] != "MODERN_REFERENCE_NOT_DR70"
        or model["dr70_fidelity"] != "NOT_RUN_NO_GOLDEN"
    ):
        raise ValueError("Modern reference classification required")

    jd = model["julian_day_ut"]
    latitude = model["latitude_deg"]
    longitude = model["longitude_deg_east"]
    _, angles = swe.houses_ex(jd, latitude, longitude, b"C", 0)
    # house_pos requires ARMC and true obliquity, not merely zodiacal cusps.
    true_obliquity = swe.calc_ut(jd, swe.ECL_NUT)[0][0]
    claims = []
    for name, (historical_house, text_lines) in HOUSE_CLAIMS.items():
        ecliptic, flags = swe.calc_ut(jd, getattr(swe, name.upper()), swe.FLG_MOSEPH)
        if not flags & swe.FLG_MOSEPH:
            raise RuntimeError(f"Moshier requested but not returned for {name}")
        # The Moon's latitude is substantial. Do not silently assume zero.
        fractional_house = swe.house_pos(
            angles[2], latitude, true_obliquity,
            (ecliptic[0], ecliptic[1]), b"C",
        )
        if not math.isfinite(fractional_house) or not 1 <= fractional_house < 13:
            raise ValueError(f"Invalid Campanus fractional house for {name}")
        modern_house = math.floor(fractional_house)
        claims.append({
            "body": name,
            "historical_text_house": historical_house,
            "source_text_line_range_not_printed_page": text_lines,
            "modern_campanus_house": modern_house,
            "modern_fractional_house": round(fractional_house, 6),
            "qualitative_match": modern_house == historical_house,
        })

    return {
        "classification": "MODERN_CAMPANUS_VS_SECONDARY_HISTORICAL_HOUSE_PROSE",
        "source": TEXT_URL,
        "historical_claim_status": "INDEXED_SECONDARY_TEXT_NOT_CHECKED_AGAINST_1980_PAGE",
        "input_variant": (
            "DOCUMENTARY_TRANSCRIPTION_13_UT"
            if case["utc_time_as_printed"] == "13:00"
            else "COUNTERFACTUAL_12_UT_NOT_THE_PUBLISHED_INPUT"
        ),
        "utc_interpreted": model["utc_interpreted"],
        "engine_version": model["engine"]["version"],
        "house_method": "Swiss house_pos: Campanus, actual ecliptic latitude",
        "claims": claims,
        "matched_claims": sum(entry["qualitative_match"] for entry in claims),
        "total_claims_same_editorial_family": len(HOUSE_CLAIMS),
        "interpretation": "QUALITATIVE_MODEL_CONSISTENCY_ONLY_NOT_INSTRUMENTAL_VALIDATION",
        "historical_numeric_residuals": "NOT_RUN_NO_INSPECTED_1980_CHART",
        "dr70_fidelity": "NOT_RUN_NO_GOLDEN",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    candidates = [c for c in load()["cases"] if c["id"] == "RAEL1980-CARTER"]
    if len(candidates) != 1:
        parser.error("Missing or ambiguous Carter input")
    swe = importlib.import_module("swisseph")
    original = candidates[0]
    control = deepcopy(original)
    control["utc_time_as_printed"] = "12:00"
    control["time_interpretation"] = "COUNTERFACTUAL: not an observed 1980 input"
    print(json.dumps({
        "published_input": compare_houses(original, swe),
        "one_hour_counterfactual": compare_houses(control, swe),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
