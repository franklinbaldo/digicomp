---
type: Documento
title: "Carter: quatro posições de casas na prosa editorial de Raël/Rudhyar"
description: "Contraprova qualitativa entre afirmações textuais de um livro atribuído ao DR-70 e cálculo Campanus moderno; sem transcrição de impressão ou fidelidade instrumental."
timestamp: 2026-11-21T09:22:00-04:00
estado: provisorio
---

# Posições de casas de Carter: um alvo numérico intermediário

## Uma saída publicada que não é uma impressão do computador

A transcrição eletrônica atribuída a **Leyla Raël e Dane Rudhyar, *Astrological Aspects: A Process-Oriented Approach*** contém, no capítulo sobre padrões triangulares, quatro afirmações **qualitativas** sobre a carta de **Jimmy Carter**:

| Corpo | Casa indicada na prosa da publicação |
| --- | --- |
| Lua | Primeira |
| Urano | Quinta |
| Plutão | Nona |
| Mercúrio | Décima primeira |

As três primeiras aparecem juntas na discussão do grande trígono de Carter; Mercúrio é descrito na casa 11 em uma passagem sobre os septis de Carter. Não se trata dos números legíveis da figura do Apêndice I, nem de emissão direta do aparelho.

**Localização textual:** [transcrição em PDF, discussão do grande trígono](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf), linhas de texto indexadas 4743–4750 da leitura feita em 21/11/2026; [Mercúrio e Lua](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf), linhas 3011–3015. O índice do Apêndice I, linhas 5237–5249, atribui o recálculo de mapas Campanus a um DR-70 e dá para Carter 01/10/1924, 13:00 UT, 32N02, 84W24. **Esses índices de linha são do texto extraído, não páginas originais; não substituem uma página impressa autenticada.**

**Limite documental:** a versão acessível permitiu leitura do texto indexado, mas o serviço de visualização devolveu erro de redirecionamento ao tentar abrir a página do PDF como imagem; **nenhum fac-símile foi verificado visualmente**, a edição dos gráficos permanece ambígua, e nenhuma página foi conferida. As quatro afirmações pertencem à **mesma fonte editorial**, não representam quatro execuções independentes de DR-70. A presença do nome do equipamento no texto não demonstra que os valores foram efetivamente produzidos por sua ROM ou exibidos no papel.

## Experimento moderno: modelo e resultados

Este experimento é uma reprodução numérica com **Swiss Ephemeris 2.10.03, Moshier para planetas**, calculado em sandbox em 21/11/2026. Não é reconstrução do firmware. Dados de entrada são a transcrição acima e seguem não conferidos com a edição física. Convenções declaradas: UTC presumido 1924-10-01 13:00, longitude geográfica leste-positiva (-84°24'), latitude norte (+32°02'), zodíaco tropical, casas Campanus ("C"), Julian Day UT 2424060.0416666665.

Para cada corpo: obter longitude e latitude eclípticas em `calc_ut(JD, planet, FLG_MOSEPH)`; obter ARMC em `houses_ex(JD, latitude, longitude, b"C")`, obliquidade verdadeira em `calc_ut(JD, ECL_NUT)[0][0]`, e posição de casa fracionária com `house_pos(ARMC, latitude, obliquidade, (longitude_ecl, latitude_ecl, distância), b"C")`. O inteiro de cada posição fracionária corresponde à casa da saída moderna para este caso. Não substituir latitude eclíptica real do planeta por zero: isso pode mudar a classe perto de cúspides.

| Corpo | Longitude eclíptica moderna | Casa fracionária moderna | Casa textual |
| --- | --- | --- | --- |
| Lua | 223,796465° | 1,542054 | 1 |
| Urano | 348,790214° | 5,724119 | 5 |
| Plutão | 103,525354° | 9,489261 | 9 |
| Mercúrio | 171,189015° | 11,805797 | 11 |

**Resultado:** os quatro enunciados qualitativos na transcrição são compatíveis com um cálculo Campanus moderno **nas premissas citadas**. É um controle de plausibilidade de entrada/convenções/modelo, **não** um ajuste calibrado ao DR-70, nem quatro validações independentes, nem uma medida de erro angular. Posições fracionárias distintas de cúspides não revelam a precisão da máquina histórica.

## Hipóteses e próxima prova

- **H1:** o desenho editorial utiliza dados que foram recalculados/conferidos num DR-70; o texto preservou ao menos a classificação de casas.
- **H2:** o livro representa um mapa calculado ou corrigido fora do DR-70, apenas posteriormente conferido pela operadora; as mesmas classes de casas seriam esperadas.
- **H3:** a transcrição eletrônica altera contexto/edição e as classes não pertencem ao material original de 1980.

As três hipóteses sobrevivem a esse controle. O teste que as distingue começa por encontrar **fac-símile da edição de 1980**, conferir a passagem textual e o mapa manuscrito de Carter com seus números, fotografar ou anotar o localizador impresso e documentar o pipeline editorial. Mesmo a leitura numérica do livro seria **comparação com edição publicada**, não saída nativa certificada. Para um teste de fidelidade do DR-70 continuam necessários exemplar, sessão, sequência de teclas, canal e valores literais.

Manter `data/fidelity/observations.json` com zero golden, não transformar essas proposições em `development` ou `holdout` e não inserir novos registros redundantes na [triagem #94](https://github.com/franklinbaldo/digicomp/pull/94). A implementação opcional do comparador moderno está nas [PRs #103](https://github.com/franklinbaldo/digicomp/pull/103) e [#104](https://github.com/franklinbaldo/digicomp/pull/104), ainda DRAFT e com obrigações de licença externa em avaliação.
