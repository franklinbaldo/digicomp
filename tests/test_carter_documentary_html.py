"""HTML contract tests using synthetic fixture data, not a DR-70 printout."""

from __future__ import annotations

from copy import deepcopy
from html.parser import HTMLParser
from io import StringIO
import json
import unittest
from unittest.mock import patch

from scripts.carter_documentary_dashboard import assemble
from scripts.carter_documentary_html import main, render_html
from test_carter_documentary_dashboard import CarterDocumentaryDashboardTest


class Structure(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags = []
        self.regions = []
        self.csp = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str]]) -> None:
        attrs = dict(attrs)
        self.tags.append(tag)
        if attrs.get("role") == "region":
            self.regions.append(attrs)
        if tag == "meta" and attrs.get("http-equiv") == "Content-Security-Policy":
            self.csp = "default-src 'none'" in attrs.get("content", "")


class CarterDocumentaryHtmlTest(unittest.TestCase):
    def setUp(self) -> None:
        fixture = CarterDocumentaryDashboardTest()
        fixture.setUp()
        self.report = assemble(fixture.modern, fixture.historical, fixture.counterfactual)

    def test_semantic_readable_two_tier_report_with_source_and_limits(self) -> None:
        out = render_html(self.report)
        parser = Structure()
        parser.feed(out)
        self.assertTrue(out.startswith("<!doctype html>"))
        self.assertIn('lang="pt-BR"', out)
        self.assertEqual(parser.tags.count("h1"), 1)
        self.assertEqual(parser.tags.count("h2"), 4)
        self.assertEqual(parser.tags.count("table"), 2)
        self.assertEqual(parser.tags.count("caption"), 2)
        self.assertEqual(parser.tags.count("th"), 19)  # 9 modern + 4 historical row headers + 10 column headers
        self.assertTrue(parser.csp)
        self.assertEqual(len(parser.regions), 2)
        self.assertTrue(all(r.get("tabindex") == "0" for r in parser.regions))
        for text in ("9/9", "4/4", "2/4", "2023", "1980",
                     "mesma família editorial", "12h UT é um contrafactual",
                     "NOT_RUN_NO_GOLDEN", "NOT_RUN_NO_INSPECTED_1980_CHART"):
            self.assertIn(text, out)
        self.assertIn("https://static1.squarespace.com/", out)
        self.assertIn("https://www.scribd.com/", out)
        self.assertNotIn("<script", out)
        self.assertNotIn("http://", out)

    def test_html_escaping_is_not_a_source_validation_substitute(self) -> None:
        bad_literal = '<img src=x onerror="alert(1)"> & "'
        self.report["modern_2023"]["rows"][0]["published_2023"] = bad_literal
        out = render_html(self.report)
        self.assertNotIn(bad_literal, out)
        self.assertNotIn("<img", out)
        self.assertIn("&lt;img", out)
        self.assertIn("&amp;", out)

    def test_cannot_promote_uninspected_or_fabricate_counts(self) -> None:
        cases = [
            ("dr70_instrumental_comparison", "PASS"),
            ("historical_chart_numeric_comparison", "PASS"),
        ]
        for key, value in cases:
            bad = deepcopy(self.report)
            bad[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                render_html(bad)
        bad = deepcopy(self.report)
        bad["historical_house_prose"]["independent_editorial_families"] = 4
        with self.assertRaises(ValueError):
            render_html(bad)
        bad = deepcopy(self.report)
        bad["modern_2023"]["within_tolerance"] = 8
        with self.assertRaises(ValueError):
            render_html(bad)

    def test_rejects_unsafe_source_and_nonfinite_model(self) -> None:
        bad = deepcopy(self.report)
        bad["historical_house_prose"]["source"] = "javascript:alert(1)"
        with self.assertRaises(ValueError):
            render_html(bad)
        bad = deepcopy(self.report)
        bad["modern_2023"]["rows"][0]["model_longitude_deg"] = float("inf")
        with self.assertRaises(ValueError):
            render_html(bad)

    def test_mismatch_remains_visible_instead_of_forced_success(self) -> None:
        bad = deepcopy(self.report)
        bad["modern_2023"]["rows"][0]["residual_arcsec"] = 1.5
        bad["modern_2023"]["rows"][0]["within_declared_tolerance"] = False
        bad["modern_2023"]["within_tolerance"] = 8
        out = render_html(bad)
        self.assertIn("8/9", out)
        self.assertIn("Diverge", out)

    def test_stdin_rejects_duplicate_keys_and_nonfinite_json(self) -> None:
        for incoming in ('{"case_id":1,"case_id":2}', '{"x":NaN}', '{"x":1e999}'):
            with self.subTest(incoming=incoming):
                with patch("sys.stdin", StringIO(incoming)), self.assertRaises(ValueError):
                    main()

    def test_json_stdin_generates_same_offline_html(self) -> None:
        with patch("sys.stdin", StringIO(json.dumps(self.report))), patch("sys.stdout", new_callable=StringIO) as output:
            main()
        self.assertEqual(output.getvalue().rstrip("\n"), render_html(self.report))


if __name__ == "__main__":
    unittest.main()
