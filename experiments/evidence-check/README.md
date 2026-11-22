---
type: Documento
title: "DR-70 — verificador Rust de evidência parcial"
description: "Comparação lexical de fragmentos preservados, sem alegar fidelidade da ROM ou criar golden sintético."
timestamp: 2026-11-21T00:00:00-04:00
estado: experimental
---

# Saídas antigas primeiro, hipóteses depois

Este instrumento parte da orientação do proprietário: **recolher saídas astrológicas disponíveis na internet**, preservá-las progressivamente e só depois ajustar modelos concorrentes em Rust e formalizar invariantes em Lean 4.

Este diretório é independente da [PR #92](https://github.com/franklinbaldo/digicomp/pull/92), que produz candidatos de doze campos H01–H12. A [PR #94](https://github.com/franklinbaldo/digicomp/pull/94) acumula as fontes publicadas, inclusive vinte mapas listados no livro *Astrological Aspects*. O catálogo amplo aceita candidatos sem entrada original e pistas ainda sem imagem. O **corpus de fidelidade** continua `observations: []`.

`fragments.tsv` lista fragmentos já documentados na [transcrição crítica Carlson](../../docs/carlson-fig1-token-ledger.md) e no [inventário do Calcuseum](../../docs/exemplares-interface.md). Eles são classificados como `candidate` ou `lead`, logo **sempre produzem Inconclusive**. Um token compartilhado por um modelo novo não prova que o DR-70 gerou aquele mesmo output.

O mecanismo `literal` compara linhas completas *exatamente*, sem normalização, e é coberto por testes falsos `FAKE` apenas em memória. Para inserir um caso real `literal`, exige-se fonte e revisão documental que sustentem a frase transcrita; o token não deve ser colocado no holdout se tiver sido usado no desenvolvimento. A comparação lexical identifica discrepâncias, não compatibilidade algorítmica. Um par real entrada → saída será necessário para fazer um teste funcional.

```sh
cargo test --manifest-path experiments/evidence-check/Cargo.toml
cargo run --manifest-path experiments/evidence-check/Cargo.toml -- experiments/evidence-check/fragments.tsv caminho/para/saida-candidata.txt
```

Quando houver outputs numéricos conferidos, construir adaptadores por campo, unidade, glifo, precisão e incerteza antes de medir resíduos circulares. A divisão development/holdout será por família documental, sessão e exemplar, e não por páginas da mesma obra. Lean 4 formalizará propriedades dos modelos, não a autoria histórica da figura.
