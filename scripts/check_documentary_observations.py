#!/usr/bin/env python3
"""Reconcile secondary Carlson candidate groups with the source catalog.

The TSV exporter can feed the separate Rust prototype in Digicomp PR #131.
Only text from one editorial figure is checked; not a DR-70 calculation,
angular comparison, independent visual review or golden case.
"""
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCUMENT = ROOT / "data/documentary-observations/carlson-fig1-f83.json"
CATALOG = ROOT / "data/output-candidates/catalog.json"
GOLDEN = ROOT / "data/fidelity/observations.json"
REPORT = ROOT / "data/documentary-observations/carlson-fig1-baseline.txt"

def _unique_properties(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result

def _reject_constant(token):
    raise ValueError(f"non-JSON numeric constant: {token}")

def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"),
                      object_pairs_hook=_unique_properties,
                      parse_constant=_reject_constant)

def rust_pairs(doc):
    """Emit only paired textual candidates, never degrees/minutes or firmware."""
    rows = doc["readings"]
    return "".join(
        "\t".join([
            rows[i]["house"], rows[i + 6]["house"],
            *rows[i]["candidate_groups"], *rows[i + 6]["candidate_groups"],
        ]) + "\n"
        for i in range(6)
    )

def validate(doc, catalog, golden):
    errors = []
    entries = catalog.get("entries", [])
    matches = [item for item in entries
               if item.get("id") == doc.get("source_catalog_id")]
    if len(matches) != 1:
        return ["catalog source must resolve to exactly one entry"]
    source = matches[0]
    for name, expected in (
        ("format_version", "1.0"),
        ("id", "DOC-CARLSON-F83-FIG1"),
        ("source_catalog_id", "OUT-CARLSON-F83"),
        ("source_family_id", source["family_id"]),
        ("source_url", source["source_url"]),
        ("source_locator", source["locator"]),
        ("transcription_reference", source["related_ledger"]),
        ("publication_lineage_alias", "OUT-CARLSON-F85"),
        ("classification", "SECONDARY_VISUAL_CANDIDATE_NOT_DEVICE_OUTPUT"),
        ("transcription_review", "NONBLIND_SECONDARY_REPORT_NOT_12_INDEPENDENT_READINGS"),
        ("sample_split", "unassigned"),
        ("native_print_authenticated", False),
        ("input_complete", False),
        ("output_complete", False),
        ("numeric_holdout_eligible", False),
        ("complete_published_angles", 0),
    ):
        if doc.get(name) != expected or type(doc.get(name)) is not type(expected):
            errors.append(f"{name}: unsupported change of provenance or certainty")
    if source.get("sample_split") != "unassigned" or source.get("numeric_holdout_eligible") is not False:
        errors.append("catalog cannot authorize documentary numeric holdout")
    if (source.get("status") != "candidate"
            or source.get("kind") != "published_chart_candidate"
            or source.get("attribution") != "attributed_calculations_not_native_output"
            or any(source.get(flag) is not False
                   for flag in ("input_complete", "output_complete", "replayable"))):
        errors.append("catalog source cannot be promoted to native/replayable output")

    # The 1983 preprint and the 1985 republication reproduce the same
    # editorial figure. A separate URL or PDF cannot become an independent
    # numeric holdout by silently rewriting just the catalog alias.
    aliases = [item for item in entries if isinstance(item, dict)
               and item.get("id") == doc.get("publication_lineage_alias")]
    if len(aliases) != 1:
        errors.append("publication lineage alias must resolve exactly once")
    else:
        alias = aliases[0]
        if alias.get("family_id") != source.get("family_id"):
            errors.append("publication lineage alias cannot be an independent family")
        if (alias.get("status") != "candidate"
                or alias.get("kind") != "published_chart_candidate"
                or alias.get("attribution") != "attributed_calculations_not_native_output"
                or alias.get("sample_split") != "unassigned"
                or alias.get("numeric_holdout_eligible") is not False
                or any(alias.get(flag) is not False
                       for flag in ("input_complete", "output_complete", "replayable"))):
            errors.append("publication lineage alias cannot become numeric holdout/replayable")
    if golden.get("observations") != []:
        errors.append("golden corpus changed; documentary baseline cannot certify it")

    # Separate *unparsed* visual candidates from the known twelve house rows.
    # The date-like string is not a birth date; the aspect-grid numbers are
    # not typed as an angle. F83/F85 are one editorial family, not two reads.
    expected_regions = (
        ("left-secondary-date-block", "4.01.1981",
         "DATE REC[...] alongside C1 SEC", "unresolved_not_birth_input"),
        ("right-aspect-grid-first-data-row", "07 54 47",
         "C1 NATAL aspect grid under ORB", "unresolved_not_angular_comparison"),
    )
    candidates = doc.get("additional_literal_candidates")
    if not isinstance(candidates, list) or len(candidates) != len(expected_regions):
        errors.append("additional candidate regions must have two unparsed entries")
    else:
        allowed = {"region", "literal_candidate", "context", "reading_status",
                   "semantic_role", "interpreted_value"}
        for i, (region, literal, context, meaning) in enumerate(expected_regions):
            candidate = candidates[i]
            if not isinstance(candidate, dict) or set(candidate) != allowed:
                errors.append(f"additional candidate {i}: unexpected fields")
                continue
            if (candidate.get("region") != region
                    or candidate.get("literal_candidate") != literal
                    or candidate.get("context") != context
                    or candidate.get("reading_status") != "single_nonblind_visual_candidate"
                    or candidate.get("semantic_role") != meaning
                    or candidate.get("interpreted_value") is not None):
                errors.append(f"additional candidate {i}: value or certainty changed")

    rows = doc.get("readings")
    if not isinstance(rows, list) or len(rows) != 12:
        return errors + ["readings: expected twelve individually addressable rows"]
    reported = source.get("reported_numeric_fragments", [])
    if len(reported) != 6:
        return errors + ["catalog must contain six reported candidate pairs"]

    seen = set()
    for position, row in enumerate(rows):
        if not isinstance(row, dict):
            errors.append(f"row {position}: not an object")
            continue
        house = f"H{position+1:02d}"
        pair_pos = position % 6
        pair = f"H{pair_pos+1:02d}/H{pair_pos+7:02d}"
        groups = row.get("candidate_groups")
        if row.get("house") != house or house in seen:
            errors.append(f"row {position}: house ordering or duplicate")
        seen.add(row.get("house"))
        if row.get("pair_id") != pair:
            errors.append(f"{house}: incorrect provenance pair")
        if not (isinstance(groups, list) and len(groups) == 2
                and all(isinstance(v, str) and len(v) == 2
                        and v.isascii() and v.isdigit() for v in groups)):
            errors.append(f"{house}: groups must be two unparsed two-digit strings")
            continue
        reference = reported[pair_pos]
        if reference.get("pair") != pair or reference.get("groups") != groups:
            errors.append(f"{house}: differs from documented catalog pair")
        if row.get("zodiac_glyph") is not None or row.get("interpreted_longitude_deg") is not None:
            errors.append(f"{house}: unresolved glyph/angle must remain null")
        if row.get("reading_status") != "secondary_pair_report_not_independently_transcribed":
            errors.append(f"{house}: second visual reading not documented")
    return errors

def report(doc):
    rows = doc["readings"]
    matching = sum(rows[i]["candidate_groups"] == rows[i+6]["candidate_groups"]
                   for i in range(6))
    return (
        "DOCUMENTARY_TEXT_BASELINE_NOT_DR70_OUTPUT\n"
        f"source_catalog_id={doc['source_catalog_id']}\n"
        f"family={doc['source_family_id']}\n"
        "reading_basis=NONBLIND_SECONDARY_PAIR_REPORT\n"
        "candidate_house_slots=12\n"
        "candidate_numeric_groups=24\n"
        "candidate_pairs=6\n"
        # A frozen fingerprint, not a second transcription or a DR-70 result.
        f"candidate_pairs_sha256={hashlib.sha256(rust_pairs(doc).encode('utf-8')).hexdigest()}\n"
        "additional_unparsed_candidates=2\n"
        "additional_interpreted_values=0\n"
        f"apparent_pair_matches={matching}\n"
        f"apparent_pair_differences={6-matching}\n"
        "complete_published_angles=0\n"
        "angular_numeric_comparisons=0\n"
        "angular_tolerance=NOT_APPLICABLE\n"
        "independent_holdout=0\n"
        "modern_reference_comparison=NOT_RUN_NO_COMPLETE_ANGLE\n"
        "device_fidelity=NOT_RUN_NO_GOLDEN\n"
    )

def main():
    try:
        doc, catalog, golden = (load_json(path)
                                for path in (DOCUMENT, CATALOG, GOLDEN))
        errors = validate(doc, catalog, golden)
        if errors:
            raise ValueError("; ".join(errors))
        actual = report(doc)
        expected = REPORT.read_text(encoding="utf-8")
        if actual != expected:
            raise ValueError("documentary baseline report drift")
    except (ValueError, OSError, TypeError, KeyError) as exc:
        print(f"FAIL documentary Carlson guard: {exc}", file=sys.stderr)
        return 1
    if sys.argv[1:] == ["--emit-rust-tsv"]:
        print(rust_pairs(doc), end="")
    elif len(sys.argv) == 1:
        print(actual, end="")
    else:
        print("usage: check_documentary_observations.py [--emit-rust-tsv]", file=sys.stderr)
        return 2
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
