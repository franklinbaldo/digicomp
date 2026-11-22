"""Guardrail tests for provenance-aware candidate outputs."""
import copy
import json
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_output_candidates import validate, load_all
# Reuse the existing SHA-exact catalog workflow for documentary validation.
from test_documentary_observations import DocumentaryCarlsonBridgeTest  # noqa: F401


class CandidateCatalogTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load_all()

    def test_twenty_book_charts_are_inventory_candidates_not_golden(self):
        book = [e for e in self.data['entries'] if e['id'].startswith('OUT-RUDHYAR-RAEL-')]
        self.assertEqual(len(book), 20)
        self.assertTrue(all(e['sample_split'] == 'unassigned' and not e['numeric_holdout_eligible'] for e in book))

    def test_workflow_checks_out_exact_event_head(self):
        # Green requires the literal event HEAD, not a synthetic merge ref.
        # A skipped verification or replaced shell command breaks adjacency.
        workflow = (ROOT / ".github/workflows/output-catalog.yml").read_text(
            encoding="utf-8"
        )
        required = (
            "      - uses: actions/checkout@v4\n"
            "        with:\n"
            "          ref: ${{ github.event.pull_request.head.sha || github.sha }}\n"
            "          persist-credentials: false\n"
            "      - name: Verify exact catalog checkout SHA\n"
            "        env:\n"
            "          EXPECTED_SHA: ${{ github.event.pull_request.head.sha || github.sha }}\n"
            '        run: test "$(git rev-parse HEAD)" = "$EXPECTED_SHA"\n'
            "      - name: Catalog checks (not historical authenticity)\n"
        )
        self.assertIn(required, workflow)

    def test_workflow_selects_shared_lexical_dependencies(self):
        # Static path-filter regression: a change to the imported lexical
        # predicate or its normative schema must run the catalog job,
        # while unrelated files must not trigger this selective workflow.
        import re

        workflow = (ROOT / ".github/workflows/output-catalog.yml").read_text(
            encoding="utf-8"
        )
        blocks = re.findall(r"(?m)^    paths:\n((?:      - '[^']+'\n)+)", workflow)
        self.assertEqual(len(blocks), 2, "expected pull_request and push filters")
        expected = {
            "data/output-candidates/**",
            "scripts/check_output_candidates.py",
            "scripts/reconstruction_gate.py",
            "data/fidelity/corpus.schema.json",
            "tests/test_output_candidates.py",
            ".github/workflows/output-catalog.yml",
        }
        for block in blocks:
            paths = set(re.findall(r"(?m)^      - '([^']+)'$", block))
            self.assertEqual(paths, expected)

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

    def test_family_whitespace_alias_cannot_cross_splits(self):
        # Synthetic distinct sources and sessions: only the provenance family
        # is shared. Whitespace must not launder a development case into holdout.
        base = self.data["entries"][0]

        def synthetic(label, family, split):
            item = copy.deepcopy(base)
            item.update(
                id=f"FAKE-{label}", family_id=family,
                source_url=f"https://example.invalid/{label}",
                locator=f"independent fake document {label}",
                kind="device_session_output", status="reviewed",
                attribution="device_native_session_output",
                sample_split=split, replayable=True,
                input_complete=True, output_complete=True,
                numeric_holdout_eligible=True,
                literal_fragments=["FAKE-OUTPUT"],
                instrumental_evidence={
                    "device_identifier": "FAKE-DEVICE",
                    "session_locator": f"FAKE-SESSION-{label}",
                    "input_as_entered": "FAKE-INPUT",
                    "key_sequence": ["FAKE-KEY"],
                    "output_channel": "printer",
                    "output_literal": "FAKE-OUTPUT",
                    "independent_reviewer": "FAKE-REVIEWER",
                    "independent_review_reference": "https://example.invalid/review",
                },
            )
            return item

        left = synthetic("DEV", "FAKE-FAMILY", "development")
        right = synthetic("HELD", "  FAKE-FAMILY \t", "holdout")
        violations = validate({"entries": [left, right]})
        self.assertTrue(any("family leakage" in e for e in violations), violations)
        right["family_id"] = "FAKE-OTHER-FAMILY"
        self.assertEqual(validate({"entries": [left, right]}), [])
        right["family_id"] = " \t "
        self.assertTrue(any("missing provenance family" in e
                            for e in validate({"entries": [right]})))
        right["family_id"] = "FAKE-OTHER-FAMILY"
        right["sample_split"] = "unassigned"
        self.assertEqual(validate({"entries": [right]}), [])

    def test_duplicate_id_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["entries"].append(copy.deepcopy(data["entries"][0]))
        self.assertTrue(any("duplicate id" in s for s in validate(data)))


    def _parse_synthetic_catalog(self, payload):
        # Only synthetic documents in the temporary sandbox. These are never
        # output candidates and cannot enter the observational corpus.
        with tempfile.TemporaryDirectory() as directory:
            target = pathlib.Path(directory)
            (target / "fixture.json").write_text(payload, encoding="utf-8")
            with patch("check_output_candidates.CATALOG_DIR", target):
                return load_all()

    def test_json_parser_preserves_unique_valid_properties(self):
        result = self._parse_synthetic_catalog(
            '{"entries":[{"id":"FAKE","sample_split":"unassigned"}]}'
        )
        self.assertEqual(result["entries"][0]["id"], "FAKE")

    def test_duplicate_json_split_rejected_before_validation(self):
        with self.assertRaisesRegex(ValueError, "duplicate JSON property"):
            self._parse_synthetic_catalog(
                '{"entries":[{"id":"FAKE","sample_split":"holdout",'
                '"sample_split":"unassigned"}]}'
            )

    def test_duplicate_json_entries_rejected_before_validation(self):
        with self.assertRaisesRegex(ValueError, "duplicate JSON property"):
            self._parse_synthetic_catalog(
                '{"entries":[{"id":"FAKE"}],"entries":[]}'
            )

    def test_duplicate_json_escaped_property_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate JSON property"):
            self._parse_synthetic_catalog(
                r'{"entries":[],"\u0065ntries":[{"id":"FAKE"}]}'
            )

    def test_duplicate_json_nested_output_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate JSON property"):
            self._parse_synthetic_catalog(
                '{"entries":[{"instrumental_evidence":'
                '{"output_literal":"FAKE-A","output_literal":"FAKE-B"}}]}'
            )

    def test_non_json_numeric_constants_rejected(self):
        for constant in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(constant=constant):
                with self.assertRaisesRegex(ValueError, "non-JSON numeric constant"):
                    self._parse_synthetic_catalog(
                        '{"entries":[],"extra":' + constant + '}'
                    )


    def test_non_finite_exponent_json_number_rejected_at_loader(self):
        # JSON syntax accepts an exponent, but Python float conversion may
        # overflow silently to infinity; it must never enter the catalog.
        for token in ("1e999", "-1e999", "1e309"):
            with self.subTest(token=token):
                with self.assertRaisesRegex(ValueError, "non-finite JSON number"):
                    self._parse_synthetic_catalog(
                        '{"entries":[],"extra":' + token + '}'
                    )
        self.assertEqual(
            self._parse_synthetic_catalog('{"entries":[],"extra":1.25e2}'),
            {"entries": []},
        )

    def test_invisible_only_instrumental_io_cannot_be_holdout(self):
        # Entirely fictional case. Controls can be preserved in raw
        # evidence, but they are not legible input, keys or output.
        original = self.data["entries"][0]
        for invisible in ("\u200b", "\u2060", "\ufeff", "\x00", "\x1b"):
            with self.subTest(invisible=repr(invisible)):
                item = copy.deepcopy(original)
                item.update(
                    id="FAKE-CONTROL-ONLY",
                    family_id="FAKE-INDEPENDENT-FAMILY",
                    source_url="https://example.invalid/control-only",
                    locator="fake independent session",
                    kind="device_session_output",
                    status="reviewed",
                    attribution="device_native_session_output",
                    sample_split="holdout",
                    replayable=True,
                    input_complete=True,
                    output_complete=True,
                    numeric_holdout_eligible=True,
                    literal_fragments=[invisible],
                    instrumental_evidence={
                        "device_identifier": "FAKE-DEVICE",
                        "session_locator": "FAKE-SESSION",
                        "input_as_entered": invisible,
                        "key_sequence": [invisible],
                        "output_channel": "printer",
                        "output_literal": invisible,
                        "independent_reviewer": "FAKE-REVIEWER",
                        "independent_review_reference": "https://example.invalid/review",
                    },
                )
                errors = validate({"entries": [item]})
                self.assertTrue(
                    any("holdout missing instrumental evidence" in err for err in errors),
                    errors,
                )
                self.assertTrue(
                    any("numeric holdout eligibility unsupported" in err for err in errors),
                    errors,
                )

        # Visible text mixed with raw controls is still a valid transcription.
        item["instrumental_evidence"]["input_as_entered"] = "FAKE-INPUT\x00"
        item["instrumental_evidence"]["key_sequence"] = ["FAKE-KEY\u200b"]
        item["instrumental_evidence"]["output_literal"] = "FAKE-OUTPUT\x1b"
        item["literal_fragments"] = ["FAKE-OUTPUT"]
        self.assertEqual(validate({"entries": [item]}), [])


if __name__ == "__main__":
    unittest.main()
