"""Contract tests: Carlson published candidates are not native DR-70 output."""
import copy
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_documentary_observations import (
    CATALOG, DOCUMENT, GOLDEN, REPORT, load_json, report, rust_pairs, validate,
)

class DocumentaryCarlsonBridgeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document = load_json(DOCUMENT)
        cls.catalog = load_json(CATALOG)
        cls.golden = load_json(GOLDEN)
        cls.baseline = REPORT.read_text(encoding="utf-8")

    def check(self, candidate):
        return validate(candidate, self.catalog, self.golden)

    def test_twelve_slots_are_provenance_reconciled(self):
        self.assertEqual(self.check(self.document), [])
        self.assertEqual(len(self.document["readings"]), 12)
        self.assertEqual(self.document["source_catalog_id"], "OUT-CARLSON-F83")
        self.assertFalse(self.document["native_print_authenticated"])
        self.assertEqual(self.golden["observations"], [])

    def test_zero_angles_and_no_holdout_are_exposed_in_frozen_report(self):
        self.assertEqual(report(self.document), self.baseline)
        self.assertIn("angular_numeric_comparisons=0", self.baseline)
        self.assertIn("independent_holdout=0", self.baseline)
        self.assertIn("device_fidelity=NOT_RUN_NO_GOLDEN", self.baseline)

    def test_additional_visual_regions_are_not_interpretable_inputs(self):
        # One nonblind reading of the same F83/F85 editorial family.
        rows = self.document["additional_literal_candidates"]
        self.assertEqual([r["literal_candidate"] for r in rows],
                         ["4.01.1981", "07 54 47"])
        self.assertTrue(all(r["interpreted_value"] is None for r in rows))
        for i, field, value in (
            (0, "semantic_role", "verified_birth_date"),
            (0, "interpreted_value", "1981-01-04"),
            (0, "literal_candidate", "4.01.1982"),
            (1, "semantic_role", "verified_aspect_angle"),
            (1, "literal_candidate", "07 54 48"),
            (1, "reading_status", "two_independent_blind_reads"),
        ):
            with self.subTest(row=i, field=field):
                tampered = copy.deepcopy(self.document)
                tampered["additional_literal_candidates"][i][field] = value
                self.assertTrue(any("additional candidate" in e
                                    for e in self.check(tampered)),
                                self.check(tampered))

        injected = copy.deepcopy(self.document)
        injected["additional_literal_candidates"][0]["parsed_as_birth"] = True
        self.assertTrue(any("additional candidate" in e
                            for e in self.check(injected)))

    def test_export_is_exactly_the_published_rust_candidate_rows(self):
        # Literal groups from Carlson secondary ledger, one editorial family.
        expected = (
            "H01\tH07\t09\t08\t09\t08\n"
            "H02\tH08\t05\t59\t05\t59\n"
            "H03\tH09\t09\t38\t09\t38\n"
            "H04\tH10\t25\t08\t25\t08\n"
            "H05\tH11\t19\t58\t19\t58\n"
            "H06\tH12\t14\t29\t14\t29\n"
        )
        self.assertEqual(rust_pairs(self.document), expected)

    def test_mutant_of_one_house_is_visible_despite_same_family(self):
        tampered = copy.deepcopy(self.document)
        tampered["readings"][9]["candidate_groups"][0] = "26"
        self.assertTrue(any("differs from documented catalog pair" in e
                            for e in self.check(tampered)))

    def test_missing_house_and_duplicate_are_refused(self):
        fewer = copy.deepcopy(self.document)
        fewer["readings"].pop()
        self.assertTrue(any("expected twelve" in e for e in self.check(fewer)))
        duplicate = copy.deepcopy(self.document)
        duplicate["readings"][11]["house"] = "H01"
        self.assertTrue(any("duplicate" in e for e in self.check(duplicate)))

    def test_hypothetical_angles_and_holdout_cannot_be_laundered(self):
        tampered = copy.deepcopy(self.document)
        tampered["sample_split"] = "holdout"
        tampered["native_print_authenticated"] = True
        tampered["readings"][0]["zodiac_glyph"] = "FAKE"
        tampered["readings"][0]["interpreted_longitude_deg"] = 9.1333
        errors = self.check(tampered)
        self.assertTrue(any("certainty" in e for e in errors), errors)
        self.assertTrue(any("angle must remain null" in e for e in errors), errors)

    def test_family_alias_and_unicode_digit_are_rejected(self):
        tampered = copy.deepcopy(self.document)
        tampered["source_family_id"] = "FAKE-INDEPENDENT"
        tampered["publication_lineage_alias"] = "FAKE-SECOND-SESSION"
        tampered["readings"][1]["candidate_groups"][0] = "٠٥"
        errors = self.check(tampered)
        self.assertTrue(any("certainty" in e for e in errors), errors)
        self.assertTrue(any("two unparsed" in e for e in errors), errors)

    def test_1985_republication_cannot_be_relabelled_as_independent_holdout(self):
        # F83 and F85 are one editorial family; two PDFs are not two cases.
        mutations = (
            ("family_id", "FAKE-SECOND-SESSION"),
            ("status", "native"),
            ("kind", "native_output"),
            ("attribution", "native_dr70_output"),
            ("sample_split", "holdout"),
            ("numeric_holdout_eligible", True),
            ("replayable", True),
            ("input_complete", True),
            ("output_complete", True),
        )
        for key, value in mutations:
            with self.subTest(key=key):
                catalog = copy.deepcopy(self.catalog)
                alias = next(e for e in catalog["entries"]
                             if e["id"] == "OUT-CARLSON-F85")
                alias[key] = value
                errors = validate(self.document, catalog, self.golden)
                self.assertTrue(any("publication lineage alias" in e
                                    for e in errors), errors)

        for change in ("missing", "duplicate"):
            with self.subTest(change=change):
                catalog = copy.deepcopy(self.catalog)
                if change == "missing":
                    catalog["entries"] = [
                        e for e in catalog["entries"]
                        if e["id"] != "OUT-CARLSON-F85"
                    ]
                else:
                    alias = next(e for e in catalog["entries"]
                                 if e["id"] == "OUT-CARLSON-F85")
                    catalog["entries"].append(copy.deepcopy(alias))
                errors = validate(self.document, catalog, self.golden)
                self.assertIn("publication lineage alias must resolve exactly once", errors)

    def test_1983_source_catalog_cannot_be_relabelled_as_device_output(self):
        for key, value in (
            ("status", "native"),
            ("kind", "native_output"),
            ("attribution", "native_dr70_output"),
            ("input_complete", True),
            ("output_complete", True),
            ("replayable", True),
        ):
            with self.subTest(key=key):
                catalog = copy.deepcopy(self.catalog)
                source = next(e for e in catalog["entries"]
                              if e["id"] == "OUT-CARLSON-F83")
                source[key] = value
                errors = validate(self.document, catalog, self.golden)
                self.assertIn(
                    "catalog source cannot be promoted to native/replayable output",
                    errors,
                )

    def test_cli_executes_real_documentary_dataset(self):
        run = subprocess.run(
            [sys.executable, "-B", str(ROOT / "scripts/check_documentary_observations.py")],
            cwd=ROOT, text=True, capture_output=True, check=False,
        )
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(run.stdout, self.baseline)
        export = subprocess.run(
            [sys.executable, "-B", str(ROOT / "scripts/check_documentary_observations.py"),
             "--emit-rust-tsv"],
            cwd=ROOT, text=True, capture_output=True, check=False,
        )
        self.assertEqual(export.returncode, 0, export.stderr)
        self.assertEqual(export.stdout, rust_pairs(self.document))


if __name__ == "__main__":
    unittest.main()
