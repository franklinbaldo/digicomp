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
            "published_values_deg": {"cusp_1": 1.0, "sun": 187.5}
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

    def test_reject_duplicate_json_keys(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"a":1,"\\u0061":2}', encoding="utf-8")
            with self.assertRaises(ValueError):
                strict_json(path)


if __name__ == "__main__":
    unittest.main()
