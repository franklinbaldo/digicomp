---
type: Documento
title: "Comparação angular de 16 mapas de Raël e Rudhyar"
description: "Transcrição visual do ascendente, meio do céu e 11ª cúspide e comparação Campanus para as figuras com entradas declaradas."
timestamp: 2026-11-23T09:25:00-04:00
estado: provisorio
---

# Comparação angular de 16 mapas de Raël e Rudhyar

**DR70-CASE-RAEL-APPENDIX-ANGLES · DOCUMENTED.** Transcrevi o ascendente, o meio do céu e a 11ª cúspide dos 16 mapas do Apêndice I que informam data, hora e coordenadas na legenda. São **48 valores**, incluindo os três de Carter como controle de continuidade. A comparação da 11ª cúspide permite examinar a divisão das casas além dos dois ângulos principais. Cada valor foi fixado antes da consulta ao resultado moderno. [Dados das figuras](../data/documentary-observations/rael-rudhyar-angles.json) · [Custódia e índice das vinte figuras](rudhyar-carter-facsimile.md).

## Resultados com as entradas nas legendas

Diferenças em segundos de arco, calculadas como valor publicado menos referência moderna, no menor arco assinado. **12 de 16 mapas** têm os três resíduos dentro de ±60″, incluindo Carter. São 36 de 48 valores dentro de ±60″ e 27 dentro de ±30″. Esses limites descrevem a distribuição observada. A fonte histórica imprime minutos inteiros. [Resultado completo em JSON](../data/documentary-observations/rael-rudhyar-angular-comparison.json).

| Folha PDF | Mapa | Ascendente | Meio do céu | Cúspide 11 |
| ---: | --- | ---: | ---: | ---: |
| 133 | Alan Watts | +2855,38 | +3761,82 | +3155,28 |
| 134 | Albert Einstein | −47,06 | −23,51 | −18,98 |
| 135 | Albert Schweitzer | +48,75 | +28,50 | +25,47 |
| 136 | Andrew Carnegie | +53,73 | −1,64 | −9,27 |
| 138 | Franklin D. Roosevelt | +433,62 | +103,17 | +538,00 |
| 139 | George Bernard Shaw | +113,82 | +162,55 | +222,22 |
| 140 | George Sand | +51,62 | −17,24 | −0,49 |
| 141 | Henry Ford | +20,37 | −19,85 | −18,62 |
| 144 | Jerry Brown | −14,06 | −26,82 | −25,90 |
| 145 | Jimmy Carter | +21,99 | +7,50 | −32,88 |
| 146 | Krishnamurti | +18,39 | −2,91 | +24,71 |
| 147 | Mohandas Gandhi | +40,82 | +20,87 | +47,38 |
| 149 | Paul Case | +864,23 | +1014,17 | +979,83 |
| 150 | Ram Das | +9,72 | +17,97 | +3,51 |
| 151 | V. Nijinsky | +46,42 | +15,10 | +32,10 |
| 152 | Werner Erhard | −20,42 | −23,38 | +7,45 |

## Comparação das entradas concorrentes

| Mapa | Variante testada além da legenda | Ascendente | Meio do céu | Cúspide 11 |
| --- | --- | ---: | ---: | ---: |
| Alan Watts | Texto do apêndice, 6 de janeiro | −17,86 | −28,40 | −14,53 |
| Franklin D. Roosevelt | Texto do apêndice, 25:16 U.T. | −273,52 | −733,50 | −265,00 |
| Franklin D. Roosevelt | Controle, 01:15 U.T. no dia 30 | +3213,51 | +3395,74 | +3697,12 |
| Jerry Brown | Texto do apêndice, latitude 43N03 | −16063,10 | −26,82 | +5394,13 |
| Werner Erhard | Controle, 03:25 U.T. no dia 5 | +3807,54 | +3564,25 | +4413,08 |

- **Watts.** A figura diz 5 de janeiro. Com o dia 6, que consta no texto, os três resíduos caem de 47′–63′ a menos de 30″. Isso favorece o dia 6 como entrada associada aos ângulos desenhados. A data da legenda permanece registrada como 5. [Texto](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf#page=126) · [Figura](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf#page=133).
- **Brown.** Com a latitude 34N03 da figura, os três resíduos ficam abaixo de 30″. A latitude 43N03 do texto desloca a diferença do ascendente para cerca de 4°28′ e a da 11ª cúspide para cerca de 1°30′. O resíduo do meio do céu é o mesmo nas duas variantes. [Texto](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf#page=125) · [Figura](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf#page=144).
- **Erhard e Roosevelt.** Contar as horas a partir da meia-noite da data escrita leva Erhard às 03:25 do dia 6, compatível com os três ângulos dentro de 30″. Para Roosevelt, tanto 25:15 quanto 25:16 deixam diferenças acima de um minuto de arco em todos os campos. Máximo de cerca de 9′ com a primeira hora e 12′ com a segunda. [Erhard](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf#page=152) · [Roosevelt](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf#page=138).
- **Shaw e Case.** Os resíduos máximos são de 3′42″ e 16′54″, respectivamente. O primeiro confronto preserva as entradas das legendas, inclusive nos casos que divergem. [Shaw](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf#page=139) · [Case](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf#page=149).

## Reprodução e limites

O cálculo usou Swiss Ephemeris 2.10.03, com `pyswisseph==2.10.3.2`, calendário gregoriano, longitudes leste positivas, zodíaco tropical e `houses_ex` em Campanus. As horas acima de 24:00 foram passadas ao dia juliano como horas decorridas desde o início da data impressa. A execução verificou a igualdade entre as cúspides 1 e 10 e os ângulos correspondentes na referência moderna. O resultado completo tem SHA-256 `e4669a62acdccc495224ad894bc2e73b83f7d56aaeff9f0076b6db89689defb2`. [Rotina executada sobre as leituras fixadas](https://github.com/franklinbaldo/digicomp/blob/fe598a514ae7ebf1715c7a001c663397e8277062/.github/workflows/rael-rudhyar-research.yml) · [Execução pública](https://github.com/franklinbaldo/digicomp/actions/runs/45185697489) · [Manual da Swiss Ephemeris](https://www.astro.com/swisseph/swephprg.htm#_Toc112949182).

As figuras foram lidas uma vez por inspeção visual, a partir das imagens de 1800 pixels no lado maior renderizadas com Poppler 26.07.0. A revisão independente continua pendente. As quatro figuras designadas *Solar Chart* ficaram fora do cálculo porque suas legendas omitem a hora. Todos os mapas pertencem à mesma família editorial. As diferenças medem a concordância com os mapas diagramados e mantêm a fidelidade instrumental em `NOT_RUN_NO_GOLDEN`.
