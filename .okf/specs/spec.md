---
type: Spec
title: SPEC — Spec
description: Especificação do tipo OKF `Spec`, que descreve os demais tipos usados no repositório.
timestamp: 2026-11-20T00:00:00-04:00
---

# SPEC — `Spec`

Um `Spec` mora em `.okf/specs/<slug>.md` e descreve um tipo OKF: o que um conceito daquele tipo representa, o frontmatter esperado e as regras que o projeto cobra.

## Frontmatter

```yaml
---
type: Spec
title: SPEC — <Tipo>
description: <uma linha>
timestamp: <ISO 8601>
---
```

Todo tipo usado no repositório precisa de um `Spec` (`okf-parser check --require-spec .okf/specs/{slug}.md`).
