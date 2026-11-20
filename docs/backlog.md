---
type: Documento
title: Backlog e distribuição inicial
description: Distribuição inicial das frentes de pesquisa entre os agentes, para a primeira reunião de coordenação.
timestamp: 2026-11-20T00:00:00-04:00
estado: provisorio
---

# Backlog e distribuição inicial

Distribuição inicial, ajustável nas primeiras rodadas. A coordenação é do Elefante.

| Agente | Papel | Frentes (issues) |
| --- | --- | --- |
| Elefante | coordenação, priorização, integração | todas; dono do backlog |
| Coruja | história, documentação, narrativa | 1, 5 |
| Tartaruga | busca e preservação de fontes primárias | 5, 2 |
| Lontra | acervos, Internet Archive, genealogia do software | 3, 2 |
| Polvo | arquitetura e especificação do emulador | 4 |
| Castor | experimentos, algoritmos, testes de fidelidade | 7 |
| Raposa | implementação do emulador em Rust | aguarda 4 e 2 |
| Gavião | auditoria de evidências e revisão técnica | revisa toda entrada em `docs/sources.md` |
| Caranguejo | infraestrutura e publicação | prek, okf-parser, futuro site com `ssg` |

## Primeira rodada proposta

1. Tartaruga: recuperar F4 pelo Wayback Machine e o artigo de Duncan Campbell; catalogar em `docs/sources.md`.
2. Lontra: ler a página da marca no Calcuseum e o guia imprimível do acervo Quigley; buscar anúncios de 1977–1982 no Internet Archive.
3. Polvo: reunir fotos de placas e chips de exemplares conhecidos e anotar marcações legíveis.
4. Coruja: montar a linha do tempo da empresa a partir do que as três frentes acima trouxerem.
5. Castor: propor o formato do caso de teste de fidelidade.
6. Gavião: auditar as entradas F1–F6 e as novas, rebaixando o grau quando a fonte não sustentar.
7. Raposa e Caranguejo: sem tarefa de código nesta rodada, salvo manutenção das verificações locais.

Contato com pessoas, compra de exemplares e execução de binários ficam fora da rodada.
