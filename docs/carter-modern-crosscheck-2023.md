---
type: Documento
title: "DR70-MODERN-CARTER-2023: cruzamento moderno de nove longitudes"
description: "Controle externo de leitura de signos, hora e coordenadas, sem confundir mapa moderno de 2023 com impressão histórica do DR-70."
timestamp: 2026-11-22T02:00:00-04:00
estado: provisorio
---

# DR70-MODERN-CARTER-2023: controle numérico moderno

**Pergunta:** a mesma entrada de Jimmy Carter, citada em transcrição secundária do apêndice de Rael/Rudhyar (1980), pode ser normalizada e calculada sem erro de signo, UTC ou longitude pelo adaptador moderno experimental da [PR #103](https://github.com/franklinbaldo/digicomp/pull/103)?

**Classe:** publicação moderna de outro serviço, **não saída instrumental do DR-70**. **Fonte:** Naomi Rabinowitz, *Jimmy Carter and the Knight of Pentacles Card* (2023), apêndice «Natal chart» que reproduz mapa AstroDienst datado **19/02/2023**. [PDF do editor](https://static1.squarespace.com/static/625588022bac29595ab0c386/t/652c6205bd50527fa4e8778a/1697407494104/Jimmy%2BCarter%2Band%2Bthe%2BKnight%2Bof%2BPentacles_final.pdf). O PDF está protegido por direitos autorais; armazenam-se apenas os nove campos mínimos, atribuição e link, não as páginas ou imagens.

**Cadeia de leitura:** os campos e a tabela foram inspecionados por camada de texto/descrição estruturada de PDF acessível na web. A captura de pixels do fac-símile retornou erro e os bytes originais não foram preservados localmente; SHA-256 do PDF **NOT_OBTAINED**. Portanto **não** atribuir dupla transcrição visual nem alegar documento original da década de 1980.

## Observação documental

A carta moderna contém data 01/10/1924, UT 13:00, latitude 32N02, longitude 84W24 e **casas Whole Signs**. Os sete planetas de Sol a Saturno e os ângulos ASC/MC são apresentados em notação signo–graus–minutos–segundos. Os nove valores literais foram congelados em [dataset](../data/modern-controls/carter-astro-dienst-2023.json). As entradas coincidem textualmente com o **candidato não validado** [RAEL1980-CARTER](../data/chart-input-candidates/rael-rudhyar-1980.json); isso não certifica a leitura do exemplar impresso de 1980 nem a convenção do DR-70.

## Hipóteses e contraprovas

**A:** normalizar UT/longitude e converter signo+grau para longitude tropical absoluta produz valores modernos compatíveis com os nove campos publicados, tolerância operacional pré-declarada de **±1 segundo de arco**. **B:** erros de fuso, sinal de longitude, signo zodiacal ou conversão 0–30 para 0–360 produzem discrepâncias significativas. O teste executa a referência com `swisseph` instalado opcionalmente, compara os **nove** campos por diferença circular e introduz negativos de hora alterada, signo trocado e coordenadas DMS inválidas.

**Restrição geométrica:** as cúspides de casas **não são comparáveis**, pois a fonte de 2023 usa Whole Signs e o laboratório calcula Campanus. Os ângulos ASC/MC e planetas são comparáveis entre sistemas de casas nas condições declaradas.

**Restrição de independência:** AstroDienst e nosso binding podem usar o **mesmo núcleo Swiss Ephemeris**. Logo não se trata de uma verificação por algoritmo independente, mas de cruzamento de **uma publicação externa de 2023 com o adaptador moderno**. Concordância não autentica o motor, ROM, teclado, formatação, casas ou efemérides históricas do DR-70.

## Resultado inicial e limites

Na sandbox (biblioteca `swisseph` **2.10.03**), nove diferenças calculadas em segundos de arco: ASC +0,013; MC -0,499; Sol +0,418; Lua +0,274; Mercúrio +0,453; Vênus +0,132; Marte +0,594; Júpiter -0,431; Saturno -0,184. **9/9 dentro de ±1″**, sempre com o rótulo `MODERN_CHART_CONTROL_NOT_DR70_OUTPUT`. A verificação da suite completa e da árvore de PR por CI precisa ser relatada **no HEAD exato**.

**Estado científico não alterado:** nenhuma medida da carta da edição de 1980 foi conferida; zero resíduos históricos, zero golden instrumental, zero ROM original e zero holdout instrumental. O único próximo avanço de fidelidade é transcrever valores efetivamente legíveis da carta histórica ou recuperar saída direta do aparelho, mantendo as fontes separadas.
