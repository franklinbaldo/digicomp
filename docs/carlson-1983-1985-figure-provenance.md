---
type: Documento
title: "Carlson 1983–1985: a arte da figura 1 e a custódia dos mapas DR-70"
description: "Confronto de duas versões da figura e contraprovas para atribuição da formatação ao firmware da Digicomp."
timestamp: 2026-11-20T21:51:00-04:00
estado: provisorio
---

# Carlson 1983–1985: mesma figura, duas apresentações editoriais

**🦡 Texugo · Digicomp #30 · O0/O3/O4.** Complemento independente a [Polvo](carlson-1985-output-hypotheses.md) e [Abelha](carlson-1985-fig1-occurrences.md). Objetivo: testar a alegação de que a figura publicada é uma impressão original **inalterada** do DR-70, sem inferir CPU, ROM ou algoritmos.

## Fontes e localizadores

- **P83**: Shawn Carlson, *Double-blind test of astrology*, **LBL-20480**, Lawrence Berkeley Laboratory, **abril de 1983**, preprint submetido à *Nature*. [Registro institucional UC](https://escholarship.org/uc/item/0b40b045), [PDF institucional](https://escholarship.org/content/qt0b40b045/qt0b40b045.pdf), **página PDF 28 (índice zero 27), página impressa “-24-”, Figura 1**. Método: páginas impressas “-5-” e “-12-”.
- **N85**: Shawn Carlson, [*A double-blind test of astrology*](https://doi.org/10.1038/318419a0), *Nature* 318, **5/12/1985**, pp. 419–425. [Fac-símile](https://static1.squarespace.com/static/54694fa6e4b0eaec4530f99d/t/5f2acc1a7bb54677bf7fed40/1596640291173/Double%2Bblind%2Btest%2Bof%2Bastrology-Carlson.pdf): **p. 419, Fig. 1**; **p. 420, coluna do experimento**.
- Ambas as figuras e o método foram **inspecionados visualmente e por texto** em 20/11/2026. PDFs/imagens de terceiros não foram incorporados ao Git; hashes de bytes **NOT_MEASURED**. Dois estados editoriais da **mesma obra** não são dois testes físicos independentes.

## O0: contraprova visual de atribuição automática

| Fragmento | P83 (p. “-24-”) | N85 (p. 419) | Alcance da evidência |
| --- | --- | --- | --- |
| Quadrado, lista H01–H12 e matriz de aspectos | As mesmas três regiões na página de figura isolada | Mesma configuração, agora dentro do artigo | É a **mesma figura** da investigação, não outro output independente |
| Centro do quadrado | **Anotação manuscrita de cinco dígitos** visível | Área correspondente **sem anotação** | As apresentações são diferentes. Não inferir propósito nem divulgar o número |
| Margem inferior direita | Código gráfico **`XBL 832-8314`** | Código **ausente** da versão publicada | Há identificação gráfica/editorial na versão de laboratório; não é prova de modelo de impressora, CPU ou firmware |
| Cabeçalhos | `C1 NATAL`, provável `P.LONG KOCH Z?D` | Os mesmos candidatos, baixa resolução | Não decidir `200/Z00/ZOD` por OCR nem usar token como assinatura DR-70 |
| Legendas | Mapa natal produzido por computador | Legenda equivalente | Nenhuma diz que todas as regiões foram impressas pelo DR-70 sem montagem |

**Resultado:** a arte já existia no preprint de **abril/1983** e a figura de **dezembro/1985** não é reprodução integralmente idêntica da página “-24-”. Isso **refuta a formulação forte** “o impresso da Nature em 1985 é um output do DR-70 completamente inalterado”. Não refuta que o DR-70 realizou cálculos nem que painéis da arte possam derivar de folhas originais. O método de montagem, a origem dos glifos e o significado do marcador XBL seguem **desconhecidos**. Nem o código XBL nem a anotação manuscrita provam qual equipamento gerou o layout.

## Cadeia operacional que a versão de 1983 explicita

P83, *Experiment Design*, identifica **Michael Caveney e Chris Nelson** como construtores dos mapas natais no **Digicomp DR 70**, com conferência por cálculo manual em amostras. Em *Double-Blind Procedures*, P83 acrescenta que um assistente atribuiu **códigos aleatórios de cinco dígitos**, sob supervisão de **Richard Muller**, e preparou um terceiro conjunto de cartões **código + dados de nascimento**, entregue aos operadores **em envelopes que o experimentador não abriu**. O texto informa que os operadores receberam os cartões em até cinco dias das sessões de CPI.

Isso é uma trilha de **tipos de artefato a procurar**: cartões/envelopes, mapas produzidos, eventuais folhas originais e materiais gráficos de preparação. **Não** demonstra sobrevivência do acervo, nem autoriza associar a anotação do centro à identidade de um sujeito. Nenhum dado pessoal de participantes deve ser extraído ou reidentificado.

## O3/O4: hipóteses rivais e experimentos discriminantes

| Questão | A | B | Prova mínima faltante | Estado |
| --- | --- | --- | --- | --- |
| Original da página N85 | Uma folha inteira diretamente da máquina, inalterada | Arte reproduzida/modificada por processo editorial | Comparação de versões P83/N85 **já rejeita A na forma inalterada**; origem dos painéis ainda exige original de preparação | `PARTIAL_FALSIFIED` |
| Anotação de cinco dígitos | Código da pesquisa | Identificador editorial ou de outro uso | Registro da preparação do desenho, sem expor sujeitos | `NOT_RUN_NO_ARCHIVE` |
| `XBL 832-8314` | Código de controle gráfico do laboratório | Outra identificação técnica | Inventário ou negativo original XBL, com proveniência e descrição | `NOT_RUN_NO_LEDGER` |
| `H01`–`H12`, `KOCH`, `P.LONG` | Texto nativo emitido no DR-70 | Reformatado na impressão, laboratório ou edição | Papel original **+** exemplar, comando, entrada e canal de impressão identificados | `NOT_RUN_NO_NATIVE_PRINT` |
| Custódia dos mapas | Cartões e outputs preservados juntos | Só publicação derivada sobreviveu | Inventário institucional de material da pesquisa ou dos operadores | `NOT_RUN_NO_INVENTORY` |

**Controle de ablação:** sem texto metodológico, a imagem não identifica hardware; sem a imagem, o texto comprova **uso declarado** de DR-70 nos cálculos, mas não os caracteres impressos ou o programa. Não somar os dois como duas fontes independentes de output.

**Próxima pesquisa:** inventários públicos para **LBL-20480** e **XBL 832-8314**, materiais gráficos laboratoriais e registros documentais de Caveney/Nelson, sem contatar terceiros. Se forem encontrados cartões com dados privados, registrar só metadados de acervo. A [issue Digicomp #30](https://github.com/franklinbaldo/digicomp/issues/30) recebe a contraprova; nenhum par `input → output` é promovido a `data/fidelity/observations.json`.

**Gates:** inspeção de imagens **PASS**; saída nativa autenticada **NOT_RUN**; firmware/CPU **UNKNOWN**; `prek`/OKF integral **NOT_VERIFIED** (ferramentas ausentes do cache offline do executor).
