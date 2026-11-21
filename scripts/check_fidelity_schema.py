"""Enforce the DR-70 corpus JSON Schema as a mandatory offline gate.

Identity checks run first. Passing this structural gate does not authenticate
any observation, historical source, device, or DR-70 numerical result.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from scripts.check_fidelity_corpus import (
    DEFAULT_CORPUS,
    CorpusError,
    _reject_nonfinite,
    _unique_pairs,
    check_corpus,
)

DEFAULT_SCHEMA = Path(__file__).resolve().parents[1] / "data/fidelity/corpus.schema.json"


def _read_json(path: Path) -> object:
    try:
        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_pairs,
            parse_constant=_reject_nonfinite,
        )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise CorpusError(f"cannot read {path}: {exc}") from exc


def check_schema(
    corpus_path: Path = DEFAULT_CORPUS, schema_path: Path = DEFAULT_SCHEMA
) -> int:
    """Return case count only if identity and the entire schema both pass."""
    try:
        from jsonschema import Draft202012Validator, FormatChecker
        from jsonschema.exceptions import SchemaError
    except ImportError as exc:
        raise CorpusError("jsonschema[format]==4.26.0 is required (run via pinned prek/uvx hook)") from exc
    count = check_corpus(corpus_path)
    schema = _read_json(schema_path)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise CorpusError(f"invalid corpus schema: {exc.message}") from exc

    corpus = _read_json(corpus_path)
    errors = sorted(
        Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(corpus),
        key=lambda error: (tuple(str(p) for p in error.absolute_path), error.message),
    )
    if errors:
        error = errors[0]
        location = "$" + "".join(
            f"[{part}]" if isinstance(part, int) else f".{part}"
            for part in error.absolute_path
        )
        raise CorpusError(f"JSON Schema violation at {location}: {error.message}")
    return count


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) > 1:
        print("usage: check_fidelity_schema.py [corpus.json]", file=sys.stderr)
        return 2
    path = Path(args[0]) if args else DEFAULT_CORPUS
    try:
        count = check_schema(path)
    except CorpusError as exc:
        print(f"FAIL {path}: {exc}", file=sys.stderr)
        return 1
    print(f"PASS {path}: {count} observations; identity + JSON Schema 2020-12")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
