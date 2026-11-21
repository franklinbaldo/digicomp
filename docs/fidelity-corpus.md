---
type: Documento
title: Corpus de fidelidade observacional do Digicomp DR-70 (v1)
description: Contrato de captura, grau epistemológico e comparação sem fabricar saídas do aparelho.
timestamp: 2026-11-20T22:01:00-04:00
estado: provisorio
---

# Corpus de fidelidade observacional v1

**Estado em 20/11/2026: zero pares autênticos de entrada → saída do DR-70 recuperados nesta frente.** Este documento especifica como registrar os primeiros, mas não inventa nenhum. O arquivo [observations.json](../data/fidelity/observations.json) nasce com `observations: []`; o contrato de dados é [corpus.schema.json](../data/fidelity/corpus.schema.json) (JSON Schema 2020-12).

## O que conta como um caso

Um caso é uma **observação histórica individual**, não uma previsão astrológica moderna. Preserve separadamente: (1) referência ao documento, imagem, vídeo ou impressão e posição exata; (2) modelo/variante/número de série efetivamente legíveis, ou `null`; (3) campos **exatamente como digitados** e teclas na ordem original; (4) caracteres, espaços, sinais, unidades e eventuais erros **literalmente mostrados** no LED ou papel; (5) explicações derivadas, se houver, sem substituir dados brutos.

No JSON, `null` significa **não observado**; não significa zero nem ausência de campo na máquina. Não reconstruir teclas, fuso, latitude, saída ou número de série por intuição. `visibility_note` descreve trechos ilegíveis. Para múltiplos quadros ou leituras, separar observações e referenciar a mesma fonte, sem concatenar um suposto display completo.

`source.directness` tem valores `device_observation` (registro visual de dispositivo efetivo), `contemporaneous_report` (testemunho/documento de época que transcreve resultados) e `secondary_report` (relato posterior). Isso classifica **a relação com a observação**, não autentica automaticamente hardware ou testemunha. `source.catalog_ref` referencia F1, F9 etc. em [sources.md](sources.md). Guardar URL e `locator` (página, quadro ou região da foto). `sha256` e `capture_date` só quando conhecidos; nunca preencher hash presumido.

## Parcial versus reexecutável

- `partial`: aceita registro autêntico incompleto, inclusive foto só do display, mas **não** entra em testes de precisão. Não preencher saídas quando a fonte não as mostra. O esquema agora recusa **casos vazios de observação**: se todos os sete campos `as_entered` e `observed_output.literal` forem `null`, uma URL, foto de gabinete ou referência bibliográfica sozinha não constitui caso do corpus. Um único literal de entrada **ou** saída basta apenas para a validação estrutural, não para autenticação histórica.
- `replayable`: exige sequência literal de teclas, canal de saída conhecido e saída literal não vazia, extraídos de observação direta ou relato contemporâneo. O esquema bloqueia a promoção de relato secundário a caso reexecutável. Além disso, revisão humana deve comprovar que todos os campos relevantes (data, hora, fuso e local, quando aplicáveis à função) foram realmente vistos; o esquema sozinho não deduz sua completude.

IDs estáveis e únicos no corpus, prefixo `DR70-`. Duplicata de mesma imagem ou citação cruzada não vira amostra independente: use um ID, cite as outras fontes nas notas ou registre a relação em issue. Uma correção de transcrição preserva histórico Git e justifica mudança; não altera silenciosamente a observação.

**Identidade literal da região (controle adicional):** dois casos com IDs diferentes não podem repetir o par exato `source.url` + `source.locator`. Quando uma mesma foto, página ou vídeo registrar eventos ou quadros realmente distintos, detalhe o `locator` com região, quadro, página e/ou instante (*timestamp*) efetivamente identificável no documento. Um único localizador genérico para duas leituras não fornece a distinção exigida; não crie sufixos arbitrários só para passar no validador. O veto compara strings literais: diferenças de grafia, espaços, maiúsculas/minúsculas, URLs de espelhos e recortes da mesma captura **não** estabelecem independência, nem são reunidos automaticamente. Na revisão de fidelidade e no holdout, agrupe manualmente por artefato original, sessão e cadeia de reprodução; múltiplos recortes de uma mesma sessão não contam como amostras independentes. O controle não autentica a fonte nem o equipamento.

## Tempo, coordenadas e referência moderna

`as_entered` contém **strings brutas**, nunca UTC nem coordenada decimal reconstituída. A indicação de fuso `+07:00` sem convenção de sinal não basta para fixar o instante. Horas ambíguas ou inexistentes por horário de verão ficam ambíguas. Só em `derived` entram `utc_candidates` (pode ser lista com múltiplos instantes), `time_model` com versão de tzdb/convenção civil, e `ephemeris_model` com versão, arquivos/flags e base temporal declarados. Se não houver informação, omita `derived` em vez de escolher uma interpretação por conveniência.

A **Swiss Ephemeris é comparador**, não origem de saída DR-70: somente após obter saída original e identificar grandeza, zodíaco, sistema de casas, época, formato e convenção angular (quando aplicáveis), calcular resíduo circular `atan2(sin(Δ),cos(Δ))` para ângulos. Antes disso, não calcular erro, taxa de acerto, compatibilidade nem alegar fidelidade. Registrar valores com precisão do display; não confundir quantização de impressão com erro instrumental.

## Controles do corpus

1. **Gate obrigatório no `prek`:** validar o JSON contra `corpus.schema.json` com `jsonschema[format]==4.26.0`, Draft 2020-12 e formatos ativados. Rejeita campos inesperados, tipos incompatíveis e `replayable` sem teclas, canal/saída ou fonte direta/contemporânea. O validador estrutural é necessário, mas não atesta a origem nem a veracidade das strings.
2. Executar `python3 -B scripts/check_fidelity_corpus.py` para recusar **IDs duplicados, pares literais `source.url` + `source.locator` duplicados, chaves JSON duplicadas em qualquer nível e números inválidos como `NaN`**. O parser JSON comum pode sobrescrever evidências silenciosamente quando uma chave se repete. O controle é local e também roda no `prek`, mas não substitui o JSON Schema nem autentica fontes; o schema continua responsável pelos tipos e pelos campos obrigatórios.
3. Conferir manualmente que a URL/locator sustentam **exatamente** o que é transcrito, mantendo `partial` quando faltarem teclas ou saída. Uma figura editorial (inclusive Carlson 1983/1985) sem vínculo demonstrado com o canal de saída do DR-70 **não** ganha status `partial` ou `replayable` por passar no esquema. As duas edições da mesma figura não são duas sessões independentes.
4. Teste negativo obrigatório: caso sintético gerado com Swiss Ephemeris deve ser rejeitado como observação histórica; exemplos inventados ficam fora de `observations.json`. Prova física/visual é diferente de benchmark astronômico.

Comandos opcionais de validação local, sem adicionar dependências ao projeto:

```bash
python -m json.tool data/fidelity/corpus.schema.json >/dev/null
python -m json.tool data/fidelity/observations.json >/dev/null
python3 -B scripts/check_fidelity_corpus.py
uvx --with 'jsonschema[format]==4.26.0' python3 -B -m scripts.check_fidelity_schema
python3 -B -m unittest discover -s tests -p test_check_fidelity_corpus.py -q
uvx --with 'jsonschema[format]==4.26.0' python3 -B -m unittest discover -s tests -p test_check_fidelity_schema.py -q
```

O validador JSON Schema (agora exigido por dois hooks de `prek`) checa estrutura e formatos. O script de identidade independente continua recusando perda de identidade por IDs ou chaves duplicados. **Nenhum desses controles autentica a fonte ou mede fidelidade numérica**; isso requer exame documental e casos históricos.

## Onde procurar o primeiro par

**F1, Calcuseum**, descreve um DR-70 serial L606 e oferece imagem das instruções, mas **não temos transcrição confiável de operação completa**: https://www.calcuseum.com/scrapbook/BONUS/10925/1.htm.

**F9, índice da AFA**, registra Richard Nolle, *The Astrologer's Computer*, parte 6, *Today's Astrologer* XLV/10, **outubro de 1983, p. 9**, como comparação DR-70/ACS. O **índice é bibliografia**, não contém os resultados testados; o artigo original permanece por recuperar via 🐢 Tartaruga #5: https://astrologers.com/wp-content/uploads/2025/07/Index-by-Title-41-50.pdf.

**Cervo #7** documentou testes de fuso/DST e um formato de entrada do programa *GAM-239/1983*; **não são** campos nem saídas DR-70: https://github.com/franklinbaldo/digicomp/issues/7#issuecomment-7053503559.

Próximo gate: quando a parte 6 original ou foto legível aparecer, abrir um caso `partial` com permalink, posição e transcrição literal. Só promover para `replayable` após conferir a sequência observada e revisão independente. Sem fotos ou saídas autênticas, a contagem continua **0**.
