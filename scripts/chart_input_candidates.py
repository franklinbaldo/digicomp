"""Parse unverified published chart inputs, never DR-70 instrumental observations.

Standard-library only. UTC and coordinate normalization is explicitly hypothetical
until the original edition and its conventions have been independently checked.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import re

DEFAULT_INPUT = (
    Path(__file__).resolve().parents[1]
    / "data/chart-input-candidates/rael-rudhyar-1980.json"
)
_COORD_RE = re.compile(r"^(\d{1,3})([NSEW])(\d{2})$")
_TIME_RE = re.compile(r"^(\d{1,2}):(\d{2})$")
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def coordinate(text: str, axis: str) -> float:
    """Return signed decimal degrees; east and north are positive."""
    match = _COORD_RE.fullmatch(text)
    if match is None or axis not in {"latitude", "longitude"}:
        raise ValueError(f"Invalid {axis}: {text!r}")
    degrees, hemisphere, minutes = int(match[1]), match[2], int(match[3])
    if (axis == "latitude" and hemisphere not in "NS") or (
        axis == "longitude" and hemisphere not in "EW"
    ):
        raise ValueError(f"Wrong hemisphere for {axis}: {text!r}")
    limit = 90 if axis == "latitude" else 180
    if minutes > 59 or degrees > limit or (degrees == limit and minutes != 0):
        raise ValueError(f"Out-of-range {axis}: {text!r}")
    result = degrees + minutes / 60
    return -result if hemisphere in "SW" else result


def hypothetical_utc(date_text: str, time_text: str) -> str:
    """Normalize continuous hours since midnight, NOT an established DR-70 rule."""
    match = _TIME_RE.fullmatch(time_text)
    if match is None:
        raise ValueError(f"Invalid hours:minutes: {time_text!r}")
    hours, minutes = int(match[1]), int(match[2])
    if hours > 47 or minutes > 59:
        raise ValueError(f"Out-of-range hours:minutes: {time_text!r}")
    if _DATE_RE.fullmatch(date_text) is None:
        raise ValueError(f"Expected calendar date YYYY-MM-DD without time or offset: {date_text!r}")
    midnight = datetime.fromisoformat(date_text).replace(tzinfo=timezone.utc)
    if midnight.hour or midnight.minute or midnight.second:
        raise ValueError("Date must be YYYY-MM-DD without a time")
    return (midnight + timedelta(hours=hours, minutes=minutes)).isoformat().replace(
        "+00:00", "Z"
    )


def normalize(case: dict) -> dict:
    if case.get("observed_chart_values") is not None:
        raise ValueError("Observed chart values belong in a separate reviewed source")
    return {
        "id": case["id"],
        "subject": case["subject"],
        "input_as_transcribed": {
            key: case[key]
            for key in (
                "date_as_printed", "utc_time_as_printed",
                "latitude_as_printed", "longitude_as_printed",
            )
        },
        "hypothetical_normalization": {
            "utc": hypothetical_utc(case["date_as_printed"], case["utc_time_as_printed"]),
            "latitude_deg": coordinate(case["latitude_as_printed"], "latitude"),
            "longitude_deg_east": coordinate(case["longitude_as_printed"], "longitude"),
            "assumption": case["time_interpretation"],
        },
        "evidence_status": "UNVERIFIED_PUBLISHED_INPUT_NOT_DR70_OUTPUT",
    }


def load(path: Path = DEFAULT_INPUT) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data["classification"] != "PUBLISHED_INPUT_CANDIDATES_NOT_DR70_OUTPUT":
        raise ValueError("Not the published-input candidate collection")
    cases = data["cases"]
    ids = [case["id"] for case in cases]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate candidate IDs")
    for case in cases:
        normalize(case)
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--id", help="Select exactly one published candidate ID")
    args = parser.parse_args()
    data = load(args.input)
    cases = [c for c in data["cases"] if args.id is None or c["id"] == args.id]
    if not cases:
        parser.error(f"Unknown candidate ID: {args.id}")
    print(json.dumps({"source": data["source"], "cases": [normalize(c) for c in cases]}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
