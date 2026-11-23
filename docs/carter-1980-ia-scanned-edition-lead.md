---
type: Documento
title: "Rael/Rudhyar 1980: exemplar digitalizado identificado, páginas não inspecionadas"
description: "Localiza o exemplar digitalizado de Astrological Aspects no Internet Archive e delimita a custódia, o acesso restrito e a primeira comparação angular histórica ainda pendente."
timestamp: 2026-11-22T21:06:00-04:00
estado: provisorio
---

# Astrological Aspects (1980): pista de fac-símile identificável

**Estado em 22/11/2026: ITEM DIGITALIZADO IDENTIFICADO / PÁGINAS INTERNAS NÃO INSPECIONADAS.** Esta ficha registra uma rota documental para avançar a [#130](https://github.com/franklinbaldo/digicomp/issues/130). Ela **não** introduz uma observação instrumental do DR-70, um golden, uma ROM, nem novos graus de Jimmy Carter.

## Identificação verificável

- **Internet Archive:** [astrologicalaspe0000rael](https://archive.org/details/astrologicalaspe0000rael). Página de catálogo consultada em 22/11/2026; título *Astrological aspects: a process-oriented approach*; autor principal catalogado Leyla Rael; coautor Dane Rudhyar; publicação registrada como **1980**, Aurora Press, Santa Fe (N.M.); extensão **iii, 244 páginas**; ISBN **0943358000 / 9780943358000**; item ARK **ark:/13960/s21c9njswqs**. O item indica digitalização, OCR, câmera, identificador persistente e coleções `internetarchivebooks`, `printdisabled` e `inlibrary`.
- **Condição de acesso observada:** `Access-restricted-item: true` no próprio catálogo. O botão de empréstimo em [Open Library, edição OL8445182M](https://openlibrary.org/books/OL8445182M/Astrological_Aspects) direcionou o visitante não autenticado à página de login. **Não foi realizado empréstimo, leitura interna, inspeção de imagens ou extração OCR da edição**; a presença de uma digitalização não prova livre acesso nem que a figura de Carter esteja legível.
- **Referência bibliográfica independente:** [Finna, Varastokirjasto, vaari.1172270](https://www.finna.fi/Record/vaari.1172270), registra Aurora Press 1980, **244 páginas**, ISBN 0-943358-00-0. O catálogo confirma a descrição bibliográfica, **não** a identidade física entre o exemplar finlandês e a cópia digitalizada pelo Internet Archive.
- **Limite editorial:** a [transcrição secundária já usada no experimento](https://www.scribd.com/document/633437269/Dane-Rudhyar-Leyla-Rael-Astrological-Aspects-A-Process-Oriented-Approach-Rudhyar-Series-Aurora-Press-Inc-2018-pdf) refere uma circulação identificada como 2018. **Não assumir** que paginação, layout, figuras ou revisões são idênticos à edição catalogada de 1980.

## Próximo procedimento e critério de aceite

1. Mediante acesso lícito a uma cópia, inspecionar **folha de rosto, créditos editoriais e a página física** que contenha eventual mapa ou lista de posições de Carter. Registrar edição, numeração *impressa* e número da imagem digitalizada separadamente; não inferir página a partir de índice OCR ou de outra edição.
2. Transcrever somente os campos numéricos **efetivamente legíveis**: corpo/ângulo/cúspide, signos, graus, minutos, segundos se impressos, latitude/longitude e horário tal como grafados. Marcar algarismos ambíguos como `UNREADABLE`, sem completar via cálculo moderno.
3. Construir um registro documental com fonte, página, transcrição literal, interpretação, família editorial, resolução impressa e grau de atribuição. Comparar com o motor moderno **somente depois** de fixar os valores históricos, registrando inclusive divergências e hipóteses rivais. Manter `data/fidelity/observations.json` exclusivo para golden instrumental.
4. Verificar, antes de publicar imagens ou fac-símiles, as permissões de reprodução; preferir link/identificador persistente e transcrição mínima acompanhada de citação.

**Resultado desta rodada:** a rota de recuperação mudou de referências bibliográficas genéricas para um **item digitalizado preciso e rastreável**, mas a **comparação angular histórica permanece NOT_RUN**. O empréstimo autenticado não foi testado; não atribuir valores impressos ou qualidade da digitalização sem abrir as páginas.


## R175: espelho de texto integral com créditos de produção (não fac-símile)

**Segunda rota, localizada em 22/11/2026:** [PDF textual hospedado pelo Tibetan Buddhist Encyclopedia](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf), cujo conteúdo extraível se apresenta como *Astrological Aspects*, associado à marca editorial **Mindfire**. O texto contém as seções `PREFACE`, `APPENDIX ONE — EXAMPLE HOROSCOPES` e `Suggested Reading by Subject`. **Não foi autenticada a proveniência dos bytes ou sua correspondência página a página com Aurora Press 1980.** O espelho não é uma segunda observação independente; é outra circulação textual da mesma obra.

**Achado de cadeia de produção:** no prefácio atribuído a Dane Rudhyar e datado de **23/03/1979**, a obra agradece a **Nicki Michaels** por aferir a exatidão dos mapas do apêndice mediante cálculo em seu computador e a **Tony Milner** pela caligrafia dos mapas; também declara Campanus como sistema de casas. Na seção posterior ao rol de **20 personagens** do Apêndice I, o texto atribui o **recálculo dos mapas a um computador astrológico DR-70 com cúspides Campanus** e, para Jimmy Carter, dá os dados literais `Oct. 1, 1924`, `32N02`, `84W24`, `13:00 U.T.`.

**Distinção de origem a preservar:** a menção ao cálculo de Nicki Michaels e a menção ao DR-70 são **duas etapas/editorias descritas na mesma família documental**, não evidência suficiente de dois motores físicos independentes. Não se sabe se o computador de Michaels era o próprio DR-70 nem se o mapa caligrafado transcreveu fielmente a saída do aparelho. Assim, mesmo números de uma futura figura requerem classe `EDITORIAL_HISTORICAL` até haver atribuição instrumental externa.

**Teste negativo de acesso visual:** o extrator textual revelou os nomes no apêndice, mas **não trouxe graus/cúspides de mapas**. A tentativa de renderização visual do PDF hospedado falhou por redirecionamento do host; o arquivo não foi baixado, as figuras não foram inspecionadas e **não se pode afirmar que o PDF as contenha ou as omita**. Esta rota serve para conferir créditos e localizadores textuais, não para transcrição angular. É vedado completar ângulos pela referência moderna ou reproduzir o PDF integral no repositório.

**Próximo passo falsificável:** ao obter acesso lícito a uma imagem identificada do apêndice de 1980, registrar folha de rosto, número da página impressa e índice da digitalização; testar presença/legibilidade de figuras, transcrever graus de Carter às cegas e somente então comparar com as referências modernas. Consultar também a seção do prefácio na edição física para confirmar autoria, nome próprio e eventual revisão editorial. Até lá: `HISTORICAL_ANGULAR_NOT_READ`, `DR70_GOLDEN=0`, `ROM=0`.


## R176: fotografia de folha de rosto de exemplar físico anunciado como 1980

**Nova rota visual observada em 22/11/2026:** [Watkins Books, anúncio de exemplar usado de *Astrological Aspects*](https://shop.watkinsbooks.com/products/astrological-aspects-by-leyla-rael-dane-rudhyar), descrito pelo livreiro como **Aurora Press, New York, 1980**, inclui [fotografia direta das páginas abertas](https://shop.watkinsbooks.com/cdn/shop/files/IMG_3603.jpg?v=1741361366). Na fotografia, a **folha de rosto visível** apresenta o título, a autoria **Leyla Rael / Dane Rudhyar**, a linha `Artwork by Tony Milner` e o endereço editorial impresso **`AURORA PRESS / 205 3rd Ave. 2A / N.Y., N.Y. 10003`**; na página oposta aparece um retrato com crédito fotográfico a Tony Milner. Essa é uma **imagem de página física**, diferentemente do espelho textual citado em R175. O nome de Nicki Michaels **não aparece nessa fotografia da folha de rosto**, o que não demonstra ausência em prefácio ou créditos.

**Divergência descritiva importante:** o anúncio de livreiro associa o exemplar a **New York, 1980**, e a página fotografada traz endereço em Nova York. O catálogo do exemplar digitalizado `astrologicalaspe0000rael` no Internet Archive registra **Santa Fe, N.M., 1980**. As duas fontes não demonstram se houve reimpressão, variantes de folha de rosto, mudança de sede editorial, ou simplesmente normalização bibliográfica distinta. A fotografia **não exibe folha de copyright, ano de impressão ou mapas do Apêndice I**; a data 1980 é **atribuição do vendedor**, não data lida na imagem. Não atribuir essa mesma folha de rosto ao exemplar do IA sem comparar suas páginas.

**Teste negativo explícito:** a fotografia não mostra o mapa de Jimmy Carter, nem uma saída do DR-70, nem número angular/cúspide. Resultado `TITLE_PAGE_PHOTO_READ` / `COPYRIGHT_PAGE_NOT_READ` / `CARTER_CHART_NOT_READ`. Como próximo passo, conferir os créditos editoriais, a página de copyright e uma figura do Apêndice I na **mesma** cópia física/digitalizada. A fotografia e a transcrição secundária continuam pertencendo à **mesma obra**, não duas medições astronômicas independentes. Reproduzir links e transcrições pontuais, não incorporar a fotografia comercial ao Git.


## R177 · 23/11/2026: localização de uma carta na tradução francesa (imagem não inspecionada)

Foi identificado um **localizador de página mais específico**, em [*Les Aspects astrologiques*, cópia catalogada no Scribd como documento 978057391](https://fr.scribd.com/document/978057391/Les-Aspects-Astrologiques-Dane-Rudhyar-Leyla-Rael-Z-Library). A página do documento declara **382 páginas** e apresenta OCR de uma versão francesa das mesmas autoras. Na folha inicial transcrita aparecem **© 1980 Leyla Rael & Dane Rudhyar**, **© Éditions du Rocher, 1982 pela tradução francesa** e ISBN **2-268-02638-8**. O copyright de tradução **não autentica a data de impressão do exemplar digitalizado**; também não identifica o exemplar de Aurora Press fotografado pela Watkins ou o do Internet Archive.

**Alvo preciso:** no texto extraído do apêndice, a entrada **Jimmy Carter** está imediatamente antes do numeral impresso **362**. A legenda OCR registra **1er oct. 1924; 32°02 N; 84°24 W; 13 h 00 T.U.** A entrada **Andrew Carnegie** precede o numeral **361**, e **Paul Case** sucede Carter antes de **363**. Logo, o **alvo de inspeção é a página impressa 362 da tradução francesa**, mas o número da imagem digital/PDF ainda não foi confirmado. Não presumir que p. 362 corresponde à paginação da edição inglesa de 1980.

**Limite visual e científico:** esse conteúdo veio da **camada textual pública da página Scribd**, não de leitura visual dos símbolos e graus impressos na carta. A sequência sugere que o apêndice possui páginas dedicadas a mapas, mas **não confirma se a imagem da carta de Carter existe, está íntegra ou é legível**. Nenhum grau de planeta/cúspide foi recuperado. A tradução pertence à **mesma família editorial Rael/Rudhyar**, não é segunda medição independente do DR-70. Estados: `FRENCH_APPENDIX_CAPTION_OCR_READ`, `CARTER_CHART_IMAGE_NOT_READ`, `HISTORICAL_ANGULAR_NOT_READ`, `DR70_GOLDEN=0`.

**Próxima prova:** inspecionar licitamente **a imagem da página impressa 362 do mesmo exemplar**, registrar créditos e página de copyright em fac-símile, associar posição da imagem à paginação e transcrever **às cegas** cada DMS realmente visível. OCR, legenda ou cálculo moderno não servem para preencher números ausentes. Não descarregar nem republicar o livro integral ou imagens protegidas no Git.

## R178 · 23/11/2026: contrato executável de transcrição cega, sem novos graus

O localizador francês da R177 agora tem um registro JSON **sem ângulos** em [`data/documentary/carter-french-1982-caption-locator.json`](../data/documentary/carter-french-1982-caption-locator.json). O estado efetivo é `INDEXED_CAPTION_ONLY`: número impresso **362 como candidato obtido da camada OCR**, página digital ainda desconhecida, nenhum fac-símile inspecionado, nenhuma latitude/longitude angular de carta transcrita. O registro não deve ser tratado como fotografia, impressão DR-70 nem segunda família editorial.

A verificação `python -S -B -m scripts.carter_historical_intake` rejeita valores angulares enquanto o registro estiver em estado OCR, impede promoção para golden instrumental e recusa estados de inspeção sem identidade da página, índice digital, digest SHA-256 declarado e registro horário UTC. Um futuro `INSPECTED_TRANSCRIBED` pode armazenar **somente literal visível e identificador de campo**, mas continua com `NOT_RUN_REQUIRES_BLIND_TRANSCRIPTION_REVIEW`; **não calcula longitude, resíduo nem proclama autenticidade da imagem**. A conferência de um digest declarado contra os bytes da fonte, a análise de direitos e uma segunda leitura cega seguem trabalhos humanos independentes. Os exemplos de inspeção nos testes são **inteiramente sintéticos**, sem pretensão documental.

Os testes negativos e a execução real do localizador fazem parte do workflow público Modern Campanus; nenhum arquivo de terceiros foi baixado ou anexado, `data/fidelity/observations.json` não foi alterado. Esta etapa prepara a recepção de uma figura efetivamente vista, **não é a comparação angular histórica prometida**.


## R179 · 23/11/2026: ISBN distingue copyright da tradução e impressão catalogada

**Nova comparação com duas fichas primárias de catálogo da Bibliothèque nationale de France (BnF):**

- [BnF FRBNF36602183, edição francesa de 1982](https://catalogue.bnf.fr/ark:/12148/cb36602183h): *Les Aspects astrologiques*, tradução por Marief Cavaignac, Éditions du Rocher, coleção **Gnose**, **378 páginas ilustradas**, **ISBN 2-268-00163-6**; impressão atribuída a C. Descamps, Condé-sur-l'Escaut.
- [BnF FRBNF36695140, edição francesa de 1997](https://catalogue.bnf.fr/ark:/12148/cb36695140t): mesmo título e tradução, Éditions du Rocher, coleção **Astrologie**, **378 páginas ilustradas**, **ISBN 2-268-02638-8**; impressão atribuída a BCI, Saint-Amand.

A [camada de texto disponibilizada no Scribd, documento 978057391](https://fr.scribd.com/document/978057391/Les-Aspects-Astrologiques-Dane-Rudhyar-Leyla-Rael-Z-Library), registra simultaneamente **© 1982 pela tradução francesa** e **ISBN 2 268 02638 8**. O **ISBN indexado corresponde à ficha BnF de 1997, não à ficha BnF de 1982**. Portanto, é incorreto inferir a *edição impressa de 1982* a partir do copyright de tradução. A coincidência de ISBN sugere uma linhagem editorial compatível com a edição catalogada em 1997, **mas não autentica data, estado, integridade ou identidade do arquivo Scribd**. A apresentação de **382 páginas digitais** na plataforma não pode ser equiparada automaticamente às **378 páginas impressas** das fichas BnF.

Para preservar a distinção no dataset, `data/documentary/carter-french-1982-caption-locator.json` fixa o ISBN OCR `2-268-02638-8` e a classificação limitada `BNF_1997_ISBN_MATCH_NOT_SCAN_AUTHENTICATION`. O validador recusa alterações que o transformem no ISBN de 1982 ou numa declaração de impressão autenticada, com teste de regressão. Esses guardas são de **consistência documental**, não uma auditoria independente das imagens.

**Consequência para a carta de Carter:** a página **362** segue apenas *candidata por OCR* na circulação francesa; não se presumem a página da digitalização, a edição material, nem os graus impressos. A leitura visual do mapa, folha de copyright do próprio exemplar e cotejo cego continuam **NOT_RUN**. **Zero resíduos angulares históricos, zero golden instrumental DR-70 e zero ROM**. O trabalho em `#148` não atualiza `data/fidelity/observations.json` nem publica material de terceiros.
