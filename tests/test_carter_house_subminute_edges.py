"""One-second Carter house consistency is a model control, never DR-70 data."""

from __future__ import annotations

from copy import deepcopy
import unittest

from scripts.chart_input_candidates import load
from scripts.carter_house_subminute_edges import _refine_edge, analyze

try:
    import swisseph as swe
except ImportError:
    swe = None


@unittest.skipUnless(swe is not None, "optional Swiss research binding absent")
class CarterHouseSubminuteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = next(c for c in load()["cases"] if c["id"] == "RAEL1980-CARTER")
        cls.result = analyze(cls.case, swe)

    def test_one_second_samples_narrow_the_minute_envelope(self):
        self.assertEqual(self.result["scanned_utc_seconds_of_day_inclusive"],
                         [36000, 57600])
        self.assertEqual(self.result["sample_interval_seconds"], 1)
        self.assertEqual(self.result["all_four_sampled_utc_seconds_inclusive"],
                         [[45270, 50602]])
        self.assertEqual(self.result["matching_sample_count"], 5333)

    def test_bisected_edges_stay_inside_sample_cells(self):
        self.assertAlmostEqual(
            self.result["entry_transition_utc_second_of_day_approx"],
            45269.58, delta=0.02,
        )
        self.assertAlmostEqual(
            self.result["exit_transition_utc_second_of_day_approx"],
            50602.14, delta=0.02,
        )
        self.assertEqual(self.result["edge_bisection_bracket_width_seconds_at_most"],
                         0.01)

    def test_no_instrumental_or_birth_time_precision_inferred(self):
        self.assertEqual(self.result["classification"],
                         "MODERN_CAMPANUS_SECOND_GRID_NOT_HISTORICAL_MEASUREMENT")
        self.assertEqual(self.result["editorial_family_count"], 1)
        self.assertEqual(self.result["subsecond_continuity"],
                         "NOT_PROVED_BY_DISCRETE_GRID")
        self.assertEqual(self.result["source_status"],
                         "INDEXED_SECONDARY_TEXT_NOT_CHECKED_AGAINST_1980_PAGE")
        self.assertEqual(self.result["historical_numeric_residuals"],
                         "NOT_RUN_NO_INSPECTED_1980_CHART")
        self.assertEqual(self.result["dr70_fidelity"], "NOT_RUN_NO_GOLDEN")

    def test_wrong_source_inputs_fail_closed(self):
        for patch in ({"utc_time_as_printed": "12:00"},
                      {"latitude_as_printed": "32N03"},
                      {"observed_chart_values": {"fabricated": True}},
                      {"status": "DR70_GOLDEN"}):
            with self.subTest(patch=patch):
                changed = deepcopy(self.case)
                changed.update(patch)
                with self.assertRaises(ValueError):
                    analyze(changed, swe)

    def test_malformed_transition_brackets_are_rejected(self):
        latitude, longitude = 32 + 2 / 60, -(84 + 24 / 60)
        with self.assertRaises(ValueError):
            _refine_edge(45269, 45271, 3, 4, latitude, longitude, swe)
        with self.assertRaises(ValueError):
            _refine_edge(45270, 45271, 3, 4, latitude, longitude, swe)
        with self.assertRaises(ValueError):
            _refine_edge(50602, 50603, 3, 4, latitude, longitude, swe)


if __name__ == "__main__":
    unittest.main()
