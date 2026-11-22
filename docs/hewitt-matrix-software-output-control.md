---
type: Documento
title: "Controle documental: Hewitt/Matrix Software, cópia da nona impressão (1999)"
description: "Output astrológico publicado com marca Matrix Software, como controle histórico de formato não atribuível ao DR-70."
timestamp: 2026-11-21T21:39:00-04:00
estado: provisorio
---

# Hewitt / Matrix Software: controle documental não DR-70

**ID:** `CTRL-HEWITT-MATRIX-F5` · **Família legada de referência bibliográfica:** `HEWITT-MATRIX-BOOK-F5-1992` · **Rota:** O0/O1, comparador para [Digicomp #130](https://github.com/franklinbaldo/digicomp/issues/130), sem ingresso no corpus golden.

## Fonte e localizador

- William W. Hewitt, *Astrology for Beginners: An Easy Guide to Understanding and Interpreting Your Chart*. O registro [Open Library, edição bibliografada 1992, ISBN 0875423078](https://openlibrary.org/books/OL1556004M/Astrology_for_beginners) é um **registro bibliográfico**, não identificação física da cópia PDF examinada.
- **Correção de custódia da variante consultada (R143):** a [camada textual do PDF universitário](https://ndl.ethernet.edu.et/bitstream/123456789/38630/1/21.pdf.pdf) traz **capa/rosto com 1999**, **copyright © 1991** e **`FIRST EDITION / Ninth printing, 1999`** no verso editorial. O código CIP **`BF1708.1.H48 1992`** é classificação/catalogação, **não** a data de impressão desta cópia. Portanto, a figura 5 foi lida em uma **reimpressão indicada como nona, de 1999**, sem cotejo com exemplar da tiragem inicial. O sufixo `-1992` do ID de família é legado de catalogação, **não proveniência comprovada da figura à tiragem de 1992**.
- [PDF universitário consultado](https://ndl.ethernet.edu.et/bitstream/123456789/38630/1/21.pdf.pdf), capítulo *The Modern Way—By Computer*, **figura 5, página impressa 114**; a figura 6 vem a seguir. A folha PDF exata **não foi estabelecida**.
- Texto extraído/indexado confrontado com [outra transcrição textual](https://pdfcoffee.com/astrology-for-beginners-an-easy-guide-to-understanding-amp-interpreting-your-chart-hewitt-4-pdf-free.html) da mesma obra. A tentativa de screenshot da folha PDF retornou timeout. **PIXELS_NOT_CHECKED; bytes/SHA-256 NOT_OBTAINED**. Textos de um livro repetidos em dois sites não são sessões independentes.
- A figura traz, segundo a camada textual, `COPYRIGHT (C) 1982` e `MATRIX SOFTWARE`. **1982 é uma marca do exemplo, não uma data comprovada de geração dos bytes, nem a data de impressão da cópia consultada (1999).**
- **Corroboração textual independente da legenda, mas no mesmo livro:** em *References*, p. **impressa 277**, item **6, Computer programs for astrology**, Hewitt recomenda Matrix Software, fornece endereço de Big Rapids e declara usar os programas da empresa há anos, com frequência. Isso dá apoio adicional à atribuição **editorial Matrix** deste controle, sem provar qual hardware, release ou impressora gerou a figura. É **a mesma obra/autoria**, não segunda testemunha independente; leitura apenas da camada textual (imagem e hash não conferidos).

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

O exemplo, nesta cópia identificada como **nona impressão de 1999** (primeira edição declarada, copyright 1991, catalogação 1992), oferece um **controle rival de formatação**: saída de software de outro fornecedor pode conter casas, aspectos, símbolos e tabelas. **Isso não prova que Carlson tenha usado Matrix**, nem que a figura de Carlson seja impressão direta de DR-70. Sem exemplar, estado de execução, firmware e entrada completa, não há par input→output reexecutável.

Classificação `PUBLISHED_NON_DR70_FORMAT_CONTROL`, `NOT_DR70`, `NOT_INSTRUMENT_CERTIFIED`, `INPUT_INCOMPLETE`, `HOLDOUT_NOT_ELIGIBLE`, `GOLDEN_NOT_ELIGIBLE`. Preservar em controle documental, **fora de** `data/fidelity/observations.json`.

**Próximo passo:** obter bytes/SHA-256 da cópia de 1999, confirmar visualmente capa/verso, figura 5 e *References* p. 277, estabelecer folhas PDF e leitura visual dupla dos doze campos e marca editorial; cotejar separadamente uma cópia realmente datada de 1992 antes de afirmar identidade entre tiragens; só então propor comparação lexical de formatos com Carlson. Nenhum valor de Hewitt deve calibrar o suposto firmware DR-70. Sem ROM original ou novo golden; sem aquisição, contato externo ou operação produtiva.
