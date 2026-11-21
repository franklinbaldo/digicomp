"""Synthetic-only regression tests for mandatory DR-70 schema validation."""

from __future__ import annotations

import json
import importlib.util
import tempfile
import unittest
from pathlib import Path

from scripts.check_fidelity_corpus import CorpusError, check_corpus
from scripts.check_fidelity_schema import check_schema


def fake_case() -> dict[str, object]:
    """Structurally complete fixture. This is not a historical observation."""
    return {
        "id": "DR70-FAKE-TEST",
        "status": "partial",
        "source": {
            "catalog_ref": "F999",
            "url": "https://example.invalid/fake",
            "locator": "fake frame 1",
            "medium": "transcription",
            "directness": "secondary_report",
        },
        "device": {"model": "DR-70", "serial": None, "variant": None},
        "as_entered": {
            "date_literal": None,
            "time_literal": None,
            "timezone_literal": None,
            "place_literal": None,
            "latitude_literal": None,
            "longitude_literal": None,
            "keys_literal": None,
        },
        "observed_output": {"channel": "unknown", "literal": None},
    }


@unittest.skipUnless(
    importlib.util.find_spec("jsonschema") is not None,
    "jsonschema[format]==4.26.0 absent; mandatory uvx prek hook runs these cases",
)
class FidelitySchemaTests(unittest.TestCase):
    def setUp(self) -> None:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.path = Path(temp.name) / "observations.json"

    def write(self, case: dict[str, object] | None) -> None:
        payload = {
            "format_version": "1.0",
            "subject": "Digicomp DR-70",
            "observations": [] if case is None else [case],
        }
        self.path.write_text(json.dumps(payload), encoding="utf-8")

    def test_empty_corpus_passes(self) -> None:
        self.write(None)
        self.assertEqual(check_schema(self.path), 0)

    def test_partial_with_no_input_and_no_output_is_rejected(self) -> None:
        # A source citation alone is not an observed DR-70 input/output.
        self.write(fake_case())
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_partial_with_only_a_literal_input_passes_structurally(self) -> None:
        # This remains synthetic: the gate does not authenticate the device.
        case = fake_case()
        case["as_entered"]["date_literal"] = "FAKE DATE"
        self.write(case)
        self.assertEqual(check_schema(self.path), 1)

    def test_partial_with_only_a_literal_output_passes_structurally(self) -> None:
        case = fake_case()
        case["observed_output"] = {"channel": "led", "literal": "FAKE DISPLAY"}
        self.write(case)
        self.assertEqual(check_schema(self.path), 1)

    def test_partial_with_only_whitespace_input_is_rejected(self) -> None:
        # A blank cell is not an observed input, even when nonempty as a string.
        case = fake_case()
        case["as_entered"]["date_literal"] = "   "
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_partial_with_only_whitespace_output_is_rejected(self) -> None:
        case = fake_case()
        case["observed_output"]["literal"] = "   "
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_replayable_with_whitespace_only_key_is_rejected(self) -> None:
        case = fake_case()
        case["status"] = "replayable"
        case["source"]["directness"] = "device_observation"
        case["as_entered"]["keys_literal"] = ["   "]
        case["observed_output"] = {"channel": "led", "literal": "FAKE OUTPUT"}
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_replayable_with_whitespace_only_output_is_rejected(self) -> None:
        case = fake_case()
        case["status"] = "replayable"
        case["source"]["directness"] = "device_observation"
        case["as_entered"]["keys_literal"] = ["FAKE KEY"]
        case["observed_output"] = {"channel": "led", "literal": "   "}
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_partial_nul_is_not_an_observed_input(self) -> None:
        # A NUL is non-whitespace but has no visible evidence glyph.
        case = fake_case()
        case["as_entered"]["date_literal"] = "\u0000"
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_partial_escape_only_output_is_rejected(self) -> None:
        case = fake_case()
        case["observed_output"]["literal"] = "\u001b"
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_replayable_del_only_key_is_rejected(self) -> None:
        case = fake_case()
        case["status"] = "replayable"
        case["source"]["directness"] = "device_observation"
        case["as_entered"]["keys_literal"] = ["\u007f"]
        case["observed_output"] = {"channel": "printer", "literal": "FAKE OUTPUT"}
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_visible_literal_next_to_controls_still_passes(self) -> None:
        case = fake_case()
        case["as_entered"]["date_literal"] = "\u0000FAKE DATE\u001b"
        self.write(case)
        self.assertEqual(check_schema(self.path), 1)

    def test_partial_zero_width_space_is_not_a_literal(self) -> None:
        case = fake_case()
        case["as_entered"]["date_literal"] = "\u200b"
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_partial_word_joiner_is_not_output(self) -> None:
        case = fake_case()
        case["observed_output"]["literal"] = "\u2060"
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_replayable_bom_is_not_a_key(self) -> None:
        case = fake_case()
        case["status"] = "replayable"
        case["source"]["directness"] = "device_observation"
        case["as_entered"]["keys_literal"] = ["\ufeff"]
        case["observed_output"] = {"channel": "led", "literal": "FAKE OUTPUT"}
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_visible_glyph_surrounded_by_controls_still_passes(self) -> None:
        case = fake_case()
        case["as_entered"]["date_literal"] = "\u200bFAKE DATE\u2060"
        self.write(case)
        self.assertEqual(check_schema(self.path), 1)

    def test_partial_visible_literal_with_surrounding_whitespace_passes(self) -> None:
        case = fake_case()
        case["as_entered"]["date_literal"] = "  FAKE DATE  "
        self.write(case)
        self.assertEqual(check_schema(self.path), 1)

    def test_replayable_synthetic_structure_passes_without_authenticating(self) -> None:
        case = fake_case()
        case["status"] = "replayable"
        case["source"]["directness"] = "contemporaneous_report"
        case["as_entered"]["keys_literal"] = ["FAKE KEY"]
        case["observed_output"] = {"channel": "printer", "literal": "FAKE OUTPUT"}
        self.write(case)
        self.assertEqual(check_schema(self.path), 1)

    def test_missing_fields_are_rejected_even_when_identity_checker_passes(self) -> None:
        case = {"id": "DR70-FAKE-TEST", "status": "replayable"}
        self.write(case)
        self.assertEqual(check_corpus(self.path), 1)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_secondary_report_cannot_be_replayable(self) -> None:
        case = fake_case()
        case["status"] = "replayable"
        case["as_entered"]["keys_literal"] = ["FAKE KEY"]
        case["observed_output"] = {"channel": "printer", "literal": "FAKE OUTPUT"}
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_replayable_requires_keys(self) -> None:
        case = fake_case()
        case["status"] = "replayable"
        case["source"]["directness"] = "device_observation"
        case["observed_output"] = {"channel": "led", "literal": "FAKE OUTPUT"}
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_replayable_requires_output(self) -> None:
        case = fake_case()
        case["status"] = "replayable"
        case["source"]["directness"] = "device_observation"
        case["as_entered"]["keys_literal"] = ["FAKE KEY"]
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_as_entered_rejects_numeric_timezone(self) -> None:
        case = fake_case()
        case["as_entered"]["timezone_literal"] = -4
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_source_rejects_bad_url(self) -> None:
        case = fake_case()
        case["source"]["url"] = "not-a-url"
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_capture_date_format_is_checked(self) -> None:
        case = fake_case()
        case["source"]["capture_date"] = "2026-02-30"
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_unexpected_field_is_rejected(self) -> None:
        case = fake_case()
        case["synthetic_claimed_golden"] = True
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_duplicate_properties_still_fail_closed(self) -> None:
        self.path.write_text(
            '{"format_version":"1.0","subject":"Digicomp DR-70",'
            '"observations":[],"observations":[]}', encoding="utf-8"
        )
        with self.assertRaisesRegex(CorpusError, "duplicate JSON property"):
            check_schema(self.path)


    def test_unpaired_surrogates_are_not_observed_literals(self) -> None:
        # JSON escape decoding permits these invalid Unicode scalar values.
        for raw in ("\ud800", "\udfff"):
            for field in ("date_literal", "time_literal"):
                with self.subTest(raw=ascii(raw), field=field):
                    case = fake_case()
                    case["as_entered"][field] = raw
                    self.write(case)
                    with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
                        check_schema(self.path)
            with self.subTest(raw=ascii(raw), field="output"):
                case = fake_case()
                case["observed_output"] = {"channel": "led", "literal": raw}
                self.write(case)
                with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
                    check_schema(self.path)

    def test_unpaired_surrogate_is_not_a_replayable_key(self) -> None:
        case = fake_case()
        case["status"] = "replayable"
        case["source"]["directness"] = "device_observation"
        case["as_entered"]["keys_literal"] = ["\ud800"]
        case["observed_output"] = {"channel": "led", "literal": "FAKE OUTPUT"}
        self.write(case)
        with self.assertRaisesRegex(CorpusError, "JSON Schema violation"):
            check_schema(self.path)

    def test_visible_unicode_text_still_counts_as_literal(self) -> None:
        case = fake_case()
        case["as_entered"]["date_literal"] = "FAKE \u00c9"
        self.write(case)
        self.assertEqual(check_schema(self.path), 1)


    def test_supplementary_plane_glyph_remains_legible(self) -> None:
        # JSON Schema is also consumed by ECMAScript regex engines, where
        # a visible astral glyph is encoded by a UTF-16 surrogate pair.
        case = fake_case()
        case["as_entered"]["date_literal"] = "\U0001F600"
        self.write(case)
        self.assertEqual(check_schema(self.path), 1)


if __name__ == "__main__":
    unittest.main()
