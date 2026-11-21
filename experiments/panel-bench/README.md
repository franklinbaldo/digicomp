---
type: Documento
title: "DR-70 — bancada experimental de eventos"
description: "Como executar e interpretar o registrador experimental de painel, sem atribuir algoritmos ou estados ao firmware histórico."
timestamp: 2026-11-21T10:00:00-04:00
estado: provisorio
---

# Bancada experimental de eventos

**Isto não é um emulador de CPU, uma ROM recuperada nem uma reconstrução de
cálculo astrológico do DR-70.** É uma ferramenta de instrumentação de
hipóteses para a [issue #4](https://github.com/franklinbaldo/digicomp/issues/4),
sem alterar o [corpus de fidelidade](../../data/fidelity/observations.json).

## Execução

Na raiz do repositório, com Python 3:

```sh
python3 -m unittest discover -s experiments/panel-bench -p 'test_*.py' -v
python3 experiments/panel-bench/dr70_panel_bench.py
```

No prompt do segundo comando:

```text
power on
shift
key UNKNOWN_KEY_1
status
power off
quit
```

O objeto de saída informa `kind=EXPERIMENTAL_PANEL_NOT_ORIGINAL_DR70` e
`observed_dr70_output=null`. Nenhum número gerado por essa ferramenta
pode entrar no corpus como impressão histórica.

## Origem das afirmações

| Item | Fonte | Grau | Modelagem implementada |
| --- | --- | --- | --- |
| Exemplar DR-70 L606, legendas LED | [Calcuseum](https://www.calcuseum.com/scrapbook/BONUS/10925/1.htm) | Fotografia externa atribuída ao L606 | **Nenhuma** emissão LED simulada; saída `null` |
| Chave física e shift iluminado com trava | [Relato de proprietário](https://deskthority.net/viewtopic.php?t=20346) | Relato secundário identificado | Liga/desliga, toggle de shift e lamp = power AND shift são **convenções experimentais**, não lógica observada |
| Demais teclas e seus sinais elétricos | Ainda não observados com sessão | **UNKNOWN** | Apenas log da etiqueta fornecida; sem execução de tecla |

O log é reproduzível, e `snapshot()` fornece uma **cópia independente**
do array de eventos para evitar que consumidores alterem o histórico do
painel por acidente. A estrutura `Panel.events` permanece mutável e
**não é uma trilha à prova de adulteração**. Eventos sintéticos são
distintos de entradas instrumentais confirmadas.

## Próxima fatia

Pedir a 🐙 Polvo, 🦊 Raposa e 🐝 Abelha revisão da superfície documentada
do teclado, associando cada controle visível a uma foto atribuída e
marcando o que não é legível. A arquitetura interna, ISA, ROM, pinagem
e saídas não estão estabelecidas. Manter a PR em rascunho até decisão de
coordenação sobre integração, sem competir com o catálogo #94.
