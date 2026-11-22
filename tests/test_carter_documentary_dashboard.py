"""Pure-stdlib rendering guards with synthetic UI fixtures, not observations."""

from __future__ import annotations

from copy import deepcopy
import unittest

from scripts.carter_documentary_dashboard import assemble, render
from scripts.carter_historical_house_claims import HOUSE_CLAIMS, TEXT_URL
from scripts.carter_modern_table import FIELDS


class CarterDocumentaryDashboardTest(unittest.TestCase):
    def setUp(self):
        self.modern = {
            "case_id": "RAEL1980-CARTER", "historical": "NOT_RUN_NO_INSPECTED_1980_NUMBERS",
            "dr70": "NOT_RUN_NO_GOLDEN", "compared": 9, "within_tolerance": 9,
            "rows": [{"field": name, "published_2023": "Libra 1° 0′ 0″",
                      "model_longitude_deg": 181., "residual_arcsec": 0.,
                      "within_declared_tolerance": True} for name in FIELDS],
        }
        claims = [{"body": body, "historical_text_house": expected,
                   "source_text_line_range_not_printed_page": locator,
                   "modern_campanus_house": expected,
                   "qualitative_match": True} for body, (expected, locator) in HOUSE_CLAIMS.items()]
        template = {"classification": "MODERN_CAMPANUS_VS_SECONDARY_HISTORICAL_HOUSE_PROSE",
                    "historical_claim_status": "INDEXED_SECONDARY_TEXT_NOT_CHECKED_AGAINST_1980_PAGE",
                    "historical_numeric_residuals": "NOT_RUN_NO_INSPECTED_1980_CHART",
                    "dr70_fidelity": "NOT_RUN_NO_GOLDEN", "source": TEXT_URL,
                    "total_claims_same_editorial_family": 4, "matched_claims": 4,
                    "claims": claims}
        self.historical = deepcopy(template)
        self.historical.update(input_variant="DOCUMENTARY_TRANSCRIPTION_13_UT", utc_interpreted="1924-10-01T13:00:00Z")
        self.counterfactual = deepcopy(template)
        self.counterfactual.update(input_variant="COUNTERFACTUAL_12_UT_NOT_THE_PUBLISHED_INPUT", utc_interpreted="1924-10-01T12:00:00Z")
        for name, wrong_house in (("mercury", 12), ("uranus", 6)):
            item = next(x for x in self.counterfactual["claims"] if x["body"] == name)
            item["modern_campanus_house"] = wrong_house
            item["qualitative_match"] = False
        self.counterfactual["matched_claims"] = 2

    def test_two_evidence_tiers_and_categorical_match_counts(self):
        result = assemble(self.modern, self.historical, self.counterfactual)
        self.assertEqual(result["historical_house_prose"]["matches_13_ut"], 4)
        self.assertEqual(result["historical_house_prose"]["matches_12_ut_counterfactual"], 2)
        output = render(result)
        for token in ("9/9", "13 UT: 4/4", "counterfactual: 2/4", "NOT_RUN_NO_GOLDEN",
                      "NOT_RUN_NO_INSPECTED_1980_CHART", "no inspected 1980", "Non-unique",
                      "One editorial family"):
            self.assertIn(token, output)

    def test_rejects_historical_promotion_or_ambiguous_duplicate_claim(self):
        for patch in ({"dr70_fidelity": "PASS"}, {"historical_claim_status": "INSPECTED"},
                      {"total_claims_same_editorial_family": 5}):
            bad = deepcopy(self.historical)
            bad.update(patch)
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                assemble(self.modern, bad, self.counterfactual)
        bad = deepcopy(self.historical)
        bad["claims"][1]["body"] = "moon"
        with self.assertRaises(ValueError):
            assemble(self.modern, bad, self.counterfactual)

    def test_rejects_numeric_promotion_or_changed_counterfactual(self):
        bad = deepcopy(self.modern)
        bad["dr70"] = "PASS"
        with self.assertRaises(ValueError):
            assemble(bad, self.historical, self.counterfactual)
        bad = deepcopy(self.counterfactual)
        bad["utc_interpreted"] = "1924-10-01T13:00:00Z"
        with self.assertRaises(ValueError):
            assemble(self.modern, self.historical, bad)

    def test_rejects_fabricated_house_match_flag(self):
        bad = deepcopy(self.historical)
        bad["claims"][0]["qualitative_match"] = False
        bad["matched_claims"] = 3
        with self.assertRaises(ValueError):
            assemble(self.modern, bad, self.counterfactual)


if __name__ == "__main__":
    unittest.main()
