---
type: Documento
title: "Digicomp DR-70 — portas de decisão para reconstrução e testes"
description: "Critérios conservadores de emulação por instrução e reconstrução comportamental, sem atribuir firmware ou saídas inexistentes ao DR-70."
timestamp: 2026-11-20T21:12:00-04:00
estado: provisorio
---

# Portas de decisão para reconstruir o DR-70

**Fatia 🦊 Raposa**, solicitada na [missão #26](https://github.com/franklinbaldo/raposa/issues/26), em colaboração com [Polvo #4](https://github.com/franklinbaldo/digicomp/issues/4), [Castor #7](https://github.com/franklinbaldo/digicomp/issues/7) e [software #2](https://github.com/franklinbaldo/digicomp/issues/2). **Estado em 20/11/2026:** não há ROM DR-70 recuperada, CPU autenticada ou par reexecutável de entrada/saída original no corpus. Hoje a única rota fundamentada é **C: documentação**. Não iniciar calculadora astrológica substituta.

A [PR #28](https://github.com/franklinbaldo/digicomp/pull/28) propõe protocolo REA, skill-ponte e AGENTS.md, ainda sujeitos a revisão **pré-merge**. Esta PR não toca no contrato, não instala REA, não analisa ROM e não presume a integração da #28. O [plano](research-plan.md), a [arquitetura provisória](architecture.md) e o [corpus de fidelidade](fidelity-corpus.md) continuam normativos.

## Árvore de decisão em duas fases

1. **A: estudar emulação por instrução.** Há imagem do programa original com origem, autorização, tamanho, SHA-256 e cadeia de custódia; CPU/ISA, byte order, mapa de endereços, bancos e periféricos corroborados por evidência independente? Só então planejar em Rust núcleo da CPU e periféricos. Um dump parcial ou disassembly plausível não demonstra ISA; chip de outro modelo Digicomp não atesta o DR-70. **Estudar ≠ emulador fiel**: para compatibilidade, exigir testes independentes de instruções, boot isolado e replay autêntico de operações.
2. **B: estudar reconstrução comportamental.** Se A não estiver fundamentada, há registro original com entrada, estado inicial, sequência de teclas e saída literal, fonte e posição precisas? Só então formular modelos concorrentes e testes diferenciais. Um único caso autoriza pesquisa, mas **não** declara algoritmo, precisão ou compatibilidade. Implementação numérica pede diversidade de casos e holdout realmente independente, definida com Castor #7. Não ter localizado ROM não prova sua inexistência.
3. **C: continuar documentação.** Sem A e B, registrar documentos, fotos e negativos delimitados; interface visual apenas quando atestada, sem apresentar saídas simuladas como originais. Este é o estado atual. Uma fonte repetida não vira outra observação independente.

**Fase 2 (independente da escolha):** nenhuma rota libera automaticamente software, execução de firmware, publicação de ROM, promessa de fidelidade ou compra/contato. Toda mudança de estado científico requer revisão da fonte primária e resultados observados fora da ferramenta de triagem.

## Critérios de aceite para função recuperada

Cada suposta função do programa deve ligar **bytes → hipótese → comportamento**, com trilha auditável:

- **Artefato:** Evidence ID, URL/detentor, método de obtenção, direitos, tamanho, SHA-256 de bytes recebidos, intervalos de offset, chip/orientação e mapeamento dos bytes ao endereço lógico; listar regiões ausentes ou divergentes.
- **Interpretação:** ISA, endianness, largura de palavra, tabela de endereços e periféricos corroborados por foto, datasheet ou teste independente. Hipóteses concorrentes devem ter teste capaz de refutá-las. Pseudocódigo de REA/desassembler é **inferência**, não fonte do fabricante.
- **Comportamento:** foto/vídeo/página, número de série se visto, data/hora/fuso/local **como digitados**, teclas em ordem, estado inicial, display/impresso **literal**, convenção angular e precisão quando observável; separar conjunto de desenvolvimento de holdout independente.
- **Conclusão:** rotular separadamente OBSERVADO (fotografia/bytes), INFERIDO (modelo), RECONSTRUÍDO (código autoral) e NÃO TESTADO (sem golden original). Identidade de saída não demonstra identidade interna de algoritmo.
- **Direitos e segurança:** nunca executar imagem desconhecida fora de isolamento, não versionar ROM proprietária sem direitos esclarecidos, nem instalar engines REA silenciosamente. O servidor/skill REA só será usado com artefato real e ferramenta conectada.

## Matriz adversarial para Polvo e Castor

| Ponto | Futuro teste discriminante | Confusão a detectar |
| --- | --- | --- |
| ROM/CPU | Marcação física de chip, bancos, leituras independentes e mapeamento de endereço | ISA suposta por disassembly ou ROM do sucessor |
| Calendário | 28/29 fevereiro, anos 1900/2000 e virada do dia, se aceitos pelo original | Gregoriano/juliano ou regra bissexta presumidos |
| Hora e fuso | UTC documentado, sinal do fuso, DST gap/fold e mudanças isoladas de longitude | Conversão prematura que esconde duas horas possíveis |
| Localização | Norte/sul, leste/oeste, zero e uma coordenada variada de cada vez | Convenção invertida ou localização imaginada |
| Efemérides | Sistema de casas, zodíaco, TT/UT, geocentria/topocentria, quando documentados | Concordância numérica casual de fórmulas diferentes |
| Display e impressão | Limiares de arredondamento, carry 59→00, zero negativo, 359°→0° | Truncamento confundido com arredondamento ou unidade |

Esta matriz **não registra funções comprovadas do DR-70**. São perguntas para aplicar apenas quando documentação ou exemplar mostrar os campos. Swiss Ephemeris é comparador de erro, não fonte de golden DR-70; não ajustar tolerância após olhar o resultado.

## Infraestrutura sintética já disponível nesta PR

[O script de triagem](../scripts/reconstruction_gate.py) aceita um JSON de **metadados declarados**, sem abrir ROM, e retorna A_INSTRUCTION_STUDY, B_BEHAVIOR_STUDY ou C_DOCUMENTATION. Para A exige digest com formato SHA-256, IDs, custódia, autorização de análise e arquitetura corroborada. Para B exige registro com teclas/saída literais, fonte direta ou contemporânea, locator, revisão da fonte e marcador não sintético. **Isso é filtro estrutural, não prova de autenticidade:** um declarante pode mentir; um hash de 64 caracteres não verifica os bytes. Ambos os flags approved_for_emulation e approved_as_authentic_dr70 são sempre false.

[Os 15 testes](../tests/test_reconstruction_gate.py) são inteiramente sintéticos, com nomes FAKE. Incluem C sem evidência, A incompleta, ausência de CPU/ROM, digest inválido, direitos ausentes, B sem teclas, notícia secundária, saída marcada sintética, fonte não revisada, tipos inválidos, trilhas A/B propostas e **nenhuma aprovação automática**. Não são resultados DR-70.

Comandos para teste local:

    python3 -B -m unittest discover -s tests -p test_reconstruction_gate.py -v
    printf '{"observations":[]}' > /tmp/dr70-no-evidence.json
    python3 -B scripts/reconstruction_gate.py /tmp/dr70-no-evidence.json

**Aceite da fatia:** três arquivos texto sem ROM, 15 testes sintéticos, dados vazios ⇒ C_DOCUMENTATION, zero autorização automática, Prek/OKF no HEAD exato quando o executor permitir. **Aceite de emulador futuro** exige A inspecionada, testes de CPU/periféricos, replay real independente, isolamento, direitos e revisão. Até lá, documentação é um resultado válido.
