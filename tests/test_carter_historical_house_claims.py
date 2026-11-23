"""Contrast 13:00 UT published candidate with a 12:00 UT counterfactual.

Historical data are qualitative house numbers in secondary indexed prose.
Computed values are modern Swiss/Moshier Campanus, never DR-70 output.
"""

from __future__ import annotations

from copy import deepcopy
import unittest

from scripts.chart_input_candidates import load
from scripts.carter_historical_house_claims import compare_houses

try:
    import swisseph as swe
except ImportError:
    swe = None


@unittest.skipUnless(swe is not None, "optional Swiss research binding absent")
class CarterHistoricalHouseClaimsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = next(c for c in load()["cases"] if c["id"] == "RAEL1980-CARTER")
        cls.control12 = deepcopy(cls.case)
        cls.control12["utc_time_as_printed"] = "12:00"
        cls.control12["time_interpretation"] = "COUNTERFACTUAL: not a printed input"

    def test_thirteen_ut_matches_four_textual_house_claims(self):
        result = compare_houses(self.case, swe)
        self.assertEqual(result["input_variant"], "DOCUMENTARY_TRANSCRIPTION_13_UT")
        self.assertEqual(result["utc_interpreted"], "1924-10-01T13:00:00Z")
        self.assertEqual(result["matched_claims"], 4)
        self.assertEqual(result["total_claims_same_editorial_family"], 4)
        actual = {c["body"]: c["modern_campanus_house"] for c in result["claims"]}
        self.assertEqual(actual, {
            "moon": 1, "mercury": 11, "pluto": 9, "uranus": 5,
        })
        # This also guards against dropping ecliptic latitude in house_pos.
        fractional = {c["body"]: c["modern_fractional_house"] for c in result["claims"]}
        for name, expected in (
            ("moon", 1.542054), ("mercury", 11.805797),
            ("pluto", 9.489261), ("uranus", 5.724119),
        ):
            with self.subTest(body=name):
                self.assertAlmostEqual(fractional[name], expected, places=3)

    def test_twelve_ut_matches_only_two_of_four(self):
        result = compare_houses(self.control12, swe)
        self.assertEqual(result["input_variant"],
                         "COUNTERFACTUAL_12_UT_NOT_THE_PUBLISHED_INPUT")
        self.assertEqual(result["utc_interpreted"], "1924-10-01T12:00:00Z")
        self.assertEqual(result["matched_claims"], 2)
        actual = {c["body"]: c["modern_campanus_house"] for c in result["claims"]}
        self.assertEqual(actual, {
            "moon": 1, "mercury": 12, "pluto": 9, "uranus": 6,
        })

    def test_historical_numeric_and_instrumental_fidelity_remain_unknown(self):
        for case in (self.case, self.control12):
            with self.subTest(hour=case["utc_time_as_printed"]):
                r = compare_houses(case, swe)
                self.assertEqual(r["classification"],
                                 "MODERN_CAMPANUS_VS_SECONDARY_HISTORICAL_HOUSE_PROSE")
                self.assertEqual(r["historical_claim_status"],
                                 "INDEXED_SECONDARY_TEXT_NOT_CHECKED_AGAINST_1980_PAGE")
                self.assertEqual(r["interpretation"],
                                 "QUALITATIVE_MODEL_CONSISTENCY_ONLY_NOT_INSTRUMENTAL_VALIDATION")
                self.assertEqual(r["historical_numeric_residuals"],
                                 "NOT_RUN_NO_INSPECTED_1980_CHART")
                self.assertEqual(r["dr70_fidelity"], "NOT_RUN_NO_GOLDEN")

    def test_wrong_input_and_promoted_golden_are_rejected(self):
        for changed in (
            {"id": "WRONG"}, {"utc_time_as_printed": "14:00"},
            {"latitude_as_printed": "32N03"},
            {"longitude_as_printed": "84W23"},
            {"observed_chart_values": {"invented": 1}},
            {"status": "DR70_GOLDEN"},
        ):
            with self.subTest(changed=changed):
                case = deepcopy(self.case)
                case.update(changed)
                with self.assertRaises(ValueError):
                    compare_houses(case, swe)


if __name__ == "__main__":
    unittest.main()
