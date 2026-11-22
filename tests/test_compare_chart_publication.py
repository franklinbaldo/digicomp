"""All numbers in these test fixtures are synthetic and never a DR-70 output."""

from pathlib import Path
import copy
import tempfile
import unittest

from scripts.compare_chart_publication import (
    compare, signed_circular_residual, strict_json, DEFAULT_PUBLICATION
)


class EditorialComparatorTest(unittest.TestCase):
    def setUp(self):
        self.reference = {
            "classification": "MODERN_REFERENCE_NOT_DR70",
            "input_candidate_id": "RAEL1980-CARTER",
            "dr70_fidelity": "NOT_RUN_NO_GOLDEN",
            "cusps_deg": {"1": 359.0},
            "angles_deg": {"ascendant": 359.0},
            "planet_longitudes": {"sun": {"longitude_deg": 188.0}}
        }
        self.publication = {
            "classification": "PUBLISHED_CHART_MANUAL_TRANSCRIPTION",
            "candidate_id": "RAEL1980-CARTER",
            "source": {"image_inspected": True, "page_locator": "SYNTHETIC TEST ONLY",
                       "reviewed_by": "unit-test", "source_url": "https://example.invalid/synthetic-fixture"},
            "angular_convention": "ecliptic_longitude_0_360_deg",
            "published_values_deg": {"cusp_1": 1.0, "sun": 187.5},
            "source_notation": {
                "cusp_1": {"kind": "absolute_longitude_0_360_deg", "literal": "1°"},
                "sun": {"kind": "zodiac_sign_degree", "literal": "7°30 Libra",
                        "sign": "Libra", "degree_within_sign": 7.5}
            }
        }

    def test_unread_candidate_runs_no_comparison(self):
        result = compare(self.reference, strict_json(DEFAULT_PUBLICATION))
        self.assertEqual(result["status"], "NOT_RUN_NO_PUBLISHED_NUMERIC_TRANSCRIPTION")
        self.assertEqual(result["residuals_deg"], [])

    def test_wrapped_circular_difference(self):
        self.assertAlmostEqual(signed_circular_residual(1, 359), 2)
        self.assertAlmostEqual(signed_circular_residual(359, 1), -2)
        result = compare(self.reference, self.publication)
        self.assertEqual(result["status"], "PUBLISHED_MAP_RESIDUALS_NOT_DR70_FIDELITY")
        self.assertEqual(result["source_locator"], "SYNTHETIC TEST ONLY")
        self.assertEqual([x["circular_difference_deg"] for x in result["residuals_deg"]], [2, -.5])

    def test_no_unreviewed_numbers(self):
        self.publication["source"]["image_inspected"] = False
        with self.assertRaises(ValueError):
            compare(self.reference, self.publication)

    def test_reject_untyped_blank_or_unresolvable_inspection_metadata(self):
        cases = (
            ("page_locator", 123), ("page_locator", ["page 1"]),
            ("page_locator", "  "), ("reviewed_by", "  "),
            ("reviewed_by", 7), ("source_url", {"bogus": True}),
            ("source_url", 123), ("source_url", "  "),
            ("source_url", "ftp://example.org/scan"),
            ("source_url", "synthetic://unit-test"),
            ("source_url", "https://"),
            ("source_url", "https://reader:secret@example.org/image"),
            ("source_url", "https://example.org/scan page"),
        )
        for field, invalid in cases:
            with self.subTest(field=field, invalid=invalid):
                published = copy.deepcopy(self.publication)
                published["source"][field] = invalid
                with self.assertRaises(ValueError):
                    compare(self.reference, published)
        for url in ("http://example.invalid/fixture", "https://example.invalid/fixture"):
            with self.subTest(accepted_url=url):
                published = copy.deepcopy(self.publication)
                published["source"]["source_url"] = url
                self.assertEqual(
                    compare(self.reference, published)["status"],
                    "PUBLISHED_MAP_RESIDUALS_NOT_DR70_FIDELITY",
                )
        for invalid_source in (None, 3, ["source"], {"image_inspected": 1}):
            with self.subTest(invalid_source=invalid_source):
                published = copy.deepcopy(self.publication)
                published["source"] = invalid_source
                with self.assertRaises(ValueError):
                    compare(self.reference, published)

    def test_reject_false_golden_and_nonfinite(self):
        self.reference["dr70_fidelity"] = "PASS"
        with self.assertRaises(ValueError):
            compare(self.reference, self.publication)
        with self.assertRaises(ValueError):
            signed_circular_residual(float("nan"), 10)

    def test_reject_mismatched_case_and_unsupported_field(self):
        self.publication["candidate_id"] = "different"
        with self.assertRaises(ValueError):
            compare(self.reference, self.publication)
        self.publication["candidate_id"] = "RAEL1980-CARTER"
        self.publication["published_values_deg"] = {"unknown": 44}
        with self.assertRaises(ValueError):
            compare(self.reference, self.publication)

    def test_reject_missing_or_unresolved_convention(self):
        del self.publication["angular_convention"]
        with self.assertRaisesRegex(ValueError, "Explicit"):
            compare(self.reference, self.publication)
        self.publication["angular_convention"] = "zodiac_degrees_within_sign_0_30"
        with self.assertRaisesRegex(ValueError, "Explicit"):
            compare(self.reference, self.publication)

    def test_reject_equal_numeric_value_but_wrong_zodiac_sign(self):
        self.reference["planet_longitudes"]["sun"]["longitude_deg"] = 15.0
        self.publication["published_values_deg"] = {"sun": 15.0}
        self.publication["source_notation"] = {
            "sun": {"kind": "zodiac_sign_degree", "literal": "15 Taurus",
                    "sign": "Taurus", "degree_within_sign": 15.0}
        }
        with self.assertRaisesRegex(ValueError, "disagrees"):
            compare(self.reference, self.publication)

    def test_unresolved_sign_has_pending_fields_and_no_residuals(self):
        self.publication["angular_convention"] = "unresolved_zodiac_notation"
        self.publication["published_values_deg"] = {}
        self.publication["unresolved_fields"] = ["sun"]
        result = compare(self.reference, self.publication)
        self.assertEqual(result["status"], "NOT_COMPARABLE_UNRESOLVED_ZODIAC_NOTATION")
        self.assertEqual(result["unresolved_fields"], ["sun"])
        self.assertEqual(result["residuals_deg"], [])
        self.publication["published_values_deg"] = {"sun": 0.0}
        with self.assertRaisesRegex(ValueError, "Unresolved"):
            compare(self.reference, self.publication)

    def test_reject_unrecorded_source_notation(self):
        del self.publication["source_notation"]["sun"]
        with self.assertRaisesRegex(ValueError, "notation"):
            compare(self.reference, self.publication)

    def test_literal_sign_must_match_declared_sign(self):
        self.publication["published_values_deg"] = {"sun": 45.0}
        self.publication["source_notation"] = {
            "sun": {"kind": "zodiac_sign_degree", "literal": "15 Aries",
                    "sign": "Taurus", "degree_within_sign": 15.0}
        }
        with self.assertRaisesRegex(ValueError, "literal sign"):
            compare(self.reference, self.publication)
        self.publication["source_notation"]["sun"]["literal"] = "15 Taurus"
        result = compare(self.reference, self.publication)
        self.assertEqual(result["status"], "PUBLISHED_MAP_RESIDUALS_NOT_DR70_FIDELITY")

    def test_literal_degree_and_absolute_number_must_match(self):
        self.publication["source_notation"]["cusp_1"]["literal"] = "2°"
        with self.assertRaisesRegex(ValueError, "printed literal"):
            compare(self.reference, self.publication)
        self.publication["source_notation"]["cusp_1"]["literal"] = "not a number at all"
        with self.assertRaisesRegex(ValueError, "unrecognized absolute"):
            compare(self.reference, self.publication)
        self.publication["source_notation"]["cusp_1"]["literal"] = "1°"
        self.publication["source_notation"]["sun"]["literal"] = "8°30 Libra"
        with self.assertRaisesRegex(ValueError, "literal degree"):
            compare(self.reference, self.publication)

    def test_unrecognized_glyph_and_invalid_minutes_fail_closed(self):
        self.publication["source_notation"]["sun"]["literal"] = "7°30 ♎"
        with self.assertRaisesRegex(ValueError, "unrecognized zodiac"):
            compare(self.reference, self.publication)
        self.publication["source_notation"]["sun"]["literal"] = "7°90 Libra"
        with self.assertRaisesRegex(ValueError, "degree-minute"):
            compare(self.reference, self.publication)
        self.publication["source_notation"]["sun"]["literal"] = "7.5 Libra"
        result = compare(self.reference, self.publication)
        self.assertEqual(len(result["residuals_deg"]), 2)

    def test_reject_json_float_overflow_even_in_ignored_fields(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "overflow.json"
            for text in ('{"ignored":1e999}', '{"ignored":{"value":-1e999}}'):
                path.write_text(text, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "Non-finite JSON numeric"):
                    strict_json(path)
            path.write_text('{"safe":1.5}', encoding="utf-8")
            self.assertEqual(strict_json(path)["safe"], 1.5)

    def test_reject_duplicate_json_keys(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"a":1,"\\u0061":2}', encoding="utf-8")
            with self.assertRaises(ValueError):
                strict_json(path)


if __name__ == "__main__":
    unittest.main()
