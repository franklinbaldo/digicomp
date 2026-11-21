---
type: Documento
title: "Carlson, figura 1: ledger O0/O1 de tokens e simetria aparente"
description: "Leitura visual conservadora das edições de 1983 e 1985; hipóteses sobre a gramática sem converter figura editorial em saída autenticada do DR-70."
timestamp: 2026-11-21T01:02:00-04:00
estado: provisorio
---

# Carlson, figura 1: ledger visual, não golden do DR-70

**🦫 Castor R128 · [Digicomp #30](https://github.com/franklinbaldo/digicomp/issues/30), [#7](https://github.com/franklinbaldo/digicomp/issues/7).** Aplicação documental O0/O1 da [rota REA local](rea-output-first.md), em complemento ao [dossiê de custódia](carlson-1983-preprint-figure-custody.md). Não há ROM nem interface REA binária nesta prova.

## Fonte, localizadores e limite O0

- **F83:** Shawn Carlson, *Double-Blind Test of Astrology*, preprint LBL-20480, capa abril/1983. [Fac-símile institucional](https://escholarship.org/content/qt0b40b045/qt0b40b045_noSplash_aa3bf76a6b22470b8665af02a57d27ae.pdf#page=27), **folha PDF 27, página impressa -24-, figura 1**. Inspeção visual da página em 21/11/2026, não OCR.
- **F85:** Carlson, *Nature* 318 (05/12/1985), p. 419, [figura 1, folha PDF 1](https://muller.lbl.gov/papers/Astrology-Carlson.pdf#page=1). Inspeção visual da página em 21/11/2026, não OCR.
- As figuras pertencem à **mesma linhagem editorial**; F83 e F85 não são duas sessões, dois aparelhos ou dois casos independentes. O artigo relata cálculo de mapas com DR-70, **não certifica o canal que gerou os caracteres da figura 1**. Leitura pública por visualizador; **bytes de PDF não obtidos nesta rodada**, hash/tamanho do arquivo = `NOT_OBTAINED`. Nenhuma imagem foi incorporada ao Git.
- **Estado O0:** `FIGURE_PUBLISHED_ORIGIN_UNATTRIBUTED`. Saída diretamente atribuível a DR-70: `NOT_RUN_NO_NATIVE_PRINT`. Caso reexecutável: `NOT_RUN_NO_GOLDEN`. O [corpus](../data/fidelity/observations.json) permanece separado e vazio.

## Mapa mínimo de regiões e tokens

As letras entre colchetes exprimem **incerteza de leitura**, não caracteres do suposto programa. Não reconstruir um arquivo ASCII ou cadeia de teclas a partir deste mapa.

| Região visual | F83 / F85 | Fragmento conferido ou leitura candidata | Grau de leitura | O que permanece desconhecido |
| --- | --- | --- | --- | --- |
| Esquerda inferior, primeira linha | ambas | `C1 NATAL TROP P[.]LONG KOCH` | alto para `NATAL`, `TROP`, `KOCH`; ponto incerto | Função de `C1`, `P`, `LONG`, `KOCH`; origem do renderer |
| Fim do mesmo cabeçalho | ambas | `Z[OD/OO/00]` **ou leitura semelhante a `200`** | **baixo** | Nem `200` nem `ZOD` devem virar constante de firmware |
| Esquerda inferior, coluna de índices | ambas | `H01` até `H12`, em ordem, com marca de atribuição e glifos | alto para sequência de IDs; parcial para valores | Sistema de casas, arredondamento e canal de saída |
| Esquerda inferior, bloco adjacente | ambas | `C1 SEC TROP P[.]LONG KOCH`; `DATE REC[...]` | parcial | Se `SEC` é modo, título ou estágio externo; complemento do rótulo de data |
| Direita superior e tabela | ambas | outro `C1 NATAL ... KOCH`; `ORB` e grade triangular de glifos | parcial | Se grade e colunas nasceram no mesmo software que os índices H |
| Centro do diagrama esquerdo | F83 apenas | `22987`, aparentemente manuscrito | médio para os algarismos | Se etiqueta de sujeito, anotação de produção ou outra coisa; **não buscar identificação pessoal** |
| Rodapé da figura | F83 apenas | `XBL 832-8314` | alto | Natureza da arte-fonte, transformações editoriais e origem do formatter |

**Controle editorial já confirmado pelo dossiê:** `22987` e `XBL 832-8314` não aparecem em F85. Isso rejeita cópia **integralmente inalterada da página F83**, não rejeita output nativo anterior à montagem. A figura original pode conter uma ou várias camadas de processamento.

## O1: simetria visível, sem inferência algorítmica

Na **única família de figura** F83/F85, os seis pares de linhas abaixo exibem **aparente repetição dos dois grupos numéricos** (graus e minutos); o glifo zodiacal intermediário é distinto ou pouco legível. Leituras candidatas a reconferir em fac-símile de resolução superior:

| Par | Grupos numéricos aparentes em ambos os índices | Estado |
| --- | --- | --- |
| `H01` / `H07` | `09` / `08` | leitura visual candidata |
| `H02` / `H08` | `05` / `59` | leitura visual candidata |
| `H03` / `H09` | `09` / `38` | leitura visual candidata |
| `H04` / `H10` | `25` / `08` | leitura visual candidata |
| `H05` / `H11` | `19` / `58` | leitura visual candidata |
| `H06` / `H12` | `14` / `29` | leitura visual candidata |

**Hipótese gramatical G1:** índices `H01`–`H12` organizam seis pares com uma transformação de glifo no segundo membro. **Alternativa G2:** a simetria resulta do esquema de apresentação ou de pós-processamento sobre números calculados em outra etapa; **alternativa G3:** ao menos um par foi mal lido na cópia disponível. Mesmo que os pares correspondam a casas opostas de um mapa astrológico, **a relação matemática genérica não identifica o aparelho ou seu firmware**. A mesma figura publicada duas vezes não valida G1 independentemente.

## O3/O4: testes discriminantes previamente definidos

1. **Origem nativa versus externa:** obter uma impressão de **exemplar DR-70 identificado**, documentação de conexão e sequência de operação que mostre a mesma gramática. Resultado atual: `NOT_RUN_NO_NATIVE_PRINT`.
2. **Regra de pares versus desenho editorial:** obter um segundo output independente com os 12 campos visíveis; comparar seis pares completos de dígitos **e glifos**, registrando cada discordância antes de normalizar o zodíaco. Resultado: `NOT_RUN_NO_GOLDEN`.
3. **Token final como palavra ou número:** localizar manual/printout nativo com cabeçalho legível ou originais de produção. Até lá recusar escolha por OCR, tipografia semelhante ou expectativa do intérprete. Resultado: `UNRESOLVED_GLYPH`.
4. **Independência de evidências:** F83, F85, reproduções online e recortes destas figuras compõem **uma família documental**, mesmo que URL ou hash difiram. Nunca separar entre calibração e holdout. Resultado: `DECLARED_SINGLE_FAMILY`; nenhuma avaliação numérica executada.

**Próxima ação coordenada:** 🐢 Tartaruga/🦉 Coruja procuram origem da figura e carta de símbolos mencionada por Carlson; 🐝 Abelha pode cotejar regiões e marcas de incerteza; 🦫 Castor preserva este ledger sem promover tokens a `observations.json`. Sem novo artefato físico, não há motivo para gerar um emulador, refinar efemérides ou pontuar fidelidade.
