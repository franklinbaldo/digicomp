---
type: Documento
title: "Carter: janela de compatibilidade das casas editoriais sob Campanus moderno"
description: "Varredura temporal por minuto e nove variações pequenas de coordenadas, para delimitar a não identificabilidade da hora a partir de quatro casas em prosa secundária."
timestamp: 2026-11-22T14:00:00-04:00
estado: provisorio
---

# Carter: quatro casas não identificam uma hora única

**Pergunta:** a correspondência de quatro classes de casa (Lua I, Mercúrio XI, Plutão IX, Urano V), encontrada na [análise anterior](carter-historical-house-claims-2026.md), seleciona 13:00 UT como instante único?

**Resultado negativo para unicidade:** usando Swiss Ephemeris 2.10.03/Moshier, casas Campanus e latitude eclíptica real, **todas as quatro classes coincidem para cada minuto entre 12:35 e 14:03 UT (inclusive)**, sob as coordenadas candidatas 32N02, 84W24 e data 01/10/1924. Às 12:34 UT são 3/4 e às 14:04 UT são 3/4. Em 12:00 são 2/4; em 13:00, 4/4. A varredura foi predefinida entre 10:00 e 16:00 UT, com passo de um minuto. O intervalo representa **89 amostras discretas** de compatibilidade no modelo, não um intervalo de nascimento inferido ou confiabilidade estatística.

| Entrada UT | Casas coincidentes | Interpretação |
| --- | ---: | --- |
| 12:00 | 2/4 | Contrafactual de uma hora; não reproduz Mercúrio XI nem Urano V |
| 12:34 | 3/4 | Fronteira anterior, na resolução de 1 minuto |
| 12:35 a 14:03 | 4/4 | Janela de consistência categórica do modelo moderno |
| 14:04 | 3/4 | Fronteira posterior, na resolução de 1 minuto |

**Sensibilidade da posição:** nove cenários com latitude e longitude deslocadas independentemente em −1′, 0 e +1′ preservam a mesma janela na grade de minutos, além de 2/4 às 12:00 e 4/4 às 13:00. Isso não avalia incerteza de algoritmo, relógio, hora legal, sistema de casas ou transcrição editorial.

**Fonte e limites:** as quatro afirmações derivam de **uma única família editorial** de Raël/Rudhyar, acessível em [transcrição secundária indexada](https://www.scribd.com/document/633437269/Dane-Rudhyar-Leyla-Rael-Astrological-Aspects-A-Process-Oriented-Approach-Rudhyar-Series-Aurora-Press-Inc-2018-pdf). Edição, páginas e figuras originais de 1979/1980/1983 não foram identificadas/inspecionadas. O cálculo moderno não autentica instrumento, produção histórica, precisão ao minuto, idade do documento nem convenção real de nascimento. **Zero resíduos angulares históricos, zero golden DR-70, zero ROM**. Esta experiência **reduz**, em vez de ampliar, a identificação horária permitida pelo controle de casas R166.

**Reprodução:** `python -m scripts.carter_house_time_envelope` e `python -m unittest discover -s tests -p 'test_carter_house_time_envelope.py' -v` com `pyswisseph==2.10.3.2` instalado isoladamente. O novo teste inclui bordas 12:34/12:35 e 14:03/14:04, nove coordenadas, entrada contrafactual e rejeição de golden artificial. Não modifica o corpus instrumental `data/fidelity/observations.json`. Quando integrado à PR #148, verificar os logs e Prek/OKF no **SHA exato**; um teste local de sandbox não certifica o workflow nem Pages.

**Refinamento posterior (grade de um segundo):** [análise subminuto](carter-house-subminute-edges-2026.md) encontra 5.333 amostras positivas entre 12:34:30 e 14:03:22 UT no mesmo modelo, sem transformar isso em uma hora histórica precisa ou em saída instrumental.
