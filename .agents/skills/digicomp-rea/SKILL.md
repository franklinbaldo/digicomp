---
type: Documento
name: digicomp-rea
title: "Skill de projeto — REA no Digicomp DR-70"
description: "Roteamento e evidências de engenharia reversa, complementando a skill oficial reverse-engineer-anything."
timestamp: 2026-11-20T21:05:00-04:00
estado: vigente
---

# REA no Digicomp DR-70

Este é um **adaptador de projeto**, e não uma cópia da skill oficial. **Ler e seguir a skill upstream `reverse-engineer-anything` antes de usar ferramentas REA.** Fonte oficial: https://github.com/morluto/rea . Instalação de instruções, quando necessária, no cliente selecionado e com procedência conferida: `npx skills add morluto/rea --skill reverse-engineer-anything`.

A skill oficial só é apropriada quando a conclusão exige binário, firmware, pacote, captura ou comportamento executado. Ela não exige nem recomenda iniciar REA para uma consulta bibliográfica ou leitura de código-fonte completo.

## Escolha da tarefa

- **Ainda sem ROM ou binário:** continuar #1–#7 (busca de fontes, chips, entrevistas publicadas, fotos, tabelas e saídas documentadas) sem tentar desmontagem fictícia.
- **Imagem ROM/EPROM:** identificar quem obteve e autorizou; conferir hash/tamanho; inventariar `inspect_firmware_regions` quando anunciado; registrar offsets e limitações; extrair apenas se a investigação exigir e com diretório separado, seguindo o guia de firmware oficial.
- **Programa nativo antigo:** identificar formato e arquitetura com dados, depois `open_binary` + provider anunciado; se nenhum provider existe, `NOT_CONFIGURED`, não pseudocódigo inventado.
- **ZIP/arquivo de distribuição:** `open_binary` para inventário e identidade, sem disparar seus membros.
- **Captura lógica gravada de PCB/EPROM:** `inspect_signal_decoders`, depois `decode_signal_recording` com canais, protocolo e digest; não afirmar decodificação sem captura real.
- **Entradas/saídas de exemplar DR-70:** Catálogo e corpus #7; não afirmar equivalência com Swiss Ephemeris, somente comparação.

## Sequência compacta

1. Definir pergunta estreita, artefato real, permissão, versão/identidade e hipótese adversária.
2. Conferir REA **já conectado**; se ausente, plano `doctor`/setup **dry-run** na máquina autorizada. Configuração e novos motores só depois de aprovação explícita.
3. Fazer inventário resumido. Seguir Evidence IDs de um offset, função, recurso ou entrada/saída para os resultados; evitar análise total repetitiva.
4. Preencher registro `docs/reverse-engineering.md`: artefato, SHA-256, origem, licença, ferramenta/provider/versão, Evidence ID, ranges, observações, inferências, limites e próximos testes.
5. Revisar a conclusão contra outra evidência independente, preservar negativos restritos ao escopo e encaminhar ao Gavião.

Não executar firmware suspeito; não distribuir ROMs, nem comprar, contatar terceiros ou criar infraestrutura sem autorização. O Jatobá só coordena; análise pesada em executor isolado autorizado.

Referências do projeto: [AGENTS.md](../../../AGENTS.md), [procedimento detalhado](../../../docs/reverse-engineering.md), [origens](../../../docs/sources.md), [plano](../../../docs/research-plan.md).
