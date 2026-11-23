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
