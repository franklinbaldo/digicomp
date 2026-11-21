---
type: Documento
title: "REA orientada pela saída: plano inverso para o Digicomp DR-70"
description: "Investigação que começa com os fragmentos de saída documentados, distingue proveniência, formula hipóteses rivais e planeja contraprovas."
timestamp: 2026-11-20T21:05:00-04:00
estado: vigente
---

# DR-70: reverse engineering a partir do output

**Esta é a rota principal da skill Digicomp.** O objetivo é **reconstruir o encadeamento entrada → estado → cálculo → formatação → saída**, trabalhando inversamente a partir do que o DR-70 teria exibido ou impresso. ROM, CPU e desmontagem aparecem depois, quando houver artefato, e não são pré-requisitos para analisar **evidência documental**.

## Inventário do que já temos, não do que desejamos

| ID local | O que está documentado | Vínculo com DR-70 | Incerteza crítica | Pode virar teste numérico? |
| --- | --- | --- | --- | --- |
| `OUT-CARLSON-1985-FIG1` | `docs/exemplares-interface.md` relata que Carlson, *Nature* 318 (1985), p. 419, fig. 1, apresenta um mapa com cabeçalho `C1 NATAL TROP P LONG KOCH 200` e campos `H01`–`H12` | Na p. 420 o artigo **afirma** que o DR-70 calculou mapas do experimento; p. 422 nomeia Michael Caveney e Chris Nelson como operadores | Não há prova de que a figura seja impressão literal/integral de um DR-70 individual, nem vínculo da figura a teclas, data e série | **Não**: candidato de formato e hipótese de origem, somente |
| `OUT-L606-DISPLAY` | Calcuseum, foto de display L606, apresenta segmentos e rótulos `NATAL`, `TROP`, `PRIM`, `SEC`, `TERT`, `SOLAR`, `LUNAR`, `DIR`, `CONV`, `ERROR`, `OFLOW` | Fotografia associada ao aparelho catalogado como DR-70 L606 | Não conhecemos estado inicial, sequência de teclas, função selecionada, leitura literal completa nem valores da máquina | **Não**: controle de interface/legendas, somente |
| `OUT-NOLLE-1983-INDEX` | Índice AFA menciona teste DR-70 vs. `ACS program` (Nolle, *Today's Astrologer*, XLV/10, out/1983, p. 9) | **Apenas referência bibliográfica**; artigo original ainda não recuperado no corpus | Nenhuma entrada nem saída foi transcrita | **Não**: alvo de aquisição documental |
| `OUT-POTTENGER-1979` | Texto contemporâneo descreve computador pré-programado e várias rotinas; `docs/1979-pottenger-dr70.md` | Depoimento textual sobre capacidades gerais | **Zero valores ou sequência de operação** | **Não**: limites de hipóteses, somente |

Referências: [inventário de exemplares](exemplares-interface.md), [corpus observacional](fidelity-corpus.md), [fonte de 1979](1979-pottenger-dr70.md), [trilha ACS](acs-comparator-provenance.md) e [análise de relógio/longitude](time-longitude-identifiability.md).

**Estado do corpus de fidelidade:** `data/fidelity/observations.json` tem `"observations": []`. Não inserir linhas nesses dados para representar figuras não autenticadas, nem criar `replayable` sem a sequência de entrada e a saída associada ao mesmo evento. A análise abaixo é **pré-fidelidade**; pode gerar perguntas e previsões, mas não observações instrumentais.

## Fluxo O0–O6: sair do output sem fabricar o programa

### O0. Autenticar o elo entre output e aparelho

Abrir um caso `DR70-CASE-ID` com URL, fonte, edição, página/frame, autor e direitos. Marcar **origem da apresentação**, que pode ser: foto do LED, papel direto do aparelho, transcrição de operador, gráfico refeito pelo editor, impressão de outro computador ou atribuição ainda não resolvida. Uma reportagem que diz "calculado no DR-70" **não prova** que os caracteres publicados foram emitidos pela impressora dele.

**Próxima evidência de maior valor:** fac-símile ou registro de operação que vincule **entrada, teclas, DR-70 e output** no mesmo evento. Até então, `OUT-CARLSON-1985-FIG1` não é saída nativa certificada.

### O1. Congelar a superfície observada

Conservar o arquivo/documento fonte com hash **somente se os bytes foram obtidos**; registrar `sha256: desconhecido` se só temos URL. Capturar localizador (p. 419, fig. 1) e transcrever os caracteres **tal como vistos**. Manter separadas duas colunas:

- `literal`: `C1 NATAL TROP P LONG KOCH 200` e os marcadores `H01`–`H12`, **conforme a transcrição já documentada**, sujeitos a cotejo.
- `interpretação`: significado **candidato** de cada marcador; nunca preencher automaticamente `P` = Placidus, `LONG` = longitude, `KOCH` = sistema de casas implementado ou `200` = precisão/versão/identificador.

Transcrever valores, sinais, espaços, casas decimais, linhas, separadores, ordem e eventuais zeros à esquerda **apenas quando legíveis no original**. Não realizar OCR automático como substituto de inspeção. Uma transcrição do texto de nosso repositório é secundária em relação à imagem original.

### O2. Inferir o formato de saída, ainda sem inferir algoritmo

Construir um mapa de campos em camadas:

```text
imagem / layout observado
    → tokens literais e posições (semântica desconhecida)
    → gramáticas alternativas (candidatas)
    → parâmetros possíveis do cálculo (hipóteses)
    → função matemática candidata
    → entrada/teclado/estado que poderia produzi-la
```

No caso Carlson, `H01`–`H12` sugere **indexação sequencial de doze campos**, mas não comprova valores das casas, sistema de casas calculado ou fidelidade. `KOCH` é texto observado na transcrição, não prova de que o DR-70 ofereça opção Koch. Especificar condições em que a hipótese de um formatter editorial externo seria indistinguível de uma impressão original.

### O3. Propor pelo menos duas hipóteses rivais por componente

| Componente investigado | Hipótese A | Hipótese B | Próxima prova que distingue |
| --- | --- | --- | --- |
| Cabeçalho da fig. 1 | Impressão nativa do DR-70 | Composição editorial ou saída de outro programa com cálculo feito no DR-70 | Impressão original, manual de impressora, captura de outro aparelho com o mesmo cabeçalho |
| `H01`–`H12` | Campos associados a casas astrológicas | Campos indexados por renderer ou software posterior | Imagem integral, descrição do autor e layout do programa comparador |
| `KOCH` | Opção de casas escolhida pelo aparelho | Palavra adicionada/convertida no pós-processamento | Manual de comandos e múltiplas saídas com opção alterada |
| Rótulo `ERROR` / `OFLOW` no L606 | Estado de erro de operação | Indicador físico sem comportamento observado | Foto/vídeo de transição de estado com entrada reproduzível |
| Cálculo de tempo/local | Instante civil + longitude por convenção A | Convenção de fuso/longitude B que produz o mesmo resultado observável | Pares controlados de relógio e longitude, com leitura independente de outra grandeza |

A hipótese **não** é um dado, e um único output pode não distinguir algoritmos diferentes. Registrar parâmetros livres e graus de liberdade; evitar ajustar tudo a uma única figura.

### O4. Criar previsões falsificáveis antes do teste

Para cada hipótese formalizar `entrada necessária`, `saída esperada` (pode ser um *intervalo*, não um número fixo), unidade, precisão, ponto de divergência e controle negativo. Casos candidatos:

- Um teste de sistema de casas precisa variar a seleção observada **mantendo data/hora/local constantes** e exigir valores reais de `H01`–`H12`, não apenas seus rótulos.
- Convenção de hora versus longitude pode produzir alias em tempo sideral; contrastar duas mudanças separadas e um canal que dependa do instante absoluto. Usar [análise condicional existente](time-longitude-identifiability.md), sem transplantar sua fórmula ao firmware.
- Para precisão e arredondamento, procurar **vários** pares de saída com mudanças pequenas de entrada, datas de fronteira e múltiplas resoluções; representar quantização e arredondamento como hipóteses rivais.
- Para a via de impressão, medir se a mesma saída aparece no LED, no papel, em fac-símile editado e no programa comparador; não presumir equivalência de formatos.

Nenhuma previsão calculada vira `observed_output`. Manter material sintético e resultados de modelos separados de `data/fidelity/observations.json`.

### O5. Executar um teste informativo, só quando houver observação elegível

O primeiro par direto deve entrar como `partial` no [corpus](fidelity-corpus.md), com campos desconhecidos em `null`. Só elevar a `replayable` se a fonte sustentar teclas literais, canal e saída completa, com revisão. Congelar um pequeno conjunto de casos como validação independente antes de calibrar parâmetros em outra amostra; não selecionar hipótese usando seu próprio holdout.

Quando houver valores angulares comparáveis, calcular diferenças circulares com convenções declaradas e **sem alterar o output histórico**. Quando não houver, declarar `NOT_RUN_NO_GOLDEN`. Não pontuar "acurácia" com figuras de autoria não atribuída ao aparelho.

### O6. Localizar implementação, apenas se e quando houver ROM ou binário

Usar o conhecimento de saída para **direcionar a inspeção de binários**: buscar tabelas de formatos, constantes, transições, periféricos e rotinas que explicariam campos concretos. Seguir o [REA upstream](https://github.com/morluto/rea/blob/main/.agents/skills/reverse-engineer-anything/SKILL.md) e o [guia de firmware](https://github.com/morluto/rea/blob/main/docs/guides/firmware/firmware-analysis.md) **somente com alvo obtido e autorizado**. Uma assinatura de Binwalk ausente em ROM plana não refuta existência de código; desmontagem para uma ISA que "faz sentido" não é identificação de CPU.

A cadeia de validação é: `bytes brutos autenticados → hipótese de hardware/ISA → função candidata → previsão de saída → observação independente`. Se o elo externo faltar, a engenharia reversa permanece documental ou comportamental, **não** emulação do firmware.

## Backlog experimental derivado da saída atual

| Prioridade | Tarefa imediata | Responsável principal | Aceite |
| --- | --- | --- | --- |
| P0 | Conferir a fig. 1 original de Carlson e o relacionamento texto–figura–DR-70, incluindo eventual fac-símile integral | 🐢 Tartaruga + 🦉 Coruja | Nota com página, o que é comprovado e o que não é |
| P0 | Catalogar literalmente os campos do output da fig. 1 **sem atribuir semântica** | 🦫 Castor + 🐝 Abelha | Tabela de tokens e posições, transcrição conferida, marcadores ilegíveis assinalados |
| P0 | Determinar se o formato é nativo do DR-70 ou pós-processado | 🦦 Lontra + 🦇 Morcego | Dois caminhos de custódia e teste de distinção, não atribuição presumida |
| P1 | Formular duas gramáticas candidatas e hipóteses para `H01`–`H12`, `KOCH` e canais de saída | 🐙 Polvo + 🦡 Texugo | Cada hipótese com observável necessário para rejeitá-la |
| P1 | Construir matriz de testes de tempo/fuso/longitude/precisão condicionados aos campos que o aparelho realmente aceite | 🦌 Cervo + 🦫 Castor | Experimentos sem output inventado, cobrindo ambiguidades e valores-limite |
| P2 | Relacionar saída autenticada a funções de código, se alguma ROM/software for recuperado | 🦊 Raposa + 🦀 Caranguejo | Evidence REA com SHA, offsets e contraprova, sem execução insegura |

O Gavião revisa se cada grau de prova corresponde ao documento e se algum resultado foi promovido indevidamente. Esta tabela não autoriza contato com operadores ou aquisição de materiais comerciais.

## Critério de conclusão desta fase

Entrega bem-sucedida **não** é um mapa astral calculado. É uma matriz auditável que responde: **qual fragmento foi literalmente observado, qual aparelho produziu qual estágio, qual hipótese permanece possível, que observação a distinguiria, e quem deve buscá-la**. Se o primeiro output bruto não for autenticável, a resposta correta é manter o alvo como parcial e procurar outro registro, sem inventar uma saída para preencher o corpus.
