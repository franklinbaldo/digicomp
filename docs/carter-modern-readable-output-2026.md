---
type: Documento
title: "Carter 2023: protótipo legível de output documental versus cálculo moderno"
description: "Tabela auditável com nove longitudes publicadas em 2023, diferenças de um motor moderno e indicação explícita da ausência de comparações históricas."
timestamp: 2026-11-22T16:00:00-04:00
estado: provisorio
---

# Uma tabela para comparar resultados reais sem confundi-los com o DR-70

**Objetivo:** atender à proposta de [Digicomp #130](https://github.com/franklinbaldo/digicomp/issues/130) de mostrar um output comparável a partir de dados documentais efetivamente publicados, sem esperar uma ROM. A fonte numérica disponível é o mapa **moderno de 2023** reproduzido por Naomi Rabinowitz, [PDF, p. 12](https://static1.squarespace.com/static/625588022bac29595ab0c386/t/652c6205bd50527fa4e8778a/1697407494104/Jimmy%2BCarter%2Band%2Bthe%2BKnight%2Bof%2BPentacles_final.pdf#page=12), transcrito em [data/modern-controls/carter-astro-dienst-2023.json](../data/modern-controls/carter-astro-dienst-2023.json). Os nove campos têm signo, grau, minuto, segundo e literal original. A leitura visual já foi descrita em [controle moderno](carter-modern-crosscheck-2023.md); o PDF original não foi arquivado nem teve SHA-256 obtido.

**Saída implementada:** `python -B -m scripts.carter_modern_table` (com binding `pyswisseph==2.10.3.2` disponível, instalado separadamente) escreve uma tabela com nove linhas de **ASC, MC, Sol a Saturno**, posição literal publicada, longitude calculada, resíduo circular assinado em segundos de arco e coluna MATCH/MISMATCH. A tolerância de comparação é explicitamente **±1 segundo de arco**, pré-declarada para este controle moderno. O programa inclui três avisos no próprio output: os mapas de casas Whole Signs e Campanus não autorizam comparar cúspides; a independência dos motores não foi estabelecida; e **não existem, nesta tabela, resíduos de carta histórica de 1980 ou fidelidade instrumental do DR-70**.

**Contrato:** o adaptador verifica família documental, ano, caso, hora 13:00 UT, nove campos literais, signo+DMS válidos, metadados modernos e estados `NOT_RUN_NO_INSPECTED_1980_NUMBERS` e `NOT_RUN_NO_GOLDEN`. Recusa fonte ou modelo rotulados golden, tolerância adulterada, número não finito, chave JSON repetida e DMS ambíguo. Desvio superior a 1″ permanece como MISMATCH visível, não é ocultado nem recalibrado. A suite `tests/test_carter_modern_table.py` usa dados da **mesma publicação moderna** para verificar a apresentação, não é uma segunda observação independente e não certifica a efeméride.

**Reprodução:** `python -S -B -m unittest discover -s tests -p 'test_carter_modern_table.py' -v` testa os contratos sem pacotes externos. Após instalar o binding opcional, `python -B -m scripts.carter_modern_table` produz o output numérico real, testado no workflow público `.github/workflows/chart-reference.yml`. Os checks e o SHA devem ser conferidos na PR #148; não se infere PASS do CI apenas da presença do script.

**Próximo dado decisivo:** fotografar ou visualizar uma página da **edição impressa identificada de Raël/Rudhyar**, transcrever cegamente graus e cúspides e executar a primeira comparação realmente histórica como registro separado. O item [Internet Archive `astrologicalaspe0000rael`](https://archive.org/details/astrologicalaspe0000rael) tem acesso restrito às páginas interiores. As qualificações do experimento não são golden instrumental, ROM nem identificação do algoritmo do DR-70.
