"""Compare two indexed editorial claims to modern angles, not DR-70 outputs.

Research-only optional dependency: pyswisseph. No historic machine run is inferred.
"""

from __future__ import annotations

import json
import math

# The unusual hour strings have not been checked on the printed page.
# All alternatives use a UTC calendar date only as a stated hypothesis.
INPUT_HYPOTHESES = {
    "extended_25h16": (1882, 1, 30, 25 + 16 / 60),
    "extended_25h15_variant": (1882, 1, 30, 25 + 15 / 60),
    "same_date_01h16": (1882, 1, 30, 1 + 16 / 60),
}
PUBLISHED_ROUNDED_ANGLES = {"moon_pluto": 39, "mars_uranus": 81}


def minimum_separation_deg(a: float, b: float) -> float:
    """Smallest ecliptic separation on a circle, in [0,180] degrees."""
    if not all(math.isfinite(v) and 0 <= v < 360 for v in (a, b)):
        raise ValueError("Both longitude arguments must be finite in [0,360)")
    difference = abs(a - b) % 360
    return min(difference, 360 - difference)


def directed_advance_deg(a: float, b: float) -> float:
    """Directed zodiacal advance from b to a in [0,360)."""
    if not all(math.isfinite(v) and 0 <= v < 360 for v in (a, b)):
        raise ValueError("Both longitude arguments must be finite in [0,360)")
    return (a - b) % 360


def calculate_hypothesis(swe, year: int, month: int, day: int, utc_hour: float) -> dict:
    """Use geocentric tropical longitudes with the explicit Moshier flag."""
    jd_ut = swe.julday(year, month, day, utc_hour)
    longitudes = {
        name: swe.calc_ut(jd_ut, planet, swe.FLG_MOSEPH)[0][0]
        for name, planet in (
            ("moon", swe.MOON), ("pluto", swe.PLUTO),
            ("mars", swe.MARS), ("uranus", swe.URANUS),
            ("saturn", swe.SATURN), ("neptune", swe.NEPTUNE),
            ("jupiter", swe.JUPITER),
        )
    }
    observed_modern = {
        "moon_pluto": minimum_separation_deg(longitudes["moon"], longitudes["pluto"]),
        "mars_uranus": minimum_separation_deg(longitudes["mars"], longitudes["uranus"]),
    }
    return {
        "julian_day_ut": jd_ut,
        "modern_separations_deg": observed_modern,
        "modern_septile_diagnostics_deg": {
            "moon_neptune_short_arc": minimum_separation_deg(longitudes["moon"], longitudes["neptune"]),
            "mars_ahead_saturn_directed": directed_advance_deg(longitudes["mars"], longitudes["saturn"]),
            "moon_jupiter_short_arc": minimum_separation_deg(longitudes["moon"], longitudes["jupiter"]),
        },
        "modern_minus_published_rounded_deg": {
            name: angle - PUBLISHED_ROUNDED_ANGLES[name]
            for name, angle in observed_modern.items()
        },
        "nearest_integer_matches": {
            name: round(angle) == PUBLISHED_ROUNDED_ANGLES[name]
            for name, angle in observed_modern.items()
        },
    }


def run() -> dict:
    try:
        import swisseph as swe
    except ImportError as exc:
        raise RuntimeError("Optional pyswisseph is required for this research-only probe") from exc
    return {
        "classification": "SECONDARY_EDITORIAL_ANGLES_VS_MODERN_EPHEMERIS_NOT_DR70",
        "historical_facsimile": "NOT_INSPECTED",
        "historical_values": PUBLISHED_ROUNDED_ANGLES,
        "source": "Rael/Rudhyar indexed novile and septile prose; facsimile not inspected",
        "septile_textual_controls": {
            "moon_neptune": "about 52 degrees",
            "mars_ahead_saturn": "just short of 51 degrees, directed",
            "moon_jupiter": "conditional on unspecified later birth hour",
            "author_textual_septile_interval_deg": [50, 53],
            "moon_jupiter_conditional_verdict": "NOT_EVALUATED_LATER_HOUR_UNSPECIFIED",
            "source_family": "SAME_EDITORIAL_BOOK_NOT_INDEPENDENT_HOLDOUT",
        },
        "engine": f"Swiss Ephemeris {swe.version}, Moshier, geocentric tropical",
        "dr70_fidelity": "NOT_RUN_NO_GOLDEN",
        "hypotheses": {
            label: calculate_hypothesis(swe, *params)
            for label, params in INPUT_HYPOTHESES.items()
        },
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, ensure_ascii=False))
