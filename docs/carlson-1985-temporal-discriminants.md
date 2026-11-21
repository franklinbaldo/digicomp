---
type: Documento
title: "Carlson 1985: painéis e testes de tempo do DR-70"
description: "Leitura crítica da figura 1 e matriz O0–O5 para distinguir relógio, longitude, modos e formatação sem inventar output histórico."
timestamp: 2026-11-20T21:45:00-04:00
estado: provisorio
---

# Painéis de Carlson antes de inferir algoritmos

🦌 Cervo · Digicomp [#7](https://github.com/franklinbaldo/digicomp/issues/7) e [#30](https://github.com/franklinbaldo/digicomp/issues/30). Complementa o [protocolo O0–O6](https://github.com/franklinbaldo/digicomp/blob/docs/rea-skill-agent-contract-20261120/docs/rea-output-first.md) e a [análise de identificabilidade anterior](time-longitude-identifiability.md). **Documento de projeto experimental, não output autenticado.**

## O0: fonte e elo instrumental

A fonte é Shawn Carlson, “A double-blind test of astrology”, *Nature* **318**, 419–425, **05/12/1985**, [DOI](https://doi.org/10.1038/318419a0), [PDF fac-similar alojado no LBL](https://muller.lbl.gov/papers/Astrology-Carlson.pdf). **Inspeção visual** da p. impressa 419 (fig. 1), 420 e 422 em 20/11/2026, por visualizador público; os bytes não foram baixados ao workspace. SHA-256 e tamanho **DESCONHECIDOS**. Sem OCR ou software histórico executado. A p. 420 relata confecção de mapas com DR-70 pelos operadores do experimento, mas **não autentica a fig. 1 como impressão contínua e inalterada desse equipamento**. Não redistribuímos a imagem.

## O1: não concatenar regiões da figura

A fig. 1 contém *regiões gráficas distintas*, possivelmente de proveniência ou estágios diferentes. O arranjo editorial **não prova** nem nega origem em uma impressora única.

| Região, p. 419 | Tokens legíveis ou leitura provisória | Limitação |
| --- | --- | --- |
| Inferior esquerda, abaixo de um desenho retangular | `C1 NATAL TROP P LONG KOCH 200`; `H01`–`H12` | Tokens documentados antes desta inspeção. Não transcrever daqui valores ilegíveis nem lhes atribuir funções sem manual |
| Ao lado dos campos `Hxx`, parte inferior central | Ao menos um cabeçalho aparentemente com `C1 SEC` | **Leitura visual provisória**; `SEC` não é modo comprovado |
| Inferior central, próximo do cabeçalho anterior | Campo que parece ler-se `DATE RECA`, seguido de data | **Grafia e números não certificados** pelo scan; desconhecemos se é outro parâmetro temporal |
| Região alta à direita | Novo cabeçalho que parece conter `C1 NATAL`, junto a tabela gráfica de layout distinto | Nenhuma prova de impressão nativa, sequência de teclas ou operação compartilhada |

O novo controle metodológico é tratar **cabeçalhos, campos de data e regiões como subobservações**, com posições e confiança separadas. A premissa “fig. 1 é um único dump consecutivo de `NATAL`” **não está sustentada**; tampouco há prova de montagem por software externo. `KOCH`, `P`, `LONG`, `200`, `SEC` e `DATE RECA` são **texto de figura**, não sintaxe operacional atribuída ao DR-70.

## O2/O3: hipóteses rivais

| Pergunta | Hipótese A | Hipótese B | Prova discriminante |
| --- | --- | --- | --- |
| Por que `NATAL` e possível `SEC` aparecem na mesma figura? | Relatórios de funções distintas do mesmo DR-70 | Partes diagramadas ou produzidas por programas diferentes | Impressão original completa com origem, manual de formato e sequência observada de operações |
| A data adicional é um relógio do cálculo? | Parâmetro temporal distinto da data de nascimento | Legenda editorial, referência posterior ou erro de leitura | Fac-símile legível e mudança isolada do campo numa sessão documentada |
| `H01`–`H12` são campos calculados pelo aparelho? | Saídas numeradas de uma rotina | Renderer posterior reapresentando resultados | Documento de saída nativa ou observação de papel/LED vinculada ao exemplar |
| Mudança angular depende de hora ou lugar? | Instante/longitude convertem-se em grandeza sideral | Outra convenção, fuso ou pós-processamento | Variações separadas de hora, longitude e canal temporal independente |

Uma origem mista é possível. Mesmo que o DR-70 tenha realizado **cálculos**, isso não autentica a **formatação** da imagem.

## O4: matriz condicional de teste, sem valores fabricados

**Pré-condição para qualquer linha:** entrada como digitada, sequência de teclas, versão/estado do exemplar, canal de saída, fotografia/registro integral e resolução dos campos. Nada disso está disponível como par autêntico atualmente. **Todos os casos = `NOT_RUN_NO_GOLDEN`.**

| Caso | Variável alterada, controles | Observação discriminante | Ressalva |
| --- | --- | --- | --- |
| T1 | Hora civil +1 h, fixando data, lugar, fuso e função, longe de transição legal | Quais campos respondem ao instante? | Não prova UTC, UT1 nem fórmula |
| T2 | Longitude +15°, preservando instante/fuso e latitude | Separar canais que respondem ao lugar | Um campo sideral isolado não identifica hora e longitude |
| T3 | Par comparativo: +1 h de instante e aproximadamente −15,041° de longitude leste | Conferir simultaneamente um canal dependente do **tempo absoluto** e o suposto ângulo sideral | Número pertence ao **comparador moderno USNO**, não ao DR-70; equivalência apenas local/aproximada |
| T4 | Duas codificações civis candidatas do mesmo instante em fuso documentado; testar também hora ambígua/inexistente por DST | Comparar políticas de fuso, sinal e desambiguação | Tzdb moderna não prova tabelas embutidas no firmware |
| T5 | Só se manual documentar um seletor: manter nascimento/local, alternar seletor e eventual segunda data | Testar se `NATAL`/`SEC` representam estados e relógios diferentes | **Não inventar teclas** a partir de legenda |
| T6 | Mudar apenas latitude, voltar ao controle e repetir com longitude | Separar sensibilidade de lugar e tempo nos campos numerados | `Hxx` ainda não são cúspides comprovadas |
| T7 | Pequenos incrementos crescentes e decrescentes no mesmo parâmetro, com repetição | Detectar truncamento, arredondamento e quantização de exibição | Sem escala e resolução autênticas, tolerância não definida |
| T8 | Fronteiras de dia/ano e calendários, após descobrir a gramática | Distinguir regra de entrada temporal de resultado astronômico | Não presumir calendário ou faixa de anos aceita |

**Controle de identificabilidade:** o [US Naval Observatory](https://aa.usno.navy.mil/faq/GAST) define tempo sideral local como tempo em Greenwich mais longitude **leste/15**. O [estudo R123](time-longitude-identifiability.md) mostra o alias: apenas um canal angular não identifica instante e longitude livres separadamente. A fig. 1 **não comprova** que o firmware usa esse algoritmo, nem que `SEC` forneça canal independente. O teste só rompe o alias se a grandeza adicional tiver resposta distinta a tempo absoluto, com resolução e formato medidos.

## O5: limite e próximo dado útil

**Status:** `NOT_RUN_NO_GOLDEN` para T1–T8. Nenhum valor da figura foi incorporado ao [corpus](fidelity-corpus.md); `data/fidelity/observations.json` continua com zero observações. Nenhuma previsão sintética é saída DR-70, nenhuma precisão foi estimada e nenhuma ROM, CPU, teclado, impressora ou efeméride foi identificada.

**Próxima observação de maior valor:** (1) leitura independente e legível dos cabeçalhos `C1 SEC` e do campo parecido com `DATE RECA`; (2) explicação contemporânea de quem formatou cada região da fig. 1; (3) uma folha integral de operação com teclas e canais vinculados a um exemplar. 🦫 Castor/🐝 Abelha devem manter blocos de tokens distintos e grau de legibilidade; 🐢 Tartaruga/🦉 Coruja devem apurar a origem editorial sem presumir impressão nativa.

Não houve compra, contato, execução de firmware, ferramenta REA conectada, alteração de corpus, ETL/IA, gasto ou experimento com equipamento. O trabalho permanece **documental**.
