---
type: Documento
title: "AstrolDeluxe: opção retrospectiva DR-70 Minor Progressions"
description: "Pista de uma convenção de progressão nomeada DR-70 em software posterior, sem atribuição de código ou algoritmo ao aparelho original."
timestamp: 2026-11-22T04:50:00-04:00
estado: provisorio
---

# Pista funcional: DR-70 Minor Progressions no AstrolDeluxe

**Escopo:** pesquisa de genealogia de programas e hipóteses funcionais, não saída observada do Digicomp DR-70 nem código recuperado. A evidência é uma **página de funcionalidades do fabricante de um software posterior**. Não demonstra que esse software incorpora ROM, equações, rotinas ou dados do equipamento.

## Fontes e grau de leitura

| Fonte | Informação documentada | Limite |
| --- | --- | --- |
| [Halloran, funcionalidades do AstrolDeluxe v5](https://www.halloran.com/dlr5feat.htm), seção *Search to Exclude or Include Derived Charts* | O filtro de tipos de mapas salvos enumera **DR-70 Minor Progressions** separadamente de *Minor Progressions*, *Tertiary Progressions* e *Special Progressions*. | Lista de opções publicada pelo fabricante, não manual técnico, impressão histórica ou especificação numérica. |
| [Halloran, funcionalidades v6.2 descritas na página v6.3](https://www.halloran.com/dlr6feat.htm), seção *Quad Wheel* | *DR-70 Minor Progressions* aparece novamente entre os tipos que podem ser comparados ao mapa natal e às progressões secundárias. A própria página informa lançamento da v6.3 em julho de 2004. | Descreve fluxo de interface posterior; não fornece fórmula, taxas, convenção de épocas ou relação de autoria com a Digicomp. |
| [Halloran, lista de recursos atual](https://www.halloran.com/dlwin.htm), seções *Multi-Wheel Comparison Functions* e *Derived Charts* | Repete a categoria **DR-70 Minor Progressions** na ferramenta de comparação. A progressão menor genérica é descrita separadamente como um dia por mês lunar. | A taxa descrita para a opção genérica **não deve** ser copiada automaticamente para a opção rotulada DR-70. |

**Constatação limitada:** um fornecedor posterior reconhece explicitamente uma modalidade com o nome DR-70 e a distingue nominalmente de modalidades vizinhas. É uma pista de **compatibilidade conceitual ou de nomenclatura** a investigar, não continuidade provada de implementação. A repetição nas páginas do mesmo fornecedor não cria fontes independentes.

## Hipóteses rivais e observação que as distingue

- **H1, convenção herdada:** o rótulo designa uma regra de cálculo historicamente associada ao equipamento. Requer descrição técnica do método e confronto com dados de uma sessão DR-70 autenticada.
- **H2, rótulo comercial:** o nome identifica uma variante que o software implementa sem reaproveitar o algoritmo ou o programa da Digicomp. Requer documentação do fornecedor para a definição exata.
- **H3, equivalência superficial:** trata-se de um alias de progressão menor convencional, distinguido só pela interface. Requer comparar duas opções do próprio software com entradas e parâmetros iguais, incluindo regra de época, horas, latitude/longitude e arredondamento.

**Experimento proposto, ainda não executado:** obter uma especificação licitamente acessível da opção e, se possível, vetores numéricos publicados pelo próprio AstrolDeluxe, fixando nascimento, evento, fuso, modo de casas, corpo celeste e versão do programa. Comparar a modalidade *Minor Progressions* com *DR-70 Minor Progressions* por entradas iguais. Divergência entre as modalidades rejeitaria H3; igualdade em alguns vetores não demonstraria H3. Mesmo uma comparação positiva com o programa posterior não valida fidelidade do DR-70 sem saída instrumental histórica.

**Estado:** `DOCUMENTED_LATER_SOFTWARE_LABEL`; fórmula `UNKNOWN`; bytes do programa `NOT_OBTAINED`; saída DR-70 `NOT_AUTHENTICATED`; corpus golden `UNCHANGED`. Nenhum programa ou conteúdo de terceiros foi copiado ou executado.

Relacionado: [Digicomp #3](https://github.com/franklinbaldo/digicomp/issues/3) (genealogia), [#130](https://github.com/franklinbaldo/digicomp/issues/130) (baseline documental) e [fontes](sources.md).
