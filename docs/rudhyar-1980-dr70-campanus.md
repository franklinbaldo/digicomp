---
type: Documento
title: "Rudhyar e Rael (1980): mapas Campanus recalculados no DR-70"
description: "Trilha documental de saída indireta do DR-70, relação com Nicki Michaels e controles de autenticidade."
timestamp: 2026-11-20T00:00:00-04:00
estado: provisorio
---

# Mapas Campanus atribuídos ao DR-70 em livro de 1980

## Achado e custódia documental

O catálogo bibliográfico da [Finna / Varastokirjasto](https://www.finna.fi/Record/vaari.1172270) registra **Leyla Rael e Dane Rudhyar, *Astrological Aspects: A Process-Oriented Approach*, Aurora Press, Nova York, 1980, 244 páginas, ISBN 0-943358-00-0**. Esta é uma confirmação de edição e existência bibliográfica, não uma inspeção do exemplar.

Uma [transcrição disponibilizada por terceiro no Scribd](https://www.scribd.com/document/205319766/Astrological-Aspects) contém duas declarações atribuídas à publicação:

1. No prefácio assinado por **Dane Rudhyar, Palo Alto, 23 de março de 1979**, agradece-se a **Nicki Michaels** por conferir a exatidão dos mapas de exemplo no seu computador; diz-se que usam cúspides de casas **Campanus**. O texto atribui a caligrafia dos mapas a **Tony Milner**.
2. Na introdução do **Apêndice I**, declara-se que os horóscopos de exemplo foram *recalculados em um computador astrológico DR-70* com casas Campanus. O índice textual do apêndice enumera cerca de 20 pessoas, entre elas Alan Watts, Einstein, Gandhi, Jimmy Carter e Franklin D. Roosevelt. A transcrição traz algumas entradas com data, latitude, longitude e hora U.T. como referências de cálculo.

Há também [outra reprodução textual no Scribd](https://www.scribd.com/document/633437269/Dane-Rudhyar-Leyla-Rael-Astrological-Aspects-A-Process-Oriented-Approach-Rudhyar-Series-Aurora-Press-Inc-2018-pdf). **Não contá-las como testemunhos independentes:** podem copiar a mesma digitalização/transcrição. A primeira tem 152 páginas exibidas pela plataforma, diferentes das 244 páginas catalogadas para a edição impressa; as páginas ilustradas/diagramas podem ter sido omitidos ou reorganizados. **Não foi confrontado fac-símile paginado da edição de 1980.** Uma tentativa de screenshot de outra cópia PDF falhou por redirecionamento HTTP; seu texto pesquisável não equivale a inspeção visual.

O [site de Nicki Michaels](https://nickimichaels.com/rudhyar-audio-archives/) e o [Rudhyar Audio Archives, de autoria/curadoria dela](https://www.astrologyuniversity.com/rudhyar-audio-archives/), corroboram a relação profissional com Rudhyar. A reportagem de [Duncan Campbell, *New Statesman* (1988), F13](sources.md) relata uma operadora com esse nome usando um DR-70. Essa convergência **fortalece a hipótese de mesma operadora**, mas não é nota fiscal, serial do aparelho, gravação de teclas ou confirmação independente das páginas do livro.

## Classificação de cada afirmação

| Alegação | Evidência efetivamente acessada | Grau |
| --- | --- | --- |
| Livro publicado em 1980, 244 páginas, ISBN | Catálogo institucional Finna | **Bibliografia confirmada por catálogo** |
| Prefácio datado de 23/03/1979 agradece Nicki, menciona Campanus e caligrafia | Transcrição de terceiro do livro | **Texto atribuído, sem fac-símile autenticado** |
| Apêndice I declara recálculo no DR-70 | Mesma transcrição, não sensor independente | **Relato técnico atribuído à obra, pendente confronto** |
| Números manuscritos em mapas reproduzem bytes ou tela/printout DR-70 | Nenhum registro direto disponível | **NÃO DEMONSTRADO** |
| Software, CPU, ROM, formato nativo, precisão do DR-70 | Nenhum binário ou teste original | **DESCONHECIDO** |

## Valor para engenharia reversa output-first

A pista é mais próxima do funcionamento real que a efeméride editorial de 1975 (F15): **a obra atribui explicitamente uma etapa de cálculo ao DR-70**. Mesmo assim, os mapas foram apresentados como **caligrafia por terceiro**; não são, por essa razão, impressão literal nativa da máquina. Um mapa publicado poderia conter ajustes editoriais, outras fontes e recálculo; não pode virar um par `replayable` em `data/fidelity/observations.json` por mera menção ao equipamento.

**Hipóteses rivais:** H1, o DR-70 produziu os números usados para os mapas; H2, um cálculo por outro método foi apenas conferido no DR-70; H3, a menção foi alterada entre edições ou na transcrição. As declarações de prefácio e apêndice favorecem H1, mas não discriminam com segurança edição e cadeia de transformação. Uma comparação só por valores modernos de Campanus não é confirmação instrumental.

**Controles prospectivos:**
- Localizar **exemplar autorizado da edição de 1980**; conferir visualmente folha de rosto/copyright, prefácio, início do Apêndice I e mapas. Registrar página impressa, página do scan, origem, tamanho e SHA-256 dos bytes efetivamente obtidos.
- Verificar se o texto de 1979 e a referência DR-70 existem na mesma edição original; confrontar eventuais reedições, sobretudo a de 2018, sem presumir identidade entre elas.
- Escolher inicialmente um ou dois mapas com entrada completa. Distinguir *números impressos no livro* de *saída literal da máquina*; manter `partial` ou item puramente bibliográfico enquanto faltarem teclas, serial, meio e gravação direta.
- Solicitar validação de hipótese ao 🦫 Castor (#7) e orientação de proveniência à 🐝 Abelha; o artigo original de **Richard Nolle XLV/10 (outubro/1983)** continua P0 para eventual comparação numérica independente.

## Limites de reprodução e uso

Nenhum livro inteiro, figura, digitalização ou texto protegido foi adicionado ao repositório; são apenas referências, paráfrases e análise original. Não houve compra, contato com pessoas/instituições, execução de firmware ou criação de observações sintéticas atribuídas ao DR-70. Os excertos em plataformas de terceiros **não provam** que as cópias foram publicadas com autorização dos titulares.
