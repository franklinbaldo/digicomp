"""Guardrail tests for provenance-aware candidate outputs."""
import copy
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_output_candidates import validate


class CandidateCatalogTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "data/output-candidates/catalog.json").read_text(encoding="utf-8"))

    def test_catalog_has_no_partition_violations(self):
        self.assertEqual(validate(self.data), [])

    def test_same_carlson_figure_cannot_cross_splits(self):
        data = copy.deepcopy(self.data)
        data["entries"][0]["sample_split"] = "development"
        data["entries"][1]["sample_split"] = "holdout"
        violations = validate(data)
        self.assertTrue(any("family leakage" in s for s in violations), violations)
        self.assertTrue(any("holdout without complete" in s for s in violations), violations)

    def test_display_photo_is_not_a_numeric_holdout(self):
        data = copy.deepcopy(self.data)
        data["entries"][2]["numeric_holdout_eligible"] = True
        self.assertTrue(any("eligibility unsupported" in s for s in validate(data)))

    def test_future_independent_complete_case_may_be_reserved(self):
        data = copy.deepcopy(self.data)
        item = copy.deepcopy(data["entries"][0])
        item.update(id="DR70-FUTURE-FAKE-TEST-ONLY", family_id="FAKE-DIFFERENT-SESSION",
                    kind="device_session_output", status="reviewed", sample_split="holdout",
                    replayable=True, input_complete=True, output_complete=True,
                    numeric_holdout_eligible=True)
        data["entries"].append(item)
        self.assertEqual(validate(data), [])

    def test_duplicate_id_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["entries"].append(copy.deepcopy(data["entries"][0]))
        self.assertTrue(any("duplicate id" in s for s in validate(data)))


if __name__ == "__main__":
    unittest.main()
