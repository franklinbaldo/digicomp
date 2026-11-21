---
type: Documento
title: "DR-70: confundimento entre relógio e longitude"
description: "Ensaio condicional de identificabilidade do tempo sideral, com observações necessárias para distinguir convenções históricas sem atribuí-las ao firmware."
timestamp: 2026-11-20T00:00:00-04:00
estado: provisorio
---

# Relógio, longitude e saídas siderais: uma ambiguidade testável

**Estado:** análise matemática de um **comparador moderno**, não identificação do algoritmo, formato de entrada ou comportamento do Digicomp DR-70. Não existe nesta frente um par autêntico de teclas/saída do aparelho. O [corpus de fidelidade](fidelity-corpus.md) permanece com **zero observações reexecutáveis**.

## Fonte, modelo e unidades

O [US Naval Observatory, *Computing Approximate Sidereal Time*](https://aa.usno.navy.mil/faq/GAST) define um procedimento para Greenwich Mean Sidereal Time, em **horas siderais**, a partir de UT1 (na aproximação simplificada, usando UTC como substituto), e recomenda somar longitude **leste positiva** dividida por 15 para obter tempo sideral local:

`LMST(t, λ) = [GMST(t) + λ/15] mod 24 h`.

No trecho entre duas horas do **mesmo dia UT**, a fórmula simplificada do USNO faz `GMST` crescer aproximadamente `1,0027379 h sideral / h civil`. Portanto, mudar o instante em `Δt` horas e simultaneamente mudar a longitude em `Δλ = -15 × 1,0027379 × Δt` graus conserva **exatamente o LMST no modelo simplificado**, módulo 24 h. Um deslocamento de uma hora corresponde a **−15,0410685°**, e de meia hora a **−7,52053425°**. A fórmula completa inclui dependência secular pequena, fronteiras de dia e aproximações próprias; a sonda calcula a compensação usando as duas avaliações efetivas de GMST, não apenas a constante.

**Contraprova:** compensar 1 h com apenas −15° deixa uma diferença de cerca de **0,04107°** de ângulo sideral (aproximadamente **9,86 s** de tempo sideral). Um display arredondado pode ocultá-la. Tratar uma coincidência de impressão como prova da convenção interna seria incorreto. O USNO distingue GMST, GAST, UT1 e TT; a implementação desta sonda substitui UT1 por UTC e usa a fórmula aproximada, **sem validar precisão astronômica para 1983** ou supor que o DR-70 use a mesma formulação.

## O que é, e o que não é, identificável

Se a única grandeza observada de uma caixa-preta for o **tempo sideral local**, e se hora UT e longitude forem ambas desconhecidas, existe uma família contínua de pares que reproduzem a mesma leitura. **Uma saída isolada não identifica separadamente relógio/fuso e longitude.** O argumento é condicional a esse canal: posições planetárias dependentes do instante absoluto, saídas de calendário, outras funções e medições independentes podem quebrar o confundimento, conforme suas precisões e algoritmos. Não se afirmou que o DR-70 realmente exiba LMST ou que sua saída tenha resolução específica.

O [texto contemporâneo de Pottenger, 1979](1979-pottenger-dr70.md) atribui ao DR-70 funções astrológicas e memória permanente, mas **não oferece entrada/saída sideral, convenção de fuso ou fórmula de tempo**. O [índice AFA](https://astrologers.com/wp-content/uploads/2025/07/Index-by-Title-41-50.pdf) cita testes DR-70/ACS em outubro/1983; não substitui o artigo e não permite extrair valores.

## Sequência para uma medição discriminante

1. Fotografar ou preservar **literalmente** teclas, programa selecionado, display e metadados do exemplar. Determinar se existe função de tempo sideral e qual saída é efetivamente legível, **sem preencher controles ausentes**.
2. Com local conhecido e horário de referência independente, procurar ensaios **que alterem só o relógio**, depois **só o campo de fuso**, depois **só a longitude**. Os formatos de teclas e valores a digitar precisam vir de manual ou observação real, não deste texto.
3. Se houver saída que dependa **apenas** de LMST, comparar a resposta às variações de 1 h e 15°/15,041° e o limite de quantização do display. Testar meia hora e o dia atravessado, evitando atribuir arredondamento ao erro de efeméride.
4. Confrontar também um canal independente dependente de instante absoluto, caso existente, e manter pares de hora em lacunas/dobras de DST como **candidatos múltiplos**, nunca UTC único presumido. Arquivar o tzdb/convenção usada na comparação.
5. Depositar no [corpus](fidelity-corpus.md) apenas observações com fonte/locator, campos literais e grau de fidelidade corretos. Não registrar saídas calculadas pelo USNO como saídas do DR-70.

## Experimento reprodutível e limites

O [Cervo R123](https://github.com/franklinbaldo/cervo/blob/main/workspace/cervo_digicomp_lst_alias_r123.py) implementa o modelo somente com Python padrão e nove testes sintéticos: alias de 1 h e 30 min, fracasso da compensação de 15°, cruzamento da meia-noite, alteração sem compensação, longitude +1°/360°, rejeição de datetime ingênuo e de fuso diferente de UTC. Esses testes são **provas de consistência matemática do comparador**, não teste do firmware.

**Próxima evidência prioritária:** instruções legíveis do exemplar L606 (Calcuseum), parte 5 de Nolle (*hardware*, setembro/1983, p. 14) e parte 6 (*DR-70/ACS*, outubro/1983, p. 9), sem presumir que conterão os campos necessários. Este texto não usa nem distribui ROM, não compra ou contata terceiros e não altera o corpus de observações.
