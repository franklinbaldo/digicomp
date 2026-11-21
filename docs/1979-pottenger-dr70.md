---
type: Documento
title: "DR-70 em 1979: programa preinstalado e limites da evidência"
description: "Leitura da transcrição de Mark Pottenger em 1979; funções atribuídas ao DR-70 sem inferir CPU, ROM física ou resultados numéricos."
timestamp: 2026-11-20T00:00:00-04:00
estado: provisorio
---

# O DR-70 na descrição de 1979

**Objeto:** Mark Pottenger, “Computers and Astrology”, *The Mutable Dilemma*, edição **Virgo 1979**. [Transcrição HTML hospedada em CCRS/Dodona](https://ccrsdodona.org/m_dilemma/1979/vir/computer.html); [índice editorial da edição](https://ccrsdodona.org/m_dilemma/). Em 20/11/2026, li o **corpo HTML completo**, não apenas o excerto de buscador referido em [F10](sources.md) e [L1](corporate-patents.md). A edição histórica é de 1979; a data de transcrição digital não foi estabelecida. **Não foi localizado fac-símile da revista.**

## O que o autor efetivamente descreve

No contexto de comparação com microcomputadores genéricos e fitas Matrix para PET/TRS-80, Pottenger trata o DR-70 como aparelho dedicado da **Digicomp Research Corp., Terrace Hill, Ithaca, NY 14850**. Afirma que chega pré-programado, sem alteração de programas pelo usuário comum, e que os programas residem em **“permanent memory”**. Segundo a descrição, o equipamento oferece:

- rotinas planetárias que cobririam vários milhares de anos;
- diversas opções de sistemas de casas e de padrões astrológicos;
- comparação entre mapas; portabilidade;
- limitação para armazenar grande quantidade de mapas, tornando-o menos adequado à pesquisa quantitativa;
- preço relativamente superior ao de microcomputador comum, **sem preço de tabela numérico**.

Isso é **testemunho textual contemporâneo atribuído a Pottenger**, não manual do fabricante ou teste instrumental por nós reproduzido. O texto não documenta especificação de precisão, exemplos de entrada/saída, número de opções, esquema de teclas ou quais sistemas de casas estavam disponíveis.

## Contraprovas e fronteiras de inferência

| Afirmação que parece plausível | O texto de 1979 permite concluir? | Evidência que ainda falta |
| --- | --- | --- |
| O usuário não podia editar facilmente o software de operação | **Relato contemporâneo sim**, no contexto do consumidor | Manual/instruções originais que definam modos de alteração |
| A máquina possui **ROM mascarada**, EPROMs, banco externo, CPU 6502 ou Z80 | **Não**. “Permanent memory” é expressão funcional, não identificação de chip | Fotos internas legíveis, marcações, manual técnico ou placa |
| O DR-70 possui código imutável e impossibilidade de dump | **Não**. Não reprogramável pelo usuário ≠ inacessível para preservação | Chipset, mapa de memória, método de leitura não invasivo |
| Executa precisamente Placidus, Koch, Igual, Fourier ou algoritmos modernos | **Não**. O autor só diz que há várias opções, sem nomeá-las | Manual ou saída identificada do aparelho |
| O texto oferece casos para o corpus de fidelidade | **Não**. Há classes funcionais, mas **zero pares numéricos** entrada/saída | Registros literais com proveniência e exemplar |
| O ano de lançamento foi 1979 | **Não**. Publicação em 1979 prova descrição pública até essa edição, não data de lançamento | Anúncio ou registro de fabricação com data |

**Comparador independente, não substituto:** o [índice AFA da série Nolle](https://astrologers.com/wp-content/uploads/2025/07/Index-by-Title-41-50.pdf) cita testes DR-70/ACS em outubro/1983, mas o conteúdo do artigo continua não recuperado. Não combinar a lista funcional de Pottenger com o índice de Nolle para inventar resultados instrumentais, algoritmo ou identidade da ACS.

## Protocolo de acesso e cadeia de custódia

- URL: `https://ccrsdodona.org/m_dilemma/1979/vir/computer.html`.
- Consulta direta normal com verificação TLS: **falhou** com certificado autoassinado. **Exceção somente de leitura** com `curl -k -L` **retornou HTTP 200 e 10.350 bytes de HTML** em 20/11/2026.
- SHA-256 dos **bytes HTML recebidos**: `d484f070318ec2292c45e4c321fa3f165639e055735557e4bc15f71e446988b7`. Não é hash de fac-símile de 1979, nem garante autenticidade ou imutabilidade do servidor.
- O índice do mesmo sítio identifica título, autor e edição. A transcrição pode conter erros editoriais de conversão; cotejo com impressão original continua necessário.
- Não foram copiados textos extensos ou mídia de terceiros ao Git, nem feita compra, contato com terceiros ou execução de software antigo.

## Encaminhamento

Atualizar o estado de [F10](sources.md) **após** a estabilização das PRs concorrentes que editam o catálogo; não repetir o texto original ali. Esta leitura permite criar **hipóteses de casos** para [Digicomp #7](https://github.com/franklinbaldo/digicomp/issues/7), mas não admite observações no corpus como `replayable`. Para [#2](https://github.com/franklinbaldo/digicomp/issues/2), investigar a forma física da memória sem assumir ROM específica; para [#4](https://github.com/franklinbaldo/digicomp/issues/4), manter CPU desconhecida.
