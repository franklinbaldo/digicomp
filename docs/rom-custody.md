---
type: Documento
title: Protocolo de quarentena offline para candidatos a ROM DR-70
description: Admissão de bytes opacos, fixidez, custódia e limites de prova sem execução nem publicação do firmware.
timestamp: 2026-11-20T00:00:00-04:00
estado: provisorio
---

# Quarentena de candidatos a ROM e software

**Missão 🦀 (#8, apoio à #2):** preparar um caminho de preservação para **eventual** código, fita, dump ou ROM do Digicomp DR-70. **Nenhum ROM DR-70 autêntico foi obtido aqui.** A ferramenta anexa processou apenas bytes sintéticos. O fato de um arquivo ter hashes corretos não identifica o equipamento, os direitos de distribuição, a validade do dump ou a integridade do suporte físico original.

## Ordem da custódia

1. **Proveniência primeiro:** registrar detentor, fonte/URL ou identificador do suporte, data e método de aquisição, operador, aparelho de leitura, conexão, parâmetros, fotos e eventuais restrições jurídicas. Se desconhecido, registrar literalmente `unknown`; não preencher por inferência. Guardar contato pessoal sensível somente em registro privado apropriado.
2. **Mídia original:** evitar montar/executar o suporte no sistema operacional comum. Se for possível, obter imagem com método adequado de bloqueio de escrita e registrar as condições de leitura, inclusive erros. Uma EPROM física exige documentação do leitor, tensão e algoritmo antes de energizá-la; **este script não lê chips**.
3. **Bytes opacos:** copiar uma aquisição já disponibilizada para uma pasta `quarentena/` não versionada, acesso restrito, com digest SHA-256 e SHA-512, tamanho e declaração de origem. Nunca abrir executáveis, montar imagens, carregar ROMs em emulador ou executar comandos embutidos só para validar o hash. Metadados não são uma licença.
4. **Fixidez:** manter o objeto pelo SHA-256, verificar periodicamente contra os dois hashes anotados; cópias independentes em suportes/localidades distintos exigem decisões de armazenamento e autorização. Não confundir chmod(0400) com imutabilidade: FDs já abertos ou usuários privilegiados podem escrever.
5. **Autenticidade:** pedir leituras independentes do mesmo chip quando cabível, registrar variações e regiões instáveis. Uma leitura idêntica repetida pelo mesmo circuito reduz certos erros, mas não demonstra proveniência do DR-70. Vincular conclusões a placa, serigrafia, placa de memória, números de série e evidência externa.
6. **Preservação externa:** considerar BagIt RFC 8493 e documentação de cadeia de custódia para troca entre arquivos, mas **o esquema experimental deste utilitário não é um bag BagIt nem um backup**. Só transferir/distribuir bytes após avaliação de direitos e autorização expressa.

## Protótipo local sem egress

Execução somente Linux/POSIX com Python padrão, sem baixar ou executar binário. Criar um diretório privado e usar apenas **arquivos cuja aquisição já esteja autorizada**:

    mkdir -m 700 -p /caminho/privado/quarentena
    python3 tools/rom_quarantine.py ingest --source /origem/autorizada/candidato.bin --root /caminho/privado/quarentena --origin 'arquivo de origem e cadeia conhecidos ou unknown'
    python3 tools/rom_quarantine.py verify --root /caminho/privado/quarentena --sha256 HASH_REAL_DE_64_HEX

Testes determinísticos sem firmware:

    python3 -m unittest discover -s tests -p test_rom_quarantine.py
    python3 -O -m unittest discover -s tests -p test_rom_quarantine.py

O código usa abertura sem seguir symlink, recusa FIFO/dispositivo, root acessível por grupo, exige origem declarada, cópia com fsync e publicação de objeto sem sobrescrita por hard link. Guarda JSON com os dois hashes e flags `executed=false`, `rights_cleared=false` e `provenance_verified=false`. Detecta alteração de bytes, hashes, tamanho, versão de esquema e promoção das flags de segurança na verificação; uma deduplicação recusa metadados com essas flags promovidas. A leitura do JSON usa descritor regular aberto sem seguir symlink, recusa FIFO/dispositivo e limita os metadados a 16.384 bytes (incluindo notas UTF-8 multibyte); rejeita JSON que não seja objeto e `size` booleano. Esses controles não assinam nem autenticam o JSON. Não substitui o primeiro registro de origem quando um digest reaparece.

**Limites críticos:** não há snapshot contra escrita maliciosa in-place na fonte, isolamento de processo, assinatura de proveniência, anti-malware, comprovante de leitor físico, journal transacional ou recuperação automática após queda entre publicação do objeto e JSON. A cópia usa permissões de arquivo, não selo de inode. Um blob órfão após crash é recusado, não aprovado automaticamente. A ferramenta não garante integridade contra adversário com privilégio de escrita no root da quarentena. Não habilitar acesso a executáveis históricos em máquinas de produção.

O diretorio `quarentena/` já está listado em `.gitignore` do projeto. Nunca usar `git add -f` para ROMs, hashes com dados pessoais ou dumps não licenciados; não usar Git LFS como via de publicação.

## Critérios de teste e estágio da prova

**Local, somente sintético:** 18 testes PASS no Python 3.13.5 e 18 PASS em `python -O`: ingresso e replay, alteração de objeto/JSON detectada, nomes iguais com bytes diferentes, deduplicação, recusa de symlink, FIFO como origem ou metadado, permissões inseguras, origem vazia, ID inválido, JSON excessivo/não objeto, `size=true` com objeto de um byte e nota de origem multibyte no limite permitido. O ensaio não mede desempenho de mídias reais. A validação de hooks `prek`/OKF do repositório completo permanece **NOT_VERIFIED** no executor sem cache de prek.

**Referências de método:** [BagIt RFC 8493](https://www.rfc-editor.org/rfc/rfc8493) (hashes/payloads opacos e validação de bags); [NDSA Levels 2.1, março/2026](https://www.ndsa.org/activities/levels-of-digital-preservation/) (fixidez, armazenamento, segurança, metadados e sustentabilidade). São referências de preservação, não validação do instrumento ou da ROM.

**Handoff:** 🦦 Lontra deve preservar metadados e hashes quando encontrar material na #2; 🦅 Gavião pode revisar os limites de captura antes de qualquer uso com bytes autênticos. Não comprar, contatar terceiros, ler ROM física, executar firmware nem publicar software sem decisão do 🐘 Elefante e do proprietário.
