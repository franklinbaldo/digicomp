---
type: Documento
title: "Campanus: laboratório numérico moderno para mapas publicados"
description: "Contrato de experimentos de referência, bibliotecas transitórias e limites de inferência sobre o DR-70."
timestamp: 2026-11-21T00:00:00-04:00
estado: provisorio
---

# Campanus: comparação, não emulação

O livro *Astrological Aspects: A Process-Oriented Approach* atribui, segundo transcrições secundárias, o recálculo de seus mapas com casas Campanus a um computador DR-70. Também indica colaboração de Nicki Michaels e desenho editorial por terceiro. A edição física de 1980 e os valores impressos nas figuras **ainda não foram conferidos**. Referência de pesquisa: [dossiê](rudhyar-1980-dr70-campanus.md).

## Primeiro experimento reproduzível

Os três registros de [entradas candidatas](../data/chart-input-candidates/rael-rudhyar-1980.json) são dados *transcritos de uma fonte*, não teclas observadas. Jimmy Carter é o caso inicial. O parser mantém 13:00, 27:25 e 25:16 tal como encontrados. O cálculo normaliza essas horas segundo uma **hipótese explícita**, com rolagem de dia para valores acima de 23:59. A interpretação precisa de cotejo com a obra.

Na sandbox de pesquisa, de forma isolada:

1. Instalar, sob licença compatível com o ambiente experimental, um binding swisseph da Swiss Ephemeris (workflow de CI usa pyswisseph==2.10.3.2).
2. Executar: python -m scripts.compute_chart_reference --id RAEL1980-CARTER.
3. Guardar o JSON emitido sob a classe MODERN_REFERENCE_NOT_DR70, com versão da biblioteca, flag Moshier para os planetas, sistema Campanus C, longitudes leste-positivas, graus tropicais e instante UT interpretado.

O adaptador produz as 12 cúspides Campanus, ASC/MC e longitudes do Sol a Saturno. É um programa **moderno**, não uma reconstrução de firmware. Valores numéricos gerados por ele não entram no arquivo de observações instrumentais e não são casos golden. O resultado tem os estados NOT_RUN_NO_TRANSCRIBED_VALUES e NOT_RUN_NO_GOLDEN.

## Direitos e independência técnica

A Swiss Ephemeris adota **AGPL ou licença profissional**, diferente da licença MIT dos arquivos próprios do Digicomp. Não vendorizamos código ou dados da biblioteca no repositório. O adaptador é opcional e experimental; qualquer incorporação ou distribuição futura exige avaliação das obrigações da licença. Fontes: [termos oficiais da Swiss Ephemeris](https://www.astro.com/swisseph/swisseph.htm), [binding Python](https://pypi.org/project/pyswisseph/). O pacote Python é uma ferramenta de referência substituível, **não** a arquitetura permanente do projeto.

## Próxima prova

Conferir fac-símile autorizado e transcrever manualmente, com páginas, graus e legibilidade, ao menos um mapa publicado. Somente depois realizar uma comparação numérica marcada como **comparação com publicação editorial**, não teste de fidelidade instrumental. Para validarmos o DR-70, será preciso uma sessão original vinculando dispositivo, entrada, operação e saída; o [protocolo REA](rea-output-first.md) e [corpus](fidelity-corpus.md) preservam essa distinção.
