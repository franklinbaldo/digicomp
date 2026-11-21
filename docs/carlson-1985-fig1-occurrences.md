---
type: Documento
title: "Carlson 1985: ledger de ocorrências da figura 1"
description: "O1/O2: regiões gráficas, dependências e limites da atribuição de saída ao Digicomp DR-70."
timestamp: 2026-11-20T21:45:00-04:00
estado: provisorio
---

# Carlson 1985: oito regiões não são oito observações

**🐝 Abelha · [Digicomp #30](https://github.com/franklinbaldo/digicomp/issues/30) / [#7](https://github.com/franklinbaldo/digicomp/issues/7).** Ledger espacial O1/O2 que complementa as [hipóteses do Polvo](carlson-1985-output-hypotheses.md). Os IDs são ocorrências **na página publicada**, não amostras de hardware nem linhas do corpus de fidelidade.

**Fonte:** Shawn Carlson, [*A double-blind test of astrology*](https://doi.org/10.1038/318419a0), *Nature* 318, pp. 419–425, 5/12/1985. Figura 1 na **página impressa 419**, primeira página do [PDF no laboratório de Richard Muller](https://muller.lbl.gov/papers/Astrology-Carlson.pdf), inspecionada visualmente em 20/11/2026. O PDF não foi custodiado nem teve seu SHA-256 medido nesta rodada. A legenda descreve um mapa derivado por computador, não uma folha diretamente impressa por exemplar identificado. A p. 420 atribui os mapas do experimento aos operadores Caveney/Nelson usando aparelho grafado “Digicom DR 70”, mas **não vincula cada caractere da figura à saída nativa nem documenta sua composição editorial**.

## O1. IDs locais e posição preservada

As marcas entre crases são **candidatas visuais**; os espaços, pontos e glifos de baixa resolução não foram promovidos a transcrição byte-a-byte.

| ID | Zona da fig. 1, p. 419 | Marca ou estrutura observável | Limite |
| --- | --- | --- | --- |
| `CAR85-F1-A` | quadrado **superior esquerdo** | diagrama gráfico | Figura, não input nem teclas observadas |
| `CAR85-F1-B1` | **inferior esquerdo**, acima da lista | `C1 NATAL` | Cabeçalho candidato, primeira instância |
| `CAR85-F1-B2` | **inferior esquerdo**, linhas da lista | `H01`–`H12` | Doze rótulos no mesmo subpainel, não doze testes |
| `CAR85-F1-C1` | **centro inferior**, primeira linha de título | `C1 SEC` | Não atesta comando ou função da máquina |
| `CAR85-F1-C2` | **centro inferior**, segundo título | `C1 SEC` | Repetição visual sem segunda execução provada |
| `CAR85-F1-C3` | **centro inferior**, entre C1 e C2 | `DATE REC` (candidato) | Data não autentica data de entrada/nascimento |
| `CAR85-F1-D1` | **topo da matriz direita** | `C1 NATAL` | Segunda instância do cabeçalho na **mesma figura** |
| `CAR85-F1-D2` | **matriz direita**, sob D1 | `ORB` (candidato) e símbolos | Sem autoria do formatador estabelecida |

**Arestas que não podemos colapsar:** B1 e D1 ocupam regiões diferentes, mesmo que a grafia coincida; C1 e C2 são duas ocorrências espaciais, não dois comandos atestados. Por outro lado, todas as oito regiões dependem do **mesmo evento editorial** da *Nature*: não formam oito documentos, oito equipamentos ou oito observações independentes. A ordem em que as regiões foram calculadas, impressas ou montadas é desconhecida.

A terminação de cabeçalho por vezes lida `200` é ambígua frente a `ZOD`, `Z00` ou outras leituras; `P LONG` versus `P.LONG` também precisa de resolução melhor. Nenhuma alternativa deve ser tratada como identificador de firmware. Não extrair números de casas ou coordenadas de glifos duvidosos.

## O2. Grafo de dependências

```text
Carlson (Nature 318/1985), fig.1 p.419 [uma obra]
  ├─ cópia PDF em muller.lbl.gov [uma representação]
  ├─ demais mirrors [se existirem: cópias da mesma obra]
  └─ A, B1/B2, C1/C2/C3, D1/D2 [oito regiões da mesma figura]
Carlson, texto de método p.420 [a mesma obra]
  └─ atribui o cálculo dos mapas a Caveney/Nelson num DR-70
                |
       elo documental NÃO recuperado:
       DR-70 → operação/teclas → captura → layout da fig.1
```

| Hipótese A | Rival B | Observação discriminante | Situação |
| --- | --- | --- | --- |
| B/C/D vêm diretamente de uma execução do DR-70 | Operador/editor juntou seções de origens distintas | Papel original + sequência de teclas + cadeia de captura | `NOT_RUN_NO_ORIGINAL` |
| B1 e D1 são operações independentes | Mesma operação, cabeçalho repetido no layout | Duas sessões físicas com identidade/tempo/entrada distintos | `NOT_RUN_NO_EVENTS` |
| C1 e C2 são modos nativos distintos | Seções produzidas pelo formatador | Manual contemporâneo e saída original com seleção observada | `NOT_RUN_NO_MANUAL` |
| Grafia da figura identifica exclusivamente o DR-70 | Grafia também aparece noutro programa ou composição editorial | Controle negativo de impressora/software comprovadamente não DR-70, da época | `NOT_RUN_NO_CONTROL` |

**Contraprova documental:** os dois `C1 NATAL` visíveis pertencem ao mesmo fac-símile. Portanto, contar os cabeçalhos como **duas fontes físicas independentes** é falso. Isso **não** demonstra se houve uma ou mais operações anteriores à montagem.

## Próxima prova e critério de não promoção

Realizar **duas transcrições cegas independentes** dos recortes fixos B1/C1/C2/D1, com IDs espaciais preservados; registrar divergências por glifo e resolução, sem oferecer antes a interpretação `200`/`ZOD`. Recuperar, se possível, papel e operação ligados a um DR-70 identificado, com input, teclas, estado, canal e saída literal antes de classificar qualquer caso como `replayable`. Cópias do mesmo artigo não são controles independentes.

**Resultado:** oito regiões de uma imagem histórica indexadas, **zero saída nativa autenticada e zero par DR-70 reexecutável**. Não modificar `data/fidelity/observations.json`, não inferir CPU/ROM, não reproduzir a figura protegida no Git.
