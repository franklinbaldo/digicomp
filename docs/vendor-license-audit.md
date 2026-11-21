---
type: Documento
title: "Auditoria de licenças e vendorização de referências astrológicas"
description: "Escopo e proveniência dos componentes de terceiros candidatos à preservação no Digicomp."
timestamp: 2026-11-21T10:20:00-04:00
estado: provisorio
---

# Licenças de software histórico e dependências astrológicas

**Finalidade:** preservar apenas código de referência com permissão documentada, sem
confundi-lo com a implementação original do Digicomp DR-70. A licença MIT do
repositório Digicomp **não relicencia** código ou dados de terceiros.

A avaliação abaixo é uma **triagem de arquivos e direitos declarados**, não
certificação jurídica independente nem comprovação de autoria de cada linha.
Antes de ampliar a cópia, revisar o arquivo exato e todas as dependências.

## Decisão de vendorização inicial

| Origem | Situação apurada | Decisão |
| --- | --- | --- |
| [Moira](https://github.com/TheDaniel166/moira), [LICENSE](https://github.com/TheDaniel166/moira/blob/main/LICENSE), [PROVENANCE](https://github.com/TheDaniel166/moira/blob/main/PROVENANCE.md) | MIT, com declaração do autor de implementação astronômica própria, sem código Swiss Ephemeris; assets astronômicos externos são outra camada | **Admitir somente** módulo isolado de ângulos, com licença, commit e hashes |
| [AltairSim](https://github.com/deltecent/altairsim), [LICENSE](https://github.com/deltecent/altairsim/blob/master/LICENSE) | Código próprio MIT, mas a árvore inclui licenças específicas MAME/SDL e imagens/ROMs; o Pascal-100 da Digicomp não é o DR-70 | Não copiar a árvore; investigar somente arquivo útil e sua própria cadeia |
| [ASTROLOG32](https://github.com/spara7C5/ASTROLOG32), [LICENSE](https://github.com/spara7C5/ASTROLOG32/blob/main/LICENSE), [CALC.CPP](https://github.com/spara7C5/ASTROLOG32/blob/main/CALC.CPP) | LICENSE de raiz MIT, mas CALC.CPP conserva **restrição de uso pessoal/sem venda ou lucro** sobre rotinas Neely/Erlewine e condições Swiss Ephemeris | **Não admitir CALC.CPP nem árvore inteira** como MIT; conflito exige esclarecimento |
| [Astrolog de Walter Pullen](https://github.com/CruiserOne/Astrolog), [license.htm](https://github.com/CruiserOne/Astrolog/blob/master/license.htm), [placalc.cpp](https://github.com/CruiserOne/Astrolog/blob/master/placalc.cpp) | GPL v2 ou posterior no cabeçalho moderno; arquivo também identifica Swiss Ephemeris e PLACALC de titulares específicos | Não incorporar ao núcleo MIT; manter como comparação externa |
| [tymat/astrolog](https://github.com/tymat/astrolog/blob/master/calc.c) e [initself/astrolog541g](https://github.com/initself/astrolog541g/blob/master/calc.c) | Códigos antigos registram limite **pessoal/sem exploração comercial** e edição Swiss Ephemeris antiga sob SEPL | **Não vendorizar** algoritmos Neely sob suposição de MIT |
| [Swiss Ephemeris](https://github.com/aloistr/swisseph/blob/master/LICENSE.TXT) | Duplo regime: AGPL e licença profissional comercial; cópia e integração exigem cumprimento das condições escolhidas | Não incorporar ao núcleo MIT; eventual comparador separado exige desenho de distribuição/licença |
| [PySwissEph](https://github.com/astrorigin/pyswisseph/blob/master/LICENSE.txt) | AGPL-3.0, encapsula outro código com licenciamento próprio | Não vendorizar no núcleo MIT |
| [AstroTransitMac](https://github.com/1223a80/AstroTransitMac/blob/main/LICENSE) | AGPL-3.0 | Não vendorizar no núcleo MIT |

**Aviso de proveniência:** a frase "código ligado a Michael Erlewine/James Neely"
em cabeçalho é evidência de genealogia declarada, **não** autorização de
relicenciamento e **não** prova de que o DR-70 utilizava a rotina.

## Componente admitido como referência matemática

- **Cópia exata:** `vendor/moira/_angles.py`, do commit
  `1bb9f66cde48f91cb13ebc5a715dec030d592b44` de Moira; Git blob
  `0df066cc4f9649be800e07dc784df6bed71cd144`.
- **Adaptador local mínimo:** `vendor/moira/constants.py` reproduz somente
  os fatores de conversão grau/radiano necessários; adaptado de
  `moira/constants.py` (Git blob
  `0c20adc02e2e4ca966de296106cfb19f9ac64496`).
- **Direitos preservados:** `vendor/moira/LICENSE` mantém integralmente MIT
  do titular `TheDaniel166`; `vendor/moira/UPSTREAM.json` registra commit,
  arquivos e hashes.
- **Objetivo:** referência independente para a seleção entre dois ramos de
  interseção ascendente/descendente do horizonte, não atribuição ao DR-70.
- **Fora de escopo:** ROM, dados JPL, kernels externos, tabelas proprietárias,
  código Swiss, interfaces GPL/AGPL e módulos Moira não revisados.
- **Fidelidade histórica:** `NOT_RUN_NO_GOLDEN`; nada ingressa em
  `data/fidelity/observations.json`.

A licença permite cópia e modificações **com preservação de avisos**. O código
do Moira declara derivação independente de fontes astronômicas primárias, mas
essa declaração ainda merece revisão de proveniência antes de expansão. Não
inferir que as tabelas atribuídas a Neely possam ser incorporadas
irrestritamente sem avaliar sua origem específica.

## Protocolo para futuras dependências

1. Fixar repositório, commit, arquivo, hash e URL histórica.
2. Ler licenças da raiz **e** avisos do arquivo, dados e dependências transitivas.
3. Distinguir obra original, cópia derivada, fórmula matemática e dados externos;
   não tratar forks ou republicações como permissões independentes.
4. Preservar notices, licença e arquivo original; documentar adaptações.
5. Isolar qualquer comparador moderno das rotas de autenticidade e testes golden.
6. Validar módulo vendorizado por testes e CI no commit exato; não declarar
   reproduzido um resultado do DR-70 por concordância com outro software.

**Limite:** se direitos de um arquivo permanecerem ambíguos, usar como
referência de investigação, sem copiá-lo. Licença "open source" não
significa "MIT", e visualização pública de código não é autorização irrestrita.
