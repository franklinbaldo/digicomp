"""Offline, accessible view of the two-tier Carter research comparison.

This is a visualization of documentary checks, never an instrument emulator
or a certificate that the Digicomp DR-70 produced the source values.
"""

from __future__ import annotations

from html import escape
import json
import math
import sys
from string import Template

from scripts.carter_historical_house_claims import HOUSE_CLAIMS, TEXT_URL
from scripts.carter_modern_table import FIELDS, FULL_CIRCLE_ARCSEC, load_control, published_arcsec

CLASSIFICATION = "DOCUMENTARY_TWO_TIER_RESEARCH_OUTPUT_NOT_DR70_FIDELITY"
HISTORICAL_STATUS = "INDEXED_SECONDARY_TEXT_NOT_CHECKED_AGAINST_1980_PAGE"
NOT_INSPECTED = "NOT_RUN_NO_INSPECTED_1980_CHART"
NOT_GOLDEN = "NOT_RUN_NO_GOLDEN"


def _text(value: object) -> str:
    return escape(str(value), quote=True)


def _validate(data: dict) -> tuple[dict, dict, str]:
    """Refuse changed attribution/status, fabricated counts and unsafe source URLs."""
    modern = data.get("modern_2023", {})
    history = data.get("historical_house_prose", {})
    if (data.get("classification") != CLASSIFICATION
            or data.get("case_id") != "RAEL1980-CARTER"
            or data.get("historical_chart_numeric_comparison") != NOT_INSPECTED
            or data.get("dr70_instrumental_comparison") != NOT_GOLDEN
            or modern.get("case_id") != "RAEL1980-CARTER"
            or modern.get("historical") != "NOT_RUN_NO_INSPECTED_1980_NUMBERS"
            or modern.get("dr70") != NOT_GOLDEN
            or history.get("source_status") != HISTORICAL_STATUS
            or history.get("precision") != "CATEGORIES_NOT_ANGULAR_RESIDUALS"
            or history.get("independent_editorial_families") != 1
            or history.get("source") != TEXT_URL):
        raise ValueError("Cannot visualize promoted or unrecognized documentary evidence")

    control = load_control()
    source = control.get("source", {})
    # This document only cites the two known editorial sources; never build
    # an HTML anchor from arbitrary output or unvalidated JSON metadata.
    if (control.get("classification") != "MODERN_CHART_CONTROL_NOT_DR70_OUTPUT"
            or source.get("publication_year") != 2023
            or source.get("chart_provider") != "AstroDienst"
            or source.get("url", "").startswith("https://static1.squarespace.com/") is not True
            or not TEXT_URL.startswith("https://www.scribd.com/")):
        raise ValueError("Unexpected documentary source metadata")

    angles = modern.get("rows", [])
    if (not isinstance(angles, list) or len(angles) != len(FIELDS)
            or {r.get("field") for r in angles} != set(FIELDS)
            or modern.get("compared") != len(FIELDS)):
        raise ValueError("Incomplete modern field set")
    matches = 0
    for row in angles:
        angle, residual = row.get("model_longitude_deg"), row.get("residual_arcsec")
        if (type(angle) not in (int, float) or type(residual) not in (int, float)
                or not math.isfinite(angle) or not 0 <= angle < 360
                or not math.isfinite(residual) or not -648000 <= residual <= 648000
                or type(row.get("within_declared_tolerance")) is not bool
                or row["within_declared_tolerance"] is not (abs(residual) <= 1)
                or not isinstance(row.get("published_2023"), str)):
            raise ValueError("Invalid modern comparison row")
        # Recompute the displayed delta from the canonical versioned DMS.
        # Range/count checks alone would accept a forged residual and 9/9 badge.
        published_entry = control["positions"][row["field"]]
        expected_printed = f'{published_entry["sign"]} {published_entry["literal"]}'
        printed_arcsec = published_arcsec(published_entry)
        expected_delta = (
            (angle * 3600 - printed_arcsec + FULL_CIRCLE_ARCSEC / 2)
            % FULL_CIRCLE_ARCSEC
        ) - FULL_CIRCLE_ARCSEC / 2
        if (row["published_2023"] != expected_printed
                or not math.isclose(residual, expected_delta, rel_tol=0, abs_tol=1e-6)):
            raise ValueError("Documentary 2023 literal or angular residual disagrees with canonical source")
        matches += row["within_declared_tolerance"]
    if modern.get("within_tolerance") != matches:
        raise ValueError("Modern match total differs from rows")

    rows = history.get("rows", [])
    if (not isinstance(rows, list) or len(rows) != len(HOUSE_CLAIMS)
            or {r.get("body") for r in rows} != set(HOUSE_CLAIMS)
            or history.get("total_claims") != len(rows)):
        raise ValueError("Incomplete historical claim set")
    matches13 = matches12 = 0
    for row in rows:
        body = row["body"]
        if (type(row.get("historical_prose_house")) is not int
                or row["historical_prose_house"] != HOUSE_CLAIMS[body][0]
                or row.get("source_text_line_range_not_page") != HOUSE_CLAIMS[body][1]
                or any(type(row.get(key)) is not int or row[key] not in range(1, 13)
                       for key in ("computed_13_ut", "computed_12_ut"))
                or type(row.get("match_13_ut")) is not bool
                or type(row.get("match_12_ut")) is not bool
                or row["match_13_ut"] is not (row["computed_13_ut"] == row["historical_prose_house"])
                or row["match_12_ut"] is not (row["computed_12_ut"] == row["historical_prose_house"])):
            raise ValueError("Invalid historical categorical row")
        matches13 += row["match_13_ut"]
        matches12 += row["match_12_ut"]
    if (history.get("matches_13_ut") != matches13
            or history.get("matches_12_ut_counterfactual") != matches12):
        raise ValueError("Historical match totals differ from rows")
    return modern, history, source["url"]


def render_html(data: dict) -> str:
    """Return a standalone HTML document using only the versioned data supplied."""
    modern, history, modern_url = _validate(data)
    angular_rows = []
    for row in modern["rows"]:
        status = "Concorda" if row["within_declared_tolerance"] else "Diverge"
        angular_rows.append(
            "<tr><th scope=\"row\">{}</th><td>{}</td><td class=\"number\">{:.6f}°</td>"
            "<td class=\"number\">{:+.3f}″</td><td>{}</td></tr>".format(
                _text(row["field"]), _text(row["published_2023"]),
                row["model_longitude_deg"], row["residual_arcsec"], status))
    house_rows = []
    for row in history["rows"]:
        status13 = "Concorda" if row["match_13_ut"] else "Diverge"
        status12 = "Concorda" if row["match_12_ut"] else "Diverge"
        house_rows.append(
            "<tr><th scope=\"row\">{}</th><td class=\"number\">{}</td>"
            "<td class=\"number\">{} ({})</td><td class=\"number\">{} ({})</td>"
            "<td>{}</td></tr>".format(
                _text(row["body"]), row["historical_prose_house"],
                row["computed_13_ut"], status13, row["computed_12_ut"], status12,
                _text(row["source_text_line_range_not_page"])))
    return Template("""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
<title>Carter | confronto documental | Digicomp</title>
<style>
:root{color-scheme:light dark;font-family:system-ui,-apple-system,sans-serif;line-height:1.55}
body{margin:0;background:Canvas;color:CanvasText}main{max-width:70rem;margin:auto;padding:1.2rem}
h1{font-size:clamp(1.55rem,4vw,2.4rem);line-height:1.2}h2{font-size:1.35rem;margin-top:2rem}
p,li{max-width:80ch}.intro{font-size:1.07rem}.statistics{display:flex;flex-wrap:wrap;gap:1rem}
.stat{border:1px solid GrayText;border-radius:.5rem;padding:.8rem 1rem;flex:1 1 10rem}
.stat strong{display:block;font-size:1.65rem}.table-scroll{overflow:auto;max-width:100%;border:1px solid GrayText;border-radius:.4rem}
.table-scroll:focus-visible,a:focus-visible{outline:3px solid Highlight;outline-offset:2px}
table{border-collapse:collapse;width:100%;min-width:42rem;text-align:left}caption{text-align:left;font-weight:600;padding:.75rem}
th,td{border-top:1px solid GrayText;padding:.6rem .7rem;vertical-align:top}thead{background:ButtonFace}
.number{font-variant-numeric:tabular-nums;white-space:nowrap}a{color:LinkText;overflow-wrap:anywhere}
.status{border-left:.25rem solid GrayText;padding-left:.9rem;margin-top:1.5rem;overflow-wrap:anywhere}
@media print{main{max-width:none}body{font-size:10pt}.table-scroll{overflow:visible}table{min-width:0}.stat{break-inside:avoid}a{color:inherit}}
</style></head><body><main>
<header><p>Digicomp DR-70 · pesquisa documental · RAEL1980-CARTER</p>
<h1>Jimmy Carter: o que podemos comparar hoje?</h1>
<p class="intro">Duas classes de evidência, <strong>sem comprovação de saída instrumental do DR-70</strong>:
posições angulares modernas publicadas em 2023 e casas astrológicas descritas em texto secundário de obra de 1980.</p></header>
<section aria-labelledby="summary"><h2 id="summary">Resultados e seus limites</h2>
<div class="statistics"><div class="stat"><strong>$modern_matches/$modern_total</strong>Ângulos 2023 dentro de ±1″</div>
<div class="stat"><strong>$matches13/$houses_total</strong>Casas compatíveis às 13h UT (modelo moderno)</div>
<div class="stat"><strong>$matches12/$houses_total</strong>Casas compatíveis às 12h UT (controle hipotético)</div></div>
<p>As quatro descrições de casas pertencem à <strong>mesma família editorial</strong>. A coincidência de quatro casas não identifica uma hora única de nascimento. A concordância angular de 2023 pode compartilhar motor astronômico com o cálculo.</p></section>
<section aria-labelledby="modern"><h2 id="modern">1. Nove posições publicadas em 2023</h2>
<p>Referência: <a href="$modern_url">AstroDienst, carta reproduzida por Naomi Rabinowitz, p. 12</a>.
Cálculo moderno Swiss Ephemeris/Moshier; tolerância pré-declarada de ±1 segundo de arco. Não comparar cúspides Whole Signs com cúspides Campanus.</p>
<div class="table-scroll" role="region" tabindex="0" aria-label="Tabela de posições angulares modernas, rolável horizontalmente">
<table><caption>Diferença circular entre a publicação de 2023 e o modelo moderno</caption><thead><tr><th scope="col">Campo</th><th scope="col">Publicado</th><th scope="col">Modelo (°)</th><th scope="col">Resíduo (″)</th><th scope="col">Resultado</th></tr></thead>
<tbody>$angular_rows</tbody></table></div></section>
<section aria-labelledby="historical"><h2 id="historical">2. Categorias de casas descritas no texto histórico</h2>
<p>Fonte: <a href="$historical_url">transcrição secundária de Raël/Rudhyar</a> (localizadores de linhas indexadas, não páginas impressas).
13h UT corresponde à entrada transcrita. <strong>12h UT é um contrafactual, não uma segunda fonte histórica.</strong>
Os dois cenários usam casas Campanus modernas, não cálculos recuperados do DR-70.</p>
<div class="table-scroll" role="region" tabindex="0" aria-label="Tabela das quatro casas históricas, rolável horizontalmente">
<table><caption>Quatro categorias da mesma família editorial</caption><thead><tr><th scope="col">Corpo</th><th scope="col">Texto</th><th scope="col">13h UT</th><th scope="col">12h UT hipotéticas</th><th scope="col">Localizador textual</th></tr></thead>
<tbody>$house_rows</tbody></table></div></section>
<section class="status" aria-labelledby="limits"><h2 id="limits">Comparações ainda não realizadas</h2>
<p>Figura histórica com graus angulares diretamente inspecionados: <code>$not_inspected</code>.<br>
Fidelidade instrumental DR-70: <code>$not_golden</code>. Não existe ROM original documentada neste teste.</p>
<p>Esta página é um relatório estático gerado dos dados versionados. Não representa emulação, observação independente ou certificação da máquina histórica.</p></section>
</main></body></html>
""").substitute(
        modern_matches=modern["within_tolerance"], modern_total=modern["compared"],
        matches13=history["matches_13_ut"], matches12=history["matches_12_ut_counterfactual"],
        houses_total=history["total_claims"], modern_url=_text(modern_url),
        historical_url=_text(history["source"]), angular_rows="\n".join(angular_rows),
        house_rows="\n".join(house_rows), not_inspected=NOT_INSPECTED, not_golden=NOT_GOLDEN)


def main() -> None:
    """Read the existing two-tier JSON report on stdin; emit offline HTML."""
    def unique(pairs: list[tuple[str, object]]) -> dict:
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"Duplicate JSON key: {key}")
            out[key] = value
        return out

    def finite_float(literal: str) -> float:
        number = float(literal)
        if not math.isfinite(number):
            raise ValueError("Non-finite JSON numeric literal")
        return number

    def reject_constant(literal: str) -> None:
        raise ValueError(f"Non-finite JSON constant: {literal}")

    report = json.load(sys.stdin, object_pairs_hook=unique,
                       parse_float=finite_float, parse_constant=reject_constant)
    print(render_html(report))


if __name__ == "__main__":
    main()
