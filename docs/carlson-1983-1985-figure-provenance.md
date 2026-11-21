---
type: Documento
title: "Carlson 1983 versus Nature 1985: cadeia editorial da figura 1"
description: "Cotejo visual de duas testemunhas documentais de um mapa calculado com DR-70, sem autenticar a impressao nativa."
timestamp: 2026-11-20T21:50:00-04:00
estado: provisorio
---

# Duas testemunhas da figura 1: preprint LBL (1983) e Nature (1985)

🦦 Lontra · [Digicomp #30](https://github.com/franklinbaldo/digicomp/issues/30) · O0 / origem do formato de saída. Resultado: **a cadeia editorial tem ao menos duas representações distintas da mesma figura; nenhuma autentica o fluxo bruto de impressão do DR-70**.

## Testemunhas efetivamente inspecionadas

| ID | Documento | Localizador visual | Natureza e limite |
| --- | --- | --- | --- |
| CARLSON-LBL-1983 | Shawn Carlson, *Double-Blind Test of Astrology*, **LBL-20480**, preprint datado **abril de 1983**, Lawrence Berkeley Laboratory; [catálogo da University of California](https://escholarship.org/uc/item/0b40b045), [PDF](https://escholarship.org/content/qt0b40b045/qt0b40b045.pdf) | **Folha PDF 28** (índice zero **27**), página impressa **-24-**, **Figure 1**; texto do método na página impressa **-5-** | Preprint institucional digitalizado; inspeção visual da imagem publicada, mas **sem download dos bytes** ou SHA-256 local nesta rodada |
| CARLSON-NATURE-1985 | Shawn Carlson, *A double-blind test of astrology*, *Nature* **318**, 419–425, **05/12/1985**, DOI [10.1038/318419a0](https://doi.org/10.1038/318419a0); [PDF de reprodução](https://static1.squarespace.com/static/54694fa6e4b0eaec4530f99d/t/5f2acc1a7bb54677bf7fed40/1596640291173/Double%2Bblind%2Btest%2Bof%2Bastrology-Carlson.pdf) | **Folha PDF 1** (índice zero **0**), página impressa **419**, **Fig. 1**; método na página impressa **420** | Reprodução da página publicada; inspeção visual. A hospedagem da cópia é de terceiro, o **DOI identifica a publicação**; sem hash dos bytes nesta rodada |

**Dependência:** são **duas versões editoriais do trabalho do mesmo autor**, não duas testemunhas independentes do uso da máquina. A data editorial de cada publicação não data necessariamente a montagem da figura, a eventual anotação à mão ou a digitalização.

## Confronto visual do mesmo desenho

- Ambas exibem a mesma **estrutura tripartida**: quadro retangular à esquerda, listagens com identificadores `H01` a `H12` abaixo e tabela de aspectos à direita. Há cabeçalhos visivelmente aparentados, incluindo `C1 NATAL` e `KOCH`. Os caracteres finais são **ambíguos na resolução disponível**: leituras `ZOD`, `Z00`, `200` não são conclusivas e não devem virar parâmetros de firmware.
- No centro do quadro esquerdo da cópia LBL-1983 há uma **anotação manuscrita de cinco dígitos**; no centro do quadro equivalente da página Nature-1985 o espaço está **vazio**. Não reproduzimos a anotação porque seu papel e eventual vínculo com participante/código de estudo não foram esclarecidos.
- A prancha do preprint é uma folha dedicada e apresenta um **identificador de produção gráfica** na parte inferior direita. A publicação Nature integra a figura na diagramação de três colunas, sem reproduzir esse identificador visível.
- O texto LBL, página impressa **-5-**, afirma que os mapas do experimento foram preparados por **Caveney e Nelson** usando um **Digicomp DR 70** e submetidos a conferência pontual por cálculo manual. Isso vincula **cálculo dos mapas do experimento** ao aparelho **segundo o autor**, mas não declara explicitamente que **os caracteres da fig. 1** são saída bruta, integral e inalterada de uma impressora conectada ao DR-70.

**Inferência limitada:** as cópias hoje acessíveis da figura **não são reproduções visualmente idênticas**. Isto obriga a separar o eventual papel impresso, a montagem gráfica submetida e as reproduções atuais; **não prova quem adicionou/removeu a anotação, nem quando**. A diferença pode remontar à preparação editorial **ou à anotação posterior em uma das cópias**. A fonte não estabelece que o DR-70 produziu o próprio desenho.

## Hipóteses concorrentes e teste discriminante

| Hipótese | Compatível com as fontes? | Evidência que distinguiria |
| --- | --- | --- |
| A: uma impressão direta do DR-70 originou a figura; manuscrito/diagramação foram acrescentados ou removidos em cópias posteriores | Sim, mas **não demonstrada** | Original em papel de impressora identificado, com marca de dispositivo, contexto de operação, data e provenance do exemplar |
| B: os cálculos foram feitos no DR-70, mas a tabela/figura foi composta em outro software, por operador ou pela editora | Sim, mas **não demonstrada** | Originais de pré-impressão, nota de composição, manual de saída, ou outro gráfico do mesmo formatter com hardware independente |
| C: uma testemunha foi anotada **após** a produção inicial; o diferencial não informa a origem dos caracteres informáticos | Sim, também não excluída | Inspeção do exemplar físico LBL, histórico de microfilmagem/digitalização, cópia anterior do mesmo preprint |

**Contraprova documental executada:** a proposição forte “as duas publicações exibem uma figura **integralmente idêntica e sem intervenção visível**” é **refutada pelo cotejo das duas folhas**. A proposição mais estreita “os caracteres computacionais básicos provêm da mesma saída” **não foi testada**: faltam resolução, master e cadeia impressora→papel. Não converter a primeira refutação em uma acusação de manipulação científica nem em prova de outro programa.

## Próxima aquisição e limites

1. Procurar cópia de maior resolução do preprint e os originais de produção da fig. 1, sobretudo negativos ou folhas de prova (sem contato institucional nesta fase).
2. Procurar **outro mapa impresso independentemente e associado por custódia ao DR-70**, não uma reimpressão de Carlson. Confrontar comprimentos de linha, separadores, glifos e ordem dos campos, sem atribuição semântica prematura.
3. Vincular qualquer candidato de saída a serial, operador, periférico, entradas/teclas e cálculo antes de adicionar casos ao `data/fidelity/observations.json`.

**Estado:** `DOCUMENTARY_TWO_WITNESSES`, `PRINT_DEVICE_NOT_AUTHENTICATED`, `NOT_RUN_NO_GOLDEN`. Nenhum dump/ROM, binário ou saída instrumental original foi obtido. Sem execução REA, compra, contato externo, reprodução de figuras no Git, alteração do corpus, ETL ou upload.
