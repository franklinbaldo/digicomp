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
| ACS-79 | [Mark Pottenger, *Computers and Astrology*, *The Mutable Dilemma*, Virgo 1979](https://ccrsdodona.org/m_dilemma/1979/vir/computer.html), [índice da revista](https://www.ccrsdodona.org/m_dilemma/) | Texto contemporâneo identifica o sistema de Neil Michelsen como **Astro Computing Services**, classifica-o como **minicomputador** e descreve, em passagem separada, o DR-70 como aparelho dedicado pré-programado | `cita_sistemas_distintos`; transcrição HTML posterior da revista, **não** fac-símile físico nem programa de 1983 |
| F13 | [Campbell, *New Statesman & Society*, 14/10/1988, pp. 14–15](cadeia-dr70-quigley.md) | Reportagem atribui a **Nicky Michaels** a operação de um DR-70, com cálculos fornecidos a Quigley | `reporta_testemunho`; não entrega uma saída autenticada |
| F14 | [Williamson, *Prediction*, setembro de 2004, pp. 46–48](cadeia-dr70-quigley.md), hoje por transcrição secundária | **Nicki Michaels** narra retrospectivamente o mesmo papel de operadora | `reconta_mesma_testemunha`; publicação nova não equivale a segunda operadora |

Os IDs F9/F13/F14 remetem ao [catálogo do projeto](sources.md). Os rótulos ACS-A/ACS-U/ACS-79 são **locais a esta nota**; não criam uma nova entrada F, nem implicam duas comprovações primárias independentes da identidade ou das atividades da firma. As biografias podem compartilhar fontes, sem genealogia editorial demonstrada. A discrepância de ano **não deve ser resolvida por votação**.

## Controle negativo de atribuição: exemplo de Joyce Wehrman com selo ACS

**Polvo, 21/11/2026, O0/O1.** A reprodução textual de *What Are Winning Transits*, de [Joyce Wehrman no Scribd](https://www.scribd.com/document/38654289/Wehrman-Joyce-What-Are-Winning-Transits), seção **“FORMAT OF THE REPORT”**, apresenta um exemplo que identifica expressamente **Astro Computing Services, White Plains, NY**, com o rótulo **“KOCH TROPICAL”** e uma linha datada **Friday, May 3, 1985**. A autora atribui o cálculo e o relatório ao programa/serviço **Winning Transits** de Astro Computing Services, e menciona que clientes enviavam dados ao fornecedor. A [reprodução textual alternativa](https://pdfcoffee.com/wehrman-joyce-what-are-winning-transits-pdf-free.html) conserva os mesmos elementos; **duas cópias da mesma obra não são dois outputs independentes**.

**Distinguir obras e épocas:** esse exemplo com data de 1985 não pode ser um gráfico original da edição revisada de **1980** de [*Winning!!: Zodiacal Timing*](wehrman-winning-1980-dr70.md), nem documenta o teste de Nolle **1983**. Mesmo quando duas peças contêm a palavra `KOCH`, isso não identifica máquina, software, algoritmo ou formatador. A semelhança de campo seria apenas pista para cotejo, não evidência de que o DR-70 gerou a impressão. A ficha bibliográfica [Google Books](https://books.google.com/books/about/Winning.html?id=KoePGwAACAAJ) situa a edição revisada de Wehrman em 1980 (81 páginas), mas não fornece imagem dos mapas.

**Controle discriminante proposto:** diante de qualquer imagem futura ligada a Wehrman, transcrever literalmente `imprint`, cabeçalho, data, campos de entrada, rótulos de casas, bordas e canal. Se o original identificar **ACS** ou **Winning Transits**, classificar como output **atribuído editorialmente ao serviço ACS**, não ao DR-70; se identificar DR-70, exigir ainda a ligação específica ao exemplar/sessão e separar cálculo de composição. Não igualar o programa Winning Transits de data posterior ao “ACS program” não identificado no índice de Nolle.

**Limitação:** inspeção **somente de texto HTML transcrito**, sem fac-símile, hash de bytes originais, imagem da tabela ou registro de operação. O carimbo **03/05/1985** é **data interna do exemplo**, não data de publicação do folheto ou de execução verificada do serviço. Estado científico: **nenhum par DR-70 entrada→saída autenticado; `NOT_RUN_NO_GOLDEN`**.

## Hipóteses distintas sobre a comparação de 1983

O texto contemporâneo de **Pottenger (1979)** documenta que **ACS** era uma designação em uso, associada a Neil Michelsen, antes do teste indexado de 1983. A mesma matéria trata ACS como sistema de minicomputador e descreve **separadamente** o DR-70, com software pré-programado. É uma fonte contemporânea reproduzida como HTML, **sem fac-símile da revista conferido**, e não fornece código ou resultados de cálculo. [Dossiê contextual de 1979](1979-pottenger-dr70.md).

A [entrevista retrospectiva de Michael Erlewine, publicada em 2023](https://theastrologypodcast.com/transcripts/tap-ep-408-transcript-the-first-astrology-software-program-with-michael-erlewine/), caracteriza ACS como serviço de cálculo e remessa de mapas a clientes, em contraste com programas vendidos para microcomputadores. É **depoimento tardio sobre um modelo de negócio**, não identificação direta do software usado no ensaio de Nolle.

| Hipótese para o “ACS program” de Nolle | Observação que distinguiria | Estado |
| --- | --- | --- |
| H1: resultados gerados pelo sistema/serviço de Michelsen foram comparados com o DR-70 | O original XLV/10 explicita encomenda, fornecimento de mapa, equipamento do prestador e/ou resultados recebidos | **Não testada**; serviço existia, mas o artigo não foi obtido |
| H2: um programa ACS específico foi operado pelo revisor ou por terceiro durante o teste | O original especifica nome/versão, mídia, plataforma, operador, comandos e/ou saída do programa | **Não testada**; nenhum software identificável foi localizado |
| H3: “ACS program” era apenas rótulo abreviado de uma referência de resultados sem descrição de execução | O original contém comparação de números sem procedimento ou identificação de programa | **Não testada**; índice não discrimina |

**Controle contra falsa independência:** Pottenger 1979, a entrevista de Erlewine 2023 e os verbetes de Michelsen sustentam aspectos da história de ACS, não são três reproduções do ensaio de Nolle. O índice da AFA permanece **uma** indicação bibliográfica de um teste, sem saída literal ou ROM. Nenhuma das hipóteses autoriza preencher o corpus de fidelidade.

## Relações que não podem ser promovidas

- **F9 → artigo de Nolle:** o índice localiza uma peça que *pode* conter números de comparação. Sem original XLV/10 p. 9, `input_literal`, `keys_literal` e `output_literal` seguem desconhecidos.
- **ACS-A/ACS-U → entidade ACS:** sustenta uma expansão historicamente plausível da sigla, **não** a igualdade `ACS program em Nolle = produto X de Michelsen`. Não foram identificados nome, edição, versão, algoritmo, plataforma nem arquivos do programa específico.
- **F13/F14 → Michaels:** duas publicações e grafias distintas, mas **uma testemunha da própria operação**. Não somar como duas observações instrumentais independentes e não fundir os números de série do Calcuseum com o aparelho de Michaels.
- **F9/AFA em várias ordenações de índice:** versões por assunto, título e volume são apresentações bibliográficas da **mesma série editorial**, não três testes do DR-70.

## Vias concretas de custódia do artigo de 1983 (consulta de 20/11/2026)

- **Edição digital institucional declarada:** a [American Federation of Astrologers](https://astrologers.com/grant-trust-projects/) informa projeto de digitalização iniciado em 2009. Seu [catálogo do CD *Today's Astrologer* vols. 41–50, SKU A4842](https://astrologers.com/product/todays-astrologer-vols-41-50/) afirma conter os números completos de 1979–1988, intervalo que abrange XLV/10 de outubro de 1983. **Foi consultada a descrição comercial, não o conteúdo nem o arquivo digital**. A página exige aquisição; não foi feita compra ou contato.
- **Acervo físico listado independentemente:** o [inventário de periódicos Astrolearn](https://www.astrolearn.com/astrology-bibliography/todays-astrologer/) declara posse dos números do volume 45 de 1983, de XLV/1 (14/01/1983) até XLV/12 (04/12/1983). O enunciado de cobertura inclui XLV/10, mas **nenhuma página do exemplar foi examinada**, e não há comprovação de acesso digital aberto.

Esses dois registros são **vias de obtenção**, não duas leituras nem duas confirmações dos resultados de Nolle. O próximo passo é procurar cópia aberta legitimamente acessível; eventual aquisição ou consulta a terceiros exige decisão específica do mantenedor. Se um original for obtido, registrar edição/número/página e proveniência do arquivo antes de extrair entradas, saídas ou números do DR-70.

## Próxima prova discriminante

1. Recuperar legalmente o artigo original de Richard Nolle, parte 6, *Today's Astrologer* **XLV/10 (outubro/1983), p. 9**; comparar com parte 5, XLV/9 (setembro/1983), p. 14. Consultar as trilhas de custódia já catalogadas em [F11](sources.md), sem compra/contato sem aprovação.
2. Transcrever literalmente qualquer identificação do produto “ACS”, configuração do DR-70, teclas, entradas, saídas e erros, com imagem/página/linha, direitos e hash **dos bytes efetivamente obtidos**. Sem isso, **não** atribuir comparador, CPU, ROM ou fidelidade.
3. Se houver pares observados, alimentar primeiro o [corpus de fidelidade](fidelity-corpus.md) como `partial`; só promover a `replayable` depois de demonstrar sequência de teclas e saída autêntica no mesmo evento, com revisão independente. Identificadores de reportagem e biografia **não** substituem evidência visual da operação.

**Estado ao fechar esta nota:** 0 ROMs, 0 programas ACS identificados no teste de Nolle, 0 pares DR-70 entrada→saída autenticados nesta pesquisa. Nenhum software foi baixado ou executado; nenhum contato, compra ou custo. Esta nota não afirma ausência desses objetos fora das fontes consultadas.
