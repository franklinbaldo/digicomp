---
type: Documento
title: "Raël/Rudhyar: primeiro controle numérico editorial para Roosevelt"
description: "Controles editoriais de novil e septil, com interpretação de hora, limites documentais e confronto moderno, sem golden DR-70."
timestamp: 2026-11-22T06:18:00-04:00
estado: provisorio
---

# Franklin D. Roosevelt: duas grandezas impressas na prosa, não no papel da máquina

## Evidência disponível

Em [*Astrological Aspects: A Process-Oriented Approach*](https://www.scribd.com/document/633437269/Dane-Rudhyar-Leyla-Rael-Astrological-Aspects-A-Process-Oriented-Approach-Rudhyar-Series-Aurora-Press-Inc-2018-pdf), de Leyla Raël e Dane Rudhyar (obra com copyright de 1980), a **transcrição secundária HTML**, na discussão do **novil** (aprox. linhas 4276–4286 da visualização Scribd), atribui à carta de Franklin D. Roosevelt duas separações angulares **expressas numericamente**:

| Relação textual | Número presente na prosa | Relação interpretativa no capítulo |
| --- | ---: | --- |
| Lua–Plutão | **39°** | Próxima do novil nominal de 40° |
| Marte–Urano | **81°** | Próxima do binovil nominal de 80° |

Esses números são **dados documentais textuais de uma única obra**. Não são dois registros independentes, nem duas longitudes planetárias, nem valores vistos na impressora/LED do DR-70. A página **física** exata e os algarismos **visualmente** impressos não foram inspecionados: **TEXT_INDEX_ONLY / FACSIMILE_NOT_READ**. A [edição bibliográfica de 1980, Aurora Press, 244 páginas](https://www.finna.fi/Record/vaari.1172270) não autentica que a cópia textual online corresponde folha a folha àquela edição. Também não há hash de PDF original nem permissão para republicá-lo.

A **transcrição textual secundária** do prefácio (índice PDF, aproximadamente linhas 91–98) atribui a **Nicki Michaels** conferência de cálculos em “seu computador” e a **Tony Milner** a caligrafia dos horóscopos do Apêndice I. A identidade do computador e a ordem operacional exata não estão estabelecidas; não se pode equiparar automaticamente o equipamento de Nicki ao DR-70. Prefácio, prosa de ângulos e apêndice pertencem à **mesma cadeia editorial**, não a três testemunhas. A edição da cópia online permanece **`source_edition=UNRESOLVED`** mesmo diante dos catálogos Aurora Press e da fotografia da folha de rosto de outro exemplar. Esses créditos também precisam de leitura visual das páginas originais.

O [Apêndice I na mesma transcrição](https://www.scribd.com/document/633437269/Dane-Rudhyar-Leyla-Rael-Astrological-Aspects-A-Process-Oriented-Approach-Rudhyar-Series-Aurora-Press-Inc-2018-pdf), aprox. linhas 6701–6733, **atribui** recálculos de mapas Campanus a um computador DR-70, mas as etapas editoriais de cálculo, conferência e desenho não estão vinculadas a uma impressão original. Para Roosevelt, a lista apresenta **30/01/1882; 41N48, 73W56; 25:16 U.T.**; a [extração da edição francesa mencionada no ledger](rudhyar-appendix-input-ledger.md) traz **25h15** na legenda, a conferir em imagem. O número de linha online não é página impressa.

## Experimento numérico reproduzido na sandbox (22/11/2026)

Executei [o script isolado](../scripts/probe_fdr_published_aspects.py) com Swiss Ephemeris **2.10.03**, algoritmo Moshier (flag `FLG_MOSEPH`), longitude **eclíptica tropical geocêntrica**, instante juliano UT. Calculei a **menor distância angular** `min(|a−b|, 360−|a−b|)`, sem usar sistema de casas. O confronto com 39° e 81° adota **arredondamento moderno ao grau inteiro apenas como hipótese**, não como regra de arredondamento demonstrada para a publicação.

| Leitura hipotética do relógio na data editorial 30/01/1882 | Lua–Plutão moderno | Marte–Urano moderno | Iguais a 39°/81° após arredondar? |
| --- | ---: | ---: | --- |
| `25:16 UT` = **31/01 01:16 UT** (hora contínua) | **38,674166°** | **80,917130°** | **sim / sim** |
| `25:15 UT` = **31/01 01:15 UT** (variante textual) | **38,665740°** | **80,917128°** | **sim / sim** |
| `01:16 UT` em **30/01** (sem avanço de dia) | **26,470695°** | **80,907931°** | **não / sim** |

Diferenças modernas relativas aos números publicados no cenário `25:16`: **−0,325834°** (Lua–Plutão) e **−0,082870°** (Marte–Urano). A primeira relação **discrimina as duas interpretações de data/hora nesse modelo**; a segunda não. A alteração 25:16→25:15 tampouco discrimina na resolução de um grau. Esse resultado é coerente com o uso de hora UT estendida no apêndice, **não prova que o DR-70 gerou a prosa** e não define tolerância/orb astrológico para os aspectos.

## Contraprova de resolução temporal: coincidência de inteiros não identifica minuto

Sob a hipótese **adicional, não autenticada editorialmente**, de arredondar ambos os arcos modernos ao grau inteiro mais próximo, `31/01/1882 01:00 UT` fornece **38,539345° / 80,917103°**, enquanto `31/01/1882 02:30 UT` fornece **39,297515° / 80,917233°**. São instantes separados por **90 minutos** e ambos seriam exibidos como **39° / 81°**. Este par de contraexemplos é testado no código, sem estimar a fronteira exata da janela. A [ablação independente de Morcego R165](https://github.com/franklinbaldo/digicomp/pull/155#issuecomment-7078344244) estimou por bisseção uma janela de cerca de 118,7 minutos, mas sua varredura não demonstra monotonicidade contínua; não incorporamos o intervalo como prova formal nem como tolerância histórica.

Portanto os dois números editoriais, por si, **não estabelecem minuto de nascimento, algoritmo ou precisão do DR-70**. Eles permitem no máximo discriminar algumas leituras de mudança de dia **sob o motor, calendário e hipótese de arredondamento declarados**.

## Controle textual de septil: mesmo livro, não outro holdout

A [cópia indexada em PDF](https://tibetanbuddhistencyclopedia.com/en/images/b/b8/Dokumen.tips_astrological-aspects.pdf), seção *The Septile*, linhas **2969–2977** do índice, atribui à carta de Roosevelt Lua–Netuno **“about 52°”**, Marte **pouco aquém de 51° adiante de Saturno**, e Lua–Júpiter como septil **se adotada hora posterior** atribuída com ressalva ao diário do pai. A faixa textual de septil é **50° a 53°**. Essas são restrições de prosa do **mesmo cluster editorial** dos 39°/81°; não há três holdouts adicionais nem leitura nativa da máquina.

A captura de página por ferramenta de PDF falhou após redirecionamento. Portanto **PDF_TEXT_INDEXED / FACSIMILE_NOT_INSPECTED**: números, diagrama e página física não foram conferidos visualmente. O horário posterior mencionado na passagem **não está numericamente identificado**.

| Controle moderno Swiss Ephemeris 2.10.03/Moshier | `25:16 UT` com rollover | `01:16 UT` sem rollover |
| --- | ---: | ---: |
| Lua–Netuno, menor arco | **52,250656°** | **40,054870°** |
| Marte adiante de Saturno, arco **dirigido** módulo 360° | **50,916592°** | **51,000669°** |
| Lua–Júpiter, menor arco | **49,104161°** | **36,971882°** |

Os dois primeiros controles do cenário 25:16 são coerentes com as expressões textuais sob **convenções modernas**. Lua–Júpiter fica abaixo da faixa textual em 25:16, **mas não contradiz nem confirma a cláusula para outra hora**. O teste registra apenas o valor e a condição `NOT_EVALUATED_LATER_HOUR_UNSPECIFIED`, sem fabricar um PASS/FAIL. A diferença de convenção **arco dirigido vs. menor arco** é testada separadamente. Nem os números nem o intervalo editorial caracterizam precisão instrumental ou regra de arredondamento original.

Próximo passo: conferir visualmente **folha de rosto, copyright, passagem do novil, passagem do septil e Apêndice I na mesma cópia** com páginas físicas e duas leituras independentes. Não incluir esses números em `data/fidelity/observations.json`.

## Como reproduzir e falsificar

Na raiz do repositório, em ambiente de pesquisa com `pyswisseph` instalado (motor opcional, **não** dependência de produção):

```sh
python scripts/probe_fdr_published_aspects.py
python -m unittest discover -s tests -p 'test_fdr_published_aspects.py'
python -O -m unittest discover -s tests -p 'test_fdr_published_aspects.py'
```

Na sandbox da Coruja: **4/4 testes PASS** no Python normal e **4/4 PASS** em `-O`, além da execução do gerador JSON; sem contato com dispositivo original. O teste com efemérides é explicitamente **SKIP** caso a dependência opcional não esteja instalada. A versão 2.10.03 foi observada localmente, não fixada nem testada em todas as plataformas. O [workflow público original da #155](https://github.com/franklinbaldo/digicomp/actions/runs/45012551372) aprovou os quatro testes anteriores no HEAD `162a0253`. Os controles suplementares dependem de novos gates SHA-exatos.

**Hipótese H1:** as separações foram lidas de um mapa editorial cujo instante era UT contínua; o cálculo moderno concorda com os inteiros relatados. **Hipótese H2:** a prosa foi derivada de outra efeméride/programa ou arredondada a partir de outro suporte e a mesma concordância era esperada. **Hipótese H3:** a extração online alterou números, edição, dia ou fuso. As três seguem abertas; a hipótese `01:16` no mesmo dia **não** reproduz a primeira grandeza sob estas convenções modernas.

**Próxima observação de maior valor:** obter imagem legível da **mesma cópia física** contendo folha de rosto, verso/copyright, passagem do novil, introdução do Apêndice I e gráfico Roosevelt; transcrever independentemente a hora, os dois ângulos e a graduação original. Isso permitirá avaliar atribuição editorial e resolução, ainda **sem** fabricar saída de impressora. Uma comparação instrumental verdadeira exigiria cadeia explícita entrada→teclas→aparelho→canal→saída.

**Classificação final:** `SECONDARY_EDITORIAL_ANGLES_VS_MODERN_EPHEMERIS_NOT_DR70`; `dr70_fidelity=NOT_RUN_NO_GOLDEN`. Não alterar `data/fidelity/observations.json`, nem admitir os dois números como holdouts independentes ou observações nativas. Relacionado a [Digicomp #130](https://github.com/franklinbaldo/digicomp/issues/130), [ledger do Apêndice](rudhyar-appendix-input-ledger.md) e [controle editorial de Carter](carter-book-qualitative-houses.md).
