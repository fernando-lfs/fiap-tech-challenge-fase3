import os
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

# -----------------------------------------------------------------------------
# 1. Constantes e Configurações
# -----------------------------------------------------------------------------
# Centralizar configurações torna o código mais limpo e fácil de manter.

# Constrói o caminho para o modelo de forma robusta, independentemente de onde
# o script é executado. Navega um nível acima (para a raiz do projeto) e
# depois entra na pasta 'models'.
MODEL_PATH = Path(__file__).parent.parent / "models" / "student_stress_rf_model.joblib"

# Mapeamento da saída numérica do modelo para textos e ícones amigáveis.
STRESS_LEVEL_MAP = {0: "✅ Baixo", 1: "⚠️ Médio", 2: "🔴 Alto"}

# Configuração unificada para cada feature, contendo a label para a UI
# e o valor máximo para o slider. Isso simplifica a geração da interface.
FEATURE_CONFIG = {
    "anxiety_level": {
        "label": "Nível de Ansiedade (0: baixo a 5: muito alto)",
        "max_val": 5,
    },
    "self_esteem": {
        "label": "Nível de Autoestima (0: baixa a 5: muito alta)",
        "max_val": 5,
    },
    "mental_health_history": {
        "label": "Histórico de Saúde Mental (0: Não, 1: Sim)",
        "max_val": 1,
    },
    "depression": {
        "label": "Nível de Depressão (0: baixo a 5: muito alto)",
        "max_val": 5,
    },
    "headache": {
        "label": "Frequência de Dor de Cabeça (0: nunca a 5: sempre)",
        "max_val": 5,
    },
    "blood_pressure": {
        "label": "Pressão Sanguínea (0: Baixa, 1: Normal, 2: Alta)",
        "max_val": 2,
    },
    "sleep_quality": {
        "label": "Qualidade do Sono (0: ruim a 5: excelente)",
        "max_val": 5,
    },
    "breathing_problem": {
        "label": "Problemas Respiratórios (0: nunca a 5: sempre)",
        "max_val": 5,
    },
    "noise_level": {
        "label": "Nível de Ruído no Ambiente (0: baixo a 5: alto)",
        "max_val": 5,
    },
    "living_conditions": {
        "label": "Condições de Moradia (0: ruins a 5: excelentes)",
        "max_val": 5,
    },
    "safety": {
        "label": "Sensação de Segurança (0: inseguro a 5: muito seguro)",
        "max_val": 5,
    },
    "basic_needs": {
        "label": "Necessidades Básicas Atendidas (0: não a 5: sim)",
        "max_val": 5,
    },
    "academic_performance": {
        "label": "Desempenho Acadêmico (0: ruim a 5: excelente)",
        "max_val": 5,
    },
    "study_load": {
        "label": "Carga de Estudos (0: baixa a 5: muito alta)",
        "max_val": 5,
    },
    "teacher_student_relationship": {
        "label": "Relação Professor-Aluno (0: ruim a 5: excelente)",
        "max_val": 5,
    },
    "future_career_concerns": {
        "label": "Preocupações com a Carreira (0: baixas a 5: altas)",
        "max_val": 5,
    },
    "social_support": {"label": "Suporte Social (0: baixo a 5: alto)", "max_val": 5},
    "peer_pressure": {
        "label": "Pressão dos Colegas (0: baixa a 5: alta)",
        "max_val": 5,
    },
    "extracurricular_activities": {
        "label": "Atividades Extracurriculares (0: poucas a 5: muitas)",
        "max_val": 5,
    },
    "bullying": {
        "label": "Frequência de Bullying (0: nunca a 5: sempre)",
        "max_val": 5,
    },
}

# A ordem das features é derivada diretamente da configuração para garantir consistência.
FEATURE_ORDER = list(FEATURE_CONFIG.keys())


# -----------------------------------------------------------------------------
# 2. Carregamento do Modelo
# -----------------------------------------------------------------------------
@st.cache_resource
def load_model(path):
    """Carrega o modelo a partir do caminho especificado."""
    try:
        model = joblib.load(path)
        return model
    except FileNotFoundError:
        st.error(f"Arquivo do modelo não encontrado. Verifique o caminho: {path}")
        return None


# -----------------------------------------------------------------------------
# 3. Configuração da Página e Interface
# -----------------------------------------------------------------------------

# --- Configuração Inicial da Página ---
st.set_page_config(
    page_title="Predição de Estresse em Estudantes",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Carregamento do Modelo ---
model = load_model(MODEL_PATH)


# --- Interface da Sidebar ---
with st.sidebar:
    st.title("Parâmetros do Estudante")
    st.markdown("Ajuste os valores para simular o perfil de um estudante.")

    user_inputs = {}
    # Loop simplificado que utiliza a estrutura de FEATURE_CONFIG
    for feature, config in FEATURE_CONFIG.items():
        user_inputs[feature] = st.slider(
            label=config["label"],
            min_value=0,
            max_value=config["max_val"],
            value=config["max_val"] // 2,  # Padrão: meio da escala
            step=1,
        )

# --- Interface da Área Principal ---
st.title("Sistema de Previsão de Estresse em Estudantes 🧠")
st.markdown(
    """
Esta aplicação utiliza um modelo de *Random Forest* para prever o nível de estresse 
de um estudante com base em fatores psicológicos, sociais e ambientais.

**Como usar:**
1. Ajuste os parâmetros na barra lateral esquerda.
2. Clique no botão "Analisar" para ver o resultado.
"""
)

# Interrompe a execução se o modelo não foi carregado, evitando erros posteriores.
if model is None:
    st.warning("O modelo não está disponível. A análise não pode ser realizada.")
    st.stop()


# --- Botão de Ação e Exibição dos Resultados ---
if st.button("Analisar Nível de Estresse", type="primary", use_container_width=True):
    # Converte os inputs do usuário em um DataFrame
    input_df = pd.DataFrame([user_inputs])
    # Garante que as colunas estejam na ordem correta que o modelo espera
    input_df = input_df[FEATURE_ORDER]

    # Realiza a predição e obtém as probabilidades
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)

    # Mapeia a predição para o texto correspondente
    result_text = STRESS_LEVEL_MAP.get(prediction[0], "Desconhecido")

    st.divider()
    st.subheader("Resultado da Análise", divider="rainbow")

    col1, col2 = st.columns([0.4, 0.6])  # Ajusta a proporção das colunas

    with col1:
        st.metric(label="**Nível de Estresse Previsto**", value=result_text)

    with col2:
        st.write("**Confiança da Predição (Probabilidade por Classe):**")
        # Prepara os dados para o gráfico de barras
        proba_df = pd.DataFrame(
            prediction_proba.T,
            index=["Baixo", "Médio", "Alto"],
            columns=["Probabilidade"],
        )
        # Exibe um gráfico de barras, que é mais intuitivo que uma tabela
        st.bar_chart(proba_df)
