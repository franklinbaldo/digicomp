"""Negative and positive contract tests, never a historical angular fixture."""

from copy import deepcopy
import json
from pathlib import Path
import unittest

from scripts.carter_historical_intake import _unique, validate


class CarterHistoricalIntakeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = json.loads(Path("data/documentary/carter-french-1982-caption-locator.json").read_text(encoding="utf-8"))

    def test_real_locator_has_no_angle_or_fake_fidelity(self):
        result = validate(self.original)
        self.assertEqual(result["fields_transcribed"], 0)
        self.assertEqual(result["state"], "INDEXED_CAPTION_ONLY")
        self.assertEqual(result["angular_comparison"], "NOT_RUN_REQUIRES_BLIND_TRANSCRIPTION_REVIEW")
        self.assertEqual(result["dr70_fidelity"], "NOT_RUN_NO_GOLDEN")
        self.assertEqual(
            result["edition_identity"],
            "BNF_1997_ISBN_MATCH_NOT_SCAN_AUTHENTICATION",
        )

    def test_isbn_match_does_not_authenticate_scanned_edition(self):
        for field, changed in (
            ("ocr_isbn", "2-268-00163-6"),
            ("edition_identity", "AUTHENTICATED_1997_PRINTING"),
            ("copy_description", "FRENCH_ORIGINAL_1982_PRINTING"),
        ):
            bad = deepcopy(self.original)
            bad[field] = changed
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate(bad)

    def test_cannot_attach_angle_or_scan_to_ocr_only(self):
        for key, value in (("angular_transcriptions", [{"field": "Sun", "verbatim": "8° Libra"}]),
                           ("image_evidence", {"sha256": "a" * 64})):
            bad = deepcopy(self.original)
            bad[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                validate(bad)

    def test_cannot_promote_editorial_to_instrumental(self):
        bad = deepcopy(self.original)
        bad["instrumental_status"] = "DR70_GOLDEN"
        with self.assertRaises(ValueError):
            validate(bad)
        bad = deepcopy(self.original)
        bad["source_family"] = "INDEPENDENT_MACHINE"
        with self.assertRaises(ValueError):
            validate(bad)

    def test_requires_image_before_claiming_visual_inspection(self):
        for state in ("INSPECTED_UNREADABLE", "INSPECTED_TRANSCRIBED"):
            bad = deepcopy(self.original)
            bad["state"] = state
            with self.subTest(state=state), self.assertRaises(ValueError):
                validate(bad)

    def _synthetic_inspected(self):
        future = deepcopy(self.original)
        future["image_evidence"] = {
            "printed_page_read": 362,
            "digital_page_index": 365,
            "sha256": "a" * 64,
            "inspected_at_utc": "2026-11-23T05:00:00Z"
        }
        future["state"] = "INSPECTED_UNREADABLE"
        return future

    def test_synthetic_unreadable_scan_keeps_zero_angles(self):
        result = validate(self._synthetic_inspected())
        self.assertEqual(result["fields_transcribed"], 0)
        self.assertEqual(result["state"], "INSPECTED_UNREADABLE")
        self.assertEqual(result["dr70_fidelity"], "NOT_RUN_NO_GOLDEN")

    def test_synthetic_transcription_not_automatically_compared(self):
        future = self._synthetic_inspected()
        future["state"] = "INSPECTED_TRANSCRIBED"
        future["angular_transcriptions"] = [{"field": "Sun", "verbatim": "Libra 8° 03′"}]
        result = validate(future)
        self.assertEqual(result["fields_transcribed"], 1)
        self.assertEqual(result["angular_comparison"], "NOT_RUN_REQUIRES_BLIND_TRANSCRIPTION_REVIEW")
        self.assertEqual(result["dr70_fidelity"], "NOT_RUN_NO_GOLDEN")

    def test_rejects_duplicate_and_uncertain_synthetic_fields(self):
        future = self._synthetic_inspected()
        future["state"] = "INSPECTED_TRANSCRIBED"
        for rows in (
            [{"field": "Sun", "verbatim": "8°? Libra"}],
            [{"field": "Sun", "verbatim": "8° Libra"}, {"field": "Sun", "verbatim": "9° Libra"}],
            [{"field": "Sun", "verbatim": "8° Libra", "computed": 188.2}],
        ):
            future["angular_transcriptions"] = rows
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                validate(future)

    def test_rejects_bad_scan_digests_and_page_indices(self):
        for field, value in (("sha256", "not-a-hash"), ("digital_page_index", True),
                             ("printed_page_read", 0), ("inspected_at_utc", "local time")):
            bad = self._synthetic_inspected()
            bad["image_evidence"][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate(bad)

    def test_rejects_nonscalar_state_and_field(self):
        bad = deepcopy(self.original)
        bad["state"] = []
        with self.assertRaises(ValueError):
            validate(bad)
        bad = self._synthetic_inspected()
        bad["state"] = "INSPECTED_TRANSCRIBED"
        bad["angular_transcriptions"] = [{"field": [], "verbatim": "8° Libra"}]
        with self.assertRaises(ValueError):
            validate(bad)

    def test_rejects_unknown_keys_and_duplicate_json_keys(self):
        bad = deepcopy(self.original)
        bad["source_independence"] = 2
        with self.assertRaises(ValueError):
            validate(bad)
        with self.assertRaisesRegex(ValueError, "Duplicate JSON"):
            json.loads('{"state":1,"state":2}', object_pairs_hook=_unique)


if __name__ == "__main__":
    unittest.main()
