"""Negative controls for candidate chart inputs. No golden samples here."""

import unittest

from scripts.chart_input_candidates import coordinate, hypothetical_utc, load, normalize


class ChartInputCandidatesTest(unittest.TestCase):
    def test_carter_coordinates_and_utc(self):
        case = next(c for c in load()["cases"] if c["id"] == "RAEL1980-CARTER")
        result = normalize(case)
        self.assertEqual(result["hypothetical_normalization"]["utc"], "1924-10-01T13:00:00Z")
        self.assertAlmostEqual(result["hypothetical_normalization"]["latitude_deg"], 32 + 2 / 60)
        self.assertAlmostEqual(result["hypothetical_normalization"]["longitude_deg_east"], -(84 + 24 / 60))
        self.assertIn("NOT_DR70_OUTPUT", result["evidence_status"])

    def test_extended_hours_cross_date_boundary(self):
        self.assertEqual(hypothetical_utc("1935-09-05", "27:25"), "1935-09-06T03:25:00Z")
        self.assertEqual(hypothetical_utc("1882-01-30", "25:16"), "1882-01-31T01:16:00Z")

    def test_reject_invalid_coordinates(self):
        for text, axis in (("90N01", "latitude"), ("181W00", "longitude"),
                           ("34S60", "latitude"), ("12E00", "latitude"), ("ab", "longitude")):
            with self.subTest(text=text), self.assertRaises(ValueError):
                coordinate(text, axis)

    def test_reject_invalid_clock(self):
        for time in ("24:60", "48:00", "13:5", "-01:00"):
            with self.subTest(time=time), self.assertRaises(ValueError):
                hypothetical_utc("1924-10-01", time)

    def test_no_observed_values_can_be_loaded_as_inputs(self):
        original = load()["cases"][0].copy()
        original["observed_chart_values"] = {"house_1": 0.0}
        with self.assertRaises(ValueError):
            normalize(original)

    def test_three_unique_candidates_and_no_output(self):
        cases = load()["cases"]
        self.assertEqual(len(cases), 3)
        self.assertTrue(all(c["observed_chart_values"] is None for c in cases))


if __name__ == "__main__":
    unittest.main()
