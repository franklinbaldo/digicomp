"""Guardrail tests for provenance-aware candidate outputs."""
import copy
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_output_candidates import validate, load_all


class CandidateCatalogTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load_all()

    def test_twenty_book_charts_are_inventory_candidates_not_golden(self):
        book = [e for e in self.data['entries'] if e['id'].startswith('OUT-RUDHYAR-RAEL-')]
        self.assertEqual(len(book), 20)
        self.assertTrue(all(e['sample_split'] == 'unassigned' and not e['numeric_holdout_eligible'] for e in book))

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
                    source_url="https://example.invalid/fictional-session",
                    locator="test-only synthetic session", kind="device_session_output",
                    status="reviewed", attribution="device_native_session_output",
                    sample_split="holdout", replayable=True, input_complete=True,
                    output_complete=True, numeric_holdout_eligible=True,
                    literal_fragments=["FAKE-NUMERIC-OUTPUT"],
                    instrumental_evidence={
                        "device_identifier": "FAKE-TEST-DEVICE",
                        "session_locator": "TEST-ONLY-SESSION",
                        "input_as_entered": "FAKE-INPUT",
                        "key_sequence": ["FAKE-KEY"],
                        "output_channel": "display",
                        "output_literal": "FAKE-NUMERIC-OUTPUT",
                        "independent_reviewer": "FAKE-REVIEWER",
                        "independent_review_reference": "https://example.invalid/review",
                    })
        data["entries"].append(item)
        self.assertEqual(validate(data), [])


    def test_holdout_flagged_lead_with_no_literal_is_rejected(self):
        # RED regression: booleans cannot certify a source that still says
        # "no output recovered", even if kind was relabeled as a session.
        data = copy.deepcopy(self.data)
        item = copy.deepcopy(data["entries"][3])
        item.update(id="DR70-FAKE-FLAG-TEST", family_id="FAKE-LEAD-FAMILY",
                    kind="device_session_output", status="lead_only",
                    attribution="no_output_recovered", sample_split="holdout",
                    replayable=True, input_complete=True, output_complete=True,
                    numeric_holdout_eligible=True, literal_fragments=[])
        data["entries"].append(item)
        violations = validate(data)
        self.assertTrue(any("holdout missing instrumental evidence" in s for s in violations), violations)

    def test_same_url_and_locator_cannot_cross_families_into_holdout(self):
        # RED regression: renaming the family must not launder a duplicate
        # source region into a supposedly independent holdout.
        data = copy.deepcopy(self.data)
        left = copy.deepcopy(data["entries"][0])
        right = copy.deepcopy(data["entries"][0])
        left.update(id="DR70-FAKE-DEV", family_id="FAKE-DEVELOPMENT",
                    sample_split="development")
        right.update(id="DR70-FAKE-HELD", family_id="FAKE-HELD",
                     kind="device_session_output", status="reviewed",
                     sample_split="holdout", replayable=True, input_complete=True,
                     output_complete=True, numeric_holdout_eligible=True)
        data["entries"].extend([left, right])
        violations = validate(data)
        self.assertTrue(any("source locator leakage" in s for s in violations), violations)

    def test_identical_instrument_session_cannot_cross_splits_by_alias(self):
        # Coruja R132: distinct source URLs, locators, and family names
        # do not make a declared physical session independent.
        data = copy.deepcopy(self.data)
        original = data["entries"][0]

        def synthetic_case(identifier, family, url, split):
            item = copy.deepcopy(original)
            item.update(
                id=identifier,
                family_id=family,
                source_url=url,
                locator=f"{identifier} fictional document",
                kind="device_session_output",
                status="reviewed",
                attribution="device_native_session_output",
                sample_split=split,
                replayable=True,
                input_complete=True,
                output_complete=True,
                numeric_holdout_eligible=True,
                literal_fragments=["FAKE-OUTPUT"],
                instrumental_evidence={
                    "device_identifier": "FAKE-DEVICE",
                    "session_locator": "FAKE-SESSION",
                    "input_as_entered": "FAKE-INPUT",
                    "key_sequence": ["FAKE-KEY"],
                    "output_channel": "printer",
                    "output_literal": "FAKE-OUTPUT",
                    "independent_reviewer": "FAKE-REVIEWER",
                    "independent_review_reference": "https://example.invalid/review",
                },
            )
            return item

        left = synthetic_case(
            "FAKE-DEV-SESSION", "FAKE-FAMILY-DEV",
            "https://example.invalid/a", "development"
        )
        right = synthetic_case(
            "FAKE-HOLD-SESSION", "FAKE-FAMILY-HOLD",
            "https://example.invalid/b", "holdout"
        )
        data["entries"].extend((left, right))
        violations = validate(data)
        self.assertTrue(any("instrument session leakage" in s for s in violations),
                        violations)

        # Same device can have truly different declared sessions.
        right["instrumental_evidence"]["session_locator"] = "FAKE-SESSION-2"
        self.assertEqual(validate(data), [])

        # The exploratory unassigned collection must stay permissive.
        right["instrumental_evidence"]["session_locator"] = "FAKE-SESSION"
        right["sample_split"] = "unassigned"
        self.assertEqual(validate(data), [])

    def test_duplicate_id_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["entries"].append(copy.deepcopy(data["entries"][0]))
        self.assertTrue(any("duplicate id" in s for s in validate(data)))


if __name__ == "__main__":
    unittest.main()
