"""Compare a manually read published chart to a MODERN reference, never DR-70 fidelity."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

DEFAULT_PUBLICATION = (
    Path(__file__).resolve().parents[1]
    / "data/published-chart-transcriptions/rael1980-carter-pending.json"
)
_ALLOWED_FIELDS = {f"cusp_{i}" for i in range(1, 13)} | {
    "ascendant", "midheaven", "sun", "moon", "mercury", "venus", "mars", "jupiter", "saturn"
}


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

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=no_duplicate_keys,
                      parse_constant=no_nonfinite)


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
    if not isinstance(values, dict) or not values:
        raise ValueError("Manual transcription needs at least one observed chart value")
    rows = []
    for field, observed in sorted(values.items()):
        if field not in _ALLOWED_FIELDS:
            raise ValueError(f"Unknown/unsupported field: {field}")
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
