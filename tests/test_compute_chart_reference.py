"""Modern comparison tests: not assertions about the DR-70."""

import math
import unittest

from scripts.chart_input_candidates import load
from scripts.compute_chart_reference import calculate

try:
    import swisseph as swe
except ImportError:
    swe = None


@unittest.skipUnless(swe, "Optional Swiss Ephemeris Python binding not installed")
class ModernReferenceTest(unittest.TestCase):
    def test_carter_produces_twelve_cusps_and_seven_planets(self):
        case = load()["cases"][0]
        result = calculate(case, swe)
        self.assertEqual(result["classification"], "MODERN_REFERENCE_NOT_DR70")
        self.assertEqual(result["dr70_fidelity"], "NOT_RUN_NO_GOLDEN")
        self.assertEqual(result["historical_chart_comparison"], "NOT_RUN_NO_TRANSCRIBED_VALUES")
        self.assertEqual(len(result["cusps_deg"]), 12)
        self.assertEqual(len(result["planet_longitudes"]), 7)
        for value in result["cusps_deg"].values():
            self.assertTrue(math.isfinite(value))
            self.assertTrue(0 <= value < 360)
        self.assertAlmostEqual(result["cusps_deg"]["1"], result["angles_deg"]["ascendant"], places=6)
        self.assertAlmostEqual(result["cusps_deg"]["7"], (result["cusps_deg"]["1"] + 180) % 360, places=6)

    def test_extended_utc_is_calculated_on_the_next_day(self):
        case = next(c for c in load()["cases"] if c["id"] == "RAEL1980-ERHARD")
        result = calculate(case, swe)
        self.assertEqual(result["utc_interpreted"], "1935-09-06T03:25:00Z")
        self.assertIn("hypothesis", result["input_time_assumption"])


if __name__ == "__main__":
    unittest.main()
