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
| Inferior esquerda, abaixo de um desenho retangular | `C1 NATAL ... KOCH Z?D` (candidato), `H01`–`H12` | A terminação publicada no catálogo como `200` pode ser `ZOD`, `Z00` ou outra; pontuação de `P.LONG`/`P LONG` também incerta. Ver [leitura independente do Polvo](carlson-1985-output-hypotheses.md); sem atribuir semântica |
| Ao lado dos campos `Hxx`, parte inferior central | Ao menos um cabeçalho aparentemente com `C1 SEC` | **Leitura visual provisória**; `SEC` não é modo comprovado |
| Inferior central, próximo do cabeçalho anterior | Campo que parece ler-se `DATE RECA`, seguido de data | **Grafia e números não certificados** pelo scan; desconhecemos se é outro parâmetro temporal |
| Região alta à direita | Novo cabeçalho que parece conter `C1 NATAL`, junto a tabela gráfica de layout distinto | Nenhuma prova de impressão nativa, sequência de teclas ou operação compartilhada |

O novo controle metodológico é tratar **cabeçalhos, campos de data e regiões como subobservações**, com posições e confiança separadas. A premissa “fig. 1 é um único dump consecutivo de `NATAL`” **não está sustentada**; tampouco há prova de montagem por software externo. `KOCH`, `P.LONG`/`P LONG`, `ZOD`/`Z00`/`200`, `SEC` e `DATE REC[A?]` são **leituras concorrentes da figura**, não sintaxe operacional atribuída ao DR-70.

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

## O4/T8b: origem do dia e escala temporal são variáveis separadas

Uma [reprodução PDF textual de *Astrological Aspects* (Leyla Raël/Dane Rudhyar)](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf), na seção `APPENDIX ONE / EXAMPLE HOROSCOPES`, **atribui recálculo das cúspides Campanus ao DR-70** e lista `Sept. 5, 1935 / 27:25 U.T.` (Werner Erhard) e `Jan. 30, 1882 / 25:16 U.T.` (Franklin D. Roosevelt). O prefácio atribuído a **23/03/1979** agradece a verificação computacional por Nicki Michaels e distingue os desenhos caligráficos de Tony Milner. A reprodução **não é o fac-símile da edição de 1980 inspecionado visualmente**, nem documenta as teclas, o estado do hardware ou o papel nativo. Diferentes cópias digitais podem depender de uma única transcrição; **zero golden**.

O [US Naval Observatory](https://aa.usno.navy.mil/faq/UT.html) adverte que o dia de GMT em almanaques astronômicos e náuticos **anteriores a 1925** começava ao **meio-dia**, e diferencia UT1 (rotação terrestre) de UTC (tempo civil atômico). O [NIST](https://www.nist.gov/blogs/taking-measure/everyday-time-and-atomic-time-part-4) documenta a transição astronômica para início à meia-noite em **01/01/1925**. A data de nascimento **1882** não prova que a notação publicada cerca de **1980** reutilize a convenção de um almanaque antigo; nem `U.T.` autoriza chamar a hora de `UTC` exato em 1882.

| Interpretação matemática hipotética | `1882-01-30, 25:16` | Estatuto |
| --- | --- | --- |
| Origem no início civil do dia (00h), contando horas estendidas | `1882-01-31 01:16` | Aritmética de rótulo, **não leitura do DR-70** |
| Origem no meio-dia (12h) de um dia astronômico histórico | `1882-01-31 13:16` | Contrafactual para demonstrar **deslocamento de 12h**; a notação 25h também excede a faixa normal de um dia astronômico e não foi atestada |

Para a outra data, **1935**, a conta com origem civil à meia-noite daria `1935-09-06 03:25`; não existe base documental para importar a convenção astronômica pré-1925. Essa conta não identifica a escala física, o fuso do nascimento, a adoção histórica de horário de verão nem a gramática do firmware. **Não misturar** escolha de início do dia com transporte de fuso ou algoritmo sideral.

**Teste discriminante futuro, condicional ao manual original:** preservar os bytes/glifos de data e hora, a proveniência da data-base e a convenção explicitamente declarada. Só comparar `(D,25:16)`, `(D+1,01:16)` e `(D,01:16)` após confirmar que essas entradas são permitidas; uma rejeição de `25:16` também é resultado observável. Fotografar tecla a tecla, display/papel integral e número/revisão do exemplar. **Status atual: `NOT_RUN_NO_GOLDEN`**, sem conversão automática para UTC ou inserção no corpus.

**Controle de identificabilidade:** o [US Naval Observatory](https://aa.usno.navy.mil/faq/GAST) define tempo sideral local como tempo em Greenwich mais longitude **leste/15**. O [estudo R123](time-longitude-identifiability.md) mostra o alias: apenas um canal angular não identifica instante e longitude livres separadamente. A fig. 1 **não comprova** que o firmware usa esse algoritmo, nem que `SEC` forneça canal independente. O teste só rompe o alias se a grandeza adicional tiver resposta distinta a tempo absoluto, com resolução e formato medidos.

## O5: limite e próximo dado útil

**Status:** `NOT_RUN_NO_GOLDEN` para T1–T8. Nenhum valor da figura foi incorporado ao [corpus](fidelity-corpus.md); `data/fidelity/observations.json` continua com zero observações. Nenhuma previsão sintética é saída DR-70, nenhuma precisão foi estimada e nenhuma ROM, CPU, teclado, impressora ou efeméride foi identificada.

**Próxima observação de maior valor:** (1) leitura independente e legível dos cabeçalhos `C1 SEC` e do campo parecido com `DATE RECA`; (2) explicação contemporânea de quem formatou cada região da fig. 1; (3) uma folha integral de operação com teclas e canais vinculados a um exemplar. 🦫 Castor/🐝 Abelha devem manter blocos de tokens distintos e grau de legibilidade; 🐢 Tartaruga/🦉 Coruja devem apurar a origem editorial sem presumir impressão nativa.

Não houve compra, contato, execução de firmware, ferramenta REA conectada, alteração de corpus, ETL/IA, gasto ou experimento com equipamento. O trabalho permanece **documental**.
