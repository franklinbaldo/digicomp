"""Fail-closed identity checks for DR-70 observational corpus (stdlib only).

This does NOT validate JSON Schema or authenticate photographs, devices or outputs.
Run: python3 scripts/check_fidelity_corpus.py [corpus.json]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

DEFAULT_CORPUS = Path(__file__).resolve().parents[1] / "data/fidelity/observations.json"


class CorpusError(ValueError):
    """A corpus could not be read without losing observational identity."""


def _unique_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for name, value in pairs:
        if name in result:
            raise CorpusError(f"duplicate JSON property {name!r} (would silently overwrite evidence)")
        result[name] = value
    return result


def _reject_nonfinite(value: str) -> None:
    raise CorpusError(f"non-JSON number {value!r} is forbidden")


def check_corpus(path: Path) -> int:
    """Return observation count or raise CorpusError on loss of identity.

    JSON Schema separately checks field types, statuses, URLs, nulls and replayability.
    """
    try:
        raw = path.read_text(encoding="utf-8")
        corpus = json.loads(raw, object_pairs_hook=_unique_pairs, parse_constant=_reject_nonfinite)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise CorpusError(f"cannot read corpus: {exc}") from exc

    if not isinstance(corpus, dict):
        raise CorpusError("corpus root must be an object")
    observations = corpus.get("observations")
    if not isinstance(observations, list):
        raise CorpusError("observations must be a list")
    seen: set[str] = set()
    seen_provenance: dict[tuple[str, str], str] = {}
    for position, item in enumerate(observations):
        if not isinstance(item, dict):
            raise CorpusError(f"observations[{position}] must be an object")
        identifier = item.get("id")
        if not isinstance(identifier, str) or not identifier:
            raise CorpusError(f"observations[{position}].id must be a nonempty string")
        if identifier in seen:
            raise CorpusError(f"duplicate observation ID {identifier!r} at index {position}")
        seen.add(identifier)
        source = item.get("source")
        if isinstance(source, dict):
            url, locator = source.get("url"), source.get("locator")
            # The schema checks source types; here we guard observational identity.
            if isinstance(url, str) and url and isinstance(locator, str) and locator:
                evidence_key = (url, locator)
                first = seen_provenance.get(evidence_key)
                if first is not None:
                    raise CorpusError(
                        f"duplicate source URL and locator for {identifier!r}; "
                        f"already used by {first!r} (same cited region is not a new observation)"
                    )
                seen_provenance[evidence_key] = identifier
    return len(observations)


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) > 1:
        print("usage: check_fidelity_corpus.py [corpus.json]", file=sys.stderr)
        return 2
    path = Path(args[0]) if args else DEFAULT_CORPUS
    try:
        count = check_corpus(path)
    except CorpusError as exc:
        print(f"FAIL {path}: {exc}", file=sys.stderr)
        return 1
    print(f"PASS {path}: {count} observation IDs and source URL+locator pairs unique; JSON keys unique")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
