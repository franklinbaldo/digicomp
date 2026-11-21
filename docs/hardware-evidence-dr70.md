---
type: Documento
title: Auditoria de arquitetura do DR-70
description: Evidências separadas por modelo e plano de identificação sem suposições sobre a CPU.
timestamp: 2026-11-20T19:45:00-04:00
estado: provisorio
---

# DR-70: o que se sabe do hardware

**Frente:** [Digicomp #4](https://github.com/franklinbaldo/digicomp/issues/4). Pesquisa documental realizada em 20/11/2026, sem exame físico, aquisição, contato com colecionadores ou execução de firmware. Este laudo não atribui CPU ao DR-70.

## Fontes e objetos distintos

| Fonte | Aparelho | Evidência efetivamente sustentada | Limite de atribuição |
| --- | --- | --- | --- |
| [Calcuseum, exemplar L606](https://www.calcuseum.com/scrapbook/BONUS/10925/1.htm) | **DR-70** | Catálogo descreve LED, série L606 e cinco fotografias externas; registra 1977 como data de introdução | A página não identifica CPU, placa interna, ROM nem data documental de fabricação |
| [Deskthority](https://deskthority.net/viewtopic.php?t=20346), [álbum associado](https://imgur.com/a/4HgqT57) | **DR-70** | Comprador relata switches MEI/WEAB, chave de ignição, shift iluminado e teclas double-shot | Relato de proprietário, não inspeção nossa de chipset |
| [Telcontar: MEI T-5](https://telcontar.net/KBK/MEI/T-5) | Switch associado ao **DR-70** | Catálogo técnico de variantes lista teclado DR-70 como ocorrência WEAB, sem part number completo | Identificação de switch não identifica CPU, ISA ou memória |
| [Fórum Oric, 10/07/2019](https://oric.forumactif.org/t730-un-oncle-cousin-de-l-oric) | **Astrion System 80**, descrito como sucessor | Pessoa que abriu um Astrion relata CI 74LS, RAM, muitos ROMs, chip **6522**, impressora e tela | **Não é um DR-70**; 6522, ROMs e suspeita de CPU 6502 não podem ser transferidos |
| [*Electronics*, 18/12/1980, p. impressa 132](https://www.worldradiohistory.com/Archive-Electronics/80s/80/Electronics-1980-12-18.pdf) | **Pascal-100**, Digicomp Research em Ithaca | Nota contemporânea descreve CPU dupla S-100, Z80-type e Pascal Microengine | Não prova que o DR-70 usa Z80 ou S-100 |
| [*Electronics*, 07/04/1982, p. impressa 170](https://www.worldradiohistory.com/Archive-Electronics/80s/82/Electronics-1982-04-07.pdf) | **Delphi-100**, Digicomp Research, Terrace Hill/Ithaca | Reportagem contemporânea descreve **Z80A e Motorola 68000**, S-100 e interfaces | Não prova que o DR-70 usa Z80A/68000 |
| [Michael Erlewine, *Some History of Matrix Software*](https://www.astrologyland.com/E-Books/pdf/matrix_history.pdf) | **DR-70** | Memória pessoal de concorrente à época descreve máquina dedicada, fechada, custosa, existente no início dos anos 1980 | O qualificativo `hard-wired` não prova lógica dedicada, tipo de ROM nem CPU |
| [Índice AFA, *Today's Astrologer*](https://astrologers.com/wp-content/uploads/2025/07/Index-by-Author-41-50.pdf) | **DR-70** | Richard Nolle, *The Astrologer's Computer*, parte 5, XLV/9, setembro/1983, p. 14: **hardware do DR-70**; parte 6, XLV/10, outubro/1983, p. 9: comparação | Índice é metadado, não artigo técnico completo |

**Controle epistêmico:** publicações *Electronics* e Erlewine foram consultadas por texto indexado/extraído de PDFs; tentativas de screenshot dessas páginas falharam (403/timeout). A leitura textual do fórum não autentica visualmente as marcações dos chips no Astrion. As fontes inspecionadas **não apresentaram foto interna identificável como DR-70**: negativo deste conjunto de consultas, não prova de ausência em todo o acervo público. Também não se deve tratar catálogo com foto como inspeção física independente do exemplar.

## Placa elétrica fotografada do exemplar L606 (nova observação)

A [foto externa da etiqueta no Calcuseum](https://www.calcuseum.com/scrapbook/BITMAP/BONUS/10925/_SMD47726.JPG), associada pela [página do exemplar L606](https://www.calcuseum.com/scrapbook/BONUS/10925/1.htm), permite ler **115 V**, **60 Hz**, **LINE FUSE 0.75 A** e **60 WATT (MAX)**. A etiqueta também mostra **DIGICOMP RESEARCH CORP.**, **TERRACE HILL, ITHACA, N.Y.** e número de série compatível com **L606**. **Grau:** transcrição visual de imagem publicada por acervo, não medição elétrica, desmontagem ou verificação independente do aparelho; a imagem tem resolução reduzida e a identificação do modelo está parcialmente cortada.

**Consequência de conservação:** uma unidade com essa etiqueta **não deve ser ligada diretamente a uma tomada de 220 V** nem alimentada para testes sem exame prévio por pessoa qualificada da fonte, fusível, isolamento e estado dos componentes. A placa informa a alimentação nominal **do exemplar fotografado**, não as tensões internas, revisão de placa, CPU, ROM ou compatibilidade elétrica de todos os DR-70. O valor do fusível **não é** um limite de corrente para programadores/leitores de memória. Fotos de conectores e da placa (sem energizar) continuam sendo o próximo passo seguro.

## Estado da arquitetura do DR-70

**Relatado sobre o DR-70:** display LED, switches MEI/WEAB, chave e gabinete fechado. **Desconhecido:** processador/ISA, ROM/EPROM, tamanho e mapa de memória, firmware, barramento, lógica de display, interfaces externas e método seguro de dump. **Observado exclusivamente em outros modelos:** chip 6522/ROM/RAM no Astrion (relato); Z80-type/Pascal Microengine no Pascal-100 e Z80A/68000 no Delphi-100 (imprensa de época). Não iniciar emulador de CPU ou anunciar recuperação de ROM com base nesses outros produtos.

## Protocolo de identificação futura

1. Sem energizar, obter fotos da **placa do DR-70** inteiro e frente/verso, etiqueta de modelo e série, silk-screen, conectores e revisão; registrar proveniência do exemplar/fotógrafo e data.
2. Transcrever literalmente os códigos de todos os CIs, quantidades/pinos, cristal, sockets, janela UV, trilhas teclado/display; separar **marcações observadas** de **funções inferidas**. Confrontar datas e part numbers com datasheets.
3. Se houver autorização expressa para análise física, só então projetar método de leitura não destrutiva: confirmar tensão/pinagem na documentação primária, impedir energização incorreta, isolamento/ESD; realizar duas leituras independentes, comparar bytes e registrar SHA-256, voltagem, método, ferramenta e exemplar. Binários não devem ser executados nem versionados antes de procedência e direitos.
4. **Critério de fechamento:** CPU/ROM identificadas somente com imagem legível de CI ou manual específico do DR-70; sem isso declarar `unknown` e documentar as fontes negativas.

**Próximo alvo:** recuperar o texto original de Richard Nolle em *Today's Astrologer* XLV/9, setembro de 1983, p. 14. Não inferir sua conclusão a partir do índice.

**Coordenação:** a [PR #9](https://github.com/franklinbaldo/digicomp/pull/9) já modifica `docs/sources.md` para F7–F10. Este dossiê é uma fatia separada para não disputar o mesmo trecho, e as referências novas deverão ser incorporadas ao catálogo canônico depois da integração da #9, sem atribuir IDs F concorrentes.

Validação: inspeção documental e Markdown com frontmatter tipado; `prek` e `okf-parser` integrais **NOT_RUN** no executor disponível.
