"""One-variable UTC experiment for two MODERN Carter charts, never DR-70.

Hold date, coordinates, Swiss Ephemeris/Moshier and four comparable fields
constant; change only 12:00 versus 13:00 UT. The independent 2026 web chart
prints whole arcminutes, so accept <60 arcseconds there. This reproduces
published precision, not historical accuracy or independent ephemerides.
"""

from __future__ import annotations

from copy import deepcopy
import unittest
import json
from pathlib import Path

from scripts.carter_qualitative_relation import ZODIAC, longitude_seconds
from scripts.chart_input_candidates import load
from scripts.compute_chart_reference import calculate

try:
    import swisseph as swe
except ImportError:
    swe = None

ROOT = Path(__file__).resolve().parents[1]
ASTRODIENST = ROOT / "data/modern-controls/carter-astro-dienst-2023.json"
ASTRO_CHARTS = ROOT / "data/modern-controls/carter-astro-charts-timezone-variant-2026.json"
FIELDS = ("ascendant", "midheaven", "sun", "moon")


def circular_delta_arcseconds(observed_arcseconds: float, calculated_degrees: float) -> float:
    """Calculated minus observed, choosing the shorter signed zodiac arc."""
    return ((calculated_degrees * 3600 - observed_arcseconds + 648000) % 1296000) - 648000


def minute_position_arcseconds(entry: dict) -> int:
    """Whole-minute source only: do not invent published seconds."""
    sign = entry["sign"]
    degrees, minutes = entry["degrees"], entry["minutes"]
    if sign not in ZODIAC or type(degrees) is not int or type(minutes) is not int:
        raise ValueError("Invalid zodiac minute position")
    if not 0 <= degrees < 30 or not 0 <= minutes < 60:
        raise ValueError("Invalid zodiac minute component")
    return ((ZODIAC[sign] * 30 + degrees) * 60 + minutes) * 60


def result_field(chart: dict, field: str) -> float:
    if field in ("ascendant", "midheaven"):
        return chart["angles_deg"][field]
    return chart["planet_longitudes"][field]["longitude_deg"]


@unittest.skipUnless(swe is not None, "optional Swiss Ephemeris binding absent")
class CarterOneVariableTimeShiftTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.published13 = json.loads(ASTRODIENST.read_text(encoding="utf-8"))
        cls.published12 = json.loads(ASTRO_CHARTS.read_text(encoding="utf-8"))
        cls.case = next(c for c in load()["cases"] if c["id"] == "RAEL1980-CARTER")
        cls.case12 = deepcopy(cls.case)
        cls.case12["utc_time_as_printed"] = "12:00"
        cls.case12["time_interpretation"] = (
            "COUNTERFACTUAL 12:00 UT at unchanged date/coordinates; "
            "not the 1980 book's literal input"
        )
        cls.reference13 = calculate(cls.case, swe)
        cls.reference12 = calculate(cls.case12, swe)

    def test_12_and_13_ut_each_reproduce_their_modern_source_at_published_resolution(self):
        """Four paired numbers, not merely a plausible angle or source assertion."""
        self.assertEqual(self.case["utc_time_as_printed"], "13:00")
        self.assertEqual(self.published13["input_as_published"]["universal_time"], "13:00")
        self.assertEqual(self.published12["input_as_displayed"]["utc_offset"], "-05:00")
        self.assertEqual(self.published12["input_as_displayed"]["local_time"], "07:00")
        self.assertEqual(self.reference12["utc_interpreted"], "1924-10-01T12:00:00Z")
        self.assertEqual(self.reference13["utc_interpreted"], "1924-10-01T13:00:00Z")
        self.assertEqual(self.reference13["classification"], "MODERN_REFERENCE_NOT_DR70")
        self.assertEqual(self.reference12["dr70_fidelity"], "NOT_RUN_NO_GOLDEN")
        for field in FIELDS:
            with self.subTest(source="AstroDienst 2023, UT 13", field=field):
                printed = longitude_seconds(self.published13["positions"][field])
                residual = circular_delta_arcseconds(
                    printed, result_field(self.reference13, field)
                )
                self.assertLessEqual(abs(residual), 1.0)
            with self.subTest(source="Astro-Charts 2026, UT 12", field=field):
                printed = minute_position_arcseconds(
                    self.published12["positions_as_displayed"][field]
                )
                residual = circular_delta_arcseconds(
                    printed, result_field(self.reference12, field)
                )
                self.assertLess(abs(residual), 60.0)

    def test_wrong_utc_variant_fails_both_ascendant_comparisons(self):
        """The one-hour contrast is identifiable at source precision."""
        wrong12 = circular_delta_arcseconds(
            minute_position_arcseconds(
                self.published12["positions_as_displayed"]["ascendant"]
            ),
            self.reference13["angles_deg"]["ascendant"],
        )
        wrong13 = circular_delta_arcseconds(
            longitude_seconds(self.published13["positions"]["ascendant"]),
            self.reference12["angles_deg"]["ascendant"],
        )
        self.assertGreater(abs(wrong12), 10 * 3600)
        self.assertGreater(abs(wrong13), 10 * 3600)

    def test_house_system_does_not_explain_ascendant_or_mc_shift(self):
        """Campanus and Placidus share the same angle geometry here.

        This says nothing about the twelve cusps (which do differ).
        """
        for reference in (self.reference12, self.reference13):
            with self.subTest(ut=reference["utc_interpreted"]):
                _, angles_placidus = swe.houses_ex(
                    reference["julian_day_ut"],
                    reference["latitude_deg"],
                    reference["longitude_deg_east"],
                    b"P",
                    0,
                )
                for field, idx in (("ascendant", 0), ("midheaven", 1)):
                    self.assertLess(
                        abs(angles_placidus[idx] - reference["angles_deg"][field]),
                        1e-9,
                    )


class SourcePrecisionGuardTest(unittest.TestCase):
    def test_invalid_and_boolean_minute_values_are_rejected(self):
        good = {"sign": "Libra", "degrees": 13, "minutes": 19}
        self.assertEqual(minute_position_arcseconds(good), 193 * 3600 + 19 * 60)
        for changed in (
            {"sign": "unknown"}, {"degrees": 30},
            {"minutes": 60}, {"minutes": True}, {"degrees": 13.0},
        ):
            with self.subTest(changed=changed), self.assertRaises(ValueError):
                minute_position_arcseconds(dict(good, **changed))


if __name__ == "__main__":
    unittest.main()
