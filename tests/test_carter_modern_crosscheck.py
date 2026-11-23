"""A 2023 published modern chart cross-check, NEVER a DR-70 golden case.

The cited AstroDienst chart uses Whole Signs, unlike the optional Campanus
calculator. Only ASC, MC, and seven planetary ecliptic longitudes are compared.
The 2023 source may use the same Swiss Ephemeris engine, so software
independence and accuracy of historical DR-70 outputs are NOT established.
"""

from __future__ import annotations

from copy import deepcopy
import json
import math
from pathlib import Path
import re
import tempfile
import unittest

from scripts.chart_input_candidates import load
from scripts.compute_chart_reference import calculate

try:
    import swisseph as swe
except ImportError:
    swe = None

CONTROL_PATH = (
    Path(__file__).resolve().parents[1]
    / "data/modern-controls/carter-astro-dienst-2023.json"
)
ZODIAC_OFFSETS = {
    "Aries": 0, "Taurus": 30, "Gemini": 60, "Cancer": 90,
    "Leo": 120, "Virgo": 150, "Libra": 180, "Scorpio": 210,
    "Sagittarius": 240, "Capricorn": 270, "Aquarius": 300, "Pisces": 330,
}
FIELDS = (
    "ascendant", "midheaven", "sun", "moon", "mercury",
    "venus", "mars", "jupiter", "saturn",
)


def strict_json(path: Path) -> dict:
    """Reject ambiguous or non-finite source fields, including nested objects."""
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate modern-control JSON key: {key!r}")
            result[key] = value
        return result

    def reject_constant(value):
        raise ValueError(f"Invalid modern-control JSON constant: {value}")

    def finite_float(value):
        parsed = float(value)
        if not math.isfinite(parsed):
            raise ValueError(f"Non-finite modern-control JSON number: {value}")
        return parsed

    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=unique_pairs,
        parse_constant=reject_constant,
        parse_float=finite_float,
    )


def published_longitude(entry: dict) -> float:
    """Decode a sign/degree/minute/second field, never degrees-within-sign alone."""
    if entry["sign"] not in ZODIAC_OFFSETS:
        raise ValueError("Unrecognized zodiac sign")
    degree, minute, second = (
        entry["degrees"], entry["minutes"], entry["seconds"]
    )
    if any(type(value) is not int for value in (degree, minute, second)):
        raise ValueError("DMS must be integral")
    if not 0 <= degree < 30 or not 0 <= minute < 60 or not 0 <= second < 60:
        raise ValueError("Out-of-range zodiac DMS")
    # Unlike the zodiac sign (supplied as metadata), the printed literal
    # contains DMS digits. Ensure that they agree with the interpreted fields.
    literal = entry.get("literal")
    if not isinstance(literal, str):
        raise ValueError("Missing printed DMS literal")
    match = re.fullmatch(r"\s*(\d{1,2})\s*°\s*(\d{1,2})\s*[′']\s*(\d{1,2})\s*[″\"]\s*", literal)
    if match is None or tuple(map(int, match.groups())) != (degree, minute, second):
        raise ValueError("Printed DMS literal disagrees with interpreted fields")
    return ZODIAC_OFFSETS[entry["sign"]] + degree + minute / 60 + second / 3600


def signed_arcseconds_delta(expected: float, actual: float) -> float:
    return ((actual - expected + 180) % 360 - 180) * 3600


class PublishedClockSourceContractTest(unittest.TestCase):
    def test_page_twelve_clock_and_tolerance_are_pinned(self):
        """The source record must not silently authorize its own tolerance.

        Without this fixed oracle, changing both the clock literal and
        tolerance_seconds can still pass the nine-field/clock suite.
        """
        control = strict_json(CONTROL_PATH)
        self.assertEqual(control["sidereal_clock"]["literal"], "8:02:19")
        self.assertEqual(control["sidereal_clock"]["tolerance_seconds"], 1)
        self.assertEqual(
            control["sidereal_clock"]["locator"],
            "PDF printed p. 12, Natal chart header: Sid. Time",
        )


    def test_page_twelve_nine_published_angles_are_pinned(self):
        """Independent test oracle: fixed transcription from the rendered p. 12.

        The nine calculated values and an adjustable tolerance are otherwise
        compared against fields loaded from the very same JSON fixture.
        Mutating both fixture fields and tolerance must never count as a pass.
        This pins a single 2023 publication, NOT nine DR-70 observations.
        """
        control = strict_json(CONTROL_PATH)
        self.assertEqual(control["source"]["publication_year"], 2023)
        self.assertEqual(control["source"]["chart_date"], "2023-02-19")
        self.assertIn("PDF printed p. 12", control["source"]["locator"])
        self.assertEqual(control["chart_house_system"], "Whole Signs")
        self.assertEqual(
            control["input_as_published"],
            {
                "date": "1924-10-01",
                "universal_time": "13:00",
                "latitude": "32N02",
                "longitude": "84W24",
            },
        )
        self.assertEqual(control["scope"]["tolerance_arcseconds"], 1)
        self.assertEqual(set(control["scope"]["comparison_only"]), set(FIELDS))
        # Read directly from the image of Naomi Rabinowitz's printed p. 12;
        # no value here is calculated using Swiss Ephemeris.
        expected = {
            "ascendant": ("Libra", 26, 5, 38, "26° 5′ 38″"),
            "midheaven": ("Cancer", 28, 27, 53, "28° 27′ 53″"),
            "sun": ("Libra", 8, 3, 42, "8° 3′ 42″"),
            "moon": ("Scorpio", 13, 47, 47, "13° 47′ 47″"),
            "mercury": ("Virgo", 21, 11, 20, "21° 11′ 20″"),
            "venus": ("Leo", 23, 19, 54, "23° 19′ 54″"),
            "mars": ("Aquarius", 25, 53, 5, "25° 53′ 5″"),
            "jupiter": ("Sagittarius", 14, 25, 51, "14° 25′ 51″"),
            "saturn": ("Scorpio", 1, 54, 52, "1° 54′ 52″"),
        }
        self.assertEqual(set(control["positions"]), set(expected))
        for name, fixed in expected.items():
            with self.subTest(name=name):
                item = control["positions"][name]
                self.assertEqual(
                    (
                        item["sign"], item["degrees"], item["minutes"],
                        item["seconds"], item["literal"],
                    ),
                    fixed,
                )


@unittest.skipUnless(swe is not None, "optional Swiss Ephemeris binding absent")
class CarterModernControlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.control = strict_json(CONTROL_PATH)
        cls.case = next(
            c for c in load()["cases"] if c["id"] == "RAEL1980-CARTER"
        )
        cls.modern = calculate(cls.case, swe)

    def test_nine_published_modern_fields_within_one_arcsecond(self):
        control = self.control
        modern = self.modern
        self.assertEqual(
            control["classification"], "MODERN_CHART_CONTROL_NOT_DR70_OUTPUT"
        )
        self.assertEqual(modern["classification"], "MODERN_REFERENCE_NOT_DR70")
        self.assertEqual(control["chart_house_system"], "Whole Signs")
        self.assertEqual(set(control["positions"]), set(FIELDS))
        self.assertEqual(set(control["scope"]["comparison_only"]), set(FIELDS))
        self.assertEqual(control["scope"]["tolerance_arcseconds"], 1)
        self.assertEqual(modern["dr70_fidelity"], "NOT_RUN_NO_GOLDEN")
        self.assertFalse(control["scope"]["golden_instrumental"])
        self.assertFalse(control["scope"]["dr70_native_output"])
        self.assertEqual(
            control["scope"]["historical_chart_residuals"],
            "NOT_RUN_NO_INSPECTED_1980_NUMBERS",
        )
        self.assertEqual(
            control["input_as_published"],
            {
                "date": self.case["date_as_printed"],
                "universal_time": self.case["utc_time_as_printed"],
                "latitude": self.case["latitude_as_printed"],
                "longitude": self.case["longitude_as_printed"],
            },
        )
        for field in FIELDS:
            expected = published_longitude(control["positions"][field])
            if field in ("ascendant", "midheaven"):
                actual = modern["angles_deg"][field]
            else:
                actual = modern["planet_longitudes"][field]["longitude_deg"]
            delta = signed_arcseconds_delta(expected, actual)
            self.assertLessEqual(
                abs(delta), control["scope"]["tolerance_arcseconds"],
                f"{field}: modern 2023 cross-control delta={delta:+.3f} arcsec",
            )

    def test_time_shift_changes_the_ascendant(self):
        shifted_case = deepcopy(self.case)
        shifted_case["utc_time_as_printed"] = "14:00"
        shifted = calculate(shifted_case, swe)
        published = published_longitude(self.control["positions"]["ascendant"])
        delta = signed_arcseconds_delta(
            published, shifted["angles_deg"]["ascendant"]
        )
        self.assertGreater(abs(delta), 60, "One-hour mutant escaped the control")

    def test_published_sidereal_clock_checks_utc_and_west_longitude(self):
        """A tenth, auxiliary clock control: NOT a DR-70 output or ephemeris gold."""
        clock = self.control["sidereal_clock"]
        self.assertEqual(
            clock["classification"], "MODERN_PUBLISHED_AUXILIARY_CLOCK_NOT_DR70"
        )
        self.assertEqual(
            clock["locator"], "PDF printed p. 12, Natal chart header: Sid. Time"
        )
        literal = clock["literal"]
        self.assertIsInstance(literal, str)
        self.assertRegex(literal, r"^(?:[01]?\d|2[0-3]):[0-5]\d:[0-5]\d$")
        hour, minute, second = map(int, literal.split(":"))
        printed_seconds = hour * 3600 + minute * 60 + second

        def local_sidereal_seconds(jd_ut, longitude_east):
            return (swe.sidtime(jd_ut) + longitude_east / 15.0) % 24 * 3600

        def signed_delta_seconds(actual):
            return (actual - printed_seconds + 43200) % 86400 - 43200

        jd = self.modern["julian_day_ut"]
        longitude_east = self.modern["longitude_deg_east"]
        actual = local_sidereal_seconds(jd, longitude_east)
        self.assertLessEqual(
            abs(signed_delta_seconds(actual)),
            clock["tolerance_seconds"],
            "Printed 2023 local sidereal clock disagrees with modern input",
        )

        # Opposite longitude sign and one-hour UTC shift must not pass.
        flipped = local_sidereal_seconds(jd, -longitude_east)
        shifted = local_sidereal_seconds(jd + 1 / 24, longitude_east)
        self.assertGreater(abs(signed_delta_seconds(flipped)), 3600)
        self.assertGreater(abs(signed_delta_seconds(shifted)), 3600)

class CarterModernInputContractTest(unittest.TestCase):
    """Guard published data and JSON parsing even without optional swisseph.

    These validation tests must run on standard-library-only installations;
    only the astronomical comparisons need the external ephemeris engine.
    """

    @classmethod
    def setUpClass(cls):
        cls.control = strict_json(CONTROL_PATH)

    def test_sign_and_range_errors_fail_closed(self):
        mars = self.control["positions"]["mars"]
        self.assertEqual(mars["sign"], "Aquarius")
        wrong = dict(mars, sign="Pisces")
        self.assertGreater(
            abs(signed_arcseconds_delta(
                published_longitude(mars), published_longitude(wrong)
            )),
            60,
        )
        with self.assertRaises(ValueError):
            published_longitude(dict(mars, minutes=60))
        with self.assertRaises(ValueError):
            published_longitude(dict(mars, degrees=30))
        with self.assertRaises(ValueError):
            published_longitude(dict(mars, sign="Unknown"))

    def test_literal_mutations_fail_closed(self):
        sun = self.control["positions"]["sun"]
        self.assertIsInstance(published_longitude(sun), float)
        for wrong in ("19° 59′ 59″", "8° 3′ 43″", "8° 3′", "8° 3′ 42″ extra"):
            with self.subTest(literal=wrong), self.assertRaises(ValueError):
                published_longitude(dict(sun, literal=wrong))
        with self.assertRaises(ValueError):
            published_longitude(dict(sun, literal=None))

    def test_ambiguous_json_rejected_even_in_unused_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.json"
            for payload in (
                '{"positions":{"sun":{"literal":"x","literal":"y"}}}',
                '{"ignored":{"nested":NaN}}',
                '{"ignored":Infinity}',
                '{"ignored":1e999}',
                '{"ignored":-1e999}',
            ):
                with self.subTest(payload=payload):
                    path.write_text(payload, encoding="utf-8")
                    with self.assertRaises(ValueError):
                        strict_json(path)
            path.write_text('{"safe":{"number":1.5}}', encoding="utf-8")
            self.assertEqual(strict_json(path)["safe"]["number"], 1.5)


if __name__ == "__main__":
    unittest.main()
