# Big Data Classes

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) ![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)

Public code and learning materials from my Big Data classes, covering distributed databases, PySpark ETL, and data lake architecture.

**English** · **[Português (PT-BR)](#aulas-de-big-data-pt-br)**

<p align="center">
    <img src="media/unisenaipj.png" alt="Unisenai representative image" width="55%">
</p>

## What this repository does

This public repository collects the code from my **Big Data classes** so others can follow the examples and learn from them. It includes practical database labs, local ETL scripts, medallion architecture exercises, and the DadosPro clickstream project.

This is study material, with independent labs rather than a single application or a production-ready platform. Some exercises intentionally contain incomplete functions. Requirements vary by class; Docker Compose files and supporting shell scripts are not tracked and must be created from the relevant lab instructions.

### What is Big Data?

Big Data is the field of storing, processing, and analyzing datasets too large, fast, or varied for traditional tools — covering distributed databases, replication, consistency trade-offs, and how systems behave when the network doesn't cooperate.

**`Big Data is defined by the "3 Vs": Volume, Velocity, and Variety — data too big, too fast, or too unstructured for a single machine to handle alone.`**

### Classes board

| Class | Description |
|---|---|
| [08/03/26](aulas/aula_08_03_26) | PACELC labs: testing in practice how distributed databases behave under failure. |
| [08/17/26](aulas/aula_08_17_26) | Redis, MongoDB and Cassandra: practical tests across Key-Value, Document and Column data models. |
| [09/21/26](aulas/aula_09_21_26) | PySpark from scratch: DataFrames, local ETL and ENEM SC dataset processing. |
| [10/05/26](aulas/aula_10_05_26) | Medallion Architecture (Bronze, Silver, Gold) with PySpark, AWS S3 and Azure Blob. |
| [10/19/26](aulas/aula_10_19_26) | DadosPro final project: clickstream event pipeline, S3, AWS Glue, Athena and Streamlit. |

## Repository structure

- [`aulas/`](aulas/): class materials grouped by date; use the board above to find each lab guide.
- [`aulas/aula_09_21_26/`](aulas/aula_09_21_26/): introductory PySpark scripts, exercises, `comum.py`, and an environment checker.
- [`aulas/aula_10_05_26/`](aulas/aula_10_05_26/): local, AWS S3, and Azure Blob medallion exercises, each with its own README and setup guide.
- [`aulas/aula_10_19_26/`](aulas/aula_10_19_26/): DadosPro generator, pipeline, Streamlit explorer, tests, `Dockerfile`, and `requirements.txt`.
- [`media/`](media/): images used in this README.

## How to run

Clone the repository and enter its directory:

```bash
git clone https://github.com/gilas-byte/aulas-big-data.git
cd aulas-big-data
```

To update an existing clone, run `git pull` from the repository root.

Each lab has its own setup. A local starting point is the [introductory PySpark lab](aulas/aula_09_21_26/README.md). With Python 3.11 and Java 8, 11, or 17 already installed, run on Linux or macOS from the repository root:

```bash
cd aulas/aula_09_21_26
python3.11 -m venv .venv
./.venv/bin/python -m pip install "pyspark==3.5.3"
./.venv/bin/python verificar_ambiente.py
./.venv/bin/python 00_primeiro_contato.py
```

This example creates a local Spark session and displays DataFrames; it does not require Docker or a cloud account. See [SETUP.md](aulas/aula_09_21_26/SETUP.md) for Windows instructions and optional dependencies used by other scripts. For the Docker labs and DadosPro, follow the specific guides linked in the classes board; there is no root-level Compose configuration.

## Status

Study repository — coursework, practical labs, and exercises.

## License

[MIT](LICENSE).

---

## Aulas de Big Data (PT-BR)

Repositório público com códigos e materiais das minhas aulas de Big Data, abrangendo bancos distribuídos, ETL com PySpark e arquitetura de data lake.

<p align="center">
    <img src="media/unisenaipj.png" alt="Imagem representativa do Unisenai" width="55%">
</p>

### O que este repositório faz

Este repositório público reúne os códigos das minhas **aulas de Big Data**, para que outras pessoas possam acompanhar os exemplos e aprender com eles. Inclui laboratórios de bancos de dados, scripts de ETL local, exercícios de arquitetura medalhão e o projeto DadosPro de eventos clickstream.

É material de estudo, com laboratórios independentes, sem uma aplicação única ou plataforma pronta para produção. Alguns exercícios contêm funções incompletas de propósito. Os requisitos variam por aula; arquivos Docker Compose e scripts shell de apoio não são versionados e precisam ser criados conforme as instruções de cada laboratório.

#### O que é Big Data?

Big Data é a área de armazenar, processar e analisar conjuntos de dados grandes, rápidos ou variados demais para as ferramentas tradicionais — abrangendo bancos de dados distribuídos, replicação, trade-offs de consistência e o comportamento dos sistemas quando a rede não coopera.

**`Big Data é definido pelos "3 Vs": Volume, Velocidade e Variedade — dados grandes, rápidos ou desestruturados demais para uma única máquina lidar sozinha.`**

#### Quadro de aulas

| Aula | Descrição |
|---|---|
| [08/03/26](aulas/aula_08_03_26) | Laboratórios PACELC: testando na prática como bancos distribuídos se comportam sob falha. |
| [08/17/26](aulas/aula_08_17_26) | Redis, MongoDB e Cassandra: testes práticos com os modelos Key-Value, Document e Column. |
| [09/21/26](aulas/aula_09_21_26) | PySpark do zero: DataFrames, ETL local e processamento da base do ENEM SC. |
| [10/05/26](aulas/aula_10_05_26) | Arquitetura Medalhão (Bronze, Silver, Gold) com PySpark, AWS S3 e Azure Blob. |
| [10/19/26](aulas/aula_10_19_26) | Projeto final DadosPro: pipeline de eventos clickstream, S3, AWS Glue, Athena e Streamlit. |

### Estrutura do repositório

- [`aulas/`](aulas/): materiais agrupados por data; os guias de cada laboratório estão vinculados no quadro acima.
- [`aulas/aula_09_21_26/`](aulas/aula_09_21_26/): scripts introdutórios de PySpark, exercícios, `comum.py` e verificador de ambiente.
- [`aulas/aula_10_05_26/`](aulas/aula_10_05_26/): exercícios de arquitetura medalhão local, AWS S3 e Azure Blob, cada um com README e guia de instalação próprios.
- [`aulas/aula_10_19_26/`](aulas/aula_10_19_26/): gerador, pipeline, explorador Streamlit, testes, `Dockerfile` e `requirements.txt` do DadosPro.
- [`media/`](media/): imagens usadas neste README.

### Como rodar

Clone o repositório e entre na pasta:

```bash
git clone https://github.com/gilas-byte/aulas-big-data.git
cd aulas-big-data
```

Para atualizar um clone existente, execute `git pull` na raiz do repositório.

Cada laboratório tem sua própria configuração. Para começar localmente, use o [laboratório introdutório de PySpark](aulas/aula_09_21_26/README.md). Com Python 3.11 e Java 8, 11 ou 17 já instalados, execute no Linux ou macOS a partir da raiz do repositório:

```bash
cd aulas/aula_09_21_26
python3.11 -m venv .venv
./.venv/bin/python -m pip install "pyspark==3.5.3"
./.venv/bin/python verificar_ambiente.py
./.venv/bin/python 00_primeiro_contato.py
```

O exemplo cria uma sessão Spark local e exibe DataFrames; não exige Docker nem conta em nuvem. O [SETUP.md](aulas/aula_09_21_26/SETUP.md) contém as instruções para Windows e as dependências opcionais usadas por outros scripts. Para os laboratórios Docker e o DadosPro, siga os guias específicos vinculados no quadro de aulas; não há configuração Compose na raiz.

### Status

Estudo — conteúdo de aulas, laboratórios práticos e exercícios.

### Licença

[MIT](LICENSE).
