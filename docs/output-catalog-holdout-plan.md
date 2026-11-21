---
type: Documento
title: "Digicomp DR-70 — inventário de saídas e separação de holdout"
description: "Plano output-first com catálogo reproduzível de fontes, deduplicação por sessão e testes Rust/Lean4 sem contaminar os casos reservados."
timestamp: 2026-11-21T00:00:00-04:00
estado: experimental
---

# Catálogo primeiro; reprodução depois

**Direção do proprietário em 21/11/2026:** recolher e catalogar **todos os exemplos localizados** de output, mesmo incompletos, para orientar a reconstrução Rust e reservar exemplos independentes como testes de holdout. Uma publicação repetida não vira outra amostra. O catálogo inicial executável é [`catalog.json`](../data/output-candidates/catalog.json), ligado ao [ledger visual Carlson](carlson-fig1-token-ledger.md) e ao [corpus de observações](fidelity-corpus.md).

## Regra de captura ampla: primeiro salvar o que apareceu

A prioridade é **recolher resultados astrológicos atribuídos ou possivelmente atribuíveis ao DR-70 que alguém publicou na internet**, não obter de imediato sessões completas. São admissíveis na coleta inicial: tabelas de posições, listas de casas, mapas, relatórios impressos, fotografias de displays com números, fotos de folhas, reprodução em artigos, vídeos, transcrições de usuários, comparações com outras máquinas e recortes cujo conteúdo seja apenas parcialmente legível. Basta um **vestígio material ou textual de resultado** e uma fonte/localização; não são exigidos data/hora de entrada, teclas, série, formato eletrônico nem atribuição comprovada nessa etapa.

Registrar como foi encontrado, inclusive unidades não identificadas, grafia, glifos incertos, números incompletos e condições de acesso. O registro mínimo para triagem é URL, posição na fonte, descrição livre do conteúdo, fragmento legível e grau de dúvida. Caso nem conteúdo de saída esteja disponível, manter registro como **pista a recuperar**, separado da contagem de outputs encontrados. A ficha poderá ser enriquecida ao longo das rodadas, sem reescrever o original.

Na figura Carlson, o ledger já documenta **seis pares candidatos** de grupos numéricos H01/H07 a H06/H12. Esses grupos foram agora inseridos em `catalog.json` como **transcrição secundária pendente de nova inspeção da imagem**, sem completar glifos faltantes, inferir graus absolutos ou criar golden. A figura de 1983 e a republicação de 1985 são uma família, não dois exemplos independentes.

A coleta deve ser ampla e contínua, inclusive fontes que não permitam reproduzir imagens integralmente no Git. Quando os direitos de reprodução não estiverem esclarecidos, conservar link, localizador, transcrição factual breve e metadados, e manter o arquivo original fora da publicação pública quando cabível. Não criar barreiras prematuras para recolher o que há.

## Duas coleções distintas

1. **Acervo amplo de candidatos:** tudo que possa conter saída, mesmo sem dados de entrada, e também pistas negativas como fotografias sem operação e artigos ainda inacessíveis. Inclui duas versões da figura 1 de Carlson (1983/1985), **uma única família**; fotografia do display L606; índice Nolle; testemunho Devine sobre impressora; vídeo Morris sem quadro legível. Os últimos não são testes numéricos, mas preservam lacunas e evitam redescoberta. URLs, localizadores e pequenos tokens são indexados; não redistribuir PDFs, fotos e figuras de terceiros sem direitos.
2. **Corpus de execução:** somente observações instrumentais de **entrada e saída da mesma sessão**, revistas por outra pessoa, com dados de entrada como digitados, sequência de teclas e caracteres literais. É o já existente `data/fidelity/observations.json` e permanece **vazio**, por ausência de caso admissível. Registros parciais úteis são preservados no catálogo, não forçados para o esquema `replayable`.

## Método de desenvolvimento e holdout

- Congelar fontes e localizadores, digitalizar/transcrever com controle visual e dupla revisão antes de normalizar unidades ou glifos. Preservar `null`, trechos ilegíveis, transcrição bruta e revisão. Se os bytes originais forem obtidos licitamente, registrar SHA-256; URL não prova identidade.
- Deduplicar por **artefato, origem, exemplar e sessão**, não apenas URL. Os documentos Carlson F83 e F85 não podem ficar um no desenvolvimento e outro no holdout. Toda repetição ou recorte da mesma impressão herda `family_id`.
- Reservar holdout **antes** de escolher constantes e modelos. Um exemplo só, ainda sem input, não permite calibrar e avaliar independentemente. Não declarar sucesso; estado atual: `NOT_RUN_NO_GOLDEN` e `NOT_RUN_NO_INDEPENDENT_HOLDOUT`. Holdout fica inacessível ao ajuste; revisão independente registra alterações e motivo.
- Rust recebe entrada original, modela hipóteses rivais de data/hora/fuso/coordenadas, efemérides, sistemas de casas, arredondamento e formatter **apenas conforme suporte documental**. Comparar texto bruto quando possível e valores angulares só com unidade e formato autenticados. O código da [PR #92](https://github.com/franklinbaldo/digicomp/pull/92) é uma exploração sintética, não atende ainda esse gate.
- Lean 4 formaliza invariantes e impossibilidades condicionais (por exemplo, simetria de pares, limites de quantização, equivalência entre parâmetros sob observações parciais). Prova de teorema de **modelo** não prova que o firmware DR-70 o implementa.
- Avaliar modelos por cobertura de campos observados, discrepâncias literais e numéricas, e rejeição explícita de casos sem entrada. Nunca maximizar desempenho no holdout e depois apresentá-lo como cego; uma vez consultado para ajuste, aquele conjunto torna-se desenvolvimento e é necessário novo holdout independente.

## Gate de admissão em desenvolvimento versus holdout (R142)

O **acervo exploratório** aceita `sample_split: unassigned` e incompletude; não exigir campos instrumentais para recolher pistas. Para admitir `holdout`, a validação estrutural requer, além dos quatro flags booleanos, `kind: device_session_output`, `status: reviewed`, `attribution: device_native_session_output`, `literal_fragments` não vazio e um objeto `instrumental_evidence` com `device_identifier`, `session_locator`, `input_as_entered`, `key_sequence` não vazia, `output_channel` (display/printer), `output_literal`, `independent_reviewer` e `independent_review_reference` não vazios. Os fragmentos literais devem ocorrer na transcrição bruta. São **declarações sujeitas a auditoria**, não autenticação automática: nenhuma destas marcas por si demonstra máquina, operador, série, papel ou dados reais.

O guard recusa o **mesmo par exato** URL HTTPS + localizador em `development` e `holdout`, mesmo que alguém renomeie a `family_id`. Também mantém a proibição de família compartilhada entre os dois grupos. Recusa ainda o mesmo par **`instrumental_evidence.device_identifier` + `instrumental_evidence.session_locator`** em ambos os splits, mesmo quando URLs, localizadores documentais e famílias diferem. O par de sessão é uma declaração a auditar, não prova física de identidade. URLs-espelho, recortes, variações textuais e famílias artificialmente separadas por regiões distintas ainda requerem revisão humana; o validador não infere identidade documental de URLs diferentes. Os testes negativos introduzem casos falsos **apenas em memória** e verificam a recusa das duas tentativas de promoção. Um exemplo positivo também é inteiramente falso para provar somente a capacidade de representar um caso futuro.

A reserva `holdout` não é pontuação de fidelidade: com `observations: []`, não há cálculo comparável nem direito a afirmar aprovação histórica.

## Execução do catálogo

```sh
python3 -B scripts/check_output_candidates.py
python3 -B -m unittest discover -s tests -p test_output_candidates.py -v
```

O primeiro teste recusa duplicidade de ID, origem sem localizador, compartilhamento de `family_id` entre desenvolvimento e holdout e promoção artificial de fotografia ou figura editorial a caso numérico. É **gate estrutural**, não autenticação. Casos simulados só existem dentro do teste unitário.

## Descoberta bibliográfica R2: vinte exemplos atribuídos a cálculos DR-70

Em *Astrological Aspects: A Process-Oriented Approach* (Leyla Raël e Dane Rudhyar; prefácio datado de 23/03/1979, edição com copyright de 1980), o prefácio informa que os mapas do Apêndice I usam cúspides Campanus, agradece a **Nicki Michaels** pela conferência em seu computador e identifica **Tony Milner** como responsável pela caligrafia dos mapas. A nota bibliográfica ao fim do apêndice diz explicitamente que **todos os exemplos foram recalculados em um DR-70**. Fontes de localização: [PDF textual](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf), [outra transcrição textual](https://pdfcoffee.com/astrological-aspects-pdf-free.html). Há **20 exemplos nomeados**: Alan Watts, Albert Einstein, Albert Schweitzer, Andrew Carnegie, Dag Hammarskjöld, Franklin D. Roosevelt, George Bernard Shaw, George Sand, Henry Ford, Herman Melville, J. Edgar Hoover, Jerry Brown, Jimmy Carter, Krishnamurti, Mohandas Gandhi, Niels Bohr, Paul Case, Ram Dass, Vaslav Nijinsky e Werner Erhard. Os registros estão distribuídos em `rudhyar-rarel-part-1.json` e `rudhyar-rarel-part-2.json` (dez por arquivo, abaixo do limite de 20 KB).

**Grau da evidência:** há uma **atribuição explícita de recálculo pelo DR-70** a esses exemplos. A diagramação não é nativa: o prefácio atribui a arte/calígrafo a outra pessoa. A inspeção visual do PDF de referência falhou por indisponibilidade do recurso de captura/redirecionamento; **não declarei nenhum valor de casas ou planetas conferido**, nem copiei páginas protegidas. A expressão “20 exemplos” é a contagem de itens enumerados, não 20 sessões DR-70 independentes. A mesma obra editorial compõe uma família documental conservadora até haver custódia por exemplo. O texto lista ainda algumas entradas biográficas de origem secundária, mas nenhum par foi validado como digitado na máquina. Para amostrar, o primeiro passo é localizar as imagens de cada mapa no exemplar, cotejar com os respectivos dados publicados e preservar os valores realmente legíveis, marcados como **atribuição editorial**.

**Pista adicional de 1988:** Duncan Campbell, [*Reagan's Secret Computer*, New Statesman & Society, 14/10/1988, pp. 14–15](https://www.duncancampbell.org/menu/journalism/newstatesman/newstatesman-1988/Reagan%27s%20secret%20computer.pdf), relata que Nicky Michaels conferiu uma impressão do DR-70 relacionada ao tratado INF. As páginas foram examinadas visualmente; a impressão **não aparece** na reprodução. Guardar como evento de output relatado, sem inventar posições planetárias nem aceitar a hora narrada como input exato. O relato de 1988 não fornece um teste numérico.

**Separação de métricas:** 30 registros de catálogo = 20 mapas listados (ainda sem leitura visual) + duas publicações da mesma figura Carlson + imagem do display L606 + quatro pistas textuais/visuais anteriores + três URLs de vídeo do mesmo colecionador no Deskthority, ainda sem quadros acessíveis. Isso **não** equivale a 30 resultados transcritos nem a 30 golden tests.

## Lacunas a fechar na próxima rodada

- 🦫 Castor + 🐝 Abelha: completar a conferência manual da tabela numérica de Carlson e manter valores incertos sob marcação, sem assumir impressora.
- 🐢 Tartaruga + 🦦 Lontra: buscar impressão independente, manual e eventual conjunto original de entrada e saída, inclusive artigo completo de Nolle. Obter autorizações de reprodução se necessário.
- 🦇 Morcego: catalogar cada novo vestígio, incluindo fotografias e vídeos, sem confundir legenda fixa com saída computada.
- 🦊 Raposa + 🦌 Cervo: conectar modelos Rust a campos somente após haver entrada histórica completa, sem ajustar a figura por retroengenharia de parâmetros inventados.
- 🐙 Polvo + 🦫 Castor: definir experimentos discriminantes e lemas Lean 4, preservando o holdout.
- 🦅 Gavião: revisar proveniência e alteração de status antes de declarar qualquer teste de fidelidade.

**Não se copiam os fac-símiles integrais para o Git público automaticamente.** Um inventário com URLs permanentes, localizadores, trechos factuais curtos e hashes de material obtido de forma autorizada permite coletar exaustivamente sem pressupor licença para redistribuição.
