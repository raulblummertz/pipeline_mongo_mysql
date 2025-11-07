# Pipeline ETL: Extração de API → Transformação com Pandas → Carga em MySQL

## 🧩 Descrição

Este projeto implementa uma **pipeline ETL (Extract, Transform, Load)** em **Python**, que executa o fluxo completo de ingestão de dados:

1. **Extração** de dados de uma **API REST**;
2. **Armazenamento** dos dados brutos em **arquivos CSV**;
3. **Transformação e limpeza** dos dados utilizando **Pandas**;
4. **Carga** dos dados tratados em um banco de dados **MySQL**.

A pipeline pode ser executada tanto por **scripts Python** quanto via **notebooks Jupyter**, o que facilita a exploração interativa e o desenvolvimento incremental.

---

## 🏗️ Estrutura do Projeto

```
pipeline_mongo_mysql/
│
├── data/
│   ├── tabela_livros.csv
│   └── tabela_produtos_2021_2029.csv
│
├── data_teste/
│   ├── tb_livros.csv
│   └── tb_produtos.csv
│
├── scripts/
│   ├── extract_and_save_data.py   # Extração dos dados da API e salvamento em CSV
│   ├── transform_data.py          # Transformação e normalização com Pandas
│   └── save_data_mysql.py         # Inserção dos dados transformados no MySQL
│
├── notebooks/
│   ├── extract_and_save_data.ipynb
│   ├── transform_data.ipynb
│   └── save_data_mysql.ipynb
│
├── .env                           # Configurações de ambiente (não versionado)
├── requirements.txt               # Dependências do projeto
└── README.md
```

---

## ⚙️ Instalação

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/raulblummertz/pipeline_mongo_mysql.git
cd pipeline_mongo_mysql
```

### 2️⃣ Criar e ativar um ambiente virtual
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

---

## 🔑 Configuração de Ambiente

Crie um arquivo **`.env`** na raiz do projeto com as variáveis de conexão e parâmetros de acesso:

```bash
DB_PASSWORD="sua_senha_mongodb" # fique a vontade pra alterar para MONGO_PASSWORD e corrigir no código também
API_URL="https://labdados.com/produtos"
DB_HOST="localhost"
DB_USER="seu_usuario_mysql"
MYSQL_PASSWORD="sua_senha_mysql"
```

> ⚠️ **Atenção:** o arquivo `.env` contém informações sensíveis e **não deve ser versionado**.  
> Adicione-o ao `.gitignore` para evitar exposição de credenciais.

---

## ▶️ Execução

Você pode executar a pipeline completa ou cada etapa separadamente.

### 1️⃣ Extrair e salvar dados da API
```bash
python scripts/extract_and_save_data.py
```
Ou via notebook:
```
notebooks/extract_and_save_data.ipynb
```

### 2️⃣ Transformar e normalizar os dados
```bash
python scripts/transform_data.py
```
Ou via notebook:
```
notebooks/transform_data.ipynb
```

### 3️⃣ Inserir dados no banco MySQL
```bash
python scripts/save_data_mysql.py
```
Ou via notebook:
```
notebooks/save_data_mysql.ipynb
```

---

## 🧠 Tecnologias Utilizadas

- **Python 3.10+**
- **Requests** — Requisições HTTP para a API
- **Pandas** — Limpeza, transformação e normalização dos dados
- **MySQL Connector (mysql-connector-python)** — Conexão e inserção no banco MySQL
- **dotenv** — Carregamento de variáveis de ambiente

---

## 🧪 Estrutura de Dados

- **`data/`**: Contém os arquivos CSV gerados a partir da API.  
- **`data_teste/`**: Conjunto de dados reduzidos para testes rápidos.  
- **`scripts/`**: Scripts Python que executam cada etapa do pipeline.  
- **`notebooks/`**: Notebooks Jupyter com a mesma lógica dos scripts, voltados para experimentação.

---

## 👤 Autor

**Raul Lummertz**  
📎 [github.com/raulblummertz](https://github.com/raulblummertz)

README criado por IA e revisado pra não deixar falar bobagem
