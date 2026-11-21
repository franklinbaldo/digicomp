---
type: Documento
name: digicomp-rea
title: "Skill Digicomp — engenharia reversa investigativa do DR-70"
description: "Método executável de investigação do aparelho, código histórico, comportamento e hipóteses, adaptado da skill REA."
timestamp: 2026-11-20T21:05:00-04:00
estado: vigente
---

# Digicomp: engenharia reversa do DR-70

**Esta é a skill canônica do projeto.** O ponto de partida é **o que queremos provar sobre o DR-70**, não qual ferramenta parece interessante. Foi concebida a partir da [skill REA `reverse-engineer-anything`, versão 63 consultada](https://github.com/morluto/rea/blob/main/.agents/skills/reverse-engineer-anything/SKILL.md) e de suas referências. Usar a skill oficial como manual técnico do motor, lendo a referência pertinente **quando** uma análise REA for necessária. Esta adaptação é própria do Digicomp; não copia nem substitui a implementação REA.

## Missão e perguntas investigativas

A pergunta central é: **qual software executava o DR-70, por quais operações e com que saídas?** Trabalhar de trás para a frente a partir dos artefatos e observações que existem.

As hipóteses de trabalho não são resultados:

1. **Máquina:** o exemplar em questão é de fato um DR-70, de qual versão, data e configuração? Não misturar modelos DR-70, Astrion/Astrio 80, Pascal-100 ou Delphi-100.
2. **Programa:** há ROM, EPROM, fita, mídia, listagem, tabela de efemérides, manual técnico ou software descendente? Distinguir software localizado de menção a software.
3. **Entradas:** que teclado, chaves, sequência de estado, formatos de data, hora, fuso, latitude e longitude o aparelho aceitava?
4. **Cálculo:** quais resultados observáveis, precisões, arredondamentos e limites cronológicos? A Swiss Ephemeris é apenas contraponto moderno.
5. **Saídas:** LED, mensagens, ordem das telas, impressão, valores intermediários e erros, com fotografia/filmagem e proveniência.
6. **Implementação:** qual CPU, chipset, mapa de memória, codificação, dados constantes e interfaces? Não presumir CPU por nome do produto.

A missão não é programar um gerador genérico de mapas astrais; só anunciar **emulação do original** com prova de firmware/ISA e periféricos, ou **reconstrução comportamental** com corpus suficiente. Sem isso, produzir pesquisa histórica, não um emulador alegado.

## Fase 0 — classificar o pedido ANTES da ferramenta

| O que temos | Pergunta legítima | Próximo passo | REA MCP agora? |
| --- | --- | --- | --- |
| Catálogo, reportagem, anúncio, patente, depoimento | O que a fonte realmente afirma? | Transcrição curta, URL, data, grau de evidência e contradições em `docs/sources.md` | **Não** |
| Manual / cartão / foto ou vídeo da máquina | Que entradas e saídas são visíveis? | Mapa de teclas/estados e caso de teste **observado**, com referência à imagem | **Não**, salvo componente binário real |
| Placa fotografada e marcações legíveis | Que chip e interconexões podem ser identificados? | Inventário do componente; datasheet e revisão cruzada; sinalizar regiões ocultas | **Não** para fotografia |
| ROM/EPROM/dump de memória | Quais bytes, vetores, tabelas e código são identificáveis? | Proveniência, direitos, hash, análise passiva focal do dump | **Talvez**: REA firmware, com limitações |
| Programa antigo nativo / imagem de mídia | O que está dentro e como se vincula ao DR-70? | Inventário do arquivo, sem executar; depois arquitetura identificada | **Sim, se suportado** |
| Captura lógica já existente | Que protocolo ou tráfego ela demonstra? | Fonte, canais, taxa, digest, decoder e janelas | **Sim, se suportado** |
| Apenas uma suposição | Que evidência falta? | Gerar checklist de aquisição e contraprova; não gerar resultados | **Não** |

`NO_ARTIFACT` significa nenhum alvo encontrado **nas fontes consultadas**, não inexistência universal. `NOT_CONFIGURED` significa provider/REA ausente; não é prova de que o artefato seja indecifrável.

## Fase 1 — criar ficha de investigação

Para cada artefato ou observação, abrir/atualizar a issue existente e preencher o formulário sem campos fictícios:

```text
DR70-CASE-ID: [identificador único]
Pergunta específica:
Classe: documento | foto | exemplar | saída | ROM | mídia | binário | captura
Exemplar/modelo/revisão/serial: [desconhecido se não visível]
Fonte e acesso (URL, data, localização lógica e pessoa autora):
Direitos/consentimento/limites de distribuição:
Bytes originais: [SHA-256 e tamanho apenas se arquivo recuperado; senão N/A]
Cadeia de custódia: [quem capturou, quando, como, se houve transformação]
Hipótese principal + rival:
Procedimento (ferramenta e versão, somente se executada):
Evidence ID / página / frame / offset / bit / região:
OBSERVAÇÃO LITERAL:
INFERÊNCIA CONDICIONAL:
ALTERNATIVAS E CONFLITOS:
ESCOPO NÃO INSPECIONADO:
Contraprova mínima:
Estado: NO_ARTIFACT | DOCUMENTED | TRIAGED | ANALYZED | CORROBORATED | REJECTED
Responsável e issue:
```

**Proibição:** não inventar `sha256` de URL, não confundir hash da página com hash do firmware, nem dizer que uma foto publicada mostra determinada placa se ela só mostra o gabinete. Toda saída extraída/transformada tem digest próprio e vinculação explícita ao original.

## Fase 2 — laboratório documental e de comportamento (já executável SEM ROM)

### Rota D1: fontes de 1977–1984 e genealogia

Prioridades: fonte de 1979 F4; artigos de Richard Nolle, *The Astrologer's Computer*, partes 5 (set/1983, hardware DR-70), 6 (out/1983, teste DR-70/ACS) e 14 (mai/1984, impressora/Astrion 80); cartão de instruções do Calcuseum; catalogação do Computer History Museum, relatos brasileiros e Quigley. Os **índices** apenas identificam artigos, não validam seu conteúdo.

Para cada documento: periódico/edição/página, transcrição curta com localização, aparelho referido, valor numérico literal quando presente, se o autor testou a máquina ou citou terceiro e possível relação com outro modelo. Resultados negativos registram termos, acervos e datas; não afirmar ausência de ROM em coleções não examinadas.

### Rota D2: interface e máquina de estados

A partir de fotos/vídeos autênticos, elaborar **tabela de observação**, não um teclado imaginado:

```text
estado_anterior | tecla/posição | duração e ordem | LED/impresso literal
estado_posterior | evidência (frame/página) | desconhecidos
```

Mapear cada tecla legível, Shift/ligar, modos, confirmação de entrada e mensagens de erro. Marcar `não visível` para o que imagem não mostra. Nunca deduzir que um botão faz determinada operação apenas pelo rótulo. Se houver máquina acessível com permissão futura, planejar testes diferencialmente, mas **não acionar terceiros nem hardware nesta fase**.

### Rota D3: saída astronômica e precisão histórica

Criar casos sob [`#7`](https://github.com/franklinbaldo/digicomp/issues/7): data/hora/local/fuso **conforme digitados**, sequência de teclas, configuração, saída literal, exemplar, edição de software, imagem, nível de certeza. Separar dados observados de transcrição derivada. Somente depois comparar com efemérides modernas, calculando erro sem "corrigir" o DR-70.

Experimentos futuros devem variar **uma entrada por vez**: fuso, meia-noite, data-limite, hemisfério, limites de longitude, casas, minutos e arredondamento. Caso inexistam saídas primárias, registrar `NO_GOLDEN_OUTPUT` e **não** fabricar fixture como se fosse real.

## Fase 3 — análise física de hardware e firmware

### Rota H1: placa e componentes

Inventariar em `#4`: foto de face/verso, resolução, data, procedência, marcações **legíveis**, datasheets públicos, número/local de ROM/EPROM e sinais entre periféricos. Gerar diagrama de conexões apenas de trilhas visíveis ou medidas reais; marcações incompletas permanecem candidatas. Chips de outros computadores Digicomp **não** identificam a CPU do DR-70.

### Rota H2: dump real, análise passiva com REA

**Somente após** origem/licença, SHA-256, tamanho, aquisição e quarentena fora do Git. Preservar a imagem bruta; não regravar sobre a cópia. Checar em primeiro lugar formato, preenchimentos, regiões repetidas, endereçamento e hipóteses de largura de palavra/ordem dos bytes, com testes que possam rejeitá-las.

No REA conectado, consultar ferramentas anunciadas. Para firmware encapsulado, `inspect_firmware_regions` via Binwalk pode dar hipóteses de regiões. **Importante para DR-70:** ROM antiga sem contêiner pode não ter assinaturas reconhecíveis. Ausência de detecção de Binwalk **não** equivale a ROM vazia ou ilegível. Binwalk 3.1.x/Unblob 26.6.x, segundo guia upstream, focam inspeção/extracção de firmware e dependem de executores compatíveis; Unblob não deve ser aplicado cegamente a ROM plana.

`extract_firmware` apenas para formato/região **identificado** e quando houver necessidade, em diretório novo, com origem/offset e hashes registrados. Se aparecer um executável nativo suportado, `open_binary` + engine anunciada (Hopper/Ghidra/IDA/Kuna) para análise focal. **Não** passar ROM arbitrária como ELF/PE nem escolher ISA com base em disassembly "que parece funcionar".

Tentar duas hipóteses concorrentes para vetores/tabelas, distinguir observação de função inferida; exigir ligação ao hardware ou a saídas reais antes de declarar algoritmo original. Exportar Evidence completa, não apenas sumário compactado; registrar origem e faixa dos bytes e qualquer transformação.

### Rota H3: captura lógica gravada

Para sinais previamente adquiridos com autorização: informar amostragem, canais, dispositivos e digest; consultar `inspect_signal_decoders`, depois `decode_signal_recording` com decoder específico. Uma anotação candidata não é confirmação de protocolo; comparar com oscilograma ou sequência de teclas conhecida. REA **não faz captura física**: sem arquivo, sem decodificação.

## Fase 4 — compatibilidade e modelos divergentes

Diferenciar os aparelhos pelo **modelo atestado**. Um recurso do Astrion 80, um manual ACS, software de Unix/PC ou algoritmo moderno são comparadores, **não** herança comprovada do DR-70. Para alegar genealogia, requerer pelo menos um dos seguintes elos: documentação contemporânea de port, identificação de desenvolvedor e código correlato, binários com identidade suficiente, ou tabela numérica idêntica com independência demonstrada. Sem isso, "semelhança" é hipótese.

Duas rotas de implementação são excludentes quanto ao rótulo:

- **Emulador de firmware:** dump autorizado + ISA/periféricos caracterizados + replay de software original com teste.
- **Reconstrução comportamental:** casos reais suficientes, comparação reprodutível e identificação explícita das lacunas.
- **Demonstração visual:** interface histórica sem reivindicação de algoritmo original.

## Fase 5 — gates e handoff

Antes de PR ou declaração pública:

1. **Evidência:** cada alegação tem documento/foto/frame/byte-range/Evidence ID real; fontes de segunda mão não viram primárias; nenhuma prova circular.
2. **Cobertura:** declarar bytes, regiões, páginas, membros e estados **não** inspecionados. Um dump parcial não prova ausência de outro módulo.
3. **Contraprova:** ao menos um teste discriminador para hipótese principal, mesmo que ainda não executável. Para regressão, demonstrar falha do mutante que remove a proteção.
4. **Custódia:** bytes e imagens originais intactos; sem ROM proprietária versionada, sem executar binário suspeito, sem segredos, contatos ou custos não autorizados.
5. **Reprodutibilidade:** ambiente, versão/provider, SHA do alvo, caminhos, testes rodados e resultados **PASS/FAIL/NOT_RUN**, sem atribuir execução não realizada.
6. **Revisão:** Gavião examina claims e Evidence; alterações em `AGENTS.md` exigem seu parecer **ANTES** do merge. Mudanças ordinárias seguem política vigente por SHA.

**Entregável mínimo de qualquer animal:** uma [ficha `DR70-CASE-ID`](../../../docs/rea-case-template.md) por nova evidência, um resultado negativo delimitado ou positivo sustentado, e o próximo teste mais barato que aumente a informação. Consolidar no [Cafezinho #8](https://github.com/franklinbaldo/digicomp/issues/8), sem abrir issue duplicada.

## Como REA se encaixa de verdade

A skill oficial possui ferramentas de investigação e orientação de conexão. O uso local preserva seu contrato: **skill instalada ≠ MCP conectado ≠ provider disponível**. Ler a [skill original](https://github.com/morluto/rea/blob/main/.agents/skills/reverse-engineer-anything/SKILL.md) e a [referência de firmware](https://github.com/morluto/rea/blob/main/docs/guides/firmware/firmware-analysis.md) na operação binária pertinente. Se REA estiver conectado, usar schemas reais; não rodar `doctor` antes de cada inspeção. Se faltar, verificar bloqueio e ler o [guia de recuperação](https://github.com/morluto/rea/blob/main/.agents/skills/reverse-engineer-anything/references/connection-and-recovery.md), preparar plano sem escrita e pedir aprovação para instalação/configuração.

Execução pesada: Ifro ou executor isolado autorizado, Jatobá somente como orquestrador. Nenhuma instalação de software pago, MCP, IAM ou infraestrutura nova sem autorização. Documentação [protocolo](../../../docs/reverse-engineering.md), [fontes](../../../docs/sources.md), [plano](../../../docs/research-plan.md), [backlog](../../../docs/backlog.md).
