"""Compare a manually read published chart to a MODERN reference, never DR-70 fidelity."""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path

DEFAULT_PUBLICATION = (
    Path(__file__).resolve().parents[1]
    / "data/published-chart-transcriptions/rael1980-carter-pending.json"
)
_ALLOWED_FIELDS = {f"cusp_{i}" for i in range(1, 13)} | {
    "ascendant", "midheaven", "sun", "moon", "mercury", "venus", "mars", "jupiter", "saturn"
}
_SIGNS = (
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
)
_ABSOLUTE = "ecliptic_longitude_0_360_deg"
_UNRESOLVED = "unresolved_zodiac_notation"


def strict_json(path: Path) -> dict:
    def no_duplicate_keys(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"Duplicate JSON key: {key!r}")
            out[key] = value
        return out

    def no_nonfinite(text):
        raise ValueError(f"Invalid JSON numeric constant: {text}")

    def finite_float(token):
        number = float(token)
        if not math.isfinite(number):
            raise ValueError(f"Non-finite JSON numeric literal: {token}")
        return number

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=no_duplicate_keys,
                      parse_constant=no_nonfinite, parse_float=finite_float)


def signed_circular_residual(observed: float, reference: float) -> float:
    for value in (observed, reference):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError("Angular data must be finite numeric degrees")
        if not 0 <= value < 360:
            raise ValueError("Angular data must be in [0,360) degrees")
    return (observed - reference + 180) % 360 - 180


def modern_value(reference: dict, field: str) -> float:
    if field.startswith("cusp_"):
        return reference["cusps_deg"][field.split("_")[1]]
    if field in ("ascendant", "midheaven"):
        return reference["angles_deg"][field]
    return reference["planet_longitudes"][field]["longitude_deg"]


def validate_notation(field: str, observed: float, notation: dict) -> None:
    """Check the printed literal against its declared interpretation.

    Only deliberately narrow spellings are supported. Abbreviations, glyphs
    and illegible characters must remain unresolved, never become residuals
    merely because asserted metadata says they match.
    """
    signed_circular_residual(observed, 0)
    if not isinstance(notation, dict) or not isinstance(notation.get("literal"), str) or not notation["literal"].strip():
        raise ValueError(f"{field}: printed literal is required for review")
    kind = notation.get("kind")
    literal = notation["literal"].strip()
    if kind == "absolute_longitude_0_360_deg":
        if set(notation) != {"kind", "literal"}:
            raise ValueError(f"{field}: unexpected absolute-notation keys")
        match = re.fullmatch(r"(\d+(?:\.\d+)?)°?", literal)
        if match is None:
            raise ValueError(f"{field}: unrecognized absolute printed literal")
        if not math.isclose(observed, float(match.group(1)), rel_tol=0, abs_tol=1e-9):
            raise ValueError(f"{field}: absolute longitude disagrees with printed literal")
        return
    if kind != "zodiac_sign_degree":
        raise ValueError(f"{field}: unknown zodiac notation kind")
    if set(notation) != {"kind", "literal", "sign", "degree_within_sign"}:
        raise ValueError(f"{field}: sign and within-sign degree required")
    sign = notation["sign"]
    degree = notation["degree_within_sign"]
    if sign not in _SIGNS or isinstance(degree, bool) or not isinstance(degree, (int, float)):
        raise ValueError(f"{field}: invalid sign or within-sign degree")
    if not math.isfinite(degree) or not 0 <= degree < 30:
        raise ValueError(f"{field}: within-sign degree must be in [0,30)")

    # Accepted: "15 Taurus", "7.5 Libra", "7°30 Libra",
    # "7°30' Libra", "7°30′ Libra". No implicit OCR repair.
    match = re.fullmatch(r"(\d{1,2}(?:\.\d+)?)(?:°(\d{1,2})(?:['′])?)?\s+([A-Za-z]+)", literal)
    if match is None:
        raise ValueError(f"{field}: unrecognized zodiac printed literal")
    printed_degrees, printed_minutes, printed_sign = match.groups()
    if printed_sign != sign:
        raise ValueError(f"{field}: printed literal sign disagrees with declared sign")
    if printed_minutes is not None and ("." in printed_degrees or int(printed_minutes) >= 60):
        raise ValueError(f"{field}: invalid printed degree-minute notation")
    printed_within_sign = float(printed_degrees)
    if printed_minutes is not None:
        printed_within_sign += int(printed_minutes) / 60
    if not math.isclose(printed_within_sign, degree, rel_tol=0, abs_tol=1e-9):
        raise ValueError(f"{field}: printed literal degree disagrees with declared within-sign degree")
    if not math.isclose(observed, 30 * _SIGNS.index(sign) + degree, rel_tol=0, abs_tol=1e-9):
        raise ValueError(f"{field}: absolute longitude disagrees with printed sign+degree")

def compare(reference: dict, publication: dict) -> dict:
    if reference.get("classification") != "MODERN_REFERENCE_NOT_DR70":
        raise ValueError("Reference is not explicitly labelled as MODERN_REFERENCE_NOT_DR70")
    if reference.get("dr70_fidelity") != "NOT_RUN_NO_GOLDEN":
        raise ValueError("Do not mix an instrumental fidelity result into an editorial comparison")
    if reference.get("input_candidate_id") != publication.get("candidate_id"):
        raise ValueError("Reference and publication candidate IDs differ")
    if publication.get("classification") == "PUBLISHED_CHART_UNREAD":
        if publication.get("published_values_deg") != {}:
            raise ValueError("Unread publication must not contain numeric values")
        return {
            "classification": "EDITORIAL_CHART_VS_MODERN_REFERENCE_NOT_DR70",
            "candidate_id": reference["input_candidate_id"],
            "status": "NOT_RUN_NO_PUBLISHED_NUMERIC_TRANSCRIPTION",
            "dr70_fidelity": "NOT_RUN_NO_GOLDEN", "residuals_deg": []
        }
    if publication.get("classification") != "PUBLISHED_CHART_MANUAL_TRANSCRIPTION":
        raise ValueError("Only an unread or manually transcribed editorial chart is supported")
    source = publication.get("source") or {}
    if not (source.get("image_inspected") is True and source.get("page_locator")
            and source.get("reviewed_by") and source.get("source_url")):
        raise ValueError("Published values require visual inspection, exact page and reviewer")
    values = publication.get("published_values_deg")
    convention = publication.get("angular_convention")
    if convention == _UNRESOLVED:
        pending = publication.get("unresolved_fields")
        if values != {} or not isinstance(pending, list) or not pending or not all(isinstance(f, str) and f in _ALLOWED_FIELDS for f in pending) or len(pending) != len(set(pending)):
            raise ValueError("Unresolved zodiac notation requires pending fields and no numeric values")
        return {
            "classification": "EDITORIAL_CHART_VS_MODERN_REFERENCE_NOT_DR70",
            "candidate_id": reference["input_candidate_id"],
            "status": "NOT_COMPARABLE_UNRESOLVED_ZODIAC_NOTATION",
            "source_locator": source["page_locator"], "unresolved_fields": sorted(pending),
            "dr70_fidelity": "NOT_RUN_NO_GOLDEN", "residuals_deg": []
        }
    if convention != _ABSOLUTE:
        raise ValueError("Explicit ecliptic_longitude_0_360_deg convention required for residuals")
    if not isinstance(values, dict) or not values:
        raise ValueError("Manual transcription needs at least one observed chart value")
    notation = publication.get("source_notation")
    if not isinstance(notation, dict) or notation.keys() != values.keys():
        raise ValueError("Each numeric field requires exactly one printed-notation record")
    rows = []
    for field, observed in sorted(values.items()):
        if field not in _ALLOWED_FIELDS:
            raise ValueError(f"Unknown/unsupported field: {field}")
        validate_notation(field, observed, notation[field])
        modern = modern_value(reference, field)
        delta = signed_circular_residual(observed, modern)
        rows.append({"field": field, "published_deg": observed,
                     "modern_reference_deg": modern, "circular_difference_deg": delta})
    return {
        "classification": "EDITORIAL_CHART_VS_MODERN_REFERENCE_NOT_DR70",
        "candidate_id": reference["input_candidate_id"],
        "status": "PUBLISHED_MAP_RESIDUALS_NOT_DR70_FIDELITY",
        "source_locator": source["page_locator"],
        "dr70_fidelity": "NOT_RUN_NO_GOLDEN", "residuals_deg": rows
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference", type=Path, required=True)
    parser.add_argument("--publication", type=Path, default=DEFAULT_PUBLICATION)
    args = parser.parse_args()
    print(json.dumps(compare(strict_json(args.reference), strict_json(args.publication)), indent=2))


if __name__ == "__main__":
    main()
