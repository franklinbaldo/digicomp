---
type: Documento
title: "Controle documental: Hewitt/Matrix Software (1992)"
description: "Output astrológico publicado com marca Matrix Software, como controle histórico de formato não atribuível ao DR-70."
timestamp: 2026-11-21T21:39:00-04:00
estado: provisorio
---

# Hewitt / Matrix Software: controle documental não DR-70

**ID:** `CTRL-HEWITT-MATRIX-F5` · **Família:** `HEWITT-MATRIX-BOOK-F5-1992` · **Rota:** O0/O1, comparador para [Digicomp #130](https://github.com/franklinbaldo/digicomp/issues/130), sem ingresso no corpus golden.

## Fonte e localizador

- William W. Hewitt, *Astrology for Beginners: An Easy Guide to Understanding and Interpreting Your Chart*. [Primeira edição bibliografada: Llewellyn, 1992, ISBN 0875423078](https://openlibrary.org/books/OL1556004M/Astrology_for_beginners).
- [PDF universitário consultado](https://ndl.ethernet.edu.et/bitstream/123456789/38630/1/21.pdf.pdf), capítulo *The Modern Way—By Computer*, **figura 5, página impressa 114**; a figura 6 vem a seguir. A folha PDF exata **não foi estabelecida**.
- Texto extraído/indexado confrontado com [outra transcrição textual](https://pdfcoffee.com/astrology-for-beginners-an-easy-guide-to-understanding-amp-interpreting-your-chart-hewitt-4-pdf-free.html) da mesma obra. A tentativa de screenshot da folha PDF retornou timeout. **PIXELS_NOT_CHECKED; bytes/SHA-256 NOT_OBTAINED**. Textos de um livro repetidos em dois sites não são sessões independentes.
- A figura traz, segundo a camada textual, `COPYRIGHT (C) 1982` e `MATRIX SOFTWARE`. **1982 é uma marca impressa no exemplo, não a data comprovada da sessão**, nem a data do livro (1992).

## Dados curtos de output publicados, ainda candidatos de OCR

| Região | Fragmento da camada textual | Grau |
| --- | --- | --- |
| Cabeçalho | `CHART DATA-SCOPE FOR HEWITT,WILLIAM` | TEXT_LAYER_ONLY |
| Colunas | `ASPECT ANALYSIS`, `HOUSES`, `PLANETS PER HOUSE` | TEXT_LAYER_ONLY |
| Casas 01/07 | `01=27LE33` / `07=27AQ33` | TEXT_LAYER_ONLY; revisar pixels |
| Casas 02/08 | `02=25VI24` / `08=25PI24` | TEXT_LAYER_ONLY; revisar pixels |
| Rodapé | `COPYRIGHT (C) 1982` / `MATRIX SOFTWARE` | TEXT_LAYER_ONLY |

São **tokens de uma saída publicada com atribuição editorial Matrix**, não bytes de impressão instrumental aferida. A camada textual é falível para números/glifos; não se devem converter esses valores em longitudes, estimar erros ou completar os outros oito campos sem imagem. Os dois lados de um par de casas são da **mesma tabela**, não amostras independentes.

## Hipóteses, falsificação e destino

O exemplo oferece um **controle rival de formatação**: saída de software de outro fornecedor pode conter casas, aspectos, símbolos e tabelas. **Isso não prova que Carlson tenha usado Matrix**, nem que a figura de Carlson seja impressão direta de DR-70. Sem exemplar, estado de execução, firmware e entrada completa, não há par input→output reexecutável.

Classificação `PUBLISHED_NON_DR70_FORMAT_CONTROL`, `NOT_DR70`, `NOT_INSTRUMENT_CERTIFIED`, `INPUT_INCOMPLETE`, `HOLDOUT_NOT_ELIGIBLE`, `GOLDEN_NOT_ELIGIBLE`. Preservar em controle documental, **fora de** `data/fidelity/observations.json`.

**Próximo passo:** imagem integral da figura 5, número da folha PDF, leitura visual dupla dos doze campos e da marca editorial; só então propor comparação lexical de formatos com Carlson. Nenhum valor de Hewitt deve calibrar o suposto firmware DR-70. Sem ROM original ou novo golden; sem aquisição, contato externo ou operação produtiva.
