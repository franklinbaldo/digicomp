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

**Cadeia de leitura (atualizada em 22/11/2026):** após a extração inicial via texto indexado, conferi diretamente a **imagem renderizada da página impressa 12 (índice PDF 11)**. ASC, MC, Sol, Lua, Mercúrio, Vênus, Marte, Júpiter, Saturno, UT, coordenadas, Whole Signs e data da carta são legíveis e concordam com o JSON. A 🦎 Lagarto registrou uma **segunda conferência visual** de 9/9 campos na [PR #148](https://github.com/franklinbaldo/digicomp/pull/148#issuecomment-7075573819); ambas consultam **a mesma publicação**, não dois documentos independentes. A tentativa de baixar os bytes do PDF falhou no executor, por isso o **SHA-256 do arquivo original continua NOT_OBTAINED**. A imagem de 2023 não autentica a edição de 1980.

## Observação documental

A carta moderna contém data 01/10/1924, UT 13:00, latitude 32N02, longitude 84W24 e **casas Whole Signs**. Os sete planetas de Sol a Saturno e os ângulos ASC/MC são apresentados em notação signo–graus–minutos–segundos. Os nove valores literais foram congelados em [dataset](../data/modern-controls/carter-astro-dienst-2023.json). As entradas coincidem textualmente com o **candidato não validado** [RAEL1980-CARTER](../data/chart-input-candidates/rael-rudhyar-1980.json); isso não certifica a leitura do exemplar impresso de 1980 nem a convenção do DR-70.

## Hipóteses e contraprovas

**A:** normalizar UT/longitude e converter signo+grau para longitude tropical absoluta produz valores modernos compatíveis com os nove campos publicados, tolerância operacional pré-declarada de **±1 segundo de arco**. **B:** erros de fuso, sinal de longitude, signo zodiacal ou conversão 0–30 para 0–360 produzem discrepâncias significativas. O teste executa a referência com `swisseph` instalado opcionalmente, compara os **nove** campos por diferença circular e introduz negativos de hora alterada, signo trocado e coordenadas DMS inválidas.

**Restrição geométrica:** as cúspides de casas **não são comparáveis**, pois a fonte de 2023 usa Whole Signs e o laboratório calcula Campanus. Os ângulos ASC/MC e planetas são comparáveis entre sistemas de casas nas condições declaradas.

**Restrição de independência:** AstroDienst e nosso binding podem usar o **mesmo núcleo Swiss Ephemeris**. Logo não se trata de uma verificação por algoritmo independente, mas de cruzamento de **uma publicação externa de 2023 com o adaptador moderno**. Concordância não autentica o motor, ROM, teclado, formatação, casas ou efemérides históricas do DR-70.

## Controle auxiliar de tempo sideral (p. 12)

Na página **12 impressa** do PDF de Naomi Rabinowitz (a página de índice 11 do arquivo), o quadro da carta AstroDienst de 19/02/2023 mostra literalmente **“Sid. Time: 8:02:19”**. É um décimo campo auxiliar de relógio, **separado** dos nove valores angulares, que permite testar a interpretação da hora UTC e do sinal da longitude. A leitura da página renderizada foi feita em 22/11/2026; os bytes do PDF não foram recuperados, e seu SHA-256 permanece **NOT_OBTAINED**. [Fonte com localizador p. 12](https://static1.squarespace.com/static/625588022bac29595ab0c386/t/652c6205bd50527fa4e8778a/1697407494104/Jimmy%2BCarter%2Band%2Bthe%2BKnight%2Bof%2BPentacles_final.pdf#page=12).

A verificação exploratória na sandbox, com `swisseph` 2.10.03, usa `(sidtime(JD_UT) + longitude_leste/15) mod 24`: para 01/10/1924 13:00 UT e 84°24′ W obtive **08:02:19,456**, diferença **+0,456 s** diante do valor publicado, dentro de tolerância predefinida de ±1 s. Contraprovas: inverter o sinal da longitude produz **19:17:31,456**; aumentar UT em uma hora produz **09:02:29,313**. A suíte verifica o relógio e essas duas mutações usando os dados normalizados pela mesma referência moderna, com teste independente dos nove ângulos.

Este cruzamento não prova independência de motor, pois AstroDienst e o binding podem utilizar Swiss Ephemeris, nem certifica as convenções de entrada do DR-70, uma carta da edição de 1980 ou qualquer saída instrumental.

## Controle histórico qualitativo já testável: septil Lua–Mercúrio

A transcrição textual secundária de *Astrological Aspects* (Raël/Rudhyar, obra catalogada em 1980) descreve na discussão de septis a **Lua de Carter na primeira casa** e um **septil entre Mercúrio e Lua**; a mesma transcrição atribui o recálculo dos mapas do Apêndice I ao DR-70. [Passagem textual](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf) (linhas indexadas 3011–3015; sem página impressa ou imagem verificadas). A qualificação «septil» **não é um número instrumental publicado** e o livro não fornece nessa passagem uma tolerância angular para o termo.

Como controle moderno de coerência, os **dois campos do próprio fac-símile AstroDienst de 2023** resultam em Mercúrio **171°11′20″** (Virgem 21°11′20″) e Lua **223°47′47″** (Escorpião 13°47′47″); separação orientada Lua menos Mercúrio **52°36′27″**. O septil matemático exato vale **360°/7 = 51°25′42,857″**; o desvio para esse ideal é **+1°10′44,143″**, usando os DMS publicados em 2023. Um cálculo Swiss/Moshier moderno no mesmo instante obtém separação aproximada **52,607450°**, corroborando a aritmética moderna sem independência de motor.

**Interpretação permitida:** a descrição histórica é *compatível em sentido astrológico aproximado* com as longitudes modernas, mas, **sem orb definido pelo autor, ela não estabelece teste histórico PASS/FAIL nem resíduo de DR-70**. A comparação se refere à mesma família editorial Raël/Rudhyar e a uma fonte moderna com possível motor compartilhado. Não acrescentar essa relação a `data/fidelity/observations.json`, não contar como mais uma sessão nem inventar graus a partir da ilustração do livro.

## Limite numérico executável da alegação qualitativa (R159)

O módulo de **biblioteca padrão**, `python -S -B -m scripts.carter_qualitative_relation`, transforma apenas os **DMS publicados no mapa moderno de 2023** em uma medida exata de sensibilidade para a **alegação textual histórica** de septil Lua–Mercúrio. Ele **não** calcula nem inventa os graus do mapa impresso em 1980. O texto de época está atualmente disponível por **transcrição secundária**, não por cotejo visual da página da edição de 1980.

- Separação menor Lua–Mercúrio do controle moderno: `189387″` = `52°36′27″`.
- Um septil exato: `1296000/7″` = `51°25′42,857142…″`.
- **Orb mínimo condicional para abranger esse par moderno:** `29709/7″` = `1°10′44,142857…″`, sem arredondar os componentes DMS de entrada.

O relatório JSON mantém `orb_declared_by_historical_text: null`, `historical_relation_test: INDETERMINATE_ORB_NOT_SPECIFIED`, `historical_chart_residual: NOT_RUN_NO_INSPECTED_1980_NUMBERS` e `dr70_fidelity: NOT_RUN_NO_GOLDEN`. Se a convenção histórica exigisse orb de até `0°30′`, esse par **moderno** ficaria fora; com `2°`, entraria. **Nenhuma dessas tolerâncias foi atribuída aos autores**. São cenários contrafactuais que mostram qual documento faltaria para decidir a afirmação histórica. O limite numérico **não** comprova o que o DR-70 calculou, a precisão de seu firmware nem qual carta foi impressa.

O teste `tests/test_carter_qualitative_relation.py` fixa a fração racional exata, rejeita DMS/literais adulterados, verifica uma mutação de +1 segundo de arco e impede promover metadados do controle a `DR70_NATIVE_GOLDEN` ou `PASS`. Ele roda **antes da instalação opcional do Swiss** no workflow `chart-reference.yml`, sob `python -S`, e devolve uma saída inconclusiva por definição. O documento histórico com graus angulares ainda precisa ser inspecionado independentemente; esse teste não aumenta o total de saídas instrumentais.

## Resultado inicial e limites

Na sandbox (biblioteca `swisseph` **2.10.03**), nove diferenças calculadas em segundos de arco: ASC +0,013; MC -0,499; Sol +0,418; Lua +0,274; Mercúrio +0,453; Vênus +0,132; Marte +0,594; Júpiter -0,431; Saturno -0,184. **9/9 dentro de ±1″**, sempre com o rótulo `MODERN_CHART_CONTROL_NOT_DR70_OUTPUT`. A verificação da suite completa e da árvore de PR por CI precisa ser relatada **no HEAD exato**.

**Estado científico não alterado:** nenhuma medida da carta da edição de 1980 foi conferida; zero resíduos históricos, zero golden instrumental, zero ROM original e zero holdout instrumental. O único próximo avanço de fidelidade é transcrever valores efetivamente legíveis da carta histórica ou recuperar saída direta do aparelho, mantendo as fontes separadas.
