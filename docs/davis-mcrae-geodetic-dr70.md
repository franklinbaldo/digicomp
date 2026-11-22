---
type: Documento
title: "DR70-CASE-MCRAE-1988: uso relatado do DR-70 na cartografia geodética"
description: "Registro bibliográfico com controle matemático separado de evidência instrumental do Digicomp."
timestamp: 2026-11-21T09:51:00-04:00
estado: provisorio
---

# DR70-CASE-MCRAE-1988 · Chris McRae e a cartografia geodética

**Pergunta:** a publicação de Chris McRae em 1988 preserva saídas de cálculos produzidos no Digicomp DR-70? **Estado:** `DOCUMENTED` para a referência retrospectiva; `NOT_RUN_NO_GOLDEN` para fidelidade de saída.

## Fonte, localização e custódia

- Obra consultada: Martin Davis (org.), *From Here to There: An Astrologer’s Guide to Astromapping*, capítulo 1, "History", p. impressa 11 (**PDF p. 17/275**); capítulo 8, Chris McRae, "Looking at the World Geodetically", pp. impressas 113–128 (**PDF pp. 117–132/275**). Data editorial definitiva do volume não confirmada no exemplar; os textos registram direitos de 2007.
- Exemplar de consulta: PDF de 275 páginas fornecido pelo mantenedor em 21/11/2026, não proveniente de acervo editorial autenticado. Tamanho **6.642.453 bytes**; SHA-256 **`6de749dc820f28ede9ddfb04a05af1f86e17fa1b783dd051cca36a3421678530`**. Digest dos bytes recebidos, não certificação da publicação original. OCR e intervenções de digitalização presentes na página inicial.
- O PDF integral **não foi adicionado ao repositório**; direitos de reprodução e edição do exemplar não foram esclarecidos. Abaixo registramos apenas fatos bibliográficos, pequenos fragmentos e resultados de análise própria.
- Fonte anterior citada pelo volume: I. I. Chris McRae, *The Geodetic World Map* (1988), American Federation of Astrologers, Tempe, Arizona (referência bibliográfica no cap. 8, p. impressa 129, **PDF p. 133**). Essa edição original ainda não foi inspecionada pelo projeto.

## Evidência delimitada

**OBSERVADO no PDF recebido:** na p. impressa 11 (PDF p. 17), Davis escreve que, em 1988, McRae informatizou o trabalho geodético usando **Digicomp DR-70, IBM XT e o programa Blue Star de Michael Erlewine**, tornando possível a publicação do mapa. O texto não divide funções ou etapas entre os três recursos, nem apresenta registro do teclado, display ou impressora do DR-70.

**RELATADO, não confirmado instrumentalmente:** a utilização do DR-70 por Chris McRae é testemunho retrospectivo de Davis, não observação direta do aparelho pelo projeto. A existência de uma publicação geodética em 1988 é documentada bibliograficamente, mas ainda não vincula uma figura publicada a uma saída nativa do DR-70.

**OBSERVADO no capítulo de McRae:** na p. impressa 113 (PDF p. 117), a regra do Meio do Céu geodético (GE-MC) associa longitude terrestre a graus do zodíaco a partir de **0° de Áries em Greenwich**, avançando para leste. Exemplos impressos: Greenwich 0° → 0° Áries; Moscou 37°35′ E → 7°35′ Touro; Nova York 73°57′ O → 16°03′ Capricórnio. A figura 1, p. impressa 114 (**PDF p. 118**), é um mapa geodético com linhas de MC; o capítulo não o identifica como impressão direta do DR-70.

**DIVERGÊNCIA preservada:** a mesma p. 113 atribui a **Berlim** a longitude **02°20′ E** e, portanto, GE-MC 02°20′ Áries. É um exemplo *literal do livro*, mas a localização geográfica associada à cidade é suspeita; não foi promovido a controle de geolocalização e exige conferência independente da edição e das coordenadas. Não corrigir silenciosamente o original.

**DESCONHECIDO:** quais cálculos ou gráficos foram efetuados no DR-70, se houve saída em papel, formato da saída, parâmetros digitados, versão da máquina e eventual transferência de dados para o IBM XT/Blue Star. O livro não comprova interoperabilidade entre eles nem parentesco de firmware.

## Controles independentes de geometria, não saídas da máquina

Arquivo: [`data/reference-controls/geodetic-mcrae-mc.json`](../data/reference-controls/geodetic-mcrae-mc.json).

- Convenção explicitada: longitude a leste positiva; `GE-MC = longitude (módulo 360°)`, origem em Áries. Conservar graus/minutos como inteiros para evitar arredondamento prematuro.
- Conjunto de **três exemplos do texto**: Greenwich, Moscou e Nova York, com entrada e resultado esperado, cada um com localizador. Berlim permanece em `excluded_source_examples` por divergência geográfica, não entra nas asserções.
- Esses casos são **testes da regra geodética publicada por McRae**, aptos a controlar uma rotina de geometria implementada futuramente; **não** são `DR70` golden cases, não provam o algoritmo ou arredondamento da máquina e não devem entrar em `data/fidelity/observations.json`, no holdout DR-70 ou como saída autenticada do dispositivo.
- Visual de referência: figura 1 da p. impressa 114 (PDF p. 118). Pode orientar inspeção de linhas MC/Ascendente, mas não serve como teste pixel-a-pixel ou prova de renderer da Digicomp, sem proveniência adicional.

## Hipóteses rivais e teste discriminador (rota O0–O6)

| Hipótese | Compatibilidade com o texto | Prova discriminadora |
| --- | --- | --- |
| H1: DR-70 produziu valores intermediários efetivamente usados na obra de 1988 | Possível, **não demonstrada** | Planilhas de cálculo, notas de procedimento, impressão identificada ou capítulo original com atribuição de tarefa e números |
| H2: IBM XT/Blue Star produziu os valores e mapas, DR-70 serviu para verificações auxiliares ou cálculos distintos | Igualmente possível | Descrição operacional de 1988 e amostras controladas de output de cada sistema |
| H3: gráfico publicado foi redesenhado/editorializado a partir de fontes múltiplas | Possível | Arquivo de plotagem/arte-final e evidência de impressão de máquina com entradas associadas |

**Próximo passo de maior informação:** localizar e examinar legalmente a edição original de McRae, *The Geodetic World Map* (1988), incluindo prefácio, créditos técnicos, tabelas, apêndices e mapas. Anotar separadamente qualquer impressão atribuída ao DR-70, dados de entrada, teclas, formato e limites. Em seguida buscar entrevistas/arquivos de McRae ou documentação Blue Star contemporânea, sem contato pessoal, compra ou redistribuição sem autorização.

**Handoff:** documentação e origem bibliográfica [#5](https://github.com/franklinbaldo/digicomp/issues/5); genealogia/comparadores [#3](https://github.com/franklinbaldo/digicomp/issues/3); critérios de fidelidade [#7](https://github.com/franklinbaldo/digicomp/issues/7). Seguir [REA O0–O6](rea-output-first.md).
