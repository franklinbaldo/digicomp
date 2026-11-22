"""Experimental safeguards and reproducibility for two rounded editorial claims."""

import unittest

from scripts.probe_fdr_published_aspects import (
    INPUT_HYPOTHESES,
    PUBLISHED_ROUNDED_ANGLES,
    minimum_separation_deg,
    directed_advance_deg,
)


class AngularControlTest(unittest.TestCase):
    def test_short_arc_and_wraparound(self):
        self.assertEqual(minimum_separation_deg(359, 1), 2)
        self.assertEqual(minimum_separation_deg(10, 190), 180)
        self.assertEqual(minimum_separation_deg(45, 45), 0)

    def test_directed_advance_not_minimum_arc(self):
        self.assertEqual(directed_advance_deg(10, 350), 20)
        self.assertEqual(directed_advance_deg(350, 10), 340)
        with self.assertRaises(ValueError):
            directed_advance_deg(float("inf"), 0)

    def test_septile_diagnostics_if_dependency_installed(self):
        from scripts.probe_fdr_published_aspects import run
        try:
            result = run()
        except RuntimeError as exc:
            self.skipTest(str(exc))
        extended = result["hypotheses"]["extended_25h16"]["modern_septile_diagnostics_deg"]
        same_day = result["hypotheses"]["same_date_01h16"]["modern_septile_diagnostics_deg"]
        self.assertAlmostEqual(extended["moon_neptune_short_arc"], 52.25065565, places=5)
        self.assertAlmostEqual(extended["mars_ahead_saturn_directed"], 50.91659187, places=5)
        self.assertAlmostEqual(extended["moon_jupiter_short_arc"], 49.10416102, places=5)
        self.assertAlmostEqual(same_day["moon_neptune_short_arc"], 40.05487028, places=5)
        self.assertEqual(result["septile_textual_controls"]["moon_jupiter_conditional_verdict"],
                         "NOT_EVALUATED_LATER_HOUR_UNSPECIFIED")
        self.assertEqual(result["dr70_fidelity"], "NOT_RUN_NO_GOLDEN")

    def test_integer_editorial_angles_do_not_identify_a_birth_minute(self):
        # Modern engine counterexample: two instants 90 minutes apart.
        # This asserts neither the historical rounding nor a DR-70 result.
        try:
            from scripts.probe_fdr_published_aspects import run
            result = run()
        except RuntimeError as exc:
            self.skipTest(str(exc))
        early = result["hypotheses"]["same_integer_01h00"]
        late = result["hypotheses"]["same_integer_02h30"]
        expected = {"moon_pluto": True, "mars_uranus": True}
        self.assertEqual(early["nearest_integer_matches"], expected)
        self.assertEqual(late["nearest_integer_matches"], expected)
        minutes_apart = (late["julian_day_ut"] - early["julian_day_ut"]) * 1440
        self.assertAlmostEqual(minutes_apart, 90, places=3)
        self.assertEqual(result["source_edition"], "UNRESOLVED")
        self.assertEqual(result["rounding_policy"],
                         "HYPOTHETICAL_NEAREST_INTEGER_NOT_HISTORICALLY_ATTESTED")

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
