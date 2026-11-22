---
type: Documento
title: "Carter: output documental em dois níveis sem confundir 1980 e 2023"
description: "Relatório reproduzível para observações categóricas de 1980 e números publicados de 2023, com limites de proveniência."
timestamp: 2026-11-22T17:11:00-04:00
estado: provisorio
---

# Saída documental Carter, duas classes de evidência

**Objetivo de Digicomp #130:** apresentar um resultado humano legível e JSON exportável sem prometer uma ROM, firmware ou golden do DR-70. Este protótipo reúne resultados que já tinham rotinas numéricas independentes, mas antes apareciam em arquivos separados.

Executar numa sandbox de pesquisa com a dependência **opcional** externa `pyswisseph==2.10.3.2`:

```sh
python -B -m unittest discover -s tests -p 'test_carter_documentary_dashboard.py' -v
python -B -m scripts.carter_documentary_dashboard
python -B -m scripts.carter_documentary_dashboard --format json
```

A mesma sequência é exercida no workflow público `chart-reference.yml`. Testes de formatação sem Swiss usam exclusivamente fixtures sintéticas declaradas; o passo numérico posterior usa os documentos versionados e o motor moderno.

## Níveis separados

1. **Controle moderno de nove números (2023)**: carta AstroDienst reproduzida em Naomi Rabinowitz, *Jimmy Carter and the Knight of Pentacles Card*, p. 12, [PDF da publicação](https://static1.squarespace.com/static/625588022bac29595ab0c386/t/652c6205bd50527fa4e8778a/1697407494104/Jimmy%2BCarter%2Band%2Bthe%2BKnight%2Bof%2BPentacles_final.pdf#page=12). O controle [JSON](../data/modern-controls/carter-astro-dienst-2023.json) contém nove longitudes publicadas, comparadas por diferença circular com a referência Swiss/Moshier (tolerância ±1 segundo de arco). AstroDienst pode usar o **mesmo motor**, portanto concordância não significa independência algorítmica.

2. **Quatro alegações históricas categóricas (edição 1980)**: Lua casa I, Mercúrio XI, Plutão IX, Urano V, da [transcrição textual secundária](https://www.scribd.com/document/633437269/Dane-Rudhyar-Leyla-Rael-Astrological-Aspects-A-Process-Oriented-Approach-Rudhyar-Series-Aurora-Press-Inc-2018-pdf), linhas indexadas 3843–3849 e 6117–6121 (não números de página). Elas formam **uma família editorial**, não quatro testemunhas independentes. O relatório mostra casas Campanus modernas em 13h UT transcritas e 12h UT contrafactuais. O resultado esperado anterior era 4/4 e 2/4; a execução automática deve confirmar ou falhar, sem forçar a saída.

O prefácio de Raël/Rudhyar, datado de 23/03/1979, agradece a Nicki Michaels por cálculos de conferência em computador e a Tony Milner pela caligrafia das cartas. O apêndice atribui o recálculo com cúspides Campanus ao DR-70; são **duas afirmações editoriais**, não prova de duas máquinas independentes ou saída impressa do DR-70. A família documental, página original e operação concreta continuam sem autenticação material.

## Critérios de interpretação

- A janela de 4/4 categorias estende-se além de uma hora; portanto 13h UT não foi inferida exclusivamente das casas.
- Não existem graus extraídos de uma figura física da edição de 1980; **sem resíduos angulares históricos**.
- Zero golden instrumental, zero ROM original. O JSON e o texto declaram expressamente `NOT_RUN_NO_INSPECTED_1980_CHART` e `NOT_RUN_NO_GOLDEN`.
- Um teste que altera categoria, hora de referência ou classificação para `PASS` deve falhar, não se converter silenciosamente em evidência.
- Continuar a busca de uma carta com graus e cúspides legíveis para alcançar uma comparação histórica quantitativa real.

## Saída HTML local e acessível (Raposa R171)

O mesmo JSON de duas classes pode ser apresentado numa **página HTML estática offline**:

```bash
set -o pipefail
python -B -m scripts.carter_documentary_dashboard --format json |
  python -S -B -m scripts.carter_documentary_html > carter-documentary.html
```

O segundo processo usa somente Python padrão e os dados versionados. Não consulta serviços externos, não executa JavaScript nem usa bibliotecas de interface. A página mostra tabelas com cabeçalhos semânticos e captions, regiões roláveis por teclado, CSP que bloqueia conteúdos remotos, CSS para 320 px e impressão, links às duas fontes e estados explícitos de ausência de comparação instrumental. O HTML é um relatório de pesquisa **gerado**, não substitui o site público, não autoriza incorporar uma carta proprietária nem comprova acessibilidade em dispositivos assistivos reais.

O parser de entrada rejeita chaves JSON duplicadas, `NaN`, `Infinity` e `1e999`; o renderer recusa promoção a `PASS`, alteração na família documental, campos ausentes, totais inconsistentes e longitudes não finitas. Valores textuais são escapados e as URLs têm origem limitada às duas fontes documentadas. A regressão usa fixtures **sintéticas somente para testar apresentação**; a exportação no workflow usa o cálculo moderno executado contra os dados versionados e arquiva o HTML por sete dias como artefato da execução. A etapa só passa se esse pipeline terminar com 9/9, 4/4 e 2/4, sem substituir categorias por graus não inspecionados.

**Limite:** sem teste físico de zoom nativo/VoiceOver/TalkBack e sem medição de output real de DR-70. A visualização não cria uma terceira família de evidência.
