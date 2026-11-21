"""Offline negative controls for corpus identity (all records synthetic)."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.check_fidelity_corpus import CorpusError, check_corpus, main


class FidelityIdentityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "observations.json"

    def write(self, payload: str) -> None:
        self.path.write_text(payload, encoding="utf-8")

    def test_empty_corpus_passes(self) -> None:
        self.write('{"observations": []}')
        self.assertEqual(check_corpus(self.path), 0)

    def test_distinct_ids_pass(self) -> None:
        self.write(json.dumps({"observations": [{"id": "DR70-FAKE1"}, {"id": "DR70-FAKE2"}]}))
        self.assertEqual(check_corpus(self.path), 2)

    def test_duplicate_ids_fail(self) -> None:
        self.write(json.dumps({"observations": [{"id": "DR70-FAKE1"}, {"id": "DR70-FAKE1"}]}))
        with self.assertRaisesRegex(CorpusError, "duplicate observation ID"):
            check_corpus(self.path)

    def test_duplicate_nested_key_fails(self) -> None:
        self.write('{"observations": [{"id": "DR70-FAKE1", "as_entered": {"date_literal": "A", "date_literal": "B"}}]}')
        with self.assertRaisesRegex(CorpusError, "duplicate JSON property 'date_literal'"):
            check_corpus(self.path)

    def test_duplicate_top_level_key_fails(self) -> None:
        self.write('{"observations": [], "observations": []}')
        with self.assertRaisesRegex(CorpusError, "duplicate JSON property 'observations'"):
            check_corpus(self.path)

    def test_non_list_fails(self) -> None:
        self.write('{"observations": {}}')
        with self.assertRaisesRegex(CorpusError, "observations must be a list"):
            check_corpus(self.path)

    def test_missing_id_fails(self) -> None:
        self.write('{"observations": [{}]}')
        with self.assertRaisesRegex(CorpusError, "nonempty string"):
            check_corpus(self.path)

    def test_nonobject_fails(self) -> None:
        self.write('{"observations": [null]}')
        with self.assertRaisesRegex(CorpusError, "must be an object"):
            check_corpus(self.path)

    def test_invalid_utf8_fails(self) -> None:
        self.path.write_bytes(b'\xff')
        with self.assertRaisesRegex(CorpusError, "cannot read corpus"):
            check_corpus(self.path)

    def test_nonfinite_json_number_fails(self) -> None:
        self.write('{"observations": [], "bogus": NaN}')
        with self.assertRaisesRegex(CorpusError, "non-JSON number"):
            check_corpus(self.path)

    def test_invalid_json_fails(self) -> None:
        self.write('{"observations": [}')
        with self.assertRaisesRegex(CorpusError, "cannot read corpus"):
            check_corpus(self.path)

    def test_cli_rejects_invalid(self) -> None:
        self.write('{"observations": [{"id": "DR70-FAKE1"}, {"id": "DR70-FAKE1"}]}')
        self.assertEqual(main([str(self.path)]), 1)


if __name__ == "__main__":
    unittest.main()
