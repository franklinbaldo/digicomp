---
type: Documento
title: "Carter: quatro atribuições de casas em prosa versus Campanus moderno"
description: "Contraste de quatro casas descritas em transcrição secundária com resultados modernos para UTC 13h e 12h, sem atribuição instrumental."
timestamp: 2026-11-22T13:00:00-04:00
estado: provisorio
---

# Carter: casas editoriais históricas versus dois horários modernos

**Pergunta:** quatro casas mencionadas em prosa de *Astrological Aspects*, atribuído a Leyla Raël e Dane Rudhyar, distinguem a entrada de 13:00 UT transcrita do apêndice e a alternativa contrafactual 12:00 UT?

**Fonte das alegações:** [transcrição web secundária](https://www.scribd.com/document/633437269/Dane-Rudhyar-Leyla-Rael-Astrological-Aspects-A-Process-Oriented-Approach-Rudhyar-Series-Aurora-Press-Inc-2018-pdf), linhas indexadas 3843–3849 e 6117–6121, consultada em 22/11/2026. O texto descreve Lua na casa 1, Mercúrio na 11, Plutão na 9 e Urano na 5. O apêndice traz Carter, 01/10/1924, 32N02, 84W24, 13:00 UT, e atribui recálculos Campanus a um DR-70. **Outra circulação textual da mesma obra:** [espelho PDF textual/Mindfire](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf), seções `PREFACE` e `APPENDIX ONE`; traz o mesmo elenco e os mesmos dados de Carter, sem constituir fonte independente ou fac-símile autenticado. O prefácio agradece a Nicki Michaels pelo cálculo no computador e a Tony Milner pela caligrafia; não há prova de que o computador de Michaels fosse distinto do DR-70 citado no apêndice. A renderização visual desse espelho falhou por redirecionamento de host. **Edição, página física e figura não inspecionadas.** São quatro alegações da mesma família editorial, não quatro testemunhos independentes.

**Método:** o script scripts/carter_historical_house_claims.py usa o adapter opcional Swiss Ephemeris 2.10.03/Moshier da #103. Calcula longitude e latitude eclíptica do corpo e chama house_pos com ARMC, latitude geográfica, obliquidade verdadeira e Campanus. A data, coordenadas e motor são mantidos; altera-se somente UT. As frações de casa abaixo são diagnósticos modernos, não medidas históricas impressas.

| Corpo | Casa textual histórica | Campanus moderno 13:00 UT | Campanus moderno 12:00 UT |
| --- | ---: | ---: | ---: |
| Lua | 1 | 1 (1,542054) | 1 (1,949325) |
| Mercúrio | 11 | 11 (11,805797) | 12 (12,254802) |
| Plutão | 9 | 9 (9,489261) | 9 (9,965509) |
| Urano | 5 | 5 (5,724119) | 6 (6,179593) |
| **Correspondências** | **4 alegações** | **4/4** | **2/4** |

**Resultado:** no modelo Campanus moderno, 13:00 UT reproduz as quatro categorias descritas no texto indexado. Às 12:00 UT, Mercúrio e Urano caem nas casas 12 e 6. Esta é uma restrição documental qualitativa, favorável à hipótese de entrada 13:00 UT **sob o motor e convenções escolhidos**; não é um teste de fidelidade instrumental.

**Limitações:** a transcrição secundária pode carregar erro ou atribuição editorial de diversos colaboradores. Não possuímos uma reprodução autenticada das cartas de 1980, cúspides, longitude histórica, tolerâncias da época, ROM, golden nativo nem resíduos angulares. Os quatro resultados vêm de uma única família editorial. Uma correspondência de casas não implica concordância de graus. A proximidade de Plutão à cúspide às 12:00 UT também recomenda não extrapolar a distinção. A carta moderna pode usar os mesmos algoritmos da referência.

**Reprodução:** com a dependência opcional de pesquisa pyswisseph==2.10.3.2 isolada, executar python -m scripts.carter_historical_house_claims e python -m unittest discover -s tests -p test_carter_historical_house_claims.py -v. O workflow chart-reference.yml executa os quatro testes e confere 4/4 contra 2/4, além da classificação não instrumental. Conferir os gates no SHA exato.

**Próxima evidência:** inspecionar uma figura de edição física e transcrever os valores numéricos nela impressos para comparar resíduos. O corpus reservado data/fidelity/observations.json não foi alterado.
