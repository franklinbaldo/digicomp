"""Independent checks for three modern-only Carter qualitative aspect pairs."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import unittest

from scripts.carter_qualitative_additional import additional_relations

CONTROL = (Path(__file__).resolve().parents[1] /
           "data/modern-controls/carter-astro-dienst-2023.json")


class CarterAdditionalAspectTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads(CONTROL.read_text(encoding="utf-8"))

    def test_three_modern_pairs_have_exact_signed_differences(self):
        result = additional_relations(self.source)
        self.assertEqual(result["classification"],
                         "MODERN_2023_VS_SECONDARY_HISTORICAL_ASPECT_NAMES")
        rows = {r["id"]: r for r in result["relations"]}
        self.assertEqual(set(rows), {
            "venus_pluto_novile", "sun_moon_semiquintile",
            "mars_jupiter_quintile",
        })
        for key, separation, nominal, deviation in (
            ("venus_pluto_novile", 143303, 144000, -697),
            ("sun_moon_semiquintile", 128645, 129600, -955),
            ("mars_jupiter_quintile", 257234, 259200, -1966),
        ):
            with self.subTest(key=key):
                self.assertEqual(rows[key]["modern_2023_separation_arcseconds"],
                                 separation)
                self.assertEqual(rows[key]["aspect_nominal_arcseconds"], nominal)
                self.assertEqual(rows[key]["modern_deviation_signed_arcseconds"],
                                 deviation)

    def test_auxiliary_visual_oracle_not_derived_from_its_json(self):
        # Independently transcribed from Rabinowitz 2023, chart on printed p.12.
        self.assertEqual(self.source["auxiliary_qualitative_positions"], {
            "pluto": {
                "sign": "Cancer", "degrees": 13, "minutes": 31,
                "seconds": 31, "literal": "13° 31′ 31″",
            }
        })
        self.assertEqual(len(self.source["positions"]), 9)
        self.assertNotIn("pluto", self.source["positions"])
        self.assertEqual(self.source["scope"]["comparison_only"],
                         ["ascendant", "midheaven", "sun", "moon", "mercury",
                          "venus", "mars", "jupiter", "saturn"])

    def test_one_second_mutant_propagates_to_novile(self):
        changed = deepcopy(self.source)
        pluto = changed["auxiliary_qualitative_positions"]["pluto"]
        pluto["seconds"] = 32
        pluto["literal"] = "13° 31′ 32″"
        result = additional_relations(changed)
        novile = result["relations"][0]
        self.assertEqual(novile["modern_2023_separation_arcseconds"], 143302)
        self.assertEqual(novile["modern_deviation_signed_arcseconds"], -698)

    def test_corrupt_or_unlabelled_auxiliary_fails_closed(self):
        for mutation in (
            {"sign": "Unknown"},
            {"degrees": 30},
            {"seconds": True},
            {"minutes": 60},
            {"literal": "13° 31′ 30″"},
        ):
            with self.subTest(mutation=mutation):
                changed = deepcopy(self.source)
                changed["auxiliary_qualitative_positions"]["pluto"].update(mutation)
                with self.assertRaises(ValueError):
                    additional_relations(changed)
        for auxiliary in (None, {}, {"pluto": self.source[
                "auxiliary_qualitative_positions"]["pluto"], "neptune": {}}):
            with self.subTest(auxiliary=auxiliary):
                changed = deepcopy(self.source)
                changed["auxiliary_qualitative_positions"] = auxiliary
                with self.assertRaises(ValueError):
                    additional_relations(changed)

    def test_no_historical_or_instrumental_pass(self):
        result = additional_relations(self.source)
        self.assertEqual(result["historical_chart_residual"],
                         "NOT_RUN_NO_INSPECTED_1980_NUMBERS")
        self.assertEqual(result["dr70_fidelity"], "NOT_RUN_NO_GOLDEN")
        self.assertTrue(all(
            row["historical_relation_test"] ==
            "INDETERMINATE_NO_INSPECTED_1980_CHART"
            for row in result["relations"]
        ))
        for key, value in (
            ("classification", "DR70_NATIVE_GOLDEN"),
            ("case_id", "SYNTHETIC"),
        ):
            with self.subTest(key=key):
                changed = deepcopy(self.source)
                changed[key] = value
                with self.assertRaises(ValueError):
                    additional_relations(changed)
        changed = deepcopy(self.source)
        changed["scope"]["golden_instrumental"] = True
        with self.assertRaises(ValueError):
            additional_relations(changed)


if __name__ == "__main__":
    unittest.main()
