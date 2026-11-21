---
type: Documento
title: "Neil L. Block Papers: programação astrológica 1977–1985, sem vínculo DR-70 demonstrado"
description: "Localizadores de software, impressões e materiais contemporâneos no inventário 35/3/418 da University of Illinois, com hipóteses rivais e limite de custódia."
timestamp: 2026-11-20T22:50:00-04:00
estado: provisorio
---

# Neil L. Block Papers: pista de software contemporâneo, não ROM atribuída

**🐙 Polvo · Digicomp #2/#3/#5 · O0.** Em 20/11/2026 examinei o [finding aid da University of Illinois Archives, *Neil L. Block Papers, 1912–1987*](https://archon.library.illinois.edu/archives/index.php?id=11306&p=collections/findingaid&rootcontentid=236248), coleção **35/3/418**. Trata-se de **outra coleção**, distinta de *Michael Erlewine Papers* **35/3/419**, já catalogada em [PR #33, inventário Erlewine/Illinois](https://github.com/franklinbaldo/digicomp/pull/33). O inventário descreve pastas e não disponibiliza seus conteúdos nesta consulta.

## Localizadores efetivos (metadados institucionais)

| Localizador 35/3/418 | Descrição no finding aid | Pergunta discriminante |
| --- | --- | --- |
| **Box 1, folders 34–40** | *Astrology—Computer Programs*, 1977–80 (2 pastas), 1980–81, 1982, 1982–84, 1983 **e 1985** | Quais máquinas, linguagens, autores e formatos estão identificados dentro dessas pastas? |
| **Box 1, folder 23** | *Aspects (Astrological)—Computer Printout*, sem data | Há papel com programa, aparelho e entrada/saída ligados por uma mesma origem? |
| **Box 1, folder 26** | *Astro-Computing Services Catalog*, 1985–86 | Identifica produtos, relatórios ou formatos ACS sem confundi-los com DR-70? |
| **Box 2, folder 13** | *Report on Standards and Methods to be Adopted in Preparing an Astronomical Computer Programme for Astrologers*, sem data | Regras e especificações de software contemporâneo, sem presumir implementação no DR-70? |
| **Box 2, folders 25–28** | *Ephemerides—Computer Printouts* 1980/1981, *Ephemeris Calculations*, *Ephemeris Computer Program* | Algum procedimento de efemérides pode ser atribuído por folha de rosto ou documentação? |
| **Box 4, folders 22–24** | Carta a Neil Michelsen (1983), *Manifest Constant Definitions—Computer Program* (1982), conversão Fortran (1976) | Distingue genealogia ACS/Fortran de firmware proprietário Digicomp? |
| **Box 4, folders 34–36** | Documentos Michelsen/AFA (1984), memorando Michelsen (1984), proposta de fabricação de minicomputadores (1981–83) | A proposta menciona Digicomp ou outra empresa? O rótulo **não** a identifica. |
| **Box 5, folders 39, 52** | *Pascal 2 Computer Programs* (1981); *Pseudo-Machine Architecture* (1978) | É documentação da experiência técnica de Block, não evidência de ISA do DR-70 até haver identificação documental. |
| **Box 7, folder 1** | *Astrology Computer Program*, sem data | Há listagem com autoria e programa/produto explicitamente atribuídos? |

Referência única: [inventário institucional, *Series 1: Original Acquisition*, listagens Box 1–7](https://archon.library.illinois.edu/archives/index.php?id=11306&p=collections/findingaid&rootcontentid=236248). A seção *Scope and Contents* identifica Neil L. Block (também Bloch, pseudônimo Gary Duncan) como programador, engenheiro e astrólogo, e informa que parte do conjunto contém materiais de Michael Erlewine. **Essa presença não unifica as coleções 35/3/418 e 35/3/419**, nem estabelece colaboração com a Digicomp.

## Hipóteses rivais e cortes de confiança

- **H1, conexão direta:** alguma pasta contém listagem, manual, contrato ou saída explicitamente ligada ao DR-70. **Observação necessária:** fac-símile do item específico com identificação de Digicomp/modelo, data, localizador e cadeia de procedência.
- **H2, comparador contemporâneo:** há código astrológico independente, possivelmente ACS ou ferramentas de Block. **Observação necessária:** capa, autoria, cabeçalho de listagem, especificação de máquina/linguagem e saída emparelhada; útil como controle, não como ROM DR-70.
- **H3, metadados genéricos:** materiais são programas e papéis de pesquisa sem relação operacional com o DR-70. **Observação necessária:** descrição das primeiras páginas ou inventário de nível de item que exclua atribuição específica.

**Resultado estrito:** o termo **"Digicomp" não aparece nos rótulos pesquisáveis do finding aid** consultado. Isso não é prova de ausência dentro das pastas, mas impede classificar qualquer uma delas como código recuperado do DR-70. **0 ROMs, 0 fontes do aparelho, 0 pares entrada/saída autenticados.** A pasta 1/40 (1985) e a 2/13 (relatório de padrões) foram confirmadas por releitura das linhas do mesmo inventário em 20/11/2026; são **mais dois localizadores catalográficos**, não duas confirmações de execução. O inventário não autoriza atribuir CPU, linguagem, ISA, software ou algoritmo ao aparelho.

## Próxima verificação legal e reproduzível

Pesquisar por digitalizações abertas já publicadas desses **localizadores precisos**, priorizando Box 1/34–40, Box 2/13 e Box 7/1. Em caso de documento aberto encontrado, congelar URL institucional, página/folha, data do item, SHA-256 dos bytes efetivamente recuperados, indicação de direitos e o elo textual com o equipamento. O site indica material físico fora do depósito principal e possibilidade de requisição: **nenhuma requisição, contato, compra ou acesso restrito foi feito** nesta rodada. Não arquivar dumps/código sem examinar procedência e licença.

**Fronteira:** esta é uma **nova rota de busca por software histórico**, não um avanço demonstrado da arquitetura do DR-70 e não um caso de fidelidade. Ver [reconstruction-gates](reconstruction-gates.md), [fontes](sources.md) e [Digicomp #2](https://github.com/franklinbaldo/digicomp/issues/2).
