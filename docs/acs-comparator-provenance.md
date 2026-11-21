---
type: Documento
title: Proveniência do comparador ACS citado na pesquisa do DR-70
description: Distingue identidade institucional plausível, índice bibliográfico, testemunhas e prova direta de software ou saídas do DR-70.
timestamp: 2026-11-20T00:00:00-04:00
estado: provisorio
---

# Comparador ACS: identidade, fontes e limites

**Pergunta:** o índice da AFA identifica um teste do DR-70 contra um “ACS program”. Isso permite identificar o programa comparador ou aproveitar resultados de fidelidade? **Ainda não.** Esta é uma trilha de proveniência, não uma ROM, uma transcrição do teste ou um novo caso no corpus [#7](https://github.com/franklinbaldo/digicomp/issues/7).

## Documentos e vínculos

| ID neste mapa | Fonte, época e posição | O que efetivamente sustenta | Tipo de relação |
| --- | --- | --- | --- |
| F9 | [AFA, índice por título dos volumes XLI–L](https://astrologers.com/wp-content/uploads/2025/07/Index-by-Title-41-50.pdf), Richard Nolle, parte 6, XLV/10, outubro de 1983, p. 9 | **Referência bibliográfica** a teste do DR-70 e comparação com “ACS program”; artigo integral não examinado | `indexa` obra original; **não** `transcreve_resultado` |
| ACS-A | [Astrodienst, Neil Michelsen](https://www.astro.com/astrowiki/en/ACS), verbete retrospectivo | A sigla ACS designou uma organização de computação astrológica de Michelsen; o verbete atribui fundação a **1973** | `descreve_organizacao`; não identifica o software testado por Nolle |
| ACS-U | [Urania Trust, Neil Michelsen](https://www.uraniatrust.org/celebrated-astrologers/neil-michelsen), biografia publicada em 2016 | Também usa ACS para Astro Computing Services; atribui fundação a **1972** | `descreve_organizacao`; a divergência 1972/1973 permanece |
| F13 | [Campbell, *New Statesman & Society*, 14/10/1988, pp. 14–15](cadeia-dr70-quigley.md) | Reportagem atribui a **Nicky Michaels** a operação de um DR-70, com cálculos fornecidos a Quigley | `reporta_testemunho`; não entrega uma saída autenticada |
| F14 | [Williamson, *Prediction*, setembro de 2004, pp. 46–48](docs/cadeia-dr70-quigley.md), hoje por transcrição secundária | **Nicki Michaels** narra retrospectivamente o mesmo papel de operadora | `reconta_mesma_testemunha`; publicação nova não equivale a segunda operadora |

Os IDs F9/F13/F14 remetem ao [catálogo do projeto](sources.md). Os rótulos ACS-A/ACS-U são **locais a esta nota**; não criam uma nova entrada F, nem implicam duas comprovações primárias independentes da identidade ou das atividades da firma. As biografias podem compartilhar fontes, sem genealogia editorial demonstrada. A discrepância de ano **não deve ser resolvida por votação**.

## Relações que não podem ser promovidas

- **F9 → artigo de Nolle:** o índice localiza uma peça que *pode* conter números de comparação. Sem original XLV/10 p. 9, `input_literal`, `keys_literal` e `output_literal` seguem desconhecidos.
- **ACS-A/ACS-U → entidade ACS:** sustenta uma expansão historicamente plausível da sigla, **não** a igualdade `ACS program em Nolle = produto X de Michelsen`. Não foram identificados nome, edição, versão, algoritmo, plataforma nem arquivos do programa específico.
- **F13/F14 → Michaels:** duas publicações e grafias distintas, mas **uma testemunha da própria operação**. Não somar como duas observações instrumentais independentes e não fundir os números de série do Calcuseum com o aparelho de Michaels.
- **F9/AFA em várias ordenações de índice:** versões por assunto, título e volume são apresentações bibliográficas da **mesma série editorial**, não três testes do DR-70.

## Próxima prova discriminante

1. Recuperar legalmente o artigo original de Richard Nolle, parte 6, *Today's Astrologer* **XLV/10 (outubro/1983), p. 9**; comparar com parte 5, XLV/9 (setembro/1983), p. 14. Consultar as trilhas de custódia já catalogadas em [F11](sources.md), sem compra/contato sem aprovação.
2. Transcrever literalmente qualquer identificação do produto “ACS”, configuração do DR-70, teclas, entradas, saídas e erros, com imagem/página/linha, direitos e hash **dos bytes efetivamente obtidos**. Sem isso, **não** atribuir comparador, CPU, ROM ou fidelidade.
3. Se houver pares observados, alimentar primeiro o [corpus de fidelidade](fidelity-corpus.md) como `partial`; só promover a `replayable` depois de demonstrar sequência de teclas e saída autêntica no mesmo evento, com revisão independente. Identificadores de reportagem e biografia **não** substituem evidência visual da operação.

**Estado ao fechar esta nota:** 0 ROMs, 0 programas ACS identificados no teste de Nolle, 0 pares DR-70 entrada→saída autenticados nesta pesquisa. Nenhum software foi baixado ou executado; nenhum contato, compra ou custo. Esta nota não afirma ausência desses objetos fora das fontes consultadas.
