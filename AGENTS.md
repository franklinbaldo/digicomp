---
type: AgentContract
title: "Digicomp DR-70 — contrato de agentes e uso do REA"
description: "Pesquisa histórica, engenharia reversa orientada por evidências e controles para o computador astrológico Digicomp DR-70."
timestamp: 2026-11-20T21:05:00-04:00
---

# Agentes · Digicomp DR-70

**Política computacional vigente (20/11/2026):** somente sandbox própria do agente e workflows GitHub Actions em repositórios públicos. É vedado executar direta ou indiretamente em qualquer outro ambiente, inclusive para despacho/orquestração. Proteger a confidencialidade de infraestrutura pessoal do proprietário; não publicar detalhes técnicos privados. Esta regra prevalece sobre orientações históricas.

**AVISO À EQUIPE: a skill canônica deste projeto é [`.agents/skills/digicomp-rea/SKILL.md`](.agents/skills/digicomp-rea/SKILL.md). LEIA E USE A ADAPTAÇÃO LOCAL EM TODA INVESTIGAÇÃO DO DR-70, com ou sem ROM. Quando o alvo requer análise binária, a adaptação aciona a skill upstream `reverse-engineer-anything` (REA) e as referências técnicas pertinentes.**

- Origem oficial: [morluto/rea](https://github.com/morluto/rea).
- Skill upstream: `reverse-engineer-anything`. Instalação da *skill*, quando necessária e aprovada no executor: `npx skills add morluto/rea --skill reverse-engineer-anything`. A instalação **não** instala nem conecta o servidor MCP/engines.
- Procedimento local **primário e obrigatório**: [skill Digicomp](.agents/skills/digicomp-rea/SKILL.md), com [rota O0–O6: engenharia reversa pelas saídas documentadas](docs/rea-output-first.md), [ficha reutilizável](docs/rea-case-template.md) e [protocolo de evidências](docs/reverse-engineering.md).
- Use a skill original e a referência REA adequada **quando a rota exigir análise de firmware/binário/captura**. Para artigo de 1983, fotografia, cartão de instruções ou inventário sem arquivo executável, use as rotas documentais da skill local. Não instale/configure REA apenas para ler documentos.
- **Não alegar que a skill, o servidor REA, Ghidra, Binwalk, Unblob ou qualquer provider estão conectados/instalados sem conferência no executor.** Na coordenação ChatGPT desta rodada, ferramentas REA não estavam expostas.

## Quando usar e quando não usar

O projeto prioriza a **recuperação do software original** e o entendimento da máquina. **Antes de procurar uma ROM ou CPU, a rota O0–O6 parte do output já documentado.** O primeiro alvo é o cabeçalho `C1 NATAL TROP P LONG KOCH 200` e os campos `H01`–`H12`, transcritos em [exemplares-interface](docs/exemplares-interface.md) a partir da figura 1 de Carlson (*Nature*, 1985). **O artigo não certifica que a figura seja uma impressão literal do DR-70**: a hipótese de composição por outro programa precisa permanecer aberta. O segundo alvo são as legendas do display L606 do Calcuseum; elas não provam funções executadas. O corpus `data/fidelity/observations.json` segue vazio; `partial` e `replayable` exigem evidência própria. Não completar seus campos com efemérides modernas.

Cada frente primeiro documenta: fragmento literal, fonte/página, vínculo ao dispositivo, hipóteses A/B sobre formato/algoritmo, observação que as diferenciaria, e próxima prova. As rotas D1–D3 (documentos, interface, saídas) e H1 (placa/chips) funcionam **sem ROM nem REA MCP**. H2 (dump) e H3 (captura lógica) exigem arquivo e permissão concretos. Cada nova evidência gera `DR70-CASE-ID`; não inventar resultados nem inferir ausência universal de firmware.

Quando houver alvo concreto, escolher a rota:

| Alvo e pergunta | Rota REA, somente se disponibilizada pelo servidor atual |
| --- | --- |
| Dump de ROM/EPROM, firmware e regiões | `inspect_firmware_regions`; extração somente quando pedida e em diretório novo isolado, com `extract_firmware` se anunciado |
| Executável nativo e código desconhecido | `open_binary` e, conforme provider disponível, funções/pseudocódigo e referências específicas |
| ZIP/pacote de programa ou acervo digital | `open_binary` para inventário; não executar conteúdo ou supor que arquivos sejam firmware |
| Captura lógica ou de sinais já gravada | `inspect_signal_decoders` e `decode_signal_recording`, com parâmetros, canais, fonte e digest explícitos |
| Captura de rede fornecida | `inspect_web_network_capture` ou ferramenta compatível anunciada, sem reproduzir tráfego |
| Foto de placa, manual, anúncio ou saída impressa | Inspeção documental; não inferir CPU/ROM a partir de título ou aparência |

A lista é orientadora, **não** substitui descobrir os nomes/esquemas realmente anunciados no MCP. Se REA não estiver disponível, documentar `NOT_CONFIGURED`, continuar pesquisa que não requer REA e encaminhar somente a configuração necessária.

## Setup controlado

- Se o MCP já estiver conectado, usar a ferramenta apropriada diretamente e evitar `doctor` repetitivo.
- Na ausência de ferramentas, verificar o cliente e estado antes de alterar configuração. Exemplo para Codex: `npx -y rea-agents@latest doctor --client codex --json` (pode fazer download da ferramenta).
- Antes de configurar servidor ou instalar motores, gerar plano **sem escrita**, `npx -y rea-agents@latest setup --client codex --dry-run --json`, substituir o cliente real, registrar caminhos/backup e pedir autorização para alterações de configuração e instalações. Não usar `--yes` nem instalar Hopper/Ghidra/IDA/engenhos por conta própria.
- Toda computação deste projeto, inclusive REA, somente pode ocorrer na **sandbox própria do agente** ou em **workflows do GitHub Actions de repositórios públicos**. Instalação/configuração de ferramentas não autoriza outros executores, infraestrutura nova, custos ou ações produtivas.

## Procedimento e provas

1. **Identidade:** declarar pergunta, origem/licença do artefato, permissão de análise, dispositivo/exemplar, tamanho, SHA-256 dos bytes, formato e caminho local de quarentena fora do Git.
2. **Hipóteses:** distinguir `CONFIRMADO`, `RELATADO`, `INFERIDO` e `DESCONHECIDO`; nenhuma suposição automática de Z80, 6502, sistemas de casas ou efemérides.
3. **Inventário mínimo:** primeiro identificação estrutural e visão resumida; aprofundar apenas função/região/feature específica. Reutilizar Evidence e sessão, não repetir análise idêntica.
4. **Proveniência do resultado:** guardar operação, versão da ferramenta/provider, Evidence ID, offset/endereço/range do artefato, fragmento relevante, limites, conclusões e contraprovas em `docs/sources.md` ou issue.
5. **Comportamento e fidelidade:** pseudocódigo é reconstrução, não código original. Static ≠ execução; saída real exige registro de exemplar, teclas, data/hora/fuso, foto ou impressão. Se não há saída real, não anunciar emulador fiel.
6. **Encerramento:** marcar cada pergunta como respondida/parcial/não resolvida; anexar índice de evidências à issue, pedir segunda opinião. Uma busca negativa é limitada aos acervos, versões e datas consultados.

## Responsáveis e colaboração

- 🦦 Lontra (#2, #3): proveniência de ROMs, imagens, eventuais sucessores; triagem de formatos e direitos, sem executar.
- 🐙 Polvo (#4): arquitetura baseada em chips e dumps, escolha de provider apenas depois da identificação do alvo.
- 🐢 Tartaruga (#5): documentação original, manuais e saídas de época; pesquisa bibliográfica não deve disparar REA desnecessariamente.
- 🦫 Castor (#7): corpus de entradas/saídas, testes negativos, limites e concordância com artefato original.
- 🦀 Caranguejo: quarentena, hashing, ambiente isolado, plano de setup REA; não habilitar ferramentas pagas sem autorização.
- 🦊 Raposa: reconstrução Rust **após** evidência de firmware ou casos de comportamento suficientes; distinguir emulação de reimplementação.
- 🦅 Gavião: revisão de autenticidade, Evidence, custos e afirmações. Todas as mudanças deste `AGENTS.md` exigem **revisão prévia ao merge**.
- 🦉 Coruja, 🦇 Morcego, 🦌 Cervo, 🦡 Texugo, 🦎 Lagarto e 🐝 Abelha: documentação, fotos, interfaces e crítica de hipóteses dentro da própria competência, compartilhando fontes por issue.

## Limites gerais

Sem compra de aparelhos, contato com terceiros, acesso físico não autorizado, distribuição de ROM proprietária, execução de firmware desconhecido em ambiente sensível, provisionamento de custo novo ou alegação de software encontrado sem cadeia de custódia. O Git não guarda dumps históricos sem direitos esclarecidos. Provas textuais ficam no acervo OKF.

Toda mudança de produto/documentação usa PR e os testes `prek`/`okf-parser`. PR ordinária com CI verde no SHA exato pode ser integrada sem aguardar Gavião, com revisão retrospectiva; **alterações em `AGENTS.md` são exceção: parecer do Gavião ANTES do merge**. Não falsificar resultado `prek`/OKF nem usar ausência de GitHub Actions como aprovação.
