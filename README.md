---
type: Documento
title: Digicomp — arqueologia digital do DR-70
description: Apresentação, objetivos e estado da pesquisa sobre o computador astrológico Digicomp DR-70.
timestamp: 2026-11-20T00:00:00-04:00
estado: provisorio
---

# Digicomp

*Digital archaeology, software preservation and emulation of the Digicomp DR-70 astrology computer.*

O Digicomp DR-70 é um computador de mesa dedicado a cálculos astrológicos, fabricado pela Digicomp Research Corporation nos Estados Unidos. O Calcuseum data o lançamento em 1977. Uma [reportagem contemporânea de 1988](docs/cadeia-dr70-quigley.md) atribui à astróloga **Nicky Michaels**, não a Joan Quigley, a posse e operação de um DR-70 para produzir cálculos destinados a Quigley. Uma entrevista retrospectiva de 2004 reitera esse papel; a posse por Quigley e a identidade de quaisquer impressões permanecem sem prova material ([fontes](docs/sources.md)).

## Objetivo

Descobrir, recuperar, compreender e, se possível, executar o **software original** do DR-70: programa, algoritmos, eventuais ROMs ou código-fonte e seus descendentes tecnológicos.

A reprodução visual do aparelho é secundária. O projeto **não** é uma calculadora astrológica genérica: uma implementação só interessa se reproduzir o comportamento do DR-70, conferido contra saídas de exemplares reais ([testes de fidelidade](docs/research-plan.md#5-testes-de-fidelidade)).

## Estado da pesquisa (2026-11-21)

| Questão | Estado |
| --- | --- |
| Fabricante e data | Digicomp Research Corporation, EUA; 1977 segundo o Calcuseum, 1981 segundo um título de fórum. A conferir. |
| Sede e fundadores | Ithaca (NY), "estudantes de pós-graduação de Cornell", segundo um único relato secundário. A conferir. |
| Processador, memória, ROM | **Desconhecidos.** Não presumir Z80, 6502 nem qualquer outro. |
| Display e teclado | Display de LED (Calcuseum); chaves MEI/WEAB lineares e chave de ignição (relato de colecionador). |
| Software, efemérides, sistemas de casas | **Desconhecidos.** |
| ROM/código original recuperado | **0 artefatos autenticados**; arquitetura de firmware desconhecida. |
| Observações instrumentais reproduzíveis | **0 casos golden**; [`observations.json`](data/fidelity/observations.json) contém `observations: []`. |
| Manuais | Nenhum localizado; o Calcuseum fotografa um cartão de instruções. |
| Ligação com Joan Quigley | Testemunhos atribuídos a Nicky/Nicki Michaels: **ela** operava DR-70 e fornecia mapas a Quigley (1988/2004); sem impressões autenticadas ou posse por Quigley demonstrada. |

## Como examinar uma evidência

O caminho de entrada é o [protocolo REA O0–O6](docs/rea-output-first.md), que exige vincular **exemplar, entrada, operação e saída** antes de propor fidelidade. O [contrato do corpus](docs/fidelity-corpus.md) distingue observação instrumental de transcrição, hipótese e teste sintético. Os candidatos e suas limitações são descritos na [issue #30](https://github.com/franklinbaldo/digicomp/issues/30).

A figura 1 de Carlson (1985) **não está autenticada como impressão literal do DR-70**. A fotografia do LED do Calcuseum mostra legendas, mas não uma sessão operacional. Nenhuma das duas pode preencher o corpus como um caso golden.

## Documentos

- [Catálogo de fontes](docs/sources.md): o que cada fonte afirma, separando fato confirmado de hipótese.
- [Linha do tempo de Nicky/Nicki Michaels e Joan Quigley](docs/cadeia-dr70-quigley.md): operadora do DR-70, destinatária de cálculos e graus de evidência.
- [Plano de pesquisa](docs/research-plan.md): frentes de investigação, critérios de conclusão e limites.
- [História comercial Matrix/Astrion](docs/matrix-dr70-astrion-trail.md): evidências documentais e hipóteses separadas de emulação.
- [Arquitetura](docs/architecture.md): possibilidades de implementação, todas provisórias.
- [Backlog da equipe](docs/backlog.md): distribuição inicial das frentes entre os agentes.

## Limites

- Nenhum firmware, ROM ou listagem de terceiros entra no repositório antes de esclarecer procedência e direitos.
- Código histórico desconhecido só roda em ambiente isolado e descartável.
- Sem compra de equipamento e sem contato externo em nome do mantenedor nesta fase.

## Verificações locais

```bash
prek install          # instala o hook de pre-commit
prek run --all-files  # okf-parser check + bloqueio de binários de firmware
```

O workflow público [DR-70 validation](.github/workflows/validate.yml) executa `prek run --all-files` em PRs e pushes da `main`, incluindo OKF e controles do corpus. Um gate verde atesta apenas as verificações executadas nesse SHA, **não** a autenticidade de ROM, manuais ou saídas do DR-70. Quando houver conteúdo suficiente, o site estático será gerado com `ssg` (Rust).

## Licença

MIT para os arquivos próprios do projeto ([LICENSE](LICENSE)). A licença não alcança firmware, manuais, fotografias ou outro material histórico de terceiros.
