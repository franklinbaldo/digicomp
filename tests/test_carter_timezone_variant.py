"""Detect a real source-convention disagreement, not a DR-70 accuracy result.

The modern AstroDienst chart reproduces 07:00 local / 13:00 UT.
The current Astro-Charts web page displays 07:00 local / UTC -05:00,
which implies 12:00 UT. Both are secondary modern chart sources.
The original civil-time rule and 1980 chart angles are not established.
No ephemeris dependency is required for these source-contract tests.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timedelta
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
ASTRODIENST = ROOT / "data/modern-controls/carter-astro-dienst-2023.json"
ASTRO_CHARTS = ROOT / "data/modern-controls/carter-astro-charts-timezone-variant-2026.json"

SIGNS = {
    "Aries": 0, "Taurus": 1, "Gemini": 2, "Cancer": 3,
    "Leo": 4, "Virgo": 5, "Libra": 6, "Scorpio": 7,
    "Sagittarius": 8, "Capricorn": 9, "Aquarius": 10, "Pisces": 11,
}


def offset_minutes(value: str) -> int:
    if not isinstance(value, str):
        raise ValueError("UTC offset must be text")
    match = re.fullmatch(r"([+-])(\d{2}):(\d{2})", value)
    if match is None:
        raise ValueError("UTC offset must be ±HH:MM")
    hour, minute = int(match[2]), int(match[3])
    if hour > 14 or minute > 59 or (hour == 14 and minute != 0):
        raise ValueError("UTC offset outside maximum range")
    return (1 if match[1] == "+" else -1) * (hour * 60 + minute)


def displayed_arcminutes(position: dict) -> int:
    """Decode displayed sign/degree/minute; never invent missing seconds."""
    if not isinstance(position, dict) or position.get("sign") not in SIGNS:
        raise ValueError("Invalid sign")
    deg, minute = position.get("degrees"), position.get("minutes")
    if type(deg) is not int or type(minute) is not int:
        raise ValueError("DMS components must be exact integers")
    if not (0 <= deg < 30 and 0 <= minute < 60):
        raise ValueError("Out-of-range DMS")
    return (SIGNS[position["sign"]] * 30 + deg) * 60 + minute


class CarterTimezoneSourceVariantTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.anchor = json.loads(ASTRODIENST.read_text(encoding="utf-8"))
        cls.variant = json.loads(ASTRO_CHARTS.read_text(encoding="utf-8"))

    def test_web_source_is_pinned_independently_of_its_fixture(self):
        data = self.variant
        self.assertEqual(data["classification"],
                         "MODERN_SECONDARY_WEB_CHART_TIMEZONE_VARIANT_NOT_DR70")
        self.assertEqual(data["case_id"], "RAEL1980-CARTER")
        self.assertEqual(
            data["source"]["url"],
            "https://www.astro-charts.com/persons/chart/jimmy-carter/",
        )
        self.assertEqual(data["source"]["angle_resolution"],
                         "whole arcminute shown (no seconds)")
        self.assertEqual(data["source"]["house_system"], "Placidus")
        self.assertEqual(data["input_as_displayed"], {
            "date": "1924-10-01",
            "local_time": "07:00",
            "timezone_literal": "UTC −5:00",
            "utc_offset": "-05:00",
            "place": "Plains, Georgia, United States",
        })
        self.assertEqual(data["positions_as_displayed"], {
            "ascendant": {"sign": "Libra", "degrees": 13, "minutes": 19},
            "midheaven": {"sign": "Cancer", "degrees": 14, "minutes": 19},
            "sun": {"sign": "Libra", "degrees": 8, "minutes": 1},
            "moon": {"sign": "Scorpio", "degrees": 13, "minutes": 11},
        })

    def test_same_seven_am_label_has_one_hour_utc_disagreement(self):
        anchor = self.anchor
        alternative = self.variant
        self.assertEqual(anchor["source"]["publication_year"], 2023)
        self.assertEqual(anchor["chart_house_system"], "Whole Signs")
        self.assertEqual(anchor["input_as_published"]["date"], "1924-10-01")
        self.assertEqual(anchor["input_as_published"]["universal_time"], "13:00")
        self.assertEqual(alternative["comparison_scope"]["astrodienst_2023_source_local_time"],
                         "07:00")
        self.assertEqual(alternative["comparison_scope"]["astrodienst_2023_source_utc_time"],
                         "13:00")
        self.assertEqual(alternative["input_as_displayed"]["local_time"], "07:00")
        local = datetime.strptime(
            alternative["input_as_displayed"]["date"] + " " +
            alternative["input_as_displayed"]["local_time"],
            "%Y-%m-%d %H:%M",
        )
        alternative_utc = local - timedelta(
            minutes=offset_minutes(alternative["input_as_displayed"]["utc_offset"])
        )
        anchor_utc = datetime.strptime(
            anchor["input_as_published"]["date"] + " " +
            anchor["input_as_published"]["universal_time"],
            "%Y-%m-%d %H:%M",
        )
        self.assertEqual(alternative_utc.isoformat(), "1924-10-01T12:00:00")
        self.assertEqual(anchor_utc - alternative_utc, timedelta(minutes=60))
        # Two conventions: neither is verified as the historical legal offset.
        self.assertTrue(
            alternative["comparison_scope"]["source_timezone_convention_disagreement"]
        )

    def test_four_displayed_angle_gaps_are_minute_resolution_only(self):
        # Deliberately discard seconds from the AstroDienst control too.
        # This reports differences BETWEEN DISPLAYED MINUTE COMPONENTS,
        # not physical angular residuals nor an explanation by timezone.
        gaps = {
            key: abs(
                displayed_arcminutes(self.anchor["positions"][key]) -
                displayed_arcminutes(self.variant["positions_as_displayed"][key])
            )
            for key in ("ascendant", "midheaven", "sun", "moon")
        }
        self.assertEqual(
            gaps, {"ascendant": 766, "midheaven": 848, "sun": 2, "moon": 36}
        )
        self.assertTrue(
            self.variant["comparison_scope"]["cannot_attribute_angular_difference_only_to_timezone"]
        )

    def test_corruption_and_golden_promotion_are_rejected(self):
        for bad in ("-15:00", "+14:01", "-05:60", "UTC -05:00", None):
            with self.subTest(offset=bad), self.assertRaises(ValueError):
                offset_minutes(bad)
        for bad in ({"minutes": 60}, {"degrees": 30}, {"minutes": True},
                    {"sign": "unknown"}):
            with self.subTest(position=bad), self.assertRaises(ValueError):
                displayed_arcminutes(dict(self.variant["positions_as_displayed"]["moon"], **bad))
        scope = self.variant["comparison_scope"]
        self.assertEqual(scope["historical_1980_chart"],
                         "NOT_RUN_NO_INSPECTED_1980_NUMBERS")
        self.assertEqual(scope["dr70_fidelity"], "NOT_RUN_NO_GOLDEN")
        self.assertEqual(scope["resolution"],
                         "UNRESOLVED_WHICH_HISTORICAL_TIMEZONE_APPLIES")
        self.assertIs(scope["golden_instrumental"], False)
        self.assertIs(
            self.anchor["scope"]["golden_instrumental"], False
        )


if __name__ == "__main__":
    unittest.main()
