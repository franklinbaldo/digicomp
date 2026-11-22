"""Quantify a 1980 qualitative septile claim using a 2023 MODERN chart.

This is a minimum-orb sensitivity calculation, not a historical chart
measurement, a DR-70 result, or confirmation that the 1980 edition
used any particular orb. No astronomy package or network access needed.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path

DEFAULT_CONTROL = (
    Path(__file__).resolve().parents[1]
    / "data/modern-controls/carter-astro-dienst-2023.json"
)
ZODIAC = {
    "Aries": 0, "Taurus": 1, "Gemini": 2, "Cancer": 3,
    "Leo": 4, "Virgo": 5, "Libra": 6, "Scorpio": 7,
    "Sagittarius": 8, "Capricorn": 9, "Aquarius": 10, "Pisces": 11,
}
FULL_CIRCLE_SECONDS = 360 * 3600


def longitude_seconds(position: dict) -> int:
    """Strictly decode printed DMS; degrees and zodiac sign are distinct."""
    if not isinstance(position, dict) or position.get("sign") not in ZODIAC:
        raise ValueError("Missing or invalid zodiac sign")
    components = (position.get("degrees"), position.get("minutes"), position.get("seconds"))
    if any(type(value) is not int for value in components):
        raise ValueError("Zodiac DMS requires exact integer components")
    degree, minute, second = components
    if not (0 <= degree < 30 and 0 <= minute < 60 and 0 <= second < 60):
        raise ValueError("Zodiac DMS component outside its range")
    if position.get("literal") != f"{degree}° {minute}′ {second}″":
        raise ValueError("Printed literal does not agree with DMS components")
    return (ZODIAC[position["sign"]] * 30 + degree) * 3600 + minute * 60 + second


def compare(control: dict) -> dict:
    """Report an exact rational threshold, WITHOUT choosing an orb."""
    if (
        control.get("classification") != "MODERN_CHART_CONTROL_NOT_DR70_OUTPUT"
        or control.get("case_id") != "RAEL1980-CARTER"
        or control.get("source", {}).get("publication_year") != 2023
        or control.get("scope", {}).get("dr70_native_output") is not False
        or control.get("scope", {}).get("golden_instrumental") is not False
        or control.get("scope", {}).get("historical_chart_residuals")
        != "NOT_RUN_NO_INSPECTED_1980_NUMBERS"
    ):
        raise ValueError("This calculation requires the labelled modern-only Carter control")
    positions = control["positions"]
    moon = longitude_seconds(positions["moon"])
    mercury = longitude_seconds(positions["mercury"])
    directed = (moon - mercury) % FULL_CIRCLE_SECONDS
    separation = min(directed, FULL_CIRCLE_SECONDS - directed)
    exact_septile = Fraction(FULL_CIRCLE_SECONDS, 7)
    difference = abs(Fraction(separation) - exact_septile)
    return {
        "classification": "MODERN_POSITIONS_VS_SECONDARY_HISTORICAL_QUALITATIVE_CLAIM",
        "relation": "Moon-Mercury septile (historical text, not chart numbers)",
        "historical_claim_evidence": "SECONDARY_TEXT_NOT_VERIFIED_AGAINST_1980_PAGE_IMAGE",
        "modern_chart_year": 2023,
        "separation_arcseconds": separation,
        "exact_septile_arcseconds": {
            "numerator": exact_septile.numerator,
            "denominator": exact_septile.denominator,
        },
        "minimum_orb_arcseconds": {
            "numerator": difference.numerator,
            "denominator": difference.denominator,
        },
        "orb_declared_by_historical_text": None,
        "historical_relation_test": "INDETERMINATE_ORB_NOT_SPECIFIED",
        "historical_chart_residual": "NOT_RUN_NO_INSPECTED_1980_NUMBERS",
        "dr70_fidelity": "NOT_RUN_NO_GOLDEN",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--control", type=Path, default=DEFAULT_CONTROL)
    args = parser.parse_args()
    control = json.loads(args.control.read_text(encoding="utf-8"))
    print(json.dumps(compare(control), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
