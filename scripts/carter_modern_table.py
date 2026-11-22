"""Human-readable REAL published-2023 vs MODERN computed Carter chart.

This never renders an instrumental or inspected-1980 DR-70 comparison.
The cited 2023 chart and this adapter may share Swiss Ephemeris.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
import re

CONTROL_PATH = Path(__file__).resolve().parents[1] / "data/modern-controls/carter-astro-dienst-2023.json"
FIELDS = ("ascendant", "midheaven", "sun", "moon", "mercury", "venus", "mars", "jupiter", "saturn")
SIGNS = ("Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces")
FULL_CIRCLE_ARCSEC = 360 * 3600


def load_control(path: Path = CONTROL_PATH) -> dict:
    """Fail closed on duplicate JSON keys and nonfinite values, including overflow."""
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"Duplicate JSON key: {key}")
            out[key] = value
        return out

    def invalid_constant(value):
        raise ValueError(f"Nonfinite JSON constant: {value}")

    def finite_float(text):
        value = float(text)
        if not math.isfinite(value):
            raise ValueError(f"Nonfinite JSON numeric literal: {text}")
        return value

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique,
                      parse_constant=invalid_constant, parse_float=finite_float)


def published_arcsec(entry: dict) -> int:
    """Validate the literal against DMS fields and decode to integer arcseconds."""
    sign = entry.get("sign")
    if sign not in SIGNS:
        raise ValueError("Unrecognized published zodiac sign")
    dms = tuple(entry.get(k) for k in ("degrees", "minutes", "seconds"))
    if any(type(x) is not int for x in dms):
        raise ValueError("Published degrees/minutes/seconds must be integers")
    deg, minute, second = dms
    if not 0 <= deg < 30 or not 0 <= minute < 60 or not 0 <= second < 60:
        raise ValueError("Published zodiac DMS out of range")
    literal = entry.get("literal")
    match = re.fullmatch(r"\s*(\d{1,2})\s*°\s*(\d{1,2})\s*[′']\s*(\d{1,2})\s*[″\"]\s*", literal) if isinstance(literal, str) else None
    if match is None or tuple(map(int, match.groups())) != dms:
        raise ValueError("Published literal differs from parsed DMS")
    return (SIGNS.index(sign) * 30 + deg) * 3600 + minute * 60 + second


def report(control: dict, model: dict) -> dict:
    """Validate source/engine boundaries and return a comparison, not fidelity."""
    scope = control.get("scope", {})
    source = control.get("source", {})
    engine = model.get("engine", {})
    if (
        control.get("classification") != "MODERN_CHART_CONTROL_NOT_DR70_OUTPUT"
        or control.get("case_id") != "RAEL1980-CARTER"
        or source.get("publication_year") != 2023
        or source.get("chart_provider") != "AstroDienst"
        or control.get("chart_house_system") != "Whole Signs"
        or control.get("input_as_published") != {"date": "1924-10-01", "universal_time": "13:00", "latitude": "32N02", "longitude": "84W24"}
        or set(control.get("positions", {})) != set(FIELDS)
        or set(scope.get("comparison_only", [])) != set(FIELDS)
        or scope.get("tolerance_arcseconds") != 1
        or scope.get("golden_instrumental") is not False
        or scope.get("dr70_native_output") is not False
        or scope.get("dr70_fidelity") != "NOT_RUN_NO_GOLDEN"
        or scope.get("historical_chart_residuals") != "NOT_RUN_NO_INSPECTED_1980_NUMBERS"
        or not str(scope.get("engine_independence", "")).startswith("NOT_ESTABLISHED:")
        or model.get("classification") != "MODERN_REFERENCE_NOT_DR70"
        or model.get("dr70_fidelity") != "NOT_RUN_NO_GOLDEN"
        or model.get("input_candidate_id") != control.get("case_id")
        or model.get("utc_interpreted") != "1924-10-01T13:00:00Z"
        or engine.get("house_system") != "Campanus (C)"
        or "Swiss Ephemeris" not in str(engine.get("name", ""))
    ):
        raise ValueError("Not the designated 2023-vs-modern control; no golden comparison allowed")

    rows = []
    for field in FIELDS:
        entry = control["positions"][field]
        printed = published_arcsec(entry)
        raw = (model.get("angles_deg", {}).get(field)
               if field in ("ascendant", "midheaven")
               else model.get("planet_longitudes", {}).get(field, {}).get("longitude_deg"))
        if type(raw) not in (float, int) or not math.isfinite(raw) or not 0 <= raw < 360:
            raise ValueError(f"Missing, nonfinite or out-of-range model position: {field}")
        residual = ((raw * 3600 - printed + FULL_CIRCLE_ARCSEC / 2) % FULL_CIRCLE_ARCSEC) - FULL_CIRCLE_ARCSEC / 2
        rows.append({"field": field, "published_2023": f'{entry["sign"]} {entry["literal"]}',
                     "model_longitude_deg": raw, "residual_arcsec": residual,
                     "within_declared_tolerance": abs(residual) <= 1})
    return {"case_id": control["case_id"], "rows": rows,
            "compared": len(rows), "within_tolerance": sum(r["within_declared_tolerance"] for r in rows),
            "historical": "NOT_RUN_NO_INSPECTED_1980_NUMBERS", "dr70": "NOT_RUN_NO_GOLDEN"}


def render(result: dict) -> str:
    """A compact human-readable output with machine status always visible."""
    lines = ["CARTER · EDITORIAL 2023 / COMPUTED MODERN (NOT DR-70)",
             "AstroDienst 2023 · 01/10/1924 13:00 UT · model Swiss/Moshier Campanus",
             "Whole Signs chart: house cusps deliberately NOT compared",
             "AstroDienst and model may share an engine: independence NOT_ESTABLISHED",
             "", f'{"Field":<11} {"Printed 2023":<27} {"Modern longitude":>17} {"Delta arcsec":>13}  Status']
    for row in result["rows"]:
        status = "MATCH" if row["within_declared_tolerance"] else "MISMATCH"
        lines.append(f'{row["field"]:<11} {row["published_2023"]:<27} {row["model_longitude_deg"]:>16.6f}° {row["residual_arcsec"]:>+13.3f}  {status}')
    lines.extend(["", f'Modern comparison: {result["within_tolerance"]}/{result["compared"]} within ±1 arcsecond',
                  f'1980 printed chart: {result["historical"]}',
                  f'DR-70 instrument fidelity: {result["dr70"]}'])
    return "\n".join(lines)


def main() -> None:
    import importlib
    from scripts.chart_input_candidates import load
    from scripts.compute_chart_reference import calculate
    swe = importlib.import_module("swisseph")
    cases = [c for c in load()["cases"] if c["id"] == "RAEL1980-CARTER"]
    if len(cases) != 1:
        raise ValueError("Ambiguous Carter candidate")
    print(render(report(load_control(), calculate(cases[0], swe))))


if __name__ == "__main__":
    main()
