---
type: Documento
title: "Modelo de caso DR70-CASE-ID"
description: "Ficha reutilizável para observações documentais, teste de comportamento, circuitos, firmware e capturas."
timestamp: 2026-11-20T21:05:00-04:00
estado: vigente
---

# Modelo de evidência: DR70-CASE-ID

**Copiar para comentário da issue temática, não preencher com dados inferidos.** Este arquivo é um molde, não uma evidência sobre o DR-70. Escrever `N/A` apenas quando o campo não é aplicável; escrever `DESCONHECIDO` quando não foi apurado.

## Identidade e pergunta

- Caso: `DR70-CASE-<ID>`
- Issue/animal responsável:
- Pergunta estreita:
- Estado: `NO_ARTIFACT` | `DOCUMENTED` | `TRIAGED` | `ANALYZED` | `CORROBORATED` | `REJECTED`
- Modelo: DR-70 | outro modelo comprovado | DESCONHECIDO
- Exemplar/serial/revisão (prova literal):
- Classe: anúncio | manual | foto | vídeo | saída | placa | ROM | executável | mídia | captura | outro
- Observação, inferência ou relato de terceiros:

## Origem e custódia

- Fonte original e URL/permalink:
- Autor, data, periódico, edição, página ou frame:
- Data da consulta / captura:
- Formato recebido e transformações:
- Direitos e consentimento para análise:
- Local de quarentena fora do Git (se houver arquivo):
- SHA-256 do **arquivo realmente recebido** (ou DESCONHECIDO):
- Tamanho em bytes do arquivo recebido (ou DESCONHECIDO):
- Digest do artefato derivado (se houver transformação):
- Como fonte/derivado se relacionam:

## Método e limites

- Método documental, teste de interface, inspeção física, REA MCP, REA CLI ou outro:
- Se REA: versão/provedor e ferramenta realmente conectados:
- Se REA: operação, `parent_evidence_id`, referências e campos paginados:
- Localização exata no alvo: página/frame/offset/range/endereço/chip:
- Amostra inspecionada e amostra **não** inspecionada:
- Obstáculo: `NO_ARTIFACT`, `NOT_CONFIGURED`, `UNSUPPORTED`, `TIMEOUT`, direitos, outro:

## Conclusões auditáveis

**OBSERVADO:** somente valores literais vistos na fonte, arquivo ou registro REA.

**RELATADO:** alegação atribuída a uma fonte identificada, sem tratá-la como constatação independente.

**INFERIDO:** implicação condicional da observação e seus pressupostos.

**DESCONHECIDO / CONTRADIÇÃO:** o que ainda não se pode concluir.

**CONTRAPROVA:** qual dado ou teste falsificaria a hipótese? Há controle de modelo concorrente?

**PRÓXIMO PASSO:** menor pesquisa com maior ganho de informação.

## Se for saída observada do aparelho

- Data/hora/fuso/local **como digitados**:
- Teclas, ordem, duração/modo **observados**:
- Versão e estado inicial do exemplar:
- LED/impressão literal:
- Unidade, precisão e arredondamento observáveis:
- Foto/vídeo, timestamp ou página:
- Comparador moderno (se houver) e erro medido **sem substituir** a saída original:

## Se for memória ou captura

- Dump integral ou parcial? Quantas faixas faltam?
- Método de leitura / voltagem / largura de palavra / interleaving / chips:
- `SHA-256` do original e de cada transformação:
- Mapeamento byte da imagem ↔ endereço lógico: provado ou hipotético?
- Regiões detectadas por REA: assinatura hipotética, limitação, bytes verificados:
- Possível ISA: alternativas e teste discriminador; **não** fazer alegação só por disassembler plausível:
- Retained Evidence: pacote exportado e restrições de redistribuição:
- Execução real do binário? SIM/ NÃO; **estática não vira dinâmica**.

## Fechamento da issue

Registrar `PASS`, `FAIL` ou `NOT_RUN` para cada teste citado, com SHA do material usado. Para revisão do Gavião, apontar especificamente os itens inferidos e as provas contrárias. Não fechar trabalho de ROM por ausência de busca em um só acervo.
