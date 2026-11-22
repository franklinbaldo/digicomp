"""Source-labelled output-table guards, runnable with stdlib alone."""

from __future__ import annotations

from copy import deepcopy
import math
from pathlib import Path
import tempfile
import unittest

from scripts.carter_modern_table import FIELDS, load_control, published_arcsec, render, report


class CarterDocumentaryTableTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.control = load_control()
        cls.model = {
            "classification": "MODERN_REFERENCE_NOT_DR70",
            "dr70_fidelity": "NOT_RUN_NO_GOLDEN", "input_candidate_id": "RAEL1980-CARTER",
            "utc_interpreted": "1924-10-01T13:00:00Z",
            "engine": {"name": "Swiss Ephemeris (Python swisseph binding)", "house_system": "Campanus (C)"},
            "angles_deg": {}, "planet_longitudes": {},
        }
        # Pure formatting fixture: positions are copied from published source,
        # never represented as observed/calculated DR-70 or a test of an ephemeris.
        for field in FIELDS:
            longitude = published_arcsec(cls.control["positions"][field]) / 3600
            if field in ("ascendant", "midheaven"):
                cls.model["angles_deg"][field] = longitude
            else:
                cls.model["planet_longitudes"][field] = {"longitude_deg": longitude}

    def test_nine_fields_and_disclaimers_visible(self):
        result = report(self.control, self.model)
        output = render(result)
        self.assertEqual((result["within_tolerance"], result["compared"]), (9, 9))
        for token in ("NOT DR-70", "NOT_ESTABLISHED", "NOT_RUN_NO_GOLDEN",
                      "NOT_RUN_NO_INSPECTED_1980_NUMBERS", "9/9", "Whole Signs"):
            self.assertIn(token, output)
        self.assertEqual(len([line for line in output.splitlines() if line.endswith("MATCH")]), 9)

    def test_model_angular_mutation_produces_visible_mismatch(self):
        wrong = deepcopy(self.model)
        wrong["angles_deg"]["ascendant"] += 2 / 3600
        result = report(self.control, wrong)
        self.assertEqual(result["within_tolerance"], 8)
        self.assertIn("MISMATCH", render(result))

    def test_golden_and_source_class_mutations_fail_closed(self):
        for key, value in (("golden_instrumental", True), ("dr70_native_output", True),
                           ("tolerance_arcseconds", 20), ("dr70_fidelity", "PASS")):
            bad = deepcopy(self.control)
            bad["scope"][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                report(bad, self.model)
        wrong = deepcopy(self.model)
        wrong["classification"] = "DR70_GOLDEN"
        with self.assertRaises(ValueError):
            report(self.control, wrong)

    def test_bad_dms_literals_and_model_nonfinite_fail_closed(self):
        for patch in ({"minutes": 60}, {"literal": "26° 5′ 39″"}, {"seconds": True}):
            item = dict(self.control["positions"]["ascendant"], **patch)
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                published_arcsec(item)
        for x in (float("nan"), math.inf, -1.0, 360.0, True):
            wrong = deepcopy(self.model)
            wrong["angles_deg"]["ascendant"] = x
            with self.subTest(x=x), self.assertRaises(ValueError):
                report(self.control, wrong)

    def test_ambiguous_source_json_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.json"
            for data in ('{"a":1,"a":2}', '{"a":NaN}', '{"a":1e999}'):
                path.write_text(data, encoding="utf-8")
                with self.subTest(data=data), self.assertRaises(ValueError):
                    load_control(path)


if __name__ == "__main__":
    unittest.main()
