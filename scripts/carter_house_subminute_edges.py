"""One-second sampling and bracket refinement of Carter modern house classes.

This measures MODEL consistency with a single secondary editorial family.
It does not infer birth time or authenticate historical DR-70 output.
"""

from __future__ import annotations

import importlib
import json

from scripts.carter_house_time_envelope import (
    START_MINUTE, END_MINUTE, _score, _windows, scan,
)
from scripts.chart_input_candidates import coordinate, load


SECONDS_PER_MINUTE = 60


def _refine_edge(left_second: int, right_second: int, before: int,
                 after: int, latitude: float, longitude: float, swe) -> float:
    """Bracket an observed score change to 0.01 second within a 1s cell."""
    if right_second - left_second != 1:
        raise ValueError("Expected adjacent sampled seconds")
    score = lambda second: _score(second / SECONDS_PER_MINUTE,
                                  latitude, longitude, swe)
    if score(left_second) != before or score(right_second) != after:
        raise ValueError("No claimed edge in sample cell")
    lo, hi = float(left_second), float(right_second)
    while hi - lo > 0.01:
        mid = (lo + hi) / 2
        if score(mid) == before:
            lo = mid
        elif score(mid) == after:
            hi = mid
        else:
            raise ValueError("Unexpected third class within boundary bracket")
    return round((lo + hi) / 2, 2)


def analyze(case: dict, swe) -> dict:
    """Exhaust 1s samples over the same 10:00–16:00 UT predeclared range."""
    minute_scan = scan(case, swe)  # Includes source/entry/golden controls.
    if minute_scan["center_all_four_intervals_utc_minutes_inclusive"] != [[755, 843]]:
        raise ValueError("Minute baseline changed; reconsider edge assumptions")
    lat = coordinate(case["latitude_as_printed"], "latitude")
    lon = coordinate(case["longitude_as_printed"], "longitude")
    start = START_MINUTE * SECONDS_PER_MINUTE
    end = END_MINUTE * SECONDS_PER_MINUTE
    scores = [_score(second / SECONDS_PER_MINUTE, lat, lon, swe)
              for second in range(start, end + 1)]
    windows = _windows(scores, start=start)
    if len(windows) != 1 or not (start < windows[0][0] <= windows[0][1] < end):
        raise ValueError("No unique internal 1-second grid window")
    first, last = windows[0]
    entry = _refine_edge(first - 1, first, scores[first - 1 - start], 4,
                         lat, lon, swe)
    exit_ = _refine_edge(last, last + 1, 4, scores[last + 1 - start],
                         lat, lon, swe)
    return {
        "classification": "MODERN_CAMPANUS_SECOND_GRID_NOT_HISTORICAL_MEASUREMENT",
        "source_status": minute_scan["source_status"],
        "editorial_family_count": 1,
        "engine_version": minute_scan["engine_version"],
        "scanned_utc_seconds_of_day_inclusive": [start, end],
        "sample_interval_seconds": 1,
        "all_four_sampled_utc_seconds_inclusive": windows,
        "matching_sample_count": last - first + 1,
        "entry_transition_utc_second_of_day_approx": entry,
        "exit_transition_utc_second_of_day_approx": exit_,
        "edge_bisection_bracket_width_seconds_at_most": 0.01,
        "interpretation": "SUBMINUTE_MODEL_CONSISTENCY_NOT_INFERRED_BIRTH_TIME",
        "subsecond_continuity": "NOT_PROVED_BY_DISCRETE_GRID",
        "historical_numeric_residuals": "NOT_RUN_NO_INSPECTED_1980_CHART",
        "dr70_fidelity": "NOT_RUN_NO_GOLDEN",
    }


def main() -> None:
    swe = importlib.import_module("swisseph")
    cases = [c for c in load()["cases"] if c["id"] == "RAEL1980-CARTER"]
    if len(cases) != 1:
        raise ValueError("Missing or ambiguous Carter input")
    print(json.dumps(analyze(cases[0], swe), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
