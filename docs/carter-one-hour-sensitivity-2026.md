---
type: Documento
title: "Carter UTC 12:00 versus 13:00: controle moderno de variável única"
description: "Experimento numérico que isola a hora UTC em quatro campos de duas cartas modernas, sem autenticar dados de 1980 ou o DR-70."
timestamp: 2026-11-22T12:00:00-04:00
estado: provisorio
---

# Carter: experiência controlada de deslocamento de uma hora (22/11/2026)

**Questão falsificável:** a discrepância dos quatro campos entre [AstroDienst na publicação de 2023, p. 12](https://static1.squarespace.com/static/625588022bac29595ab0c386/t/652c6205bd50527fa4e8778a/1697407494104/Jimmy%2BCarter%2Band%2Bthe%2BKnight%2Bof%2BPentacles_final.pdf#page=12) e [Astro-Charts consultado em 22/11/2026](https://www.astro-charts.com/persons/chart/jimmy-carter/) pode ser reproduzida mudando **somente** a entrada UT 13:00 para 12:00?

Método: mesmo 01/10/1924, latitude +32°02′, longitude leste −84°24′, Swiss Ephemeris `swisseph.version=2.10.03`, planetas com `FLG_MOSEPH`, casas Campanus no laboratório. Para cada uma das duas horas, comparar ASC, MC, Sol e Lua à fonte **correspondente**; o controle de 2023 contém segundos (±1″ operacional), enquanto o Astro-Charts publica apenas minutos (critério de **menos que 60″ em módulo**, sem inventar segundos).

| Campo | 12:00 UT, graus absolutos | 13:00 UT, graus absolutos | Variação de 12→13, ″ | Residual às posições Astro-Charts 12:00, ″ | Residual às posições AstroDienst 13:00, ″ |
| --- | ---: | ---: | ---: | ---: | ---: |
| ASC | 193,305594625 | 206,093892524 | +46.037,872 | −39,859 | +0,013 |
| MC | 104,311730174 | 118,464583694 | +50.950,273 | −17,771 | −0,499 |
| Sol | 188,020770065 | 188,061782704 | +147,646 | +14,772 | +0,418 |
| Lua | 223,194894845 | 223,796465000 | +2.165,653 | +41,621 | +0,274 |

*Residual* é ângulo calculado menos longitude publicada, reduzido ao arco assinado menor. Saída exploratória produzida na sandbox em 22/11/2026. Os testes versionados em `tests/test_carter_one_variable_utc.py` reproduzem a comparação por fonte, a contraprova de entrada trocada e a invariância de ASC/MC ao trocar Campanus por Placidus (não se aplica às cúspides). Executá-los no workflow público `chart-reference.yml` após instalar o binding opcional.

**Resultado moderno:** 4/4 campos a 12:00 dentro de menos de 60″ dos componentes Astro-Charts; 4/4 a 13:00 dentro de ±1″ dos campos AstroDienst. A troca de uma hora reproduz, portanto, a **magnitude e o sentido** das divergências publicadas, mantendo as outras entradas do cálculo fixas. ASC e MC coincidem entre Placidus e Campanus para a mesma entrada neste ensaio; não explicar as variações desses ângulos pela escolha do sistema de casas.

**O que não fica demonstrado:** não provamos qual efeméride, algoritmo, arredondamento ou UTC real cada serviço empregou internamente; a página Astro-Charts não foi preservada em snapshot com hash. A lei estadual de 1919 favorece CST (UTC−06, 13:00 UT) como hora **legal** em 1924, mas o relógio real do nascimento não foi inspecionado. A fonte de 2023 e o laboratório podem compartilhar Swiss Ephemeris. **Não há carta da edição de 1980 transcrita numericamente, golden instrumental, ROM original nem residual DR-70.** A impressão de 1980 permanece a próxima evidência discriminante.

Não editar `data/fidelity/observations.json` ou transformar este ensaio de 2023/2026 em observação de saída histórica.
