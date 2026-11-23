"""Fail-closed intake for a *future* inspected historical Carter chart.

The checked-in locator contains only an OCR caption, never printed angles.
A future chart transcription requires an identified page image and review;
even accepted transcription remains editorial evidence, not a DR-70 golden.
"""

from __future__ import annotations

import argparse
from datetime import datetime
import json
from pathlib import Path
import re

STATES = frozenset({"INDEXED_CAPTION_ONLY", "INSPECTED_UNREADABLE", "INSPECTED_TRANSCRIBED"})
FIELDS = frozenset({"ASC", "MC", "Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"})
SOURCE = "https://fr.scribd.com/document/978057391/Les-Aspects-Astrologiques-Dane-Rudhyar-Leyla-Rael-Z-Library"
EXPECTED_KEYS = frozenset({"case_id", "source_family", "source_url", "copy_description", "printed_page_candidate_from_ocr", "caption_ocr", "state", "image_evidence", "angular_transcriptions", "instrumental_status", "ocr_isbn", "edition_identity"})
IMAGE_KEYS = frozenset({"printed_page_read", "digital_page_index", "sha256", "inspected_at_utc"})
TRANSCRIPTION_KEYS = frozenset({"field", "verbatim"})


def _is_inspected_timestamp(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None and parsed.utcoffset().total_seconds() == 0


def validate(record: object) -> dict:
    """Reject nominal transcriptions without identified scans; do not fill values.

    Shape checks cannot authenticate an inspection or a declared image hash;
    independent human review of the original image remains necessary.
    """
    if not isinstance(record, dict) or set(record) != EXPECTED_KEYS:
        raise ValueError("Unexpected historical locator shape")
    if (record["case_id"] != "RAEL1980-CARTER"
            or record["source_family"] != "RAEL_RUDHYAR_ASTROLOGICAL_ASPECTS"
            or record["source_url"] != SOURCE
            or record["copy_description"] != "FRENCH_TRANSLATION_COPYRIGHT_1982_UNAUTHENTICATED_SCAN"
            or record["printed_page_candidate_from_ocr"] != 362
            or record["caption_ocr"] != "Jimmy Carter; 1er oct. 1924; 32°02 N; 84°24 W; 13 h 00 T.U."
            or record["instrumental_status"] != "NO_DR70_GOLDEN"
            or record["ocr_isbn"] != "2-268-02638-8"
            or record["edition_identity"] != "BNF_1997_ISBN_MATCH_NOT_SCAN_AUTHENTICATION"):
        raise ValueError("Unexpected provenance, editorial copy, or fidelity status")
    state = record["state"]
    rows = record["angular_transcriptions"]
    image = record["image_evidence"]
    if not isinstance(state, str) or state not in STATES or not isinstance(rows, list):
        raise ValueError("Unknown inspection state or rows")
    if state == "INDEXED_CAPTION_ONLY":
        if image is not None or rows:
            raise ValueError("OCR-only locator cannot contain image evidence or chart angles")
    else:
        if (not isinstance(image, dict) or set(image) != IMAGE_KEYS
                or type(image["printed_page_read"]) is not int or image["printed_page_read"] < 1
                or type(image["digital_page_index"]) is not int or image["digital_page_index"] < 0
                or not isinstance(image["sha256"], str)
                or re.fullmatch(r"[0-9a-f]{64}", image["sha256"]) is None
                or not _is_inspected_timestamp(image["inspected_at_utc"])):
            raise ValueError("Inspection requires page identity, image digest and UTC time")
        if (state == "INSPECTED_UNREADABLE" and rows) or (state == "INSPECTED_TRANSCRIBED" and not rows):
            raise ValueError("Chart angular values must reflect inspection state")
        seen: set[str] = set()
        for row in rows:
            if not isinstance(row, dict) or set(row) != TRANSCRIPTION_KEYS:
                raise ValueError("Angular transcription has unexpected fields")
            field = row["field"]
            literal = row["verbatim"]
            if (not isinstance(field, str) or field not in FIELDS or field in seen
                    or not isinstance(literal, str) or not 2 <= len(literal.strip()) <= 160
                    or any(ch in literal for ch in "\r\n\x00")
                    or "?" in literal or "�" in literal):
                raise ValueError("Duplicate, uncertain or invalid angular transcription")
            seen.add(field)
    return {
        "case_id": record["case_id"],
        "classification": "EDITORIAL_LOCATOR_OR_TRANSCRIPTION_NOT_DR70_GOLDEN",
        "state": state,
        "edition_identity": record["edition_identity"],
        "fields_transcribed": len(rows),
        "independent_editorial_families": 1,
        "angular_comparison": "NOT_RUN_REQUIRES_BLIND_TRANSCRIPTION_REVIEW",
        "dr70_fidelity": "NOT_RUN_NO_GOLDEN",
    }


def _unique(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for k, v in pairs:
        if k in result:
            raise ValueError("Duplicate JSON key: " + k)
        result[k] = v
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", default="data/documentary/carter-french-1982-caption-locator.json")
    args = parser.parse_args()
    record = json.loads(Path(args.file).read_text(encoding="utf-8"), object_pairs_hook=_unique)
    print(json.dumps(validate(record), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
