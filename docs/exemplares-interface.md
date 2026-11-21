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

## Rechecagem documental R123 (20/11/2026): novas portas e falsos atalhos

- **OpenCHM, acesso institucional:** o [CHM anunciou a abertura do OpenCHM em 21/01/2026](https://computerhistory.org/press-releases/computer-history-museum-launches-digital-portal-to-its-vast-collection/), com busca por objetos, software, imagens e documentação. Seu [portal para desenvolvedores](https://dev.computerhistory.org/portal/catalogue-products/collections-api-36) descreve uma API somente de leitura para metadados, mas **requer cadastro/chave de autorização** (cota anunciada de 3.600 chamadas/hora e 100/minuto). A página legada do DR-70, catálogo **102746921**, ainda retornou 403 à consulta web desta rodada; **não foi feita consulta autenticada à API, nem confirmado que a migração contém imagens, ROM, manuais ou um objeto físico acessível**. Este é um **caminho de busca**, não novo exemplar.
- **Política de acesso CHM:** a [orientação oficial de pesquisa](https://computerhistory.org/access-and-research/) indica consulta presencial por agendamento, algumas taxas possíveis, prazo recomendado de **ao menos três semanas** para solicitação e até quatro semanas para materiais complexos. O museu **proíbe operar os computadores de sua coleção permanente**. Assim, eventual contato futuro precisará de autorização do dono e pedido delimitado de metadados/fotografias/documentos, **não de energização ou dump operacional feito pelo museu**.
- **Lote 108 reavaliado:** o [leilão de outubro de 2018](https://www.gotoauction.com/sales/view/98892.html) anuncia uma **galeria geral de 252 fotos**, mas o texto indexado não relaciona uma imagem específica ao lote 108. Não transferir a existência da galeria para a afirmação de que uma foto autentica aquele DR-70; sem número de série ou ligação foto–lote.
- **Fonte a manter fora do inventário de hardware confirmado:** [artigo de Rudy Mazer, Effortball, 07/09/2026](https://effortball.com/blog/silicon-ephemeris-unearthing-the-digicomp-dr70-astrology-microcomputer-1981) narra um exemplar de brechó em San Jose por US$ 100 e atribui CPU **6502 ou Z80**, 1–2 KB de SRAM, EPROMs, interface de impressora e vínculo empresarial com ACS. **Não apresenta série, foto de placa, dump, laudo, nota fiscal ou fonte primária** que sustente esses detalhes. A referência a displays VFD/LCD tampouco corresponde à classificação LED do [Calcuseum](https://www.calcuseum.com/scrapbook/BONUS/10925/1.htm). Classificação: **alegações não autenticadas**, não E6 e não especificação do DR-70. A divergência não prova sozinha falsidade; impede promoção epistemológica.

**Resultado R123:** nenhuma ROM, tabela de instruções, foto interna autenticada, saída literal nem novo exemplar individualmente distinguível foi recuperado nesta rechecagem. Priorizar metadados por catálogo, sem cadastro, compra ou contato nesta etapa.

## Auditoria R124 (20/11/2026): canal de impressão e assinatura do output

**Pergunta O0/O3 de [#30](https://github.com/franklinbaldo/digicomp/issues/30):** o leiaute da fig. 1 de Carlson foi impresso diretamente por um DR-70, reformatado a partir de cálculos feitos nele ou montado editorialmente? A declaração de uso do DR-70 no artigo **não distingue** essas três alternativas.

| Controle público examinado | Resultado estrito | Inferência proibida |
| --- | --- | --- |
| [Calcuseum L606, cinco fotos](https://www.calcuseum.com/scrapbook/BONUS/10925/1.htm), sobretudo [vista lateral](https://www.calcuseum.com/scrapbook/BITMAP/BONUS/10925/_SMD47725.JPG) e [foto das instruções](https://www.calcuseum.com/scrapbook/BITMAP/BONUS/10925/_SMD47727.JPG) | Imagens externas, de baixa resolução na lateral; não exibem impressora ligada, papel legível ou interior do manual. Não se determina um canal de impressão a partir dos cabos e detalhes visíveis. | A ausência de impressora **nessas cinco fotos** não comprova inexistência de porta, acessório ou função de impressão no modelo. |
| [AFA, índice por autor dos volumes XLI–L](https://astrologers.com/wp-content/uploads/2025/07/Index-by-Author-41-50.pdf), Richard Nolle, parte 14, *Today's Astrologer*, XLVI/6, **maio de 1984, p. 13** (PDF do índice, p. 42) | O índice bibliográfico contém a expressão **“Digicomp DR-70 with printer”** e referência ao Astrion 80. A entrada já constava do catálogo de [fontes F9](sources.md), não é descoberta de uma nova máquina. | O **artigo original não foi obtido** nesta auditoria. Não há foto de conector, marca/modelo da impressora, impressão literal ou prova de que a fig. 1 de **1983** saiu desse periférico. |
| [CAELi, *Within Orb*, episódio 6, James Dotson, 31/07/2023](https://caeli.institute/2023/07/31/within-orb-episode-6-with-james-dotson/), transcrição em torno de 06:31–06:48 | Memória retrospectiva de um mapa astrológico impresso no período aproximado do fim dos anos 1970/início dos 1980; conversa também menciona um nome Digicomp, com esclarecimento editorial do DR-70. | **Não existe ligação de custódia** entre aquele papel lembrado e um DR-70 identificado. Não é exemplar novo, nem amostra independente da gramática `C1 NATAL`. |

**Localizadores para recuperar o artigo integral (R125, 20/11):** o [inventário de fascículos do AstroLearn](https://www.astrolearn.com/astrology-bibliography/todays-astrologer/) declara conservar *Today's Astrologer* **vol. 46, n. 1–7 (jan.–jun. 1984)**, intervalo que inclui o **n. 6**, identificado pelo índice AFA como **maio/1984, p. 13**. É indicação de acervo físico, **não leitura ou fotografia do artigo**. A [AFA informa digitalização dos volumes 1–70 e distribuição comercial em PDF](https://astrologers.com/grant-trust-projects/), inclusive bloco 41–50; não se verificou acesso livre ao PDF integral. São duas **vias de localização**, não duas fontes independentes sobre capacidade de impressão. Nenhum contato ou aquisição foi realizado. Priorizar reprodução lícita da **página 13 do n. 6** para saber se há imagem, descrição de porta, periférico e saída; o resumo bibliográfico, isolado, não atesta esses elementos.

### Três modelos rivais, todos ainda abertos

- **A — papel nativo:** um DR-70 identificado, por sua interface de saída, gera diretamente os cabeçalhos, símbolos, casas e diagrama. **Contraprova decisiva:** foto/scan de papel original com série, periférico/conector e operação associada; uma montagem posterior identificada derrubaria A para aquela figura.
- **B — cálculo DR-70, apresentação externa:** resultados são transcritos, exportados ou digitados em outro equipamento ou programa que os formata. **Discriminante:** fichas ou registros brutos do cálculo acompanhados da etapa de transferência e arte-final.
- **C — figura editorial/terceiro:** parte ou todo o formato publicado vem de processo independente; o relato de cálculo pelo DR-70 pode continuar verdadeiro. **Discriminante:** matriz original, arquivo gráfico, impressor ou registro editorial com procedência da figura.

O [preprint institucional LBL-20480 de 1983](carlson-1983-preprint-figure-custody.md) e a publicação *Nature* de 1985 são **duas versões da mesma obra**, não duas medições instrumentais. A diferença gráfica entre versões restringe a hipótese de uma figura editorial inteiramente inalterada, mas não autentica a origem da tipografia de cada painel.

**Busca negativa delimitada:** consultas públicas por `"C1 NATAL" "KOCH"`, `"C1 SEC" "KOCH"` e `"NATAL TROP" "P.LONG"` não forneceram, nesta rodada, uma **impressão independente com aparelho identificável**; retornos do próprio Carlson/republicações não contam como segundo exemplar. Busca não exaustiva, portanto não prova inexistência de impressos históricos. Sem arquivo original recuperado, não há hash de bytes para estas imagens/documentos e nenhum caso `replayable`: `NOT_RUN_NO_NATIVE_PRINT`, corpus de fidelidade segue sem golden.

**Próximo experimento informativo:** fac-símile do artigo de Nolle de maio/1984 (p. 13), fotografia legível de **impressora, ligação e papel em operação** no mesmo DR-70, e depois cotejo cego dos tokens com Carlson 1983. Sem contato com terceiros, compra, download de firmware ou execução histórica nesta etapa.

## Próximas verificações, sem contato externo

1. **P0/P1:** localizar páginas internas do cartão do Calcuseum e eventuais impressões originais, com fotografia legível, série e procedência. O negativo atual limita-se às cinco fotos públicas inspecionadas.
2. **P1:** obter metadados públicos do CHM **102746921** e fotografias associadas por índice/espelho lícito; confirmar se há manual, ROM ou papel de entrada/saída, sem assumir que o objeto está acessível.
3. **P1:** buscar imagens do lote **108** de 2018 em arquivo público e cruzar detalhes/série para eventual deduplicação; não assumir que o leilão prova venda.
4. **P1:** procurar anexos e descrição do método no preprint **LBL-20480** citado por Carlson, mantendo dados pessoais dos participantes fora do repositório; exigir proveniência antes de transformar a figura 1 em caso de teste.
5. **P2:** uma eventual reconstrução visual precisa separar foto **confirmada**, legenda transcrita, função **não comprovada** e hipótese. Sem emulador genérico antes da recuperação do software.

**Limites:** esta nota usa apenas URLs e fatos públicos, não redistribui fotografias, PDF ou firmware e não identifica proprietários atuais a partir de anúncios. Nenhum contato foi feito. Observação de um registro público não é prova de guarda física ou de duplicidade.
