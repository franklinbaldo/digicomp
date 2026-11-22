"""Negative controls for candidate chart inputs. No golden samples here."""

import tempfile
import unittest
from pathlib import Path

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

    def test_rejects_datetime_or_offset_disguised_as_calendar_date(self):
        # fromisoformat accepts compact dates and midnight datetimes; replacing
        # their tzinfo would silently discard an explicit UTC offset.
        for date in (
            "19241001",
            "1924-10-01T00:00:00",
            "1924-10-01T00:00:00Z",
            "1924-10-01T00:00:00+05:00",
            "1924-10-01 00:00:00",
            "1924-02-30",
        ):
            with self.subTest(date=date), self.assertRaises(ValueError):
                hypothetical_utc(date, "13:00")
        self.assertEqual(
            hypothetical_utc("1924-10-01", "13:00"), "1924-10-01T13:00:00Z"
        )

    def test_no_observed_values_can_be_loaded_as_inputs(self):
        original = load()["cases"][0].copy()
        original["observed_chart_values"] = {"house_1": 0.0}
        with self.assertRaises(ValueError):
            normalize(original)

    def test_rejects_duplicate_json_keys_in_nested_input_and_source(self):
        # A later duplicate can silently replace an inspected date/coordinate.
        # These are synthetic mutations, not readings from the publication.
        examples = (
            '{"classification":"PUBLISHED_INPUT_CANDIDATES_NOT_DR70_OUTPUT",'
            '"source":{"locator":"page A","locator":"page B"},"cases":[]}',
            '{"classification":"PUBLISHED_INPUT_CANDIDATES_NOT_DR70_OUTPUT",'
            '"cases":[{"id":"same","id":"rewritten"}]}',
        )
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "candidate.json"
            for content in examples:
                with self.subTest(content=content):
                    path.write_text(content, encoding="utf-8")
                    with self.assertRaisesRegex(ValueError, "Duplicate chart-input JSON property"):
                        load(path)

    def test_rejects_non_json_constants_and_float_overflow(self):
        # Prevent differing JSON decoders from interpreting NaN/Infinity or 1e999.
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "candidate.json"
            for number in ("NaN", "Infinity", "-Infinity", "1e999"):
                with self.subTest(number=number):
                    path.write_text(
                        '{"classification":"PUBLISHED_INPUT_CANDIDATES_NOT_DR70_OUTPUT",'
                        '"source":{"unverified_value":' + number + '},"cases":[]}',
                        encoding="utf-8",
                    )
                    with self.assertRaisesRegex(ValueError, "Non-"):
                        load(path)

    def test_three_unique_candidates_and_no_output(self):
        cases = load()["cases"]
        self.assertEqual(len(cases), 3)
        self.assertTrue(all(c["observed_chart_values"] is None for c in cases))


if __name__ == "__main__":
    unittest.main()
