"""Separate book's secondary-text septile heuristic from the unknown 1980 chart."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import unittest

from scripts.carter_qualitative_relation import compare, longitude_seconds

CONTROL = (
    Path(__file__).resolve().parents[1]
    / "data/modern-controls/carter-astro-dienst-2023.json"
)


class CarterSeptileSensitivityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.control = json.loads(CONTROL.read_text(encoding="utf-8"))

    def test_modern_published_values_yield_exact_orb_threshold(self):
        result = compare(self.control)
        self.assertEqual(result["classification"],
                         "MODERN_POSITIONS_VS_SECONDARY_HISTORICAL_QUALITATIVE_CLAIM")
        self.assertEqual(result["separation_arcseconds"], 189387)
        self.assertEqual(result["exact_septile_arcseconds"],
                         {"numerator": 1296000, "denominator": 7})
        self.assertEqual(result["minimum_orb_arcseconds"],
                         {"numerator": 29709, "denominator": 7})
        self.assertEqual(result["secondary_text_nominal_range_degrees"], [50, 53])
        self.assertEqual(result["secondary_text_range_status"],
                         "HEURISTIC_WITH_EXCEPTIONS_NOT_STRICT_ORB")
        self.assertTrue(result["modern_pair_in_secondary_nominal_range"])
        self.assertEqual(result["historical_relation_test"],
                         "INDETERMINATE_NO_INSPECTED_1980_CHART")
        self.assertEqual(result["historical_chart_residual"],
                         "NOT_RUN_NO_INSPECTED_1980_NUMBERS")
        self.assertEqual(result["dr70_fidelity"], "NOT_RUN_NO_GOLDEN")

    def test_one_second_mutant_changes_threshold(self):
        data = deepcopy(self.control)
        data["positions"]["moon"]["seconds"] += 1
        data["positions"]["moon"]["literal"] = "13° 47′ 48″"
        mutated = compare(data)
        self.assertEqual(mutated["separation_arcseconds"], 189388)
        self.assertEqual(mutated["minimum_orb_arcseconds"],
                         {"numerator": 29716, "denominator": 7})
        self.assertTrue(mutated["modern_pair_in_secondary_nominal_range"])
        self.assertEqual(mutated["historical_relation_test"],
                         "INDETERMINATE_NO_INSPECTED_1980_CHART")

    def test_unresolved_historical_data_cannot_be_promoted(self):
        for key, value in (
            ("classification", "DR70_NATIVE_GOLDEN"),
            ("case_id", "SYNTHETIC"),
        ):
            with self.subTest(key=key):
                data = deepcopy(self.control)
                data[key] = value
                with self.assertRaises(ValueError):
                    compare(data)
        for key, value in (
            ("dr70_native_output", True),
            ("golden_instrumental", True),
            ("historical_chart_residuals", "PASS"),
        ):
            with self.subTest(key=key):
                data = deepcopy(self.control)
                data["scope"][key] = value
                with self.assertRaises(ValueError):
                    compare(data)

    def test_numeric_and_literal_corruptions_fail_closed(self):
        moon = self.control["positions"]["moon"]
        self.assertEqual(longitude_seconds(moon), 223 * 3600 + 47 * 60 + 47)
        for patch in (
            {"sign": "Unknown"},
            {"degrees": 30},
            {"minutes": 60},
            {"seconds": True},
            {"seconds": 47.0},
            {"literal": "13° 47′ 46″"},
            {"literal": "13° 47′ 47″ extra"},
        ):
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                longitude_seconds(dict(moon, **patch))

    def test_nominal_text_range_is_dynamic_and_not_an_historical_pass(self):
        result = compare(self.control)
        threshold = (result["minimum_orb_arcseconds"]["numerator"] /
                     result["minimum_orb_arcseconds"]["denominator"])
        self.assertGreater(threshold, 30 * 60)
        self.assertLess(threshold, 2 * 3600)
        # A modern pair outside 53° fails only the *nominal* textual range,
        # not an undocumented strict instrument or chart-fidelity test.
        outside = deepcopy(self.control)
        outside["positions"]["moon"]["degrees"] = 14
        outside["positions"]["moon"]["literal"] = "14° 47′ 47″"
        outside_result = compare(outside)
        self.assertEqual(outside_result["separation_arcseconds"], 192987)
        self.assertFalse(outside_result["modern_pair_in_secondary_nominal_range"])
        self.assertEqual(outside_result["secondary_text_range_status"],
                         "HEURISTIC_WITH_EXCEPTIONS_NOT_STRICT_ORB")
        for candidate in (result, outside_result):
            self.assertEqual(candidate["historical_relation_test"],
                             "INDETERMINATE_NO_INSPECTED_1980_CHART")
            self.assertEqual(candidate["dr70_fidelity"], "NOT_RUN_NO_GOLDEN")


if __name__ == "__main__":
    unittest.main()
