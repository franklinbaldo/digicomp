---
type: Documento
title: "Carlson 1985: gramáticas rivais da figura 1 e teste de proveniência DR-70"
description: "Caso documental O0–O4 para cabeçalhos, casas, legendas e saída impressa, sem atribuir formatação ao firmware."
timestamp: 2026-11-20T21:41:00-04:00
estado: provisorio
---

# Carlson 1985: output-first sem confundir figura e firmware

**Responsável:** 🐙 Polvo · [Digicomp #30](https://github.com/franklinbaldo/digicomp/issues/30) / [#4](https://github.com/franklinbaldo/digicomp/issues/4). **Método:** O0–O4 do [protocolo REA integrado na PR #28](https://github.com/franklinbaldo/digicomp/pull/28). Este estudo documental foi originalmente preparado antes daquela integração. Não houve acesso à máquina nem análise de ROM.

## O0. O que a fonte primária permite associar ao DR-70

Fonte: Shawn Carlson, [*A double-blind test of astrology*](https://doi.org/10.1038/318419a0), *Nature* **318**, pp. 419–425, **5 dez. 1985**; [fac-símile PDF mantido pelo laboratório de Richard Muller](https://muller.lbl.gov/papers/Astrology-Carlson.pdf), **p. 419, fig. 1 e p. 420, coluna de método**. Consulta visual da página 419 em 20/11/2026, com confrontação do texto da página seguinte.

- **Observação documental, p. 419:** a fig. 1 apresenta um diagrama de mapa, uma listagem de posições/casas e uma matriz de aspectos. A legenda chama o conjunto de mapa natal produzido por computador. A figura **não identifica o modelo ou número de série do equipamento**.
- **Declaração explícita do artigo, p. 420:** Michael Caveney e Chris Nelson produziram todos os mapas natais do experimento em um aparelho referido pelo artigo como **"Digicomp DR 70 Astrological Computer"**, conferindo amostras à mão. O texto estabelece o método geral, **não a cadeia de custódia da imagem da fig. 1**.
- **Separação essencial:** "mapas calculados no DR-70" não implica "cada caractere, símbolo, diagrama ou coluna da figura impresso diretamente pelo DR-70". Edição, recomposição, transferência ou saída de outro programa continuam hipóteses abertas.
- **Identidade física:** nada associa a figura ao exemplar **L606** fotografado no Calcuseum. A foto de painel L606 e os artigos Nolle são **controles de proveniência distintos**.

**Material recebido:** somente acesso web ao PDF e captura visual; arquivo original não armazenado nem hasheado nesta rodada. SHA-256 de bytes recebidos: **DESCONHECIDO**; não preencher hash fictício. Direitos: reprodução editorial de 1985, apenas referências e transcrição mínima, sem copiar imagem ao repositório.

## O1. Tokens e posições, com ambiguidade mantida

| Região da figura | Transcrição restrita | Confiança/ressalva |
| --- | --- | --- |
| Cabeçalho da listagem inferior esquerda | `C1 NATAL TROP P.LONG KOCH Z?D` | **Candidato visual**, não string byte-a-byte; pontos/espaços e os dois glifos finais são de baixa resolução |
| Cabeçalho da matriz direita | `C1 NATAL TROP P.LONG KOCH Z?D` | Aparência semelhante, porém a repetição na mesma figura **não é amostra independente** |
| Segunda listagem | `C1 SEC TROP P.LONG KOCH Z?D` | `SEC` visível; significado, operação e origem tipográfica desconhecidos |
| Lista de doze linhas | `H01` até `H12` | Sequência observável; os valores com glifos zodiacais NÃO foram aceitos como dados numéricos |
| Matriz | `ORB` e uma palavra semelhante a `SCAN` | Abreviaturas e números contíguos exigem cotejo em imagem de maior resolução |
| Data no corpo | `DATE REC` ou semelhante, `4.01.1981` | Transcrição aproximada; **não** inferir formato de calendário nem que seja input digitado |

**Correção de leitura pendente:** o catálogo anterior reproduziu a terminação `200`, e a habilidade O1 ainda a cita. Uma inspeção visual do fac-símile de 1985 favorece **`ZOD`** como leitura possível, mas também existem extrações automáticas divergentes (`Z00`, `ZOO`, `200`). **Nenhuma é promovida a literal definitivo.** `200` não é base segura para inferir precisão, versão ou capacidade; `ZOD` também não demonstra algoritmo zodiacal. Similarmente, `P.LONG` é grafia candidata, não token de firmware autenticado.

## O2–O4. Hipóteses rivais e contraprovas predefinidas

| Fragmento/pergunta | Hipótese A | Hipótese B | Observação que as separaria | Estado |
| --- | --- | --- | --- | --- |
| **Origem do layout** | A impressora/periférico do DR-70 gera diretamente o mesmo layout | Dados calculados no DR-70 foram redesenhados/formatados por terceiros ou por outro programa | Papel original ou foto contínua mostrando **DR-70 identificado → comando → impressão**, com o mesmo conjunto de cabeçalhos e símbolos; controle negativo com outros programas da época | `NOT_RUN_NO_NATIVE_PRINT` |
| **`H01`–`H12`** | Índices de doze resultados de cálculo do aparelho | Índices definidos pelo formatter/edição sobre números provenientes de qualquer origem | Saída original preservada e comando documentado que altere um campo mantendo os outros constantes; comparar o conjunto de linhas no papel e no LED | `NOT_RUN_NO_INPUT` |
| **`KOCH`** | Texto de configuração ou seleção realmente emitido pelo software DR-70 | Legenda adicionada pelo operador/editor, ou importada de outro gerador | Dois registros de **mesmo exemplar**, mesmo input, seletor observado alterado, saída literal com/sem `KOCH`; manual contemporâneo da máquina que vincule comando a etiqueta | `NOT_RUN_NO_PAIRED_OUTPUT` |
| **`P.LONG` ou `P LONG`** | Abreviatura estável de campo de saída nativo | Convenção do impressor, anotação editorial ou erro de leitura do PDF | Fac-símile integral de saída autenticada + repetição em fontes independentes, distinguindo espaços, pontos e alinhamento fixo | `NOT_RUN_NO_UNEDITED_PRINT` |
| **`200` / `ZOD` / `Z00`** | Há palavra/código impresso que parece `ZOD` | Três algarismos `200` ou string distinta; perda de fidelidade na rasterização | Mesma linha em negativo, foto de resolução superior ou outra impressão **da mesma origem**; transcrição cega por dois leitores antes de interpretar | `NOT_RUN_LOW_RES` |
| **`NATAL` e `SEC`** | Modos selecionáveis do DR-70 codificados na saída | Rótulos do formatador ou fontes diversas reunidas na montagem | Manual com sequência de seleção + captura do estado do LED e papel para cada modo, sem reusar a própria figura como validação | `NOT_RUN_NO_SEQUENCE` |
| **Matriz de aspectos e ORB** | Output nativo do mesmo fluxo da lista de casas | Produção em segunda etapa ou outro software usando posições calculadas no DR-70 | Sequência de teclas, tipo de impressora/cabo, ordem temporal das duas saídas e registro da transferência entre equipamentos | `NOT_RUN_NO_CHAIN` |

**Tentativa explícita de falsificação da atribuição automática:** se um impresso de **outro programa com origem demonstrada**, anterior ou contemporâneo, contiver o mesmo cabeçalho, não prova que a figura veio desse outro programa, mas **refuta a exclusividade do formato como assinatura do DR-70**. Se o DR-70 não possuir periférico de impressão e houver prova física forte dessa ausência em uma revisão identificada, a hipótese de impressão direta nessa revisão cai; a ausência de conector em uma foto externa isolada não basta.

## Interface L606 e hardware: o que NÃO segue da figura

As legendas `NATAL`, `SEC`, `ERROR` e `OFLOW` são fotografadas no **display/painel L606**, mas a coincidência parcial com tokens impressos em Carlson não estabelece identidade de formatter, integração com impressora nem modelo de CPU. A [árvore de decisão A/B/C](reconstruction-gates.md) ainda aponta para **C, documentação**: não há dump DR-70 com SHA/custódia e ISA corroborada, nem replay com input, teclas e output original. A marca de outro equipamento Digicomp (Z80/6502/68000/6522) não resolve nenhuma das alternativas desta matriz.

## Próximo experimento mínimo e critério de aceite

1. **Transcrição dupla cega** de recorte da fig. 1 em fac-símile de resolução maior: salvar versões e proveniência separadas; registrar cada caractere duvidoso, incluindo `Z?D`, `P.LONG`, `DATE REC`, e símbolos. Não usar OCR como árbitro da grafia.
2. **Recuperar impressão/folha original** associada aos operadores ou manual de comando/impressora do DR-70. Vincular exemplar, série, comando, interface e saída no **mesmo evento**. A apresentação em *Nature* isolada não basta.
3. **Só depois**, registrar um caso `partial` no corpus; `replayable` requer input e sequência completa. Não converter desenhos, tokens ambíguos, exemplo editorial ou hipóteses em `data/fidelity/observations.json`.

**Resultados efetivos:** análise documental e hipótese A/B, com falsificadores especificados; testes empíricos e REA binário **NOT_RUN** por falta de observação elegível/ROM. Este trabalho não mede a precisão do DR-70, não identifica sua CPU nem recupera software original.
