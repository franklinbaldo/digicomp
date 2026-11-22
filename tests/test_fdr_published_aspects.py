"""Experimental safeguards and reproducibility for two rounded editorial claims."""

import unittest

from scripts.probe_fdr_published_aspects import (
    INPUT_HYPOTHESES,
    PUBLISHED_ROUNDED_ANGLES,
    minimum_separation_deg,
)


class AngularControlTest(unittest.TestCase):
    def test_short_arc_and_wraparound(self):
        self.assertEqual(minimum_separation_deg(359, 1), 2)
        self.assertEqual(minimum_separation_deg(10, 190), 180)
        self.assertEqual(minimum_separation_deg(45, 45), 0)

    def test_no_nonfinite_or_invalid_longitude(self):
        for invalid in (-1, 360, float("nan"), float("inf")):
            with self.subTest(value=invalid):
                with self.assertRaises(ValueError):
                    minimum_separation_deg(invalid, 1)

    def test_source_constants_do_not_claim_machine_output(self):
        self.assertEqual(PUBLISHED_ROUNDED_ANGLES, {"moon_pluto": 39, "mars_uranus": 81})
        self.assertEqual(INPUT_HYPOTHESES["extended_25h16"], (1882, 1, 30, 25 + 16 / 60))

    def test_modern_rollover_control_if_dependency_installed(self):
        try:
            from scripts.probe_fdr_published_aspects import run
            result = run()
        except RuntimeError as exc:
            self.skipTest(str(exc))
        self.assertEqual(result["dr70_fidelity"], "NOT_RUN_NO_GOLDEN")
        extended = result["hypotheses"]["extended_25h16"]
        same_date = result["hypotheses"]["same_date_01h16"]
        variant = result["hypotheses"]["extended_25h15_variant"]
        self.assertEqual(extended["nearest_integer_matches"], {
            "moon_pluto": True, "mars_uranus": True,
        })
        self.assertEqual(variant["nearest_integer_matches"], extended["nearest_integer_matches"])
        self.assertEqual(same_date["nearest_integer_matches"], {
            "moon_pluto": False, "mars_uranus": True,
        })
        self.assertAlmostEqual(extended["modern_separations_deg"]["moon_pluto"], 38.67416636, places=5)
        self.assertAlmostEqual(same_date["modern_separations_deg"]["moon_pluto"], 26.47069530, places=5)


if __name__ == "__main__":
    unittest.main()
