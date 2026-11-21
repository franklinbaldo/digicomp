---
type: Documento
title: "Famílias de software astrológico contemporâneas ao DR-70 (1977–1985)"
description: "Pistas de programas, mídias e procedimentos de triagem, sem atribuir parentesco não provado."
timestamp: 2026-11-20T00:00:00-04:00
estado: exploratorio
---

# Software astrológico contemporâneo: pista, não ROM

**Escopo:** investigação exploratória da 🦊 Raposa, em [Digicomp #8](https://github.com/franklinbaldo/digicomp/issues/8) e [#3](https://github.com/franklinbaldo/digicomp/issues/3), 20/11/2026. **Nenhum programa ou ROM original do DR-70 foi encontrado ou executado nesta pesquisa.** Contemporaneidade não implica genealogia de código.

## Documentos e artefatos localizados

| Evidência consultada | Período | O que sustenta, estritamente | Grau |
| --- | --- | --- | --- |
| [Entrevista de Michael Erlewine (Matrix, 23/12/2008)](https://astrologysoftware.com/m/community/interviews/michael_erlewine.html) | Memória de 1977–1978 | O próprio autor relata programa planetário num Commodore PET de 8 KiB, ajuda de James Neely, distribuição de fitas cassete e versões para Apple II e TRS-80. | **Relatado pelo autor, retrospectivo**; nem fita nem listing original conferidos |
| [Museu Ingenium, item 1991.0404.001](https://collection.ingenium.ca/en/id/1991.0404.001/) | Fita Tandy de 1980 | Catálogo de cassete *Astrology* para TRS-80, Level II, RAM 16K, com estojo e manual. Trata-se de **outro fabricante**; demonstra mídia de época concreta, não ancestralidade DR-70. | **Confirmado como item catalogado pelo museu**; nenhum dump lido |
| [Astrolabe, histórico institucional](https://alabe.com/history.htm) | 1979–1984 | A empresa diz ter começado como Astro-Graphics Services em 1979, com programas TRS-80/Apple II; Astro-Scope em 1980, Nova em 1984 e distribuição CCRS em 1984. | **Relatado pela própria empresa**, retrospectivo; sem conexão estabelecida com Digicomp |
| [Open Library, livro de Michael Erlewine](https://openlibrary.org/works/OL6373938W/Manual_of_Computer_Programming_for_Astrologers) | Edição de junho/1980 | Registro de *Manual of Computer Programming for Astrologers*, ISBN 0-86690-099-3, editora American Federation of Astrologers. Possível pista de algoritmos da época, **não manual DR-70**. | **Confirmado como registro bibliográfico**; livro integral não examinado |
| [Índice AFA, *Today's Astrologer*, vols. XLI–L](https://astrologers.com/wp-content/uploads/2025/07/Index-by-Title-41-50.pdf), páginas PDF 40 e 42 (índices 39/41) | 1983–1984 | Nolle: parte 4, Matrix M-30 (XLV/8, ago/1983, p.9); parte 5, hardware DR-70 (XLV/9, set/1983, p.14); parte 6, **teste do DR-70 comparado a programa “ACS”** (XLV/10, out/1983, p.9); partes 12–13, Matrix M-65/M-65-A/B (XLVI/4–5, abr/1984); parte 14, DR-70 com impressora e Astrion 80 (XLVI/6, mai/1984, p.13); parte 16, AGS AstroStar I (XLVI/8, jul/1984, p.8). | **Confirmado apenas no índice**, páginas inspecionadas por imagem; fascículos originais não lidos |

A sigla **“ACS” da parte 6 não está resolvida** nesta evidência. Não expandir automaticamente para nome comercial, nem confundir com AGS/Astrolabe. O índice registra uma comparação, mas não informa resultados, valores calculados, código, plataforma ou parentesco tecnológico.

## Ordem das próximas buscas

1. **DR-70 original (P0):** manual técnico/programação, listing, etiqueta de firmware, foto legível da placa e chips, ROM/EPROM com proveniência ([#2](https://github.com/franklinbaldo/digicomp/issues/2), [#4](https://github.com/franklinbaldo/digicomp/issues/4)). Não atribuir CPU a partir de outro produto Digicomp.
2. **Contraprova do comportamento (P1):** fascículos originais com Nolle set/1983 (hardware DR-70) e sobretudo out/1983 (comparação DR-70/ACS), com fotos e saídas literais se houver ([#5](https://github.com/franklinbaldo/digicomp/issues/5), [#7](https://github.com/franklinbaldo/digicomp/issues/7)). Primeiro buscar acesso público lícito; compras e contatos precisam de autorização.
3. **Controles de época, não substitutos:** Matrix PET/Apple II/TRS-80, Tandy TRS-80, Astro-Graphics/Astrolabe, Matrix M-30/M-65 e Compuchart, somente se material original for localizado. Comparar formatos/precisão sem transferir automaticamente os algoritmos para o DR-70.

## Formato de preservação e triagem futura

| Material encontrado | Inspeção sem executar código | Limite |
| --- | --- | --- |
| Fita cassete/imagem digital | Registrar fotos, fabricante, lados, duração, cadeia de custódia; preservar captura bruta e decodificação em arquivos separados, com hashes próprios | Uma cassete Tandy/Matrix não é ROM do DR-70 |
| Listagem impressa/OCR | Preservar fac-símile, página e linhas; versionar transcrição separada, com dúvidas de leitura | Dialetos BASIC e erros de OCR podem mudar cálculos |
| ROM/EPROM binária | Registrar chips, ordem/orientação, tamanho e SHA-256 dos bytes originais, sem alterar arquivo; análise estática numa cópia isolada | Dump hexadecimal ou strings não identificam automaticamente CPU |
| Arquivo CP/M, Apple II, PET ou TRS-80 | Conservar imagem original e metadados; extração offline em cópia de trabalho só após identificar formato | Nome/extensão não prova relação com DR-70 |
| Impressão astrológica | Registrar entrada, comandos, saída literal, arredondamento, fuso e identificação do exemplar | Efemérides modernas são controle de erro, não algoritmo original |

Ferramentas candidatas para **etapa posterior**, quando houver bytes com proveniência: SHA-256, visualizador hexadecimal, inspeção textual estática, decodificador de mídia apropriado e desassemblador apenas quando a arquitetura for sustentada por prova independente. **Não executar firmware desconhecido**, não inferir CPU do resultado de um desassemblador, não versionar binários de direitos incertos. Seguir o fluxo de quarentena do [plano](research-plan.md).

## Evidência ausente e próximo experimento

As páginas do índice AFA foram inspecionadas visualmente, não os fascículos originais. O objeto Tandy é catalogação museológica, não leitura de fita. A entrevista Matrix é memória do autor, não documento de 1977. **Busca negativa limitada às fontes relacionadas acima:** não apareceu código, ROM, dump, listing ou saída DR-70 autenticada.

O experimento de maior valor é obter o artigo de outubro de 1983, resolver o que “ACS” denota **a partir do original** e verificar se contém os mesmos dados de entrada e resultados comparáveis do DR-70. Evitar construir emulador numérico genérico antes dessas evidências.
