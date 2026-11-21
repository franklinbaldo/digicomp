---
type: Documento
title: "Copia DECUS de Kermit-80 para Digicomp Delphi 100 (1984-1985)"
description: "Inventario de quatro arquivos de Kermit-80, verificacao estatica do HEX e limites de atribuicao ao DR-70."
timestamp: 2026-11-20T00:00:00-04:00
estado: provisorio
---

# Kermit-80: fonte e overlay concretos do Delphi 100, nao do DR-70

**Escopo:** Digicomp [#2](https://github.com/franklinbaldo/digicomp/issues/2) e [#3](https://github.com/franklinbaldo/digicomp/issues/3). Pesquisa publica de 20/11/2026. A fonte recuperada e codigo de **comunicacao Kermit para Digicomp Delphi 100**, nao programa astrologico nem firmware do DR-70. Nenhuma equivalencia entre os dois modelos foi estabelecida.

## Origem e cadeia de custodia

1. O [Info-Kermit Digest v1 n. 42 (06/12/1984)](https://groups.google.com/g/net.micro.cpm/c/_GWgL_GQYng), documento contemporaneo, anuncia Kermit-80 4.03, com `DELPHI` / `CP4DEL` para **Digicomp Delphi 100**, e o modulo fonte `CP4SYS.ASM`. E uma noticia de distribuicao, nao teste do DR-70.
2. Uma **segunda localizacao**, o [espelho do acervo DECUS VAX86B/Kermit](https://www.digiater.nl/openvms/decus/vax86b/kermit/), oferece individualmente os arquivos. O indice exibe `1985-11-10 00:00` para os quatro itens abaixo. Esse timestamp de listagem **nao demonstra** data de criacao do codigo, nem autenticidade perante os originais do CU20B/Columbia.
3. Foram baixados quatro arquivos desse espelho por HTTPS para scratch temporario fora do Git; SHA-256 calculado sobre os **bytes baixados**, sem executa-los, compila-los ou incluir software de terceiros no repositorio.

| Arquivo original | Bytes | SHA-256 exato do download |
| --- | ---: | --- |
| [cp4del.hex](https://www.digiater.nl/openvms/decus/vax86b/kermit/cp4del.hex) | 2.218 | `ba2a6a37dc59cb988e1af91507967d6e5d809c1e8de742301828635747f91c99` |
| [cp4sys.asm](https://www.digiater.nl/openvms/decus/vax86b/kermit/cp4sys.asm) | 79.117 | `1ad80bc2aeb2ac21cc69722b5302a6bd83a603c32f6a9c76d8c8aaa998f68077` |
| [cp4typ.asm](https://www.digiater.nl/openvms/decus/vax86b/kermit/cp4typ.asm) | 8.149 | `57531cf68966a638f26d562d834d2bfdf02bbf9b7bd9e8d44f9c29263035a102` |
| [cp4ann.txt](https://www.digiater.nl/openvms/decus/vax86b/kermit/cp4ann.txt) | 7.721 | `a5c4d82e39f1d946e0f4d0c12e9dffc0f99aa041bb6c47c293115d353974f27d` |

A captura e de **2026-11-20, horario de Rondonia**, feita via GET do espelho. O indice aponta conteudo de 1985; a identificacao do anuncio de 1984 decorre do texto do proprio anuncio. Nao foi provado que os bytes do espelho coincidam com a publicacao original.

## Conteudo estatico observado

- `cp4sys.asm` contem comentario de revisao `edit 7: 29 August 1984 by Bdale Garbee @ CMU`, atribuindo a inclusao do suporte Delphi 100 e terminal Netronics Smartvid. E **autoria declarada no fonte**, nao identificacao de empregado/projetista da Digicomp.
- O ramo condicional `IF delphi` de `cp4sys.asm` define portas de dados `22h`, status `23h`, baud rate `29h`, flags de transmissao e recepcao `01h`/`02h`, e `z80 EQU true` com comentario de estar usando o lado Z80 de um *dual processor*. Isto se refere **somente ao Delphi 100**, nao identifica CPU do DR-70.
- `cp4typ.asm` tem a chave de montagem `delphi EQU FALSE` na configuracao generica, acompanhada do nome **Digicomp Delphi 100**; `FALSE` e escolha padrao de montagem, nao evidencia de que o port nao existia.
- `cp4del.hex` contem texto ASCII embutido `CP4SYS.ASM` e `Digicomp Delphi 100`. Uma leitura de registros Intel HEX **sem executar codigo** encontrou 52 linhas, 797 bytes de dados, enderecos `0x3700` a `0x3A22`, intervalos vazios `0x3798..0x379C` e `0x37E5`. Tamanhos de registros e soma de verificacao modular de todas as linhas passaram. Uma mutacao de checksum foi rejeitada.
- **Ressalva de formato:** o arquivo termina em `:0000000000` (registro de dados vazio), nao no EOF Intel HEX usual `:00000001FF`. O inspetor adotou tratamento explicito de terminador legado na **ultima** linha. Um controle sem esse terminador foi rejeitado. Isso nao equivale a validacao por um carregador historico.

## Manifesto Kermit reproduzido em 1988: composicao por overlay

- [Robert P. Sabo e Remmington G. Bishop, *LO-CO-GRAF* (Naval Postgraduate School, marco/1988), p. impressa 79, folha PDF 99](https://upload.wikimedia.org/wikipedia/commons/1/1d/LO-CO-GRAF-_generating_maps_to_support_command_%28IA_locografgenerati00sabo%29.pdf#page=99): a lista de distribuicao Kermit reproduzida no apendice foi conferida **visualmente** na pagina. Ela identifica `CP4KER.HEX` como porcao independente da maquina a combinar com um dos overlays, e `CP4DEL.HEX` como overlay para **Digicomp Delphi 100 (terminal required)**. A tese descreve um projeto em outro computador; a listagem e **testemunho documental de empacotamento**, nao relato de uso ou teste do Delphi 100.
- [Columbia University, *Kermit Software Source Code Archive*](https://www.columbia.edu/kermit/archive.html), secao **CP/M-80**, conserva um catalogo de Kermit-80 4.11, datado 23/04/1991, que inclui o Delphi 100 na lista de plataformas. A versao de **1991** nao foi equiparada aos quatro arquivos do espelho DECUS de **1985**: arquivos Columbia/DECUS **nao foram confrontados byte a byte**, e o SHA-256 cruzado segue `NOT_RUN`.
- O anuncio de 1984, o espelho DECUS e a lista reproduzida na tese podem derivar da **mesma distribuicao Columbia**. Suas coincidencias de nomes nao constituem testemunhos independentes de execucao de software nem custodia independente dos bytes. Nenhuma dessas fontes associa `CP4DEL.HEX` ao **DR-70**.

## Distincoes e proximas provas

**Provado neste espelho:** existem bytes de uma configuracao/overlay Kermit para *Delphi 100* e fonte ASM que documenta portas e a atribuicao interna da revisao. O espelho nao atesta que os arquivos tenham sido escritos pela Digicomp, usados em maquina real ou distribuídos para DR-70. O texto da fonte credita Bdale Garbee pelo *port*, nao pelo projeto do hardware.

**Ainda ausente:** ROM, EPROM, listagem, algoritmo, CPU e saidas autenticadas do **DR-70**. A pista de um lado Z80 e **exclusiva do Delphi 100**, sem inferencia de parentesco de firmware. Proximo teste de custodia: comparar bytes/hash com o arquivo mantido na Columbia/Kermit ou outra copia independente e procurar fotos internas/manuais DR-70. Nenhum contato ou compra de equipamento foi feito; nenhum binario executado.
