---
type: Documento
title: Plano de pesquisa
description: Frentes de investigação para recuperar e compreender o software do Digicomp DR-70, com critérios de conclusão e limites.
timestamp: 2026-11-20T00:00:00-04:00
estado: provisorio
---

# Plano de pesquisa

A pergunta central é: **o que o DR-70 calcula, e como?** Tudo o mais serve a ela.

## 1. Frentes

Cada frente corresponde a uma issue do repositório. A issue se fecha quando o critério de conclusão é cumprido, inclusive com resultado negativo documentado.

| # | Frente | Critério de conclusão |
| --- | --- | --- |
| 1 | Pessoas da Digicomp Research Corporation | Lista de nomes com fonte de cada um; registros empresariais procurados (estado de Nova York) e resultado anotado. |
| 2 | Software original | Inventário de onde código, listagens, ROMs ou fitas poderiam estar, com cada local consultado e o resultado. |
| 3 | Genealogia dos programas | Linha do tempo dos produtos Digicomp e dos softwares astrológicos contemporâneos, com hipóteses de reaproveitamento marcadas como tais. |
| 4 | Arquitetura eletrônica | Processador, memória e periféricos identificados por evidência (foto de placa, marcação de chip, manual) ou declarados desconhecidos. |
| 5 | Manuais e publicações | Manual de operação, tabela de comandos ou anúncio de época localizado e catalogado em `docs/sources.md`. |
| 6 | Exemplares e colaboradores | Lista de exemplares conhecidos (dono, série, estado) e de colecionadores, museus e ex-funcionários, sem compra nem contato nesta fase. |
| 7 | Testes de fidelidade | Formato de caso de teste definido e primeiros casos reais catalogados. |

## 2. Ordem sugerida

1. Fontes baratas: Wayback Machine (F4), página da marca no Calcuseum, artigo de Duncan Campbell, guia imprimível do acervo Quigley.
2. Fotos de exemplares existentes: marcações de chips resolvem boa parte da frente 4 sem abrir nenhum aparelho.
3. Anúncios e resenhas em revistas de 1977–1982 (Internet Archive, Google Books, acervos de revistas de astrologia e de microcomputação).
4. Registros empresariais e patentes.
5. Contato humano (antigos donos, colecionadores, Hoover), só depois de autorização expressa.

## 3. Hipóteses a testar, não a presumir

- O DR-70 usa microprocessador de propósito geral. Pode ser chip de calculadora, lógica dedicada ou microcontrolador.
- As efemérides são calculadas por série. Podem vir de tabelas em ROM, com faixa de datas limitada.
- O lançamento foi em 1977 e a placa é de um único fabricante.

## 4. Política de procedência

- Material recuperado vai para `quarentena/`, fora do Git, com registro de origem, data, quem forneceu e termos de uso.
- Só entra no repositório o que tiver direitos esclarecidos ou for análise própria (descrição, hash, metadados).
- Binário desconhecido só roda em máquina virtual descartável, sem credenciais nem rede.

## 5. Testes de fidelidade

Um caso de teste é uma tupla registrada a partir de um exemplar real:

- entrada: data, hora, fuso, local (como digitado no aparelho) e sequência de teclas;
- saída: o que o display ou a impressão mostrou, literalmente;
- procedência: exemplar (série), quem registrou, foto ou vídeo.

Comparar com a Swiss Ephemeris mede o erro do original, e esse erro faz parte do comportamento a reproduzir.

## 6. Limites desta fase

Autorizado: pesquisa em fontes públicas, documentação, issues. Não autorizado: compra de equipamento, contratação, contato externo em nome do mantenedor, execução de código histórico em infraestrutura sensível, incorporação de firmware sem procedência.
