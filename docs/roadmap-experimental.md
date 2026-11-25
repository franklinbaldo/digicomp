---
type: Documento
title: Roadmap Experimental
description: Objetivos científicos, referências, experimentos e critérios de validação do Digicomp DR-70.
timestamp: 2026-11-25T08:00:00-04:00
estado: provisorio
---

# Roadmap Experimental

O Digicomp investiga como o DR-70 calculava e apresentava seus resultados. O primeiro marco é gerar, com um comando, um relatório que compare o mapa publicado de Jimmy Carter com um cálculo moderno. Em paralelo, a pesquisa histórica procura uma sessão do aparelho que vincule entrada, operação e saída, além de manuais, código e ROMs. Começar pelos documentos já disponíveis e usar bibliotecas modernas como referências provisórias. [Direção do projeto na issue #130](https://github.com/franklinbaldo/digicomp/issues/130)

## Objetivos científicos

1. **Medir a concordância com documentos de época.** Reproduzir as condições publicadas, medir resíduos em posições e ângulos e testar quanto fuso, escala de tempo, coordenadas, sistema de casas e arredondamento explicam os desvios.

2. **Identificar o comportamento do aparelho.** Recuperar instruções e saídas literais. Formular hipóteses com previsões distintas e medir a fidelidade nos modos e campos efetivamente observados.

3. **Recuperar o software original.** Rastrear desenvolvedores, versões e descendentes. Se aparecer uma ROM ou listagem, documentar exemplar, cadeia de custódia, hash e direitos antes de comparar sua execução com as observações. Manter o cálculo e o comparador separados da interface para permitir trocar os motores de referência. [Repositório Digicomp](../README.md)

## Resultados confirmados e trabalho pendente

| Estado | Evidência ou tarefa |
| --- | --- |
| **Confirmado documentalmente** | Tim Smith descreveu o DR-70 em *Matrix Magazine* em 1978. O Calcuseum fotografa o exemplar L606 e um impresso de instruções. *Astrological Aspects* atribui ao DR-70 o recálculo dos mapas em Campanus. A cópia Mindfire traz 20 mapas. [Smith](tim-smith-matrix-1978.md) · [L606](https://www.calcuseum.com/scrapbook/BONUS/10925/1.htm) · [PR #158](https://github.com/franklinbaldo/digicomp/pull/158) |
| **Resultado documental integrado** | Na #159, ASC, MC e cúspide 11 ficaram todos dentro de 60″ em **12 de 16** mapas, usando as entradas das figuras. Na grade de ±180 s da #160, Shaw e Case admitem deslocamentos de hora compatíveis com os três ângulos. Roosevelt permanece discrepante nessa grade. As leituras visuais ainda pedem revisão independente. [PR #159](https://github.com/franklinbaldo/digicomp/pull/159) · [PR #160](https://github.com/franklinbaldo/digicomp/pull/160) |
| **Resultado moderno em rascunho** | O controle de Carter da #148 obteve **9 de 9** campos comparáveis dentro de ±1″, contando sete posições planetárias, ASC e MC. A fonte moderna usa Whole Signs. Os dois lados podem compartilhar o motor Swiss Ephemeris. A #148 e sua base #103 estão abertas em rascunho. [PR #148](https://github.com/franklinbaldo/digicomp/pull/148) · [PR #103](https://github.com/franklinbaldo/digicomp/pull/103) |
| **Hipóteses** | Parte dos resíduos pode vir de entradas diferentes das legendas, conversão de horário ou arredondamento editorial. O cabeçalho KOCH de Carlson oferece um teste de formato. A autoria instrumental da figura e a regra usada pelo aparelho continuam em aberto. [Análise de horário](https://github.com/franklinbaldo/digicomp/pull/160) · [Exemplares e interface](exemplares-interface.md) |
| **Pendente de evidência instrumental** | Em 25/11/2026, o corpus na `main` tem **zero registros** e o projeto registra **zero ROMs ou códigos originais autenticados**. Recuperar uma sessão reexecutável e estabelecer a procedência do software são entregas independentes da comparação editorial. [Corpus na main](../data/fidelity/observations.json) · [Estado da pesquisa](../README.md#estado-da-pesquisa-2026-11-21) |

## Livros e fontes de época

| Prioridade | Referência e uso |
| --- | --- |
| **Imediata** | Leyla Raël e Dane Rudhyar, *Astrological Aspects: A Process-Oriented Approach* (1980). Revisar o apêndice I, folhas 133–152 da cópia Mindfire, com atenção à declaração de recálculo e ao mapa de Carter na folha 145. [Inventário e transcrição](https://github.com/franklinbaldo/digicomp/pull/158) |
| **Alta** | Michael Erlewine, *Manual of Computer Programming for Astrologers* (1980) e errata de 1982. Procurar fórmulas, exemplos completos e convenções de época. O programa natal em BASIC de Erlewine, publicado em *Matrix Magazine* VII (1980), oferece um comparador histórico. [Open Library](https://openlibrary.org/works/OL6373938W/Manual_of_Computer_Programming_for_Astrologers) · [Acervo Illinois](https://archon.library.illinois.edu/archives/?id=13321&p=collections%2Ffindingaid&q=&rootcontentid=238976) · [Índice de Matrix](https://alexandriaibase.org/celestial-bodies/neptune/) |
| **Alta** | Richard Nolle, “The Astrologer’s Computer”, *Today’s Astrologer* XLV/10 (out. 1983), p. 9, e o fascículo XLV/9 (set. 1983), p. 14. Buscar tabelas, parâmetros e identificação do aparelho no possível confronto com ACS. Cruzar com Smith, o impresso do L606 e o fac-símile de “Computers and Astrology”, de Mark Pottenger (1979). [Índice AFA](https://astrologers.com/wp-content/uploads/2025/07/Index-by-Title-41-50.pdf) · [Pottenger](https://ccrsdodona.org/m_dilemma/1979/vir/computer.html) |
| **Controle de época e de cálculo** | Digicomp Research Corporation, *True Lunar Nodes 1850–2000* (1975), e Neil F. Michelsen, *The American Ephemeris 1931 to 1980 & Book of Tables* (1976), para comparar tabelas, definições e precisão. Jean Meeus, *Astronomical Algorithms*, 2ª ed. (1998), para verificar conversões de tempo e coordenadas com exemplos numéricos. [Astrolearn](https://www.astrolearn.com/astrology-bibliography/bibliography-of-astrology-page-43-daivagna-daton/) · [Michelsen no U.S. Naval Observatory](https://1535.sydneyplus.com/genieplus/final/ViewRecord.aspx?record=376a59c7-0af7-46b6-acb0-5557c5dd0ab8&template=Books) · [Meeus no U.S. Naval Observatory](https://1535.sydneyplus.com/genieplus/final/ViewRecord.aspx?record=9ff397d1-1fba-479f-85ab-8a51de0ca72c&template=Books) |

Na busca de saídas literais, examinar a figura de Carlson, o acervo Joan Quigley e o vídeo listado abaixo. Registrar página ou minuto, edição, cadeia de reprodução e quais campos aparecem legíveis. Em vídeo, procurar continuidade entre a digitação e o display ou papel. [Carlson, *Nature* (1985)](https://doi.org/10.1038/318419a0) · [Guia do acervo Hoover](https://oac.cdlib.org/findaid/ark:/13030/c8kp86wv) · [Vídeo indicado na pesquisa](https://youtu.be/9WE-03yEPGU)

## Bibliotecas candidatas

| Candidata | Papel e decisão proposta |
| --- | --- |
| **Python · `pyswisseph`** | Primeira referência para Campanus, ASC, MC e longitudes. Reusar #103 e #148 com `pyswisseph==2.10.3.2`, flags retornadas e arquivos efetivos registrados. Uso experimental isolado. A licença do motor é AGPL ou profissional. [PR #103](https://github.com/franklinbaldo/digicomp/pull/103) · [Documentação Astrodienst](https://www.astro.com/swisseph-download/doc/swisseph.pdf) |
| **Python · Skyfield e PyEphem** | Priorizar Skyfield para um controle de Sol e Lua, com versão e kernel fixos. Confrontar com JPL Horizons sob o mesmo referencial e registrar eventual genealogia comum das efemérides. PyEphem é candidato a um segundo ensaio de posições, sujeito à conferência das convenções. [Skyfield](https://pypi.org/project/skyfield/) · [PyEphem](https://pypi.org/project/ephem/) · [Horizons](https://ssd.jpl.nasa.gov/horizons/manual.html) |
| **Rust · Astronomy Engine e binding Swiss Ephemeris** | Estender o verificador integrado na #98 para comparar o JSON do experimento. Avaliar o port de Astronomy Engine em longitudes e um binding Swiss para paridade com o mesmo motor. Medir cobertura de Campanus e Koch, maturidade, dependências nativas e reprodução do build. Verificar a licença do crate, do motor e dos dados antes de incorporar qualquer dependência ao núcleo. [PR #98](https://github.com/franklinbaldo/digicomp/pull/98) · [Port candidato](https://github.com/lmxp2001/Astronomy-Engine-Rust-port) |

## Experimentos prioritários e sequência de PRs

| PR proposta | Dependência | Entrega e aceite |
| --- | --- | --- |
| **1 · Carter executável** | #158–#160 integradas. Reusar as partes pertinentes de #103 e #148. | Um comando gera JSON versionado para **1 out. 1924, 13:00 U.T., 32°02′ N, 84°24′ W**, em Campanus tropical. Registrar a entrada literal, a interpretação de U.T. e os resíduos de ASC, MC e cúspide 11. Reproduzir também os nove campos do controle moderno compatível. |
| **2 · Bibliografia e transcrição** | Em paralelo com a PR 1. | Dois leitores transcrevem Carter de forma independente. Registrar desacordos e sua resolução com localizador. Inventariar Nolle, Erlewine, Smith, o cartão L606 e as passagens úteis dos vídeos. |
| **3 · Comparação em Rust** | Contrato JSON da PR 1. | Reusar a #98 e obter os mesmos resíduos e estados de comparabilidade com o mesmo JSON. Cobrir passagem por 0°/360°, limite de tolerância, unidade inválida e dados ausentes. |
| **4 · Controle de efemérides e hipóteses** | PR 1 e famílias de fonte revisadas na PR 2. | Comparar Sol e Lua com Skyfield/Horizons. Testar separadamente hora, coordenadas, sistema de casas e quantização. Fixar hipóteses antes de avaliar uma família documental reservada. Tratar os mapas de Raël e Rudhyar como uma só família. Sem família elegível, relatar apenas o ensaio exploratório. |
| **5 · Primeira sessão instrumental** | Fonte com sessão reexecutável e comparador da PR 1 ou 3. | Registrar exemplar ou variante observável, sequência de teclas, entrada, modo e saída literal com revisão independente. Publicar resultados por campo e a cobertura do modo observado. Conservar capturas incompletas como evidência parcial conforme o contrato do corpus. |

## Critérios de validação

- **Proveniência.** Guardar edição, página ou quadro, URL, hash quando houver artefato disponível, transcrição literal e família documental. Preservar dúvidas de leitura e distinguir valores observados de normalizações. [Contrato do corpus](fidelity-corpus.md)

- **Comparabilidade.** Alinhar instante, escala de tempo, referencial, longitude geográfica, zodíaco, sistema de casas e convenções de saída antes de calcular resíduos. Usar distância angular circular em segundos de arco. Marcar campos sem informação suficiente como incomparáveis e registrar o motivo.

- **Aceite numérico.** Fixar os limites antes de rodar. Usar ±1″ para os nove campos do controle moderno e 60″ como faixa exploratória do ensaio editorial da #159. Na validação instrumental, derivar a tolerância da resolução observada e da regra de exibição em teste. Publicar campos comparáveis, total esperado, resíduos e divergências.

- **Reprodução e generalização.** Rodar no SHA da PR com versões e parâmetros explícitos, `prek`, OKF e testes do escopo. Cobrir hora deliberadamente errada, inversão de longitude, virada de dia e rejeição de saída sintética como observação. Reservar famílias independentes para avaliar regras ajustadas. Se duas regras permanecerem compatíveis com os dados, especificar uma entrada em que suas previsões divirjam. [Protocolo de evidência](rea-output-first.md)
