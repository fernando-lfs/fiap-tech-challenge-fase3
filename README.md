# 🎓 Análise e Previsão de Fatores de Estresse em Estudantes

Este projeto desenvolve uma solução completa de Machine Learning para identificar proativamente estudantes em risco de estresse elevado, criado para o Tech Challenge da Fase 3 da Pós-Graduação em Engenharia de Machine Learning da FIAP.

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Principais Funcionalidades](#-principais-funcionalidades)
- [Stack Tecnológica](#%EF%B8%8F-stack-tecnológica)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Instalação e Configuração](#-instalação-e-configuração)
- [Resultados e Pipeline](#-resultados-e-pipeline)
- [Fonte dos Dados](#-fonte-dos-dados)
- [Licença](#%EF%B8%8F-licença)

---

## 🎯 Sobre o Projeto

O estresse acadêmico impacta diretamente o bem-estar e o desempenho dos estudantes. Este projeto oferece uma ferramenta baseada em dados para que instituições de ensino possam identificar estudantes vulneráveis e criar programas de apoio direcionados.

A solução utiliza um modelo de classificação que prevê o nível de estresse (**Baixo**, **Médio** ou **Alto**) a partir de 20 variáveis relacionadas a fatores psicométricos e hábitos de vida. O resultado é acessível através de um dashboard interativo onde é possível simular cenários e obter previsões em tempo real.

---

## ✨ Principais Funcionalidades

- **Análise Exploratória Completa**: Notebook Jupyter com investigação detalhada das relações entre variáveis e qualidade dos dados
- **Modelo Preditivo de Alta Performance**: Random Forest com **89% de acurácia** na classificação dos níveis de estresse
- **Interface Interativa**: Dashboard web desenvolvido em Streamlit, permitindo simulações e previsões instantâneas sem conhecimento técnico

---

## 🛠️ Stack Tecnológica

### Ambiente e Linguagem
- **Python 3.10**
- **Poetry**: gerenciamento de dependências e ambientes virtuais
- **Jupyter Notebook**: análise exploratória e experimentação

### Dados e Armazenamento
- **MinIO**: sistema de armazenamento de objetos S3-compatível para desacoplamento de dados e código

### Análise e Visualização
- **Pandas**: manipulação e análise de dados
- **Matplotlib & Seaborn**: visualizações e gráficos

### Machine Learning
- **Scikit-Learn**: treinamento, validação e avaliação de modelos
- **Joblib**: serialização e carregamento de modelos

### Deploy
- **Streamlit**: framework para construção do dashboard interativo

---

## 📂 Estrutura do Repositório

```
.
├── .gitignore
├── README.md
├── poetry.lock
├── pyproject.toml
├── config.py                               ## Dicionário tradução features
│
├── dashboard/
│   └── app.py                              # Aplicação Streamlit
│
├── data/
│   └── StressLevelDataset.csv              # Dataset original
│
├── minio/
│   ├── data/                               # Dados do MinIO
│   └── minio.exe                           # Servidor MinIO
│
├── models/
│   └── student_stress_rf_model.joblib      # Modelo treinado
│
├── notebooks/
│   └── 01-analise-exploratoria.ipynb       # Análise exploratória
│
└── scripts/
    └── setup_minio.py                      # Configuração do MinIO
```

---

## 🚀 Instalação e Configuração

### Pré-requisitos

Certifique-se de ter instalado:
- [Git](https://git-scm.com/)
- [Python 3.10.x](https://www.python.org/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [MinIO Server](https://min.io/download) (baixar e colocar na pasta `minio/`)

### Passo 1: Clone o Repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

### Passo 2: Instale as Dependências

O Poetry criará automaticamente um ambiente virtual isolado:

```bash
poetry install
```

### Passo 3: Configure o MinIO

O MinIO simula um ambiente de armazenamento em nuvem, garantindo reprodutibilidade.

**3.1. Inicie o servidor MinIO**

Em um terminal, execute (mantenha este terminal aberto):

```bash
.\minio\minio.exe server .\minio\data --console-address ":9090"
```

**3.2. Configure o bucket e faça upload dos dados**

Em um **novo terminal**, execute o script de setup. Ele criará o bucket `student-stress` e fará o upload do dataset `StressLevelDataset.csv` automaticamente.

```bash
poetry run python scripts/setup_minio.py
```

> **Nota**: Este comando precisa ser executado apenas uma vez.

### Passo 4: Execute o Dashboard

Com o MinIO em execução, inicie a aplicação:

```bash
poetry run streamlit run dashboard/app.py
```

O dashboard será aberto automaticamente no seu navegador padrão.

### (Opcional) Passo 5: Explore a Análise de Dados

Para executar o notebook de análise exploratória:

1. Ative o ambiente virtual:
   ```bash
   poetry shell
   ```

2. Abra o notebook no VSCode ou Jupyter:
   - Arquivo: `notebooks/01-analise-exploratoria.ipynb`
   - Selecione o kernel do ambiente Poetry
   - Execute as células para carregar os dados do MinIO e visualizar as análises

---

## 📊 Resultados e Pipeline

O desenvolvimento seguiu um pipeline estruturado de Machine Learning:

### 1. Definição do Problema
Classificação multiclasse para prever o nível de estresse em três categorias: Baixo, Médio e Alto.

### 2. Coleta e Armazenamento
Dataset público do Kaggle armazenado em servidor MinIO local, simulando ambiente de produção.

### 3. Análise Exploratória
A análise revelou um dataset de excelente qualidade:
- Sem valores ausentes ou duplicados
- Balanceamento perfeito entre as classes
- 20 features relevantes e correlacionadas com a variável-alvo

### 4. Pré-processamento
Divisão estratificada dos dados em treino (80%) e teste (20%), mantendo a proporção das classes.

### 5. Modelagem
Três modelos foram treinados e comparados:
- **DummyClassifier** (baseline)
- **DecisionTreeClassifier**
- **RandomForestClassifier** ✅

O Random Forest foi selecionado por apresentar o melhor desempenho, com **89% de acurácia**.

### 6. Deploy
Modelo disponibilizado através de dashboard interativo em Streamlit, permitindo previsões em tempo real com interface intuitiva.

---

## 📚 Fonte dos Dados

Dataset público disponível no Kaggle:

**[Student Stress Factors - A Comprehensive Analysis](https://www.kaggle.com/datasets/rxnach/student-stress-factors-a-comprehensive-analysis/data)**  
Autor: RUCHI NACHANKAR

A escolha de um dataset público permitiu focar nas etapas de modelagem e deploy, que são o escopo principal do desafio.

---

## ⚖️ Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---