"""Offline documentary-family accounting; controls are not DR-70 samples."""
import copy
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "scripts/report_documentary_comparability.py"
spec = importlib.util.spec_from_file_location("documentary_comparability", FILE)
reporter = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = reporter
spec.loader.exec_module(reporter)


def entry(ident, family, fragments=None):
    return {"id": ident, "family_id": family,
            "reported_numeric_fragments": fragments or []}


PAIRS = [{"pair": "H01/H07", "groups": ["09", "08"]},
         {"pair": "H02/H08", "groups": ["05", "59"]}]
GOLDEN = {"observations": []}


class DocumentaryComparabilityTest(unittest.TestCase):
    def test_republication_is_one_family_not_two_holdouts(self):
        rows = [entry("F83", "CARLSON", PAIRS), entry("F85", "CARLSON", PAIRS)]
        report = reporter.summarize(rows, GOLDEN)
        self.assertEqual(report["distinct_documentary_families"], 1)
        self.assertEqual(report["families_with_numeric_group_candidates"], 1)
        self.assertEqual(report["unique_candidate_pairs_within_families"], 2)
        self.assertEqual(report["complete_historical_angles_compared"], 0)
        self.assertEqual(report["independent_holdout_scores_computed"], 0)

    def test_whitespace_alias_does_not_inflate_documentary_family_count(self):
        # The catalog holdout guard already uses family.strip() as identity.
        rows = [entry("F83", "CARLSON", PAIRS),
                entry("F85", "  CARLSON  ", PAIRS)]
        report = reporter.summarize(rows, GOLDEN)
        self.assertEqual(report["distinct_documentary_families"], 1)
        self.assertEqual(report["families_with_numeric_group_candidates"], 1)
        self.assertEqual(report["unique_candidate_pairs_within_families"], 2)
        self.assertEqual(report["family_coverage"][0]["family_id"], "CARLSON")
        self.assertEqual(report["family_coverage"][0]["catalog_ids"], ["F83", "F85"])
        self.assertEqual(report["independent_holdout_scores_computed"], 0)

    def test_conflict_across_whitespace_alias_is_still_rejected(self):
        conflicting = copy.deepcopy(PAIRS)
        conflicting[0]["groups"] = ["09", "09"]
        with self.assertRaisesRegex(ValueError, "conflicting editorial readings"):
            reporter.summarize([entry("F83", "CARLSON", PAIRS),
                                entry("F85", " CARLSON ", conflicting)], GOLDEN)

    def test_distinct_family_still_not_a_fidelity_score(self):
        rows = [entry("F83", "CARLSON", PAIRS), entry("SECOND", "OTHER", PAIRS)]
        report = reporter.summarize(rows, GOLDEN)
        self.assertEqual(report["unique_candidate_pairs_within_families"], 4)
        self.assertEqual(report["angular_residuals_computed"], 0)
        self.assertEqual(report["fidelity_corpus_records_unvalidated"], 0)

    def test_conflicting_same_family_readings_are_rejected(self):
        changed = copy.deepcopy(PAIRS)
        changed[0]["groups"] = ["09", "09"]
        with self.assertRaisesRegex(ValueError, "conflicting editorial readings"):
            reporter.summarize([entry("F83", "CARLSON", PAIRS),
                                entry("F85", "CARLSON", changed)], GOLDEN)

    def test_duplicate_ids_and_invalid_groups_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            reporter.summarize([entry("X", "A"), entry("X", "B")], GOLDEN)
        for groups in ([9, "08"], ["09", "eight"], ["09"], ["09", "08", "01"]):
            with self.subTest(groups=groups):
                with self.assertRaisesRegex(ValueError, "non-comparable"):
                    reporter.summarize(
                        [entry("X", "A", [{"pair": "A", "groups": groups}])], GOLDEN
                    )

    def test_unvalidated_fidelity_rows_do_not_claim_instrumental_provenance(self):
        # API-only synthetic rows: neither status nor record count certifies a device.
        for row in ({"fake": True}, {"status": "partial"}, {"status": "replayable"}):
            with self.subTest(row=row):
                report = reporter.summarize([entry("F83", "CARLSON", PAIRS)],
                                            {"observations": [row]})
                self.assertEqual(report["fidelity_corpus_records_unvalidated"], 1)
                self.assertNotIn("golden_instrumental_observations", report)
                self.assertFalse(any("certified" in key or "authenticated" in key
                                     for key in report))
                self.assertEqual(report["angular_residuals_computed"], 0)
                self.assertEqual(report["independent_holdout_scores_computed"], 0)

    def test_malformed_gold_list_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "golden"):
            reporter.summarize([], {"observations": None})

    def test_json_rejects_duplicate_nonfinite_and_overflow(self):
        import tempfile
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "test.json"
            for content in ('{"a": 1, "a": 2}', '{"a": NaN}', '{"a": 1e999}'):
                with self.subTest(content=content):
                    path.write_text(content, encoding="utf-8")
                    with self.assertRaises(ValueError):
                        reporter.read_json(path)

    def test_current_real_corpus_is_one_partial_numeric_family(self):
        entries = []
        for path in sorted(reporter.CATALOG_DIR.glob("*.json")):
            entries.extend(reporter.read_json(path)["entries"])
        report = reporter.summarize(entries, reporter.read_json(reporter.GOLDEN))
        self.assertEqual(report["classification"], "DOCUMENTARY_COVERAGE_NOT_DR70_FIDELITY")
        self.assertEqual(report["catalog_entries"], 30)
        self.assertEqual(report["distinct_documentary_families"], 8)
        self.assertEqual(report["families_with_numeric_group_candidates"], 1)
        self.assertEqual(report["unique_candidate_pairs_within_families"], 6)
        self.assertEqual(report["fidelity_corpus_records_unvalidated"], 0)
        self.assertEqual(report["angular_residuals_computed"], 0)
        self.assertEqual(report["independent_holdout_scores_computed"], 0)


if __name__ == "__main__":
    unittest.main()
