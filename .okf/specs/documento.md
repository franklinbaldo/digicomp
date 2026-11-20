---
type: Spec
title: SPEC — Documento
description: Especificação do tipo OKF `Documento`, usado pelos textos de apresentação, plano e arquitetura do projeto Digicomp.
timestamp: 2026-11-20T00:00:00-04:00
---

# SPEC — `Documento`

Um `Documento` é um texto de referência do projeto: apresentação, catálogo de fontes, plano de pesquisa ou arquitetura.

## Frontmatter

```yaml
---
type: Documento
title: <título>
description: <uma linha>
timestamp: <ISO 8601 da última revisão substantiva>
estado: <provisorio | vigente>
---
```

## Regras

- Toda afirmação histórica ou técnica deve indicar a fonte ou ser marcada como hipótese.
- `estado: provisorio` sinaliza texto que pode ser reescrito sem aviso nas primeiras rodadas.
