"""Modern Swiss Ephemeris/Moshier Campanus baseline, NOT DR-70 output.

This is an OPTIONAL research adapter. It uses an independently installed Swiss
Ephemeris Python binding; its AGPL/professional licensing must be considered
before integrating any linked code into a distributed product.
"""

from __future__ import annotations

import argparse
from datetime import datetime
import importlib
import json
from pathlib import Path

from scripts.chart_input_candidates import DEFAULT_INPUT, load, normalize

PLANETS = ("SUN", "MOON", "MERCURY", "VENUS", "MARS", "JUPITER", "SATURN")


def calculate(case: dict, swe) -> dict:
    chart = normalize(case)
    input_data = chart["hypothetical_normalization"]
    instant = datetime.fromisoformat(input_data["utc"].replace("Z", "+00:00"))
    hour = instant.hour + instant.minute / 60 + instant.second / 3600
    jd_ut = swe.julday(instant.year, instant.month, instant.day, hour)
    latitude = input_data["latitude_deg"]
    longitude = input_data["longitude_deg_east"]
    cusps, angles = swe.houses_ex(jd_ut, latitude, longitude, b"C", 0)
    if len(cusps) != 12 or len(angles) < 2:
        raise ValueError("Expected 12 Campanus cusps and ASC/MC from Swiss Ephemeris")
    planets = {}
    for name in PLANETS:
        position, flags = swe.calc_ut(jd_ut, getattr(swe, name), swe.FLG_MOSEPH)
        if not flags & swe.FLG_MOSEPH:
            raise RuntimeError(f"Unexpected planet ephemeris backend for {name}: {flags}")
        planets[name.lower()] = {"longitude_deg": position[0], "returned_flags": flags}
    return {
        "classification": "MODERN_REFERENCE_NOT_DR70",
        "input_candidate_id": case["id"],
        "input_source_status": chart["evidence_status"],
        "input_time_assumption": input_data["assumption"],
        "utc_interpreted": input_data["utc"],
        "latitude_deg": latitude,
        "longitude_deg_east": longitude,
        "julian_day_ut": jd_ut,
        "engine": {
            "name": "Swiss Ephemeris (Python swisseph binding)",
            "version": str(swe.version),
            "planetary_ephemeris": "Moshier requested and returned, no external ephemeris files",
            "house_system": "Campanus (C)",
            "zodiac": "tropical",
            "degree_range": "[0,360)",
            "license_note": "External Swiss Ephemeris dual license: AGPL or professional. Experimental adapter only."
        },
        "cusps_deg": {str(index): value for index, value in enumerate(cusps, 1)},
        "angles_deg": {"ascendant": angles[0], "midheaven": angles[1]},
        "planet_longitudes": planets,
        "historical_chart_comparison": "NOT_RUN_NO_TRANSCRIBED_VALUES",
        "dr70_fidelity": "NOT_RUN_NO_GOLDEN"
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--id", default="RAEL1980-CARTER")
    args = parser.parse_args()
    candidates = [c for c in load(args.input)["cases"] if c["id"] == args.id]
    if len(candidates) != 1:
        parser.error("Unknown or ambiguous candidate ID")
    try:
        swe = importlib.import_module("swisseph")
    except ImportError as error:
        parser.error(f"Optional binding not installed: {error}; install pyswisseph in an isolated research environment")
    print(json.dumps(calculate(candidates[0], swe), indent=2))


if __name__ == "__main__":
    main()
