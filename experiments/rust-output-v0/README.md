---
type: Documento
title: "DR-70: primeiro gerador experimental de campos H01–H12"
description: "Duas hipóteses rivais em Rust, com entrada idêntica e sem alegação de fidelidade ao aparelho."
timestamp: 2026-11-21T00:00:00-04:00
estado: experimental
---

# Primeiro gerador de saída, não um emulador

O corpus canônico `data/fidelity/observations.json` está vazio. A figura 1 de Carlson (1985) tem uma transcrição documental do cabeçalho `C1 NATAL TROP P LONG KOCH 200` e identificadores `H01`–`H12`, **sem** vínculo instrumental completo de entrada → teclas → saída. Este protótipo não copia esse cabeçalho como se fosse uma emissão do DR-70, não interpreta `KOCH`, não calcula efemérides nem simula teclado.

O argumento `--ascendant` é um **valor de referência fornecido pelo experimentador**, em graus e centésimos, não uma entrada histórica certificada. Os dois modelos usam exatamente esse mesmo valor:

- `equal`: H01 = ascendente; demais campos espaçados em 30°.
- `whole-sign`: H01 = começo do signo de 30° que contém o ascendente; demais campos espaçados em 30°.

Esses dois modelos representam uma **ablação útil**: a presença dos mesmos doze rótulos não identifica a regra matemática. Nenhum deles é alegado como algoritmo do DR-70 ou sistema KOCH.

```sh
cargo test --manifest-path experiments/rust-output-v0/Cargo.toml
cargo run --manifest-path experiments/rust-output-v0/Cargo.toml -- --ascendant 15.25 --model equal
cargo run --manifest-path experiments/rust-output-v0/Cargo.toml -- --ascendant 15.25 --model whole-sign
```

Para a mesma entrada `15.25`, os primeiros campos são respectivamente `H01 015.25` e `H01 000.00`; ambos os resultados são **SYNTHETIC**, nunca `observed_output`. Em `proofs/CandidateAmbiguity.lean`, Lean 4 verifica que os candidatos divergem nessa entrada e coincidem em um limite de signo. Execute com `lean proofs/CandidateAmbiguity.lean` se Lean 4 estiver instalado. A prova não identifica qual algoritmo o aparelho utilizava.

Próximo marco: obter uma entrada registrada por teclas e sua saída do **mesmo DR-70**, fixar a transcrição literal como golden independente, e só então avaliar hipóteses de efemérides/tempo/local/formatador. Sem isso, o status permanece `NOT_RUN_NO_GOLDEN`.
