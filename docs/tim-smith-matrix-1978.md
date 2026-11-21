---
type: Documento
title: "DR-70 em 1978: o relato técnico de Tim Smith"
description: "Fac-símile do artigo de Tim Smith na Matrix Magazine, com especificação de memória, comandos de exemplo e descrição da impressora."
timestamp: 2026-11-21T09:29:47-04:00
estado: provisorio
---

# O DR-70 descrito por Tim Smith em 1978

**DR70-CASE-MATRIX-1978-SMITH · DOCUMENTED.** Tim Smith assina *Digicomp's DR-70: The First Astrological Desktop Computer*, na *Matrix Magazine*, n.º 1, inverno de 1978, pp. 57–58. A nota editorial na p. 57 o identifica como o astrólogo e programador que desenvolveu o DR-70. O artigo descreve um projeto com entregas previstas para março daquela edição e uma impressora cuja produção estava prevista para julho. A cronologia de fabricação e entrega de unidades permanece em aberto. [Fac-símile das pp. 57–58, a partir da folha 68 do PDF](https://assets.libsyn.com/show/59251/Matrix_Magazine_1-4.pdf#page=68).

## O que a fonte documenta

| Localizador na revista | Afirmação atribuída à fonte | Verificação ainda necessária |
| --- | --- | --- |
| p. 57, primeiro parágrafo de Smith | CPU de 8 bits, **28K bytes de ROM por máscara metálica** e **1K bytes de RAM** para trabalho e armazenamento do usuário. A maior parte do software foi escrita em assembly e a Digicomp desenvolveu rotinas próprias de ponto flutuante. | Modelo da CPU, ISA, marcações e organização dos chips, mapa de memória e conteúdo da ROM. |
| p. 57, mesmo parágrafo | Rotinas de interrupção associadas ao estado do teclado alternam atualização dos LEDs, interpretação das teclas, cálculos e transferência à impressora. Smith descreve início de cálculo antes do fim de certas entradas e conferência com a sequência completa. | Ordem e temporização observáveis, regras de interpretação e diferenças entre revisões. |
| p. 57, nota editorial | A revista lista seis sistemas de casas: Placidus, Campanus, Meridian, Koch, Porphyry e Regiomontanus. Também atribui ao aparelho uma efeméride de 3000 a.C. a 7000 d.C. e anuncia precisão para 1850–2000. | Algoritmos, limites aceitos, calendários, unidades, arredondamento e erros medidos. |
| p. 58, dois primeiros parágrafos | Smith exemplifica a consulta da posição do Sol natal com `NATAL ☉` e a do Sol progredido com `SECondary ☉`. Afirma que entradas anteriores podem abreviar novas sequências enquanto a máquina permanece ligada. | Teclas físicas exatas, estado inicial, dados de entrada e valores exibidos. Os exemplos descrevem comandos, sem registrar uma sessão. |
| p. 58, terceiro parágrafo | Smith descreve um **manual de instruções** com mapas de exemplo e duas seções de referência no fim, para sequências comuns e entradas mais complexas. | Recuperar o manual, conferir edição e comparar o conteúdo com o impresso fotografado junto ao L606. |
| p. 58, último parágrafo de Smith | A **impressora companheira** teria fonte própria e um cabo para o DR-70. Segundo Smith, poderia ordenar e listar dados do mapa ou registrar as entradas de teclado em papel. | Identificar o periférico produzido, seu protocolo e uma impressão ligada a uma unidade e a uma sessão. |

## Impressão e testes de fidelidade

A descrição torna plausível uma cadeia direta do DR-70 à impressora. Para a figura de Carlson, continuam em aberto tanto a hipótese de que seus blocos incorporam uma listagem da impressora companheira quanto a de que outra máquina ou composição editorial formatou os cálculos. A observação que distingue as hipóteses é uma listagem da impressora identificada, de preferência com o registro das teclas da mesma sessão, comparável aos cabeçalhos e à ordem dos campos de Carlson. [Hipóteses e localizadores da figura de Carlson](carlson-1985-output-hypotheses.md).

A p. 57 contém uma fotografia frontal com segmentos visíveis e sem serial ou operação identificados. A p. 59 do mesmo número traz uma tabela de obliquidade sem atribuição visível ao DR-70. Para comparações de fidelidade, o estado é `NOT_RUN_NO_GOLDEN`. A primeira busca documental deve priorizar o manual e material da impressora que exponha o formato de listagem e de registro das teclas. [Foto na folha 68](https://assets.libsyn.com/show/59251/Matrix_Magazine_1-4.pdf#page=68) · [Tabela na folha 70](https://assets.libsyn.com/show/59251/Matrix_Magazine_1-4.pdf#page=70).

## Custódia e cobertura

- Consulta em 21/11/2026. O [catálogo público de Michael Erlewine](https://startypes.com/e-books.aspx) lista a coletânea digital *Matrix Magazine Issues 1 to 4*, publicada em 16/08/2023. O [link de download divulgado pelo editor](https://assets.libsyn.com/show/59251/Matrix_Magazine_1-4.pdf) redirecionou para [o PDF no servidor estático](https://static.libsyn.com/p/assets/e/5/8/b/e58bfb975056ee9da04421dee9605cbd/Matrix_Magazine_1-4.pdf). A coletânea tem 253 folhas e 90.400.056 bytes. SHA-256 do PDF recebido: `74571da7edf231321bdee7d5ea0d8772f3360f9aaa26a1147ec636e0c3771069`.
- A inspeção visual usou Poppler 26.07.0. No PDF, a capa do n.º 1 está na folha 8, e as pp. impressas 5 e 57–60 estão nas folhas 15 e 68–71, respectivamente, em contagem a partir de 1. O artigo técnico ocupa as folhas 68–69. A análise se limita às páginas citadas. [Capa e sumário do n.º 1](https://assets.libsyn.com/show/59251/Matrix_Magazine_1-4.pdf#page=8).
- SHA-256 dos PNGs de inspeção gerados com `pdftoppm -f 62 -l 71 -scale-to 2100 -png`: folha 68, `88f8bf15c68ff8eb6ebc4e7fdf57f196c33c9842f515dccbf192213fab399a1f`; folha 69, `047ff20ad9fd8b6affe60edc6f0c5c891a98c5fb5b0f1fe8fdf1e53cd4ebd00b`. O repositório guarda referências e paráfrases. A licença de redistribuição das páginas permanece indeterminada.

Frentes relacionadas: [desenvolvedores #1](https://github.com/franklinbaldo/digicomp/issues/1), [arquitetura #4](https://github.com/franklinbaldo/digicomp/issues/4), [manuais #5](https://github.com/franklinbaldo/digicomp/issues/5) e [proveniência de saídas #30](https://github.com/franklinbaldo/digicomp/issues/30).
