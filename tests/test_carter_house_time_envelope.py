"""Negative and positive boundaries for the modern Carter house-time envelope."""

from __future__ import annotations

from copy import deepcopy
import unittest

from scripts.chart_input_candidates import load
from scripts.carter_house_time_envelope import (
    START_MINUTE, END_MINUTE, _score, _windows, scan,
)

try:
    import swisseph as swe
except ImportError:
    swe = None


@unittest.skipUnless(swe is not None, "optional Swiss research binding absent")
class CarterHouseTimeEnvelopeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = next(c for c in load()["cases"] if c["id"] == "RAEL1980-CARTER")
        cls.result = scan(cls.case, swe)

    def test_scanned_interval_is_broader_than_single_published_hour(self):
        self.assertEqual(self.result["window_scanned_utc_minutes_inclusive"], [600, 960])
        self.assertEqual(self.result["resolution_minutes"], 1)
        self.assertEqual(self.result["center_all_four_intervals_utc_minutes_inclusive"],
                         [[12 * 60 + 35, 14 * 60 + 3]])
        self.assertLess(12 * 60 + 35, 13 * 60)
        self.assertGreater(14 * 60 + 3, 13 * 60)

    def test_one_minute_outside_each_edge_loses_a_match(self):
        lat, lon = 32 + 2 / 60, -(84 + 24 / 60)
        self.assertEqual([_score(m, lat, lon, swe) for m in (754, 755, 843, 844)],
                         [3, 4, 4, 3])
        self.assertEqual([_score(m, lat, lon, swe) for m in (720, 780)], [2, 4])

    def test_nine_coordinate_perturbations_do_not_select_a_unique_minute(self):
        controls = self.result["coordinate_controls"]
        self.assertEqual(len(controls), 9)
        self.assertEqual({(c["latitude_delta_arcmin"], c["longitude_east_delta_arcmin"])
                          for c in controls}, {(lat, lon)
                                                for lat in (-1, 0, 1)
                                                for lon in (-1, 0, 1)})
        for c in controls:
            with self.subTest(c=c):
                self.assertEqual(c["all_four_intervals_inclusive_utc_minutes"],
                                 [[755, 843]])
                self.assertEqual(c["matches_12_00_ut"], 2)
                self.assertEqual(c["matches_13_00_ut"], 4)

    def test_golden_and_historical_precision_are_not_inferred(self):
        self.assertEqual(self.result["editorial_family_count"], 1)
        self.assertEqual(self.result["dr70_fidelity"], "NOT_RUN_NO_GOLDEN")
        self.assertEqual(self.result["historical_numeric_residuals"],
                         "NOT_RUN_NO_INSPECTED_1980_CHART")
        self.assertEqual(self.result["interpretation"],
                         "MODEL_CONSISTENCY_WINDOW_NOT_INFERRED_BIRTH_TIME")
        self.assertEqual(self.result["source_status"],
                         "INDEXED_SECONDARY_TEXT_NOT_CHECKED_AGAINST_1980_PAGE")

    def test_wrong_inputs_and_outside_scan_do_not_succeed(self):
        for modification in ({"utc_time_as_printed": "12:00"},
                             {"latitude_as_printed": "32N03"},
                             {"status": "DR70_GOLDEN"},
                             {"observed_chart_values": {"invented": 1}}):
            with self.subTest(modification=modification):
                case = deepcopy(self.case)
                case.update(modification)
                with self.assertRaises(ValueError):
                    scan(case, swe)
        with self.assertRaises(ValueError):
            _score(START_MINUTE - 1, 0, 0, swe)
        with self.assertRaises(ValueError):
            _score(END_MINUTE + 1, 0, 0, swe)
        self.assertEqual(_windows([4, 4, 3, 4], start=600), [[600, 601], [603, 603]])
        self.assertEqual(_windows([3, 3], start=600), [])


if __name__ == "__main__":
    unittest.main()
