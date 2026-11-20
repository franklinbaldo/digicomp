---
type: Documento
title: "Trilha de software Digicomp: Pascal-100, Delphi 100 e SBIR"
description: "Fontes de 1980–1984 e limites de atribuição ao firmware do DR-70."
timestamp: 2026-11-20T00:00:00-04:00
estado: provisorio
---

# Digicomp: trilha de software fora do DR-70

Pesquisa pública da 🦦 Lontra em 20/11/2026 para [Digicomp #2](https://github.com/franklinbaldo/digicomp/issues/2) (software original) e [#3](https://github.com/franklinbaldo/digicomp/issues/3) (genealogia). **Nenhum firmware, ROM, EPROM ou listagem do DR-70 foi recuperado.**

## Fontes recuperadas e grau

**SW1 — *Electronics*, 18/12/1980, p. impressa 133.** [Edição digitalizada](https://www.worldradiohistory.com/Archive-Electronics/80s/80/Electronics-1980-12-18.pdf), coluna *Products Newsletter*. A publicação contemporânea descreve a CPU **Pascal-100** de duas placas S-100, combinando microprocessador tipo Z80 e Pascal Microengine da Western Digital; menciona compatibilidade CP/M/UCSD Pascal, preço anunciado de US$ 1.485 e fabricante **Digicomp Research Inc., Ithaca**. O ganho de velocidade citado é alegação da fonte, não benchmark independente. **Estado:** trecho textual extraído do PDF; o recorte visual não foi conferido porque a renderização retornou HTTP 403. O texto diz respeito ao Pascal-100, **não demonstra arquitetura do DR-70**.

**SW2 — Info-Kermit Digest 1(42), de 06/12/1984.** [Mensagem histórica de Charles Carvalho, 05/12/1984](https://groups.google.com/g/net.micro.cpm/c/_GWgL_GQYng), preservada em Usenet. O anúncio de **Kermit-80 v4.03** enumera suporte a **Digicomp Delphi 100**. Na tabela de configuração: símbolo `DELPHI`, arquivo `CP4DEL` e fonte de configurações `CP4SYS.ASM`; indica terminal externo. **Estado:** mensagem técnica contemporânea integralmente legível, não teste físico em hardware, e não é software do DR-70.

**SW3 — arquivo de fontes Columbia/Kermit.** [Kermit Project, seção CP/M-80](https://www.kermitproject.org/archive.html), índice atualizado em 2025. A lista de plataformas inclui **Digicomp Delphi 100** para **Kermit-80 v4.11, de 23/04/1991**, em assembler 8080, com ponteiros para `cpm80.zip`, `cpm80.tar.gz` e lista de arquivos. **Estado:** catálogo consultado, sem baixar/hachear os pacotes nem conferir o módulo Delphi. A data de 1991 é da versão Kermit, não do lançamento do computador. **Fonte de um software de comunicações distinto do firmware astrológico**.

**SW4 — SBIR, prêmio 39036.** [Registro governamental](https://www.sbir.gov/awards/39036) lista **Digicomp Research Corp., Terrace Hill, Ithaca NY**, prêmio Phase I de **1983**, **US$ 48.072**, ramo USAF, projeto **Multi-Level Secure Computer System**, cujo resumo propõe arquitetura microprocessada de hardware e software. James Elkins consta somente como contato comercial. **Estado:** prêmio registrado e resumo lidos, não código-fonte executado ou demonstrado. Não estabelece autoria do DR-70 nem conclusão efetiva de protótipo. O endereço Terrace Hill coincide com a pista do artigo de 1979 [L1](corporate-patents.md), mas não certifica continuidade jurídica da razão social.

## Cronologia segura

| Data | Evidência | Inferência permitida |
| --- | --- | --- |
| 1977 (segundo catálogo) | [F1](sources.md): DR-70 | Ano relatado; falta documento de lançamento |
| 1979 | [L1](corporate-patents.md): DR-70, Digicomp e endereço Terrace Hill | Documento textual contemporâneo, não placa ou ROM |
| Dezembro de 1980 | SW1: Pascal-100 | Outro produto da Digicomp |
| 1983 | SW4: contrato SBIR | Outra frente de pesquisa da corporação |
| Dezembro de 1984 | SW2: port Kermit de Delphi 100 | Outra plataforma computacional da marca |
| Abril de 1991 | SW3: Kermit-80 v4.11 arquivado | Manutenção do software Kermit, não data de máquina |

**Atenção:** nenhuma dessas fontes comprova código compartilhado, processador compartilhado ou os mesmos engenheiros entre DR-70, Pascal-100, Delphi 100 e a proposta SBIR. **Z80 no Pascal-100 não implica Z80 no DR-70.** `Inc.` (SW1) e `Corp.` (SW4) podem refletir grafias editoriais ou pessoas jurídicas distintas; a identidade societária requer documento próprio.

## Inventário de consultas, restrição da busca

- *Electronics* digitalizada: **trecho textual localizado**, PDF do recorte não inspecionado visualmente, nenhum hash dos bytes originais.
- Mensagem Info-Kermit 1984: **documento contemporâneo aberto** com símbolos de código.
- Arquivo de código-fonte Kermit: **índice localizado**, sem recuperação dos arquivos e sem SHA-256.
- Base SBIR: **registro de prêmio aberto**, sem artefatos técnicos do DR-70.

**Resultado negativo delimitado:** entre essas fontes não apareceu ROM, EPROM, fita ou listagem reconhecível do DR-70. Isso não prova inexistência em outros acervos.

## Próximos experimentos

1. Em [#2](https://github.com/franklinbaldo/digicomp/issues/2), baixar em quarentena **somente com custódia de origem** a lista de fontes Kermit, conferir `CP4SYS.ASM` / `DELPHI` / `CP4DEL`, registrar tamanho e hash sem executar programa desconhecido. Material será de outro computador e não se torna ROM do DR-70.
2. Em [#3](https://github.com/franklinbaldo/digicomp/issues/3), buscar anúncios originais de 1977–1982 que discriminem DR-70, Pascal-100 e Delphi 100; cruzar endereço Terrace Hill e nomes societários sem identificar criadores por mera coincidência.
3. Priorizar **manual, fotos de placas e listagens do DR-70** antes de escrever emulador; não comprar hardware nem contatar pessoas sem instrução nova.
4. Solicitar revisão retrospectiva 🦅 do grau de evidência de cada alegação.

Nenhuma ROM, fonte ou programa de terceiros foi incluído neste repositório. Nenhum binário foi executado, e não houve contato externo, custo novo ou mudança operacional.
