"""Sensitivity of modern Campanus house matches to UT and printed coordinates.

This is a MODEL consistency window for four claims from one secondary
editorial transcription, never historical measurement or DR-70 fidelity.
"""

from __future__ import annotations

import importlib
import json
import math

from scripts.carter_historical_house_claims import HOUSE_CLAIMS, compare_houses
from scripts.chart_input_candidates import coordinate, load

START_MINUTE = 10 * 60
END_MINUTE = 16 * 60


def _score(minute: int, latitude: float, longitude: float, swe) -> int:
    """Count categorical matches using true ecliptic latitude for each body."""
    if not START_MINUTE <= minute <= END_MINUTE:
        raise ValueError("Minute outside predeclared 10:00–16:00 UT range")
    jd = swe.julday(1924, 10, 1, minute / 60)
    _, angles = swe.houses_ex(jd, latitude, longitude, b"C", 0)
    true_obliquity = swe.calc_ut(jd, swe.ECL_NUT)[0][0]
    matches = 0
    for name, (expected, _) in HOUSE_CLAIMS.items():
        position, returned_flags = swe.calc_ut(
            jd, getattr(swe, name.upper()), swe.FLG_MOSEPH,
        )
        if not returned_flags & swe.FLG_MOSEPH:
            raise RuntimeError(f"Moshier not returned for {name}")
        fractional = swe.house_pos(
            angles[2], latitude, true_obliquity,
            (position[0], position[1]), b"C",
        )
        if not math.isfinite(fractional) or not 1 <= fractional < 13:
            raise ValueError(f"Invalid house for {name}")
        matches += math.floor(fractional) == expected
    return matches


def _windows(scores: list[int], start: int = START_MINUTE) -> list[list[int]]:
    """Inclusive minute intervals with all four claims matched."""
    intervals = []
    beginning = None
    for index, value in enumerate(scores):
        minute = start + index
        if value == len(HOUSE_CLAIMS) and beginning is None:
            beginning = minute
        if value != len(HOUSE_CLAIMS) and beginning is not None:
            intervals.append([beginning, minute - 1])
            beginning = None
    if beginning is not None:
        intervals.append([beginning, start + len(scores) - 1])
    return intervals


def scan(case: dict, swe) -> dict:
    """Predeclared 1-minute sweep, plus 3×3 ±1′ coordinate controls."""
    original = compare_houses(case, swe)
    if (
        original["utc_interpreted"] != "1924-10-01T13:00:00Z"
        or original["input_variant"] != "DOCUMENTARY_TRANSCRIPTION_13_UT"
    ):
        raise ValueError("Only the transcribed 13:00 UT candidate is admitted")
    latitude = coordinate(case["latitude_as_printed"], "latitude")
    longitude = coordinate(case["longitude_as_printed"], "longitude")
    controls = []
    for lat_delta_arcmin in (-1, 0, 1):
        for lon_delta_arcmin in (-1, 0, 1):
            scores = [
                _score(minute, latitude + lat_delta_arcmin / 60,
                       longitude + lon_delta_arcmin / 60, swe)
                for minute in range(START_MINUTE, END_MINUTE + 1)
            ]
            controls.append({
                "latitude_delta_arcmin": lat_delta_arcmin,
                "longitude_east_delta_arcmin": lon_delta_arcmin,
                "all_four_intervals_inclusive_utc_minutes": _windows(scores),
                "matches_12_00_ut": scores[12 * 60 - START_MINUTE],
                "matches_13_00_ut": scores[13 * 60 - START_MINUTE],
            })
    center = next(
        item for item in controls
        if item["latitude_delta_arcmin"] == item["longitude_east_delta_arcmin"] == 0
    )
    return {
        "classification": "MODERN_CAMPANUS_TIME_ENVELOPE_NOT_HISTORICAL_MEASUREMENT",
        "source_status": original["historical_claim_status"],
        "engine_version": original["engine_version"],
        "editorial_family_count": 1,
        "historical_numeric_residuals": "NOT_RUN_NO_INSPECTED_1980_CHART",
        "dr70_fidelity": "NOT_RUN_NO_GOLDEN",
        "window_scanned_utc_minutes_inclusive": [START_MINUTE, END_MINUTE],
        "resolution_minutes": 1,
        "center_all_four_intervals_utc_minutes_inclusive": center["all_four_intervals_inclusive_utc_minutes"],
        "coordinate_controls": controls,
        "interpretation": "MODEL_CONSISTENCY_WINDOW_NOT_INFERRED_BIRTH_TIME",
    }


def main() -> None:
    swe = importlib.import_module("swisseph")
    cases = [c for c in load()["cases"] if c["id"] == "RAEL1980-CARTER"]
    if len(cases) != 1:
        raise ValueError("Missing or ambiguous Carter input")
    print(json.dumps(scan(cases[0], swe), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
