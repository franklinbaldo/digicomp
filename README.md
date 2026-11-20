---
type: Documento
title: Digicomp — arqueologia digital do DR-70
description: Apresentação, objetivos e estado da pesquisa sobre o computador astrológico Digicomp DR-70.
timestamp: 2026-11-20T00:00:00-04:00
estado: provisorio
---

# Digicomp

*Digital archaeology, software preservation and emulation of the Digicomp DR-70 astrology computer.*

O Digicomp DR-70 é um computador de mesa dedicado a cálculos astrológicos, fabricado pela Digicomp Research Corporation nos Estados Unidos. O Calcuseum data o lançamento em 1977. Um relato de 2025 atribui aos antigos donos da empresa a afirmação de que a astróloga Joan Quigley, conselheira de Nancy Reagan, usava um DR-70 para levantar mapas. Essa ligação ainda não foi verificada em fonte primária ([fontes](docs/sources.md)).

## Objetivo

Descobrir, recuperar, compreender e, se possível, executar o **software original** do DR-70: programa, algoritmos, eventuais ROMs ou código-fonte e seus descendentes tecnológicos.

A reprodução visual do aparelho é secundária. O projeto **não** é uma calculadora astrológica genérica: uma implementação só interessa se reproduzir o comportamento do DR-70, conferido contra saídas de exemplares reais ([testes de fidelidade](docs/research-plan.md#5-testes-de-fidelidade)).

## Estado da pesquisa (2026-11-20)

| Questão | Estado |
| --- | --- |
| Fabricante e data | Digicomp Research Corporation, EUA; 1977 segundo o Calcuseum, 1981 segundo um título de fórum. A conferir. |
| Sede e fundadores | Ithaca (NY), "estudantes de pós-graduação de Cornell", segundo um único relato secundário. A conferir. |
| Processador, memória, ROM | **Desconhecidos.** Não presumir Z80, 6502 nem qualquer outro. |
| Display e teclado | Display de LED (Calcuseum); chaves MEI/WEAB lineares e chave de ignição (relato de colecionador). |
| Software, efemérides, sistemas de casas | **Desconhecidos.** |
| Manuais | Nenhum localizado; o Calcuseum fotografa um cartão de instruções. |
| Ligação com Joan Quigley | Alegada pelos antigos donos, segundo relato de terceiro. Acervo Quigley na Hoover Institution ainda não inspecionado. |

## Documentos

- [Catálogo de fontes](docs/sources.md): o que cada fonte afirma, separando fato confirmado de hipótese.
- [Plano de pesquisa](docs/research-plan.md): frentes de investigação, critérios de conclusão e limites.
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

Não há CI obrigatório no GitHub Actions nesta fase. Quando houver conteúdo suficiente, o site estático será gerado com `ssg` (Rust).

## Licença

MIT para os arquivos próprios do projeto ([LICENSE](LICENSE)). A licença não alcança firmware, manuais, fotografias ou outro material histórico de terceiros.
