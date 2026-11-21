---
type: Documento
title: DR-70 — exemplares públicos, operadores e sinais da interface
description: Inventário conservador de registros de aparelhos, fotografias e uso contemporâneo, sem atribuição de ROM ou deduplicação não comprovada.
timestamp: 2026-11-20T00:00:00-04:00
estado: provisorio
---

# DR-70: inventário de exemplares e evidência da interface

Levantamento público de 20/11/2026 para [Digicomp #6](https://github.com/franklinbaldo/digicomp/issues/6) e [#7](https://github.com/franklinbaldo/digicomp/issues/7). A prioridade é **encontrar o software original**. Esta nota não autoriza construção de UI, simulador, compra, contato ou execução de firmware.

**Regra de contagem:** linhas abaixo são *registros de fontes*, não contagem de máquinas diferentes. Um mesmo DR-70 pode aparecer em vários registros; sem série, cadeia de posse ou foto comparável, não somar exemplares.

## Inventário de registros

| ID | Fonte e identificação | O que sustenta | O que não sustenta |
| --- | --- | --- | --- |
| E1 | [Calcuseum, DR70](https://www.calcuseum.com/scrapbook/BONUS/10925/1.htm) e [foto da plaqueta](https://www.calcuseum.com/scrapbook/BITMAP/BONUS/10925/_SMD47726.JPG) | O catálogo associa as fotos ao DR70 de série **L606**; plaqueta fotografada com marca, modelo e local Ithaca (NY). | Não há inspeção física independente, inventário de ROM/CPU, estado funcional atual ou proprietário atual demonstrado. **1977** é data atribuída pelo catálogo, não data de fabricação lida na plaqueta. |
| E2 | [Deskthority, tópico 20346](https://deskthority.net/viewtopic.php?t=20346) | Relato de compra de um DR-70 e observações sobre teclado/chave de ignição; fonte secundária de operador/colecionador. | Série, posse atual e distinção física em relação a E1 não verificadas nesta rodada; acesso direto ao tópico retornou **403**. |
| E3 | [Computer History Museum, catálogo 102746921](https://computerhistory.org/collections/catalog/102746921), citado em [índice do CHM](https://computerhistory.org/playlists/decoding-democracy-election-resources-from-chms-collections/) | Referência catalográfica pública a DR-70 com data descritiva de 1978. | Página do objeto retornou **403** na consulta; não certificar série, localização física atual, material acompanhante ou funcionamento. |
| E4 | [Constelar, perfil de Zeferino Pina Costa (19/08/2018)](https://constelar.com.br/comunidade/astrologos/zeferino-a-sete-maos/) | Depoimento retrospectivo atribuído a Carlos Alberto Boton de que Zeferino teria trazido um **DR-70 versão 1** ao Brasil. | Não é prova de sobrevivência do exemplar, série, paradeiro ou posse; foto publicada é descrita como modelo **idêntico**, não o próprio aparelho. |
| E5 | [Grant Ranch Estate, GoToAuction, anúncio 98892](https://www.gotoauction.com/sales/view/98892.html) | Catálogo de leilão concluído em **24/10 e 29/10/2018**, Littleton, Colorado, que identifica o lote **108** como “Digicomp DR70” junto a rádio AM/FM e toca-discos Akai. | Não há série, foto do objeto individual comprovada, condição operacional, comprador, entrega ou continuação de custódia. Texto indexado foi acessível; abertura direta da página retornou **403**. |
| U1 | [Shawn Carlson, *Nature* 318, 419–425 (05/12/1985)](https://doi.org/10.1038/318419a0), [PDF alojado no LBL](https://muller.lbl.gov/papers/Astrology-Carlson.pdf), p. **420** | Relato **contemporâneo** do emprego de um **“Digicom DR 70 Astrological Computer”** para elaborar mapas de nascimento por **Michael Caveney** e **Chris Nelson**, então dirigentes da seção de San Francisco do NCGR; o artigo afirma conferência pontual por cálculo manual. | Não informa série, proprietário, chip, ROM, método de extração, paradeiro do aparelho nem disponibiliza sequência de teclas. **U1 é uso documentado, não sexto exemplar.** |

**Graus:** E1 representa aparelho *descrito e fotografado pelo acervo*; E2/E4 são relatos de pessoas, não verificação técnica; E3/E5 são registros institucionais/comerciais da existência de referências; U1 é afirmação de uso em artigo contemporâneo, mais forte para a existência de operação histórica, não para a identidade física da máquina. Não deduplicar E1–E5 automaticamente.

## Interface: o que as fotografias efetivamente mostram

No [Calcuseum](https://www.calcuseum.com/scrapbook/BONUS/10925/1.htm) há cinco fotos associadas ao registro E1:

- [Vista do aparelho](https://www.calcuseum.com/scrapbook/BITMAP/ED/DIGICOMP/_SMD10925.JPG) e [vista lateral](https://www.calcuseum.com/scrapbook/BITMAP/BONUS/10925/_SMD47725.JPG): gabinete azul, teclado físico e módulo de display frontal. As imagens não mostram placa eletrônica ou instruções de firmware.
- [Detalhe do display](https://www.calcuseum.com/scrapbook/BITMAP/BONUS/10925/_SMD47724.JPG): segmentos numéricos vermelhos e indicações impressas, entre as quais **NATAL, TROP, PRIM, SEC, TERT, SOLAR, LUNAR, DIR, CONV, ERROR, OFLOW**. Essas são **legendas visíveis**, não comandos, modos implementados ou garantia de precisão. Os dígitos fotografados não têm entrada/estado inicial documentados e **não são caso reproduzível**.
- [Foto rotulada “Instructions”](https://www.calcuseum.com/scrapbook/BITMAP/BONUS/10925/_SMD47727.JPG): capa fechada ou dobrada com marca Digicomp; **nenhuma tabela de comandos legível** nessa imagem. A presença da foto não equivale à recuperação de manual.
- [Plaqueta](https://www.calcuseum.com/scrapbook/BITMAP/BONUS/10925/_SMD47726.JPG): identificação do modelo/série. Não permite inferir CPU ou tipo de memória.

### Saída publicada em 1985: pista, não corpus pronto

O artigo de Carlson contém na página **419, fig. 1**, um *natal chart* gerado por computador, com cabeçalhos como `C1 NATAL TROP P LONG KOCH 200` e campos de casas `H01`–`H12`. Na página **420** o autor diz que os mapas do experimento foram construídos usando o DR-70; na página **422** identifica nominalmente Michael Caveney e Chris Nelson como operadores.

A figura é um **formato de apresentação contemporâneo** e uma pista útil para identificar impressões e manuais; o artigo **não afirma explicitamente que a figura é uma captura direta e inalterada da saída do equipamento específico**. Sem entrada original completa, série, sequência de teclas e ligação documental da figura ao hardware, **não catalogar números da figura como vetor de fidelidade autenticado**. A análise do experimento não valida astrologia nem revela o algoritmo da ROM.

## Próximas verificações, sem contato externo

1. **P0/P1:** localizar páginas internas do cartão do Calcuseum e eventuais impressões originais, com fotografia legível, série e procedência. O negativo atual limita-se às cinco fotos públicas inspecionadas.
2. **P1:** obter metadados públicos do CHM **102746921** e fotografias associadas por índice/espelho lícito; confirmar se há manual, ROM ou papel de entrada/saída, sem assumir que o objeto está acessível.
3. **P1:** buscar imagens do lote **108** de 2018 em arquivo público e cruzar detalhes/série para eventual deduplicação; não assumir que o leilão prova venda.
4. **P1:** procurar anexos e descrição do método no preprint **LBL-20480** citado por Carlson, mantendo dados pessoais dos participantes fora do repositório; exigir proveniência antes de transformar a figura 1 em caso de teste.
5. **P2:** uma eventual reconstrução visual precisa separar foto **confirmada**, legenda transcrita, função **não comprovada** e hipótese. Sem emulador genérico antes da recuperação do software.

**Limites:** esta nota usa apenas URLs e fatos públicos, não redistribui fotografias, PDF ou firmware e não identifica proprietários atuais a partir de anúncios. Nenhum contato foi feito. Observação de um registro público não é prova de guarda física ou de duplicidade.
