---
type: Documento
title: Arquitetura (provisória)
description: Possibilidades de implementação de um emulador ou reimplementação do DR-70, condicionadas ao que a pesquisa descobrir.
timestamp: 2026-11-20T00:00:00-04:00
estado: provisorio
---

# Arquitetura (provisória)

Nada aqui está decidido. A arquitetura depende de uma pergunta ainda sem resposta: **existe uma imagem do programa original?**

## Cenário A: ROM recuperada, processador conhecido

Emulação em nível de instrução, em Rust.

- Núcleo da CPU identificada pela frente 4 do plano, testado contra suítes de teste da CPU quando existirem.
- Periféricos mínimos: teclado (matriz), display de LED, chave de ligar, impressora se houver.
- Fidelidade medida pelos casos reais de `docs/research-plan.md`.
- A ROM nunca é distribuída pelo repositório sem direitos esclarecidos; o emulador a carrega de caminho local.

## Cenário B: sem ROM, com manual e saídas reais

Reimplementação comportamental: reproduz a interface (teclas, mensagens, formatos) e os resultados numéricos, inclusive arredondamentos e erros, a partir de casos de teste. Exige muitos casos reais. O resultado é documentado como reconstrução, não como emulação.

## Cenário C: sem ROM e sem saídas suficientes

Documentação histórica e simulação visual com aviso explícito de que os cálculos não são os do DR-70. É o resultado menos desejado e não deve ser apresentado como emulação.

## Escolhas de ferramenta

- Linguagem: Rust para emulador e utilitários.
- Site: `ssg` (Rust) quando houver conteúdo que justifique; sem Astro, Svelte ou frameworks pesados.
- Validação do acervo Markdown: `okf-parser`, rodado pelo `prek`.
- Execução computacional (análises, builds e testes): exclusivamente na sandbox própria dos agentes ou em workflows GitHub Actions de repositórios públicos.
