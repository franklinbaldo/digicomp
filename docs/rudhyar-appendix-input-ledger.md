---
type: Documento
title: "Raël/Rudhyar: dados publicados em seis cartas do Apêndice I"
description: "Ledger O0/O1 de dados biográficos textuais associados a mapas atribuídos ao DR-70, preservando anomalias e sem criar golden instrumental."
timestamp: 2026-11-21T10:15:00-04:00
estado: provisorio
---

# Seis entradas declaradas para mapas de Raël/Rudhyar

## Fonte, custódia e classe da evidência

**🦇 Morcego R145 · leitura de texto HTML em 21/11/2026.** A edição de *Astrological Aspects: A Process-Oriented Approach*, de Leyla Raël e Dane Rudhyar (copyright 1980), declara no **Apêndice I, "Example Horoscopes"**, que os exemplos foram recalculados com cúspides Campanus em um computador astrológico DR-70. O prefácio de 23/03/1979 agradece a Nicki Michaels pela conferência dos mapas no computador e a Tony Milner pela caligrafia dos desenhos. **Nenhuma dessas declarações atribui a tipografia dos gráficos a uma impressora DR-70.**

Fonte textual consultada: [Scribd, transcrição do livro, seção Appendix I](https://www.scribd.com/document/633437269/Dane-Rudhyar-Leyla-Rael-Astrological-Aspects-A-Process-Oriented-Approach-Rudhyar-Series-Aurora-Press-Inc-2018-pdf), trecho situado aproximadamente nas linhas **6701–6746** do HTML indexado. [PDF de referência](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf) aparece na busca textual, mas não foi possível conferir a imagem da página nesta leitura. Não houve download, hash, screenshot ou inspeção da página impressa; as linhas acima são posições da transcrição HTML, **não paginação editorial**. Cópias textuais do mesmo livro não são fontes independentes.

A lista abaixo é uma **extração curta de fatos de nascimento declarados no livro**, não de teclas ou dados digitados na máquina. O autor diz que estes seis casos são exceções à origem usual (*The Circle Book of Charts*, revisão 1979). Mantive coordenadas e relógios **em sua forma textual**, inclusive anomalias, sem converter fuso, data ou local. O uso de maiúsculas/minúsculas em alguns campos pode refletir o extrator.

## Valores publicados no texto de referência (não certificados no fac-símile)

| Pessoa citada | Data textual | Coordenadas textuais | UT textual | Observação |
| --- | --- | --- | --- | --- |
| Edmund G. Brown Jr. | April 7, 1938 | `43N03 118W15` | `20:00 U.T.` | Latitude requer cotejo visual; documento atribui retificação a A. L. Milner |
| Jimmy Carter | Oct. 1, 1924 | `32N02 84W24` | `13:00 U.T.` | Já usado como pista em [Carter](carter-book-qualitative-houses.md); não duplicar sessão |
| Werner Erhard | Sept. 5, 1935 | `39N57 75W10` | `27:25 U.T.` | Hora maior que 23 no HTML; **não** inferir dia seguinte nem emendar OCR |
| Franklin D. Roosevelt | Jan. 30, 1882 | `41N48 73W56` | `25:16 U.T.` | Hora maior que 23 no HTML; **não** corrigir silenciosamente |
| Albert Schweitzer | Jan. 14, 1875 | `48N45 8E00` | `6:22 U.T.` | Grafia do leste/zeros ainda depende do fac-símile |
| Alan Watts | Jan. 6, 1915 | `51N25 0W00` | `6:20 U.T.` | Sem confirmação de formato de entrada do DR-70 |

**Alerta editorial:** no [índice textual alternativo](https://pdfcoffee.com/astrological-aspects-pdf-free.html) aparecem variantes como `75WlO` (letra l / algarismo 1) e `8Eoo` (letras o / zeros), enquanto o Scribd indexa `75W10` e `8E00`. É possível que até a aparente precisão da transcrição seja produzida pelo pipeline de cópia/OCR. Nenhuma grafia conflitante deve ser promovida como literal da impressora histórica.

## Próximos testes que esses registros podem orientar

1. **Contrato de ingestão:** uma rotina que espera hora civil de 00–23 deve rejeitar `27:25` e `25:16` de forma explícita, ou classificá-los como `AMBIGUOUS_EXTENDED_UT`; jamais ajustar para datas calculadas sem observação que justifique. Testes com esses literais verificariam o **nosso parser de fontes**, não firmware histórico.
2. **Distinção de canal:** encontrar o fac-símile de cada gráfico, conferir diretamente a hora/coordenadas impressas e os valores astrológicos do desenho, registrar revisão dupla e separar o que foi **calculado**, **conferido** e **redesenhado** por pessoas diferentes. Ainda será uma saída *editorialmente apresentada*, não saída nativa certificada.
3. **Hipóteses matemáticas:** somente depois de confirmar os desenhos e seus campos, comparar cenários Campanus alternativos com o Rust; não testar a saída sintética contra uma versão normalizada da própria entrada e denominar isso fidelidade. Reservar famílias independentes **antes** de calibrar.
4. **Corpus:** não acrescentar registros a `data/fidelity/observations.json`; permanece `observations: []`. Estes seis casos integram a **mesma família documental** dos vinte mapas já catalogados em [plano de holdout](output-catalog-holdout-plan.md). Não são seis sessões instrumentais autenticadas nem seis holdouts.

**Resultado R145:** seis localizadores de dados textuais com anomalias explícitas, sem um único output instrumental recuperado. Estado para fidelidade: `NOT_RUN_NO_GOLDEN`; estado para revisão visual: `FIGURE_NOT_READ`.

## Controle cruzado com a tradução francesa (1982, leitura textual)

**🐝 Abelha · 21/11/2026.** Localizei outra edição, [*Les Aspects astrologiques*, Éditions du Rocher](https://fr.scribd.com/document/978057391/Les-Aspects-Astrologiques-Dane-Rudhyar-Leyla-Rael-Z-Library). A transcrição HTML disponível indica tradução por Marie Cavaignac, copyright original 1980 e copyright francês **1982**; o Scribd anuncia 382 páginas. É **uma tradução derivada**, não testemunha instrumental independente dos cálculos e nem o fac-símile inglês de 1980. **FIGURE_NOT_READ**: só o texto indexado foi acessível; não conferi visualmente qualquer mapa, página impressa, edição física ou hash dos bytes.

Essa versão oferece localizadores editoriais *provisórios* para uma futura conferência visual: abertura do apêndice nas pp. **356–357**, quadro atribuído a **Jimmy Carter na p. 362**, Jerry Brown na p. **360**, Franklin D. Roosevelt na p. **374** e Alan Watts na p. **377** (números mostrados no texto extraído, ainda sem confronto com a imagem). Na introdução do apêndice, a tradução também atribui os exemplos a recálculos no **DR-70/Campanus**; isto não prova que os quadros sejam impressão nativa.

Três diferenças **dentro da transcrição francesa**, entre introdução e legendas dos próprios mapas, desaconselham tratar as entradas de cima como literais canônicos:

| Campo | Introdução francesa (pp. 356–357, OCR) | Legenda francesa (página indicada, OCR) | Estado |
| --- | --- | --- | --- |
| Jerry/Edmund G. Brown Jr., latitude | `43°03N` | p. 360: `34°03N` | **Conflito 43 ↔ 34**, confirmar nas imagens |
| Franklin D. Roosevelt, hora UT | `25h16` | p. 374: `25h15` | **Conflito 16 ↔ 15 minutos**, não normalizar |
| Alan Watts, data | **6 jan. 1915** | p. 377: **5 jan. 1915** | **Conflito de dia**, não escolher por conveniência |

Os números podem refletir erro editorial, variação entre etapas de composição ou OCR. A transcrição inglesa secundária registra **43N03, 25:16 e 6 jan.**, isto é, concorda com a **introdução** francesa e não resolve o conflito com as **legendas**. **Não** alterar `data/chart-input-candidates/rael-rudhyar-1980.json`, não inferir teclas, não completar valores angulares e não adicionar golden. Próximo teste: verificar, na mesma cópia física autorizada, página de créditos, introdução e as três figuras (360, 374, 377), começando por Carter p. 362; atribuir revisão dupla a qualquer transcrição de glifos.
