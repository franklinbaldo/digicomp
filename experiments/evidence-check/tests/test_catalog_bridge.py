"""Negative tests for documentary catalog bridge; no network, device or synthetic golden."""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "experiments/evidence-check"))
from catalog_bridge import CATALOG, PAIRS, CatalogDrift, check  # noqa: E402


class CatalogBridgeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog_text = CATALOG.read_text(encoding="utf-8")
        cls.pairs_text = PAIRS.read_text(encoding="utf-8")

    def mutate(self, action) -> str:
        data = json.loads(self.catalog_text)
        action(data["entries"][0], data["entries"][1])
        return json.dumps(data)

    def test_actual_canonical_catalog_and_tsv_match(self) -> None:
        report = check(self.catalog_text, self.pairs_text)
        self.assertIn("candidate_pairs_crosschecked=6", report)
        self.assertIn("independent_transcriptions=0", report)
        self.assertIn("NOT_RUN_NO_GOLDEN", report)

    def test_rejects_same_length_numeric_mutation(self) -> None:
        bad = self.mutate(
            lambda f83, f85: f83["reported_numeric_fragments"][3].update(groups=["26", "08"])
        )
        with self.assertRaisesRegex(CatalogDrift, "left TSV groups differ"):
            check(bad, self.pairs_text)

    def test_rejects_second_side_drift_without_reinterpreting_source(self) -> None:
        bad_tsv = self.pairs_text.replace(
            "H04\tH10\t25\t08\t25\t08", "H04\tH10\t25\t08\t26\t08"
        )
        self.assertNotEqual(bad_tsv, self.pairs_text)
        with self.assertRaisesRegex(CatalogDrift, "right TSV groups differ"):
            check(self.catalog_text, bad_tsv)

    def test_rejects_forged_holdout_and_instrument_attribution(self) -> None:
        for mutation in (
            lambda a, b: a.update(numeric_holdout_eligible=True),
            lambda a, b: a.update(attribution="native_dr70_output"),
            lambda a, b: b.update(family_id="INDEPENDENT-SESSION"),
            lambda a, b: a.update(source_url="https://invalid.example/not-original.pdf"),
        ):
            with self.subTest(mutation=mutation):
                with self.assertRaises(CatalogDrift):
                    check(self.mutate(mutation), self.pairs_text)

    def test_rejects_missing_or_duplicate_pairs(self) -> None:
        bad = self.mutate(
            lambda a, b: a["reported_numeric_fragments"].append(
                a["reported_numeric_fragments"][0]
            )
        )
        with self.assertRaises(CatalogDrift):
            check(bad, self.pairs_text)
        bad_tsv = "\n".join(
            line for line in self.pairs_text.splitlines() if not line.startswith("H06\t")
        )
        with self.assertRaises(CatalogDrift):
            check(self.catalog_text, bad_tsv)

    def test_rejects_ambiguous_duplicate_json_keys(self) -> None:
        ambiguous = self.catalog_text.replace(
            '"format_version": "0.1",',
            '"format_version": "0.1", "format_version": "2",',
            1,
        )
        with self.assertRaisesRegex(CatalogDrift, "duplicate JSON key"):
            check(ambiguous, self.pairs_text)


if __name__ == "__main__":
    unittest.main()
