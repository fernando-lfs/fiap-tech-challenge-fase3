# 🎓 Análise e Previsão de Fatores de Estresse em Estudantes

Este projeto desenvolve uma solução completa de Machine Learning para identificar proativamente estudantes em risco de estresse elevado, criado para o Tech Challenge da Fase 3 da Pós-Graduação em Engenharia de Machine Learning da FIAP.

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Principais Funcionalidades](#-principais-funcionalidades)
- [Stack Tecnológica](#%EF%B8%8F-stack-tecnológica)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Instalação e Configuração](#-instalação-e-configuração)
- [Fonte dos Dados](#-fonte-dos-dados)

---

## 🎯 Sobre o Projeto

O estresse acadêmico impacta diretamente o bem-estar e o desempenho dos estudantes. Este projeto oferece uma ferramenta baseada em dados para que instituições de ensino possam identificar estudantes vulneráveis e criar programas de apoio direcionados.

A solução utiliza um modelo de classificação que prevê o nível de estresse (**Baixo**, **Médio** ou **Alto**) a partir de 20 variáveis relacionadas a fatores psicométricos e hábitos de vida. O resultado é acessível através de um dashboard interativo onde é possível simular cenários e obter previsões em tempo real.

---

## ✨ Principais Funcionalidades

- **Análise Exploratória Completa**: Notebook Jupyter com investigação detalhada das relações entre variáveis e qualidade dos dados
- **Modelo Preditivo de Alta Performance**: Random Forest com **89% de acurácia** na classificação dos níveis de estresse
- **Interface Interativa**: Dashboard web desenvolvido em Streamlit, disponibilizando o modelo em uma interface interativa e intuitiva, que permite simulações e previsões em tempo real.

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
│   └── projeto_estresse_estudantes.ipynb       # Análise exploratória
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
   - Arquivo: `notebooks/projeto_estresse_estudantes.ipynb`
   - Selecione o kernel do ambiente Poetry
   - Execute as células para carregar os dados do MinIO e visualizar as análises

---

## 📚 Fonte dos Dados

Dataset público disponível no Kaggle:

**[Student Stress Factors - A Comprehensive Analysis](https://www.kaggle.com/datasets/rxnach/student-stress-factors-a-comprehensive-analysis/data)**  
Autor: RUCHI NACHANKAR

---