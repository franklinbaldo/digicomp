"""Arithmetic of three 2023 Carter pairs named in secondary historical prose.

Only the external 2023 AstroDienst chart supplies angular DMS. The text
attributed to Raël/Rudhyar (1980) supplies qualitative aspect names, not
visually checked 1980 longitudes. Nothing here certifies DR-70 output.
No Swiss Ephemeris dependency is used.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from scripts.carter_qualitative_relation import (
    DEFAULT_CONTROL, FULL_CIRCLE_SECONDS, compare, longitude_seconds,
)

# The source's secondary-text line indices are not physical printed pages.
CLAIMS = (
    ("venus_pluto_novile", "venus", "pluto", 40, "3357-3359"),
    ("sun_moon_semiquintile", "sun", "moon", 36, "3412-3413"),
    ("mars_jupiter_quintile", "mars", "jupiter", 72, "3412-3413"),
)


def additional_relations(control: dict) -> dict:
    """Return exact modern differences, labelled inconclusive historically."""
    # Also enforces the existing fail-closed modern-only/golden guards.
    compare(control)
    auxiliary = control.get("auxiliary_qualitative_positions")
    if not isinstance(auxiliary, dict) or set(auxiliary) != {"pluto"}:
        raise ValueError("Only the documented 2023 auxiliary Pluto is accepted")
    if control.get("source", {}).get("source_pdf_sha256") is not None:
        raise ValueError("This experiment has no obtained source PDF hash")
    positions = control["positions"]
    if set(positions) != {
        "ascendant", "midheaven", "sun", "moon", "mercury", "venus",
        "mars", "jupiter", "saturn",
    }:
        raise ValueError("Preserve the original nine-field modern control")
    dms = {name: longitude_seconds(value) for name, value in
           {**positions, **auxiliary}.items()}
    relations = []
    for key, first, second, nominal_degrees, text_lines in CLAIMS:
        directed = (dms[first] - dms[second]) % FULL_CIRCLE_SECONDS
        separation = min(directed, FULL_CIRCLE_SECONDS - directed)
        nominal = nominal_degrees * 3600
        relations.append({
            "id": key,
            "source_text_lines_not_printed_pages": text_lines,
            "modern_2023_separation_arcseconds": separation,
            "aspect_nominal_arcseconds": nominal,
            "modern_deviation_signed_arcseconds": separation - nominal,
            "historical_relation_test": "INDETERMINATE_NO_INSPECTED_1980_CHART",
        })
    return {
        "classification": "MODERN_2023_VS_SECONDARY_HISTORICAL_ASPECT_NAMES",
        "claim_source_status": "SECONDARY_TEXT_NOT_VERIFIED_AGAINST_1980_PAGE_IMAGE",
        "modern_source_status": "ONE_2023_PUBLICATION_NOT_INDEPENDENT_SESSIONS",
        "auxiliary_pluto_role": "2023_DMS_ONLY_NOT_ONE_OF_NINE_REFERENCE_FIELDS",
        "relations": relations,
        "historical_chart_residual": "NOT_RUN_NO_INSPECTED_1980_NUMBERS",
        "dr70_fidelity": "NOT_RUN_NO_GOLDEN",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--control", type=Path, default=DEFAULT_CONTROL)
    args = parser.parse_args()
    with args.control.open(encoding="utf-8") as stream:
        control = json.load(stream)
    print(json.dumps(additional_relations(control), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
