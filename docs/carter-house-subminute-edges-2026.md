---
type: Documento
title: "Carter: fronteiras subminuto da compatibilidade Campanus moderna"
description: "Amostragem a cada segundo, bissecção de mudanças categóricas e limites da inferência histórica."
timestamp: 2026-11-22T15:15:00-04:00
estado: provisorio
---

# Carter: fronteiras subminuto não são hora de nascimento

**Motivação:** a [varredura de um minuto](carter-house-time-envelope-2026.md) registrou 89 amostras (12:35–14:03 UT) com as quatro casas mencionadas em prosa editorial da família Raël/Rudhyar. O minuto é apenas a resolução da grade, não a precisão de um dado histórico.

**Novo controle moderno:** mesmo caso de 01/10/1924, coordenadas candidatas 32N02/84W24, Campanus, Swiss Ephemeris 2.10.03/Moshier e latitude eclíptica real. Testamos **21.601 instantes** de 10:00:00 a 16:00:00 UT em grade de um segundo. As quatro classes coincidem em 5.333 instantes consecutivos, de **12:34:30 a 14:03:22 UT**, ambos inclusivos. No segundo imediatamente anterior e no posterior, apenas 3/4 coincidem.

A bissecção *dentro das duas células de um segundo* estima mudanças de categoria próximas de **12:34:29,58** e **14:03:22,14 UT**, com largura numérica final inferior a 0,01 s. Esses decimais são uma propriedade computacional condicionada ao modelo e às entradas, **não a precisão do relógio de 1924, da impressão de 1980 ou do dispositivo**. Uma grade discreta não prova ausência de excursões entre amostras, embora a comparação tenha sido ampliada de minuto para segundo.

| Grade | Primeira amostra 4/4 | Última amostra 4/4 | Número de amostras |
| --- | --- | --- | ---: |
| 1 minuto | 12:35:00 | 14:03:00 | 89 |
| 1 segundo | 12:34:30 | 14:03:22 | 5.333 |

**Controles:** entradas alteradas (12h UT, latitude diferente, valor instrumental fabricado, classificação golden) devem ser rejeitadas. Bissecção sem células adjacentes ou sem mudança de classe também deve falhar. As quatro alegações editoriais são **uma única família de fonte**, acessada por [transcrição secundária](https://www.scribd.com/document/633437269/Dane-Rudhyar-Leyla-Rael-Astrological-Aspects-A-Process-Oriented-Approach-Rudhyar-Series-Aurora-Press-Inc-2018-pdf), não quatro observações independentes.

**Alcance:** o experimento reforça a **não unicidade da hora inferida das quatro casas** no motor moderno. Não compara graus ou cúspides lidos diretamente numa figura de 1980; não recupera ROM; não constitui saída golden instrumental nem resíduo histórico do DR-70.

**Reprodução:** executar 'python -B -m unittest discover -s tests -p test_carter_house_subminute_edges.py -v' e 'python -B -m scripts.carter_house_subminute_edges' com 'pyswisseph==2.10.3.2'. A etapa de GitHub Actions deve ser verificada separadamente no SHA final da PR.
