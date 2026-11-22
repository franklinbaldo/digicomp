"""All numbers in these test fixtures are synthetic and never a DR-70 output."""

from pathlib import Path
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
                       "reviewed_by": "unit-test", "source_url": "synthetic://unit-test"},
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

    def test_reject_duplicate_json_keys(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"a":1,"\\u0061":2}', encoding="utf-8")
            with self.assertRaises(ValueError):
                strict_json(path)


if __name__ == "__main__":
    unittest.main()
