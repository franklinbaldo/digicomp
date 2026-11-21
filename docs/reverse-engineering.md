---
type: Documento
title: "Protocolo REA: análise e cadeia de evidências do DR-70"
description: "Procedimento de coleta, triagem e engenharia reversa responsável de firmware, software e sinais originais do Digicomp DR-70."
timestamp: 2026-11-20T21:05:00-04:00
estado: vigente
---

# Protocolo de engenharia reversa · DR-70

O objetivo é **entender o comportamento do software original do DR-70**, não produzir de início um horóscopo que apenas se pareça com a saída da máquina. **A skill de projeto [Digicomp REA](../.agents/skills/digicomp-rea/SKILL.md) é o procedimento inicial em toda investigação**, inclusive sem ROM; organiza rotas documentais D1–D3 e físicas H1–H3. A skill externa [Reverse Engineer Anything](https://github.com/morluto/rea), `reverse-engineer-anything`, é o motor para operações binárias quando o artefato existir e o REA estiver de fato conectado. A ficha reutilizável de evidência é [DR70-CASE-ID](rea-case-template.md).

## Regra principal: saída documentada → hipóteses rivais

Antes de qualquer binário, começar em [**REA orientada pela saída**](rea-output-first.md), que cataloga o cabeçalho `C1 NATAL TROP P LONG KOCH 200`, os campos `H01`–`H12` (figura 1 de Carlson, 1985, **ainda não atribuída como impressão nativa**), as legendas do display L606 e o índice de testes DR-70/ACS de Nolle. A figura não é um par input/output reexecutável; preservar `observations: []` até existir fonte com entrada e saída ligadas.

A ordem é **proveniência da saída → transcrição literal → gramática candidata → hipóteses rivais de cálculo e de pós-processamento → previsões discriminantes → teste com observações autênticas → correlação com ROM se recuperada**. A recuperação do código é objetivo, mas não precisa preceder a especificação das perguntas nem justificar um emulador genérico.

## 1. Estado dos alvos

| Categoria | Estado nesta rodada | Próximo dado necessário |
| --- | --- | --- |
| ROM, EPROM ou firmware original | **Não localizado neste acervo** | Dump com procedência, direitos e digest |
| Programa de distribuição / mídia original | **Não localizado neste acervo** | Imagem de mídia, inventário da coleção |
| Arquitetura CPU e mapeamento de memória | **Desconhecidos** | Identificação de componentes por foto de placa ou manual |
| Artigos, instruções e fotos de exemplares | **Pistas catalogadas em docs/sources.md** | Foto/scan integral com proveniência |
| Saída autêntica da máquina | **Não comprovada no corpus atual** | Teclas/entradas, saída literal, exemplar e fonte |

"Não localizado" refere-se ao acervo atual, **não** significa que não exista em outros lugares.

## 2. Checklist mínimo para receber artefato

Antes de invocar o REA, preencher em issue ou registro de evidência:

| Campo | Conteúdo esperado |
| --- | --- |
| `artifact_id` | Identificador estável no projeto; não deduzido de nome de arquivo |
| `source` | URL/permalink ou custódia do exemplar, data de obtenção |
| `authorization` | Por que é lícito analisar; direitos e restrições de divulgação |
| `original_sha256`, `size_bytes` | Hash dos bytes e tamanho; não confiar apenas no nome |
| `acquisition_method` | Digitalização, leitura de EPROM, arquivo recebido ou foto/captura |
| `location` | Caminho local em quarentena **fora do Git** |
| `question` | Uma pergunta concreta (ex.: endereço de entrada de tecla, tabela de efemérides) |
| `evidence` | Operação REA, provider/versão, Evidence ID, offset/range, limitação |
| `conclusion` | Observado, inferido, relatado ou ainda desconhecido |
| `next_test` | Uma contraprova e o artefato/dado necessário |

Dados binários e ROMs proprietárias permanecem em quarentena. No Git ficam apenas metadados, hashes, descrições próprias e testes autorizados.

## 3. Rotas por evidência

**ROM/firmware:** procurar marcas físicas e memória mapeada em fotos, caso não haja dump. Se surgir um dump com permissão, iniciar inventário de regiões com `inspect_firmware_regions` **somente se anunciado**. Para extração, usar `extract_firmware` e diretório novo explicitamente selecionado, lendo antes o guia de firmware do upstream. Não interpretar strings, sequências repetidas ou assinatura falsa como prova de CPU, nem rodar bytes desconhecidos.

**Software nativo:** confirmar formato, cabeçalho, instruções e arquitetura; usar `open_binary` e o provider disponível. Pseudocódigo de ferramenta é uma **reconstrução**, não código-fonte recuperado. Quando providers nativos estiverem ausentes, manter o registro `NOT_CONFIGURED` e a investigação de proveniência, sem emulação adivinhada.

**ZIP, fita ou imagem de disco:** inventário passivo e hash por membro quando permitido; nenhuma execução de instalador de terceiros. O REA tem rota de arquivo `open_binary`, com resultados e limites. Identificar mídia e offset do conteúdo antes de qualquer interpretação.

**Capturas de linhas de dados / sinais:** se houver captura já gravada e autorização, registrar dispositivo, amostragem, canais e timestamp; consultar decoders disponíveis com `inspect_signal_decoders`; decodificar com `decode_signal_recording`. Não confundir uma decodificação candidata com prova de protocolo sem teste de controle.

**Saída histórica:** o corpus de #7 exige exemplar, ID, entrada, sequência de teclas, data, hora, fuso, longitude/latitude como digitados, tela/impressão literal, foto/vídeo, data do testemunho e grau de confiança. Uma efeméride moderna pode medir divergência, não atestar o algoritmo original.

## 4. Resultado de uma análise REA

Para cada hipótese, registrar:

```text
Questão:
Artefato / SHA-256 / tamanho / origem e licença:
Operação REA / ferramenta / provider / versão / ambiente:
Evidence ID / offset / faixa / módulo / símbolo:
OBSERVADO:
INFERIDO:
NÃO CONFIRMADO:
Busca negativa delimitada (quais arquivos / endereços / versões foram inspecionados):
Contraprova proposta:
Decisão: conservar / aprofundar / rejeitar hipótese / aguardar novo alvo
```

Resumos da ferramenta podem omitir partes. Inspecionar a Evidence preservada por ID e páginas antes de dizer que a pesquisa cobriu o binário todo. Separar análise estática de observação de execução. Não repetir uma análise idêntica em outro agente se o mesmo digest e Evidence já foram registrados.

## 5. Distribuição por competência

| Responsável | Entrega REA pertinente |
| --- | --- |
| Lontra (#2, #3) | Inventário de ROMs/arquivos e genealogia; licença e custódia |
| Polvo (#4) | Hipóteses de ISA, placas, periféricos, mapas de memória **se houver prova** |
| Tartaruga (#5) | Manuais, folhas de comandos e artigos originais, fonte por página |
| Castor (#7) | Testes diferenciais e corpus com saída observada, sem "ground truth" inventado |
| Caranguejo | Quarentena, checksums, ferramentas isoladas e proposta de configuração reversível |
| Raposa | Emulador Rust somente após ROM/CPU ou especificação por saídas suficiente |
| Gavião | Auditoria de claims, Evidence, fontes e revisão do AGENTS antes de merge |

Coruja, Morcego, Cervo, Texugo, Lagarto e Abelha continuam com investigações documentais específicas e devem observar o mesmo esquema de proveniência.

## 6. Como preparar o ambiente sem configurá-lo automaticamente

A instalação da skill **não registra o servidor REA**. A instalação de Ghidra, Hopper, IDA, Binwalk ou Unblob também não ocorre automaticamente. O agente deve primeiro verificar se o REA está disponível na sessão e, se não, relatar o estado e preparar o plano de configuração **sem escrita**. Exemplo para Codex, após identificar o cliente real:

```bash
npx -y rea-agents@latest doctor --client codex --json
npx -y rea-agents@latest setup --client codex --dry-run --json
```

Os comandos podem adquirir pacotes e escrever cache local; conferir procedência e escopo. **Não aplicar o plano**, instalar motores, modificar MCP/IAM ou criar recursos sem aprovação. Preferir versões fixadas após avaliar a distribuição oficial. Se o REA ainda não estiver conectado, continuar trabalho histórico/documental, sem atribuir a análise ao REA.

O checkout e o CI da casa devem usar `prek`/`okf-parser`; não remover controles para facilitar documentação. Mudanças em `AGENTS.md` exigem revisão Gavião **antes** do merge.
