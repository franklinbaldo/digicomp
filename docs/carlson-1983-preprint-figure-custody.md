---
type: Documento
title: "Carlson 1983: figura 1 no preprint LBL-20480"
description: "Inspecao visual anterior a Nature e contraprovas da atribuicao ao software do DR-70."
timestamp: 2026-11-20T22:00:00-04:00
estado: provisorio
---

# Figura de Carlson anterior a Nature (1985): fonte primaria de 1983

**🦦 Lontra R121 · [Digicomp #30](https://github.com/franklinbaldo/digicomp/issues/30), #2 e #3.** Escopo **O0/O3** da investigacao output-first: historia material da figura, nao reverse engineering de ROM.

## Localizadores e custodia

1. **Preprint institucional:** Shawn Carlson, *Double-Blind Test of Astrology*, **LBL-20480**, Lawrence Berkeley Laboratory, capa datada **abril/1983**, submetido a Nature. [Registro UC/eScholarship](https://escholarship.org/uc/item/0b40b045); [PDF institucional](https://escholarship.org/content/qt0b40b045/qt0b40b045_noSplash_aa3bf76a6b22470b8665af02a57d27ae.pdf).
2. **Figura 1:** folha PDF **27** (indice zero 26), pagina impressa **-24-**, inspecionada **visualmente** em 20/11/2026. O indice de figuras, pagina impressa **-21-**, descreve um mapa natal derivado por computador, nao uma impressao nativa de exemplar identificado.
3. **Atribuicao instrumental:** pagina impressa **-5-** diz que Michael Caveney e Chris Nelson fizeram os mapas do experimento em **Digicomp DR 70**, com conferencia amostral manual. A frase **nao declara** que a figura 1 reproduz literalmente bytes emitidos por firmware ou impressora do DR-70.
4. **Artigo posterior:** [Nature 318, 419–425](https://doi.org/10.1038/318419a0), recebido 11/04/1983, aceito 14/10/1985 e publicado 05/12/1985. A figura correspondente **ja estava no preprint de abril/1983**, portanto sua origem nao pode ser atribuida exclusivamente a diagramacao da edicao de 1985.

**Cadeia de custodia:** PDF aberto no visualizador da fonte publica; a pagina foi examinada em imagem, nao apenas por OCR. O GET direto em Ifro retornou **HTTP 403**. Arquivo integral **nao** depositado localmente; tamanho, SHA-256 e identidade dos bytes = **NOT_OBTAINED**. Nao importar imagem ou PDF protegido para Git.

## Inventario visual da figura 1 (1983)

| ID | Regiao | Observacao visual | Limite |
| --- | --- | --- | --- |
| LBL83-A | Superior esquerda | Diagrama retangular, dados astrologicos distribuidos nas bordas | Nao evidencia impressora nativa |
| LBL83-B | Inferior esquerda | Cabecalho aparente C1 NATAL TROP P LONG KOCH ZOO/200 e campos H01–H12 | Z versus 2 e O versus 0 **ambiguos** na copia |
| LBL83-C | Central inferior | Segundo cabecalho aparente C1 SEC ... KOCH ... | Repeticao na mesma figura nao e nova sessao |
| LBL83-D | Direita | Tabela triangular de aspectos e outro cabecalho aparente C1 NATAL | Nao atribuir renderer a CPU ou firmware |
| LBL83-E | Centro do diagrama | Anotacao **aparentemente manuscrita** 22987 | Nao identificar como numero de serie |
| LBL83-F | Rodape direito | Identificador grafico XBL 832-8314 | Nao inferir autor, data de operacao ou impressora |

Os fragmentos sao **leituras candidatas**, nao transcricao byte-a-byte. O texto extraido do PDF confunde caracteres, como Cl ~TAL, ZOO e HIS. Nao promover automaticamente o token 200, o significado de KOCH ou H01–H12 a comportamento instrumental. A anotacao aparente pode ser posterior ao calculo; nao prova que todo o layout tenha sido composto fora do aparelho.

## Confronto visual entre as edicoes de 1983 e 1985

Confronto por **inspecao visual de paginas**, em 20/11/2026: na [figura 1 do preprint de 1983, p. -24-](https://escholarship.org/content/qt0b40b045/qt0b40b045_noSplash_aa3bf76a6b22470b8665af02a57d27ae.pdf#page=27), veem-se os digitos **aparentemente manuscritos** `22987` no centro do diagrama esquerdo e a marca `XBL 832-8314` no rodape direito. Na [figura 1 publicada em Nature, p. 419](https://muller.lbl.gov/papers/Astrology-Carlson.pdf#page=1), **nenhum desses dois elementos aparece**; o arranjo geral dos paineis com glifos semelhantes permanece. Esta e uma comparacao visual, **nao** uma comparacao pixel a pixel de arquivos autenticados.

O contraste rejeita somente a tese de que a pagina de 1985 reproduz a pagina de 1983 **integralmente e sem edicao**. Nao identifica quem inseriu ou retirou marcas, nem se houve recorte, recomposicao ou outros tratamentos. **Nao** comprova nem exclui impressao nativa do DR-70, autoria do desenho, hardware, firmware ou veracidade instrumental dos calculos. As duas edicoes nao sao duas observacoes independentes. O codigo `XBL 832-8314` e pista para busca de arte de producao original, nao atribuicao de equipamento.

## Controle independente da marca XBL (O0, busca dirigida 21/11/2026)

A marca `XBL 832-8314` visivel na figura de Carlson tem um **controle contextual de 1983**, mas ainda nao um registro de catalogo individual. Em outro trabalho do Lawrence Berkeley Laboratory, **Arion J. Hunt, *Light Scattering Studies of Silica Aerogels*, LBL-15756, fevereiro de 1983**, a [figura 1, pagina impressa -9-, folha PDF 13](https://escholarship.org/content/qt4c68q9m3/qt4c68q9m3.pdf#page=13) traz `XBL 832-1229` sob um **desenho esquematico** de aerogel. A mesma obra atribui `XBL 832-1231` a figura 3 e `XBL 832-1230` a figura 4 (pp. impressas -11- e -12-). O conteudo independente do DR-70 mostra que o padrao `XBL 832-...` circulava como marca de **figuras em publicacoes** do laboratorio e nao pode, isoladamente, identificar hardware ou saida de impressora do DR-70. [Fac-simile institucional LBL-15756](https://escholarship.org/uc/item/4c68q9m3).

A [pagina institucional do Berkeley Lab Photo Archive](https://it.lbl.gov/service/records/photo-archive/) aponta para [photos.lbl.gov](https://photos.lbl.gov/), acervo publico de imagens; **nao equivale a ficha encontrada da arte XBL 832-8314**. Na busca publica delimitada desta rodada pelo codigo integral `"XBL 832-8314"`, variantes `"832-8314"`, `site:photos.lbl.gov` e `site:escholarship.org`, nao apareceu ficha independente da figura nem original de reproducao vinculado ao codigo. A pagina de entrada de photos.lbl.gov exigia consentimento de cookies, sem indice pesquisavel acessivel nesta via. Resultado: `NOT_FOUND_IN_QUERIED_PUBLIC_INDEXES`, **nao** prova de inexistencia no acervo.

**Interpretacoes abertas:** (A) desenho de producao institucional a partir de impressao nativa; (B) desenho/colagem a partir de calculos do DR-70 formatados externamente; (C) diagramacao a partir de varias fontes. O uso comparativo da familia `XBL` **nao resolve A/B/C** nem autentica uma saida, mas orienta a procura por ficha original da arte ou registro de preparacao no laboratorio. Nenhum novo golden/ROM, nenhum dado pessoal.

## Material de interpretacao enviado aos astrologos (O0, nova pista)

O mesmo [preprint LBL-20480 de abril/1983](https://escholarship.org/content/qt0b40b045/qt0b40b045_noSplash_aa3bf76a6b22470b8665af02a57d27ae.pdf#page=17), **pagina impressa -13- / folha PDF 17 (indice zero 16)**, foi conferido em imagem. Na secao *Materials for the astrologers*, Carlson informa que o **primeiro envio** aos participantes profissionais continha uma carta **explicando os simbolos usados nos mapas natais construidos por computador**, alem de modelo de interpretacao e folhas com cabecalhos. O texto afirma que os mapas traziam codigos dos participantes; nao apresenta a carta, nem a legenda integral, nem informa quem diagramou cada painel da figura 1.

**Consequencia para a custodia da figura:** houve ao menos um **documento explicativo separado do mapa**, mencionado pelo proprio autor. Uma copia historica da carta com legenda (sem dados pessoais dos participantes) seria alvo O0 mais discriminante que recontar tokens do mesmo fac-simile: permitiria verificar se os glifos `H01`–`H12`, `C1 SEC`, `ORB` e `KOCH` eram descritos como convencoes do formulario entregue aos astrologos, como saida do aparelho ou se sua origem continuava indeterminada. **A existencia declarada da carta nao demonstra que ela sobreviveu nem que foi gerada pelo DR-70.**

**Hipoteses rivais:** (A) legenda explica representacao nativa do DR-70; (B) legenda explica uma formatacao montada depois dos calculos; (C) documento so traduz simbolos astrologicos sem identificar o formatador. **Contraprova minima:** localizar copia licita da carta/folha de instrucoes datada e vinculada a esse experimento; cotejar glifos e termos com a fig. 1 sem usar nomes ou dados natais dos sujeitos. **Estado:** `DOCUMENTED_LETTER_MENTION`, conteudo da carta `NOT_OBTAINED`, origem da tipografia `NOT_RUN_NO_ORIGINAL`. Nada acrescentar ao corpus de golden outputs.

## Hipoteses rivais e falsificacao

| Hipotese | Predicao discriminante | Resultado |
| --- | --- | --- |
| **A: layout originalmente nativo** do DR-70/periferico, depois fotografado/anotado | Papel comprovado do mesmo modelo com impressora, serie, comandos e layout identico | **NOT_RUN_NO_GOLDEN** |
| **B: formatacao de terceiro**, mesmo que calculos tenham sido feitos no DR-70 | Arte de producao, manual de impressora, fonte/renderizador intermediario | **NOT_RUN_NO_GOLDEN** |
| **C: figura produzida somente na diagramacao Nature 1985** | Nenhuma versao anterior teria mesma estrutura e cabecalhos | **REFUTADA neste sentido restrito**: a figura correspondente esta no preprint de 1983 |

**Nao independentes:** preprint 1983 e artigo 1985 sao **versoes da mesma obra**, nao duas impressoes instrumentais nem testemunhos independentes. O novo achado melhora a cronologia da **imagem**, nao a prova do software. Comparacao pixel a pixel 1983–1985 **NOT_RUN** (copia integral Nature nao custodiada).

**Proximo teste:** obter o PDF institucional integral com hash, confrontar as duas figuras visualmente e encontrar um printout ou fotografia autenticados de **DR-70 identificado**, com input e comandos. Ate la, **nao acrescentar observacoes** a data/fidelity/observations.json nem executar REA binaria.

**Limites:** nao foram encontrados ROM, CPU, software DR-70, serie do aparelho de Carlson nem valores repetiveis com input. Sem compra, contato, execucao historica ou custo. Relacionado ao [ledger de ocorrencias 1985](carlson-1985-fig1-occurrences.md) e ao [plano de testes](reconstruction-gates.md).
