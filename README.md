# 🎓 Análise e Previsão de Fatores de Estresse em Estudantes

Este repositório contém o desenvolvimento de um projeto de Machine Learning para a Pós-Graduação em Engenharia de Machine Learning da FIAP. O objetivo é criar uma solução de ponta a ponta, desde a definição do problema até a implantação de um modelo preditivo.

## 📝 Sobre o Projeto

O estresse acadêmico é um desafio crescente que afeta o bem-estar e o desempenho dos estudantes. Este projeto visa desenvolver uma solução baseada em dados que permita a instituições de ensino **identificar proativamente estudantes com risco de estresse elevado**.

Através de um modelo de classificação, a ferramenta poderá prever o nível de estresse (Baixo, Médio ou Alto) com base em diversos fatores psicométricos e hábitos de vida, possibilitando a criação de programas de apoio mais direcionados e eficazes.

### 🎯 Status do Projeto

O projeto está sendo desenvolvido em fases, seguindo uma pipeline de Machine Learning bem definida. O status atual é:

  * **Fase 1: Definição do Problema** - ✅ Concluída
  * **Fase 2: Coleta de Dados** - ✅ Concluída
  * **Fase 3: Armazenamento dos Dados** - ✅ Concluída
  * **Fase 4: Análise Exploratória de Dados (EDA)** - ⏳ Em Andamento
  * **Fase 5: Pré-processamento e Engenharia de Features** - 📋 A Fazer
  * **Fase 6: Modelagem, Treinamento e Avaliação** - 📋 A Fazer
  * **Fase 7: Deploy (Implantação)** - 📋 A Fazer

## 🛠️ Tecnologias Utilizadas

Este projeto utiliza um conjunto de ferramentas modernas para garantir a reprodutibilidade e a eficiência do desenvolvimento:

  * **🐍 Python 3:** Linguagem principal para análise e modelagem.
  * **📦 Poetry:** Gerenciador de dependências e ambientes virtuais.
  * **📓 Jupyter Notebooks:** Para análise exploratória de dados e experimentação.
  * **💾 MinIO:** Sistema de armazenamento de objetos S3-compatível, usado para desacoplar os dados do código.
  * **📊 Pandas, Matplotlib, Seaborn:** Bibliotecas para manipulação e visualização de dados.
  * **🤖 Scikit-Learn:** Framework para treinamento e avaliação dos modelos de Machine Learning.

## 📂 Estrutura do Repositório

O projeto está organizado da seguinte forma para garantir clareza e separação de responsabilidades:

```
.
│   .gitignore
│   README.md
│   poetry.lock
│   pyproject.toml
│
├───data
│   └─── StressLevelDataset.csv
│
├───minio
│   ├─── data
│   └─── minio.exe
│
└───notebooks
    └─── 01-analise-exploratoria.ipynb
```

## 🚀 Como Executar o Projeto

Para replicar o ambiente e executar a análise, siga os passos abaixo.

### **Pré-requisitos**

  * [Git](https://git-scm.com/)
  * [Python 3.10.x](https://www.python.org/)
  * [Poetry](https://www.google.com/search?q=https://python-poetry.org/docs/%23installation) instalado e configurado.
  * [MinIO Server](https://www.min.io/download) baixado e disponível na pasta `minio/` do projeto.

### **1. Clone o Repositório**

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DO_SEU_REPOSITORIO>
```

### **2. Instale as Dependências**

O Poetry cuidará da criação do ambiente virtual e da instalação de todas as bibliotecas necessárias.

```bash
poetry install
```

### **3. Configure e Inicie o Armazenamento de Dados (MinIO)**

Este projeto utiliza o MinIO para simular um ambiente de armazenamento em nuvem (como o AWS S3), garantindo que o projeto seja 100% reprodutível.

1.  **Inicie o Servidor de Armazenamento (MinIO):**
    Abra um terminal na raiz do projeto e execute o comando abaixo para iniciar o servidor MinIO. **Mantenha este terminal aberto** durante a execução do projeto.
    ```bash
    .\minio\minio.exe server .\minio\data --console-address ":9090"
    ```

2.  **Configure o Ambiente MinIO Automaticamente:**
    Em um **novo terminal**, na raiz do projeto, execute o script de setup. Este comando irá criar o bucket e fazer o upload do dataset `StressLevelDataset.csv` [cite: 35] automaticamente.
    ```bash
    poetry run python setup.py
    ```
    Você só precisa executar este comando uma vez.

### **4. Execute a Análise Exploratória**

Com o servidor MinIO rodando e as dependências instaladas, você pode iniciar a análise.

1.  **Ative o ambiente virtual do Poetry:**

    ```bash
    poetry shell
    ```

2.  **Inicie o Jupyter Notebook (via VSCode):**

      * Abra o arquivo `notebooks/01-analise-exploratoria.ipynb` no VSCode.
      * Certifique-se de que o Kernel do Jupyter está apontando para o ambiente virtual criado pelo Poetry.
      * Agora você pode executar as células do notebook para carregar os dados do MinIO e realizar a análise.

## 📊 Fonte dos Dados

O dataset utilizado neste projeto foi obtido da plataforma Kaggle e está disponível publicamente:

  * **Nome:** [Student Stress Factors - A Comprehensive Analysis](https://www.kaggle.com/datasets/rxnach/student-stress-factors-a-comprehensive-analysis/data)
  * **Proprietário:** RUCHI NACHANKAR

A escolha de um dataset público otimizou o tempo do projeto, permitindo focar nas etapas de modelagem e deploy, que são o escopo principal do desafio.