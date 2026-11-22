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

O crate possui dois binários; `default-run = "dr70-evidence-check"` preserva o comando original sem `--bin`. O workflow executa esse caminho com uma previsão descartável e verifica cinco resultados `Inconclusive`, nunca um suposto acerto da máquina. Para selecionar explicitamente o comparador lexical: `cargo run --manifest-path experiments/evidence-check/Cargo.toml --bin dr70-evidence-check -- FRAGMENTS.tsv PREDICTED.txt`.

Quando houver outputs numéricos conferidos, construir adaptadores por campo, unidade, glifo, precisão e incerteza antes de medir resíduos circulares. A divisão development/holdout será por família documental, sessão e exemplar, e não por páginas da mesma obra. Lean 4 formalizará propriedades dos modelos, não a autoria histórica da figura.

## Sondagem de layout publicado (Carlson, uma família)

A [transcrição secundária](../../docs/carlson-fig1-token-ledger.md) da figura 1 do preprint LBL-20480 (1983, página impressa -24-) relata **seis pares aparentes** de grupos de dois algarismos, H01/H07 a H06/H12. O par 1983/1985 é **uma única família editorial**, não duas amostras independentes. O arquivo [published-pairs.tsv](published-pairs.tsv) congela somente esses grupos candidatos e aponta a edição/posição e a incerteza do glifo. Ele não é dump, tabela de graus completos, entrada de sessão ou impressão autenticada.

O binário Rust `published_layout` lê a transcrição documental e emite um **protótipo de formatação, não uma saída reconstruída da máquina**. Ele compara a igualdade textual dos grupos relatados em cada par e publica sua cobertura em [published-layout-baseline.txt](published-layout-baseline.txt). O placeholder `[GLYPH_UNREAD]` foi criado pelo protótipo e não é texto da fonte. A aparente concordância 6/6 ocorre **dentro do mesmo desenho**, logo não valida o DR-70 nem é uma medição angular contra efemérides. Os campos H01/H07…H06/H12 são **pares de casas opostas**: sob a hipótese ainda não confirmada de que os grupos representem graus/minutos em casas Koch, a repetição dos dois grupos pode resultar da geometria antipodal (cúspides separadas por 180°, com signo distinto), sem constituir seis medições independentes. Essa leitura condicional foi destacada na [análise da Coruja](https://github.com/franklinbaldo/digicomp/issues/130#issuecomment-7073537253); os glifos e ângulos integrais permanecem ilegíveis. Um controle adversarial altera um dos grupos e exige diferença explícita. Saída numérica completa, teste de entrada→saída, holdout independente e corpus golden: **zero**.

```sh
cargo test --manifest-path experiments/evidence-check/Cargo.toml
cargo run --manifest-path experiments/evidence-check/Cargo.toml --bin published_layout
```

A [PR #133](https://github.com/franklinbaldo/digicomp/pull/133) incorporou na `main` uma representação documental canônica com os doze slots e um exportador `python3 -B scripts/check_documentary_observations.py --emit-rust-tsv`. A [PR #134](https://github.com/franklinbaldo/digicomp/pull/134), empilhada após esta, verifica a ponte com o catálogo. **Após a integração da #98 e a reconciliação da #131 com a `main`, o documento da #133 e a sonda Rust coexistem na mesma árvore.** Os seis registros TSV foram cotejados, byte a byte (120 bytes de dados), com as doze linhas documentais canônicas. Ainda assim, o workflow da #131 não impõe esse cotejo automaticamente; a [PR #134](https://github.com/franklinbaldo/digicomp/pull/134) acrescenta o gate de integração e precisa de CI no HEAD final. Esta coincidência textual não autentica saída do DR-70. A sonda não promove os pares a `literal` nem ao holdout. A direção atual consta da [issue #130](https://github.com/franklinbaldo/digicomp/issues/130).
