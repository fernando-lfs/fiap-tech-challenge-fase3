import streamlit as st
import pandas as pd
import joblib

# -----------------------------------------------------------------------------
# Configuração da Página
# -----------------------------------------------------------------------------
# Define o título da página, o ícone e o layout.
# A configuração 'wide' aproveita melhor o espaço da tela.
st.set_page_config(page_title="Predição de Estresse em Estudantes", layout="wide")


# -----------------------------------------------------------------------------
# Carregamento do Modelo
# -----------------------------------------------------------------------------
# O decorador @st.cache_resource garante que o modelo seja carregado apenas uma vez,
# otimizando o desempenho da aplicação.
@st.cache_resource
def load_model():
    """Carrega o modelo de Random Forest a partir do arquivo .joblib."""
    try:
        # Caminho corrigido para apontar para a pasta 'models'
        model = joblib.load("models/student_stress_rf_model.joblib")
        return model
    except FileNotFoundError:
        # Mensagem de erro também atualizada para clareza
        st.error(
            "Arquivo do modelo não encontrado. Verifique o caminho 'models/student_stress_rf_model.joblib'"
        )
        return None


# Carrega o modelo ao iniciar a aplicação
model = load_model()

# -----------------------------------------------------------------------------
# Interface do Usuário (Sidebar)
# -----------------------------------------------------------------------------
# A sidebar é usada para agrupar os controles de entrada do usuário, mantendo
# a área principal da página limpa para exibir os resultados.

st.sidebar.title("Parâmetros do Estudante")
st.sidebar.markdown(
    "Ajuste os valores abaixo para simular as características e o ambiente de um estudante."
)

# --- Dicionário para armazenar as entradas do usuário ---
user_inputs = {}

# --- Criação dos sliders na sidebar ---
# Cada slider representa uma feature do modelo. Os valores min, max e default
# são baseados na escala original do dataset (geralmente de 0 a 5).

feature_explainer = {
    "anxiety_level": "Nível de Ansiedade (0: baixo a 5: muito alto)",
    "self_esteem": "Nível de Autoestima\n(0: baixa a 5: muito alta)",
    "mental_health_history": "Histórico de Saúde Mental\n(0: Não, 1: Sim)",
    "depression": "Nível de Depressão\n(0: baixo a 5: muito alto)",
    "headache": "Frequência de Dor de Cabeça\n(0: nunca a 5: sempre)",
    "blood_pressure": "Pressão Sanguínea\n(0: Baixa, 1: Normal, 2: Alta)",
    "sleep_quality": "Qualidade do Sono\n(0: ruim a 5: excelente)",
    "breathing_problem": "Problemas Respiratórios\n(0: nunca a 5: sempre)",
    "noise_level": "Nível de Ruído no Ambiente\n(0: baixo a 5: alto)",
    "living_conditions": "Condições de Moradia\n(0: ruins a 5: excelentes)",
    "safety": "Sensação de Segurança\n(0: inseguro a 5: muito seguro)",
    "basic_needs": "Atendimento das Necessidades Básicas\n(0: não atendidas a 5: totalmente atendidas)",
    "academic_performance": "Desempenho Acadêmico\n(0: ruim a 5: excelente)",
    "study_load": "Carga de Estudos\n(0: baixa a 5: muito alta)",
    "teacher_student_relationship": "Relação Professor-Aluno\n(0: ruim a 5: excelente)",
    "future_career_concerns": "Preocupações com a Carreira\n(0: baixas a 5: altas)",
    "social_support": "Suporte Social\n(0: baixo a 5: alto)",
    "peer_pressure": "Pressão dos Colegas\n(0: baixa a 5: alta)",
    "extracurricular_activities": "Atividades Extracurriculares\n(0: poucas a 5: muitas)",
    "bullying": "Frequência de Bullying\n(0: nunca a 5: sempre)",
}


for feature, label in feature_explainer.items():
    # Define o range do slider com base na feature
    max_val = (
        1
        if feature == "mental_health_history"
        else (2 if feature == "blood_pressure" else 5)
    )

    user_inputs[feature] = st.sidebar.slider(
        label=label,
        min_value=0,
        max_value=max_val,
        value=max_val // 2,  # Valor padrão é o meio da escala
        step=1,
    )

# -----------------------------------------------------------------------------
# Área Principal da Aplicação
# -----------------------------------------------------------------------------
st.title("Sistema de Previsão de Estresse em Estudantes 🧠")

st.markdown(
    """
Esta aplicação utiliza um modelo de Machine Learning (*Random Forest*) para prever o nível de estresse 
de um estudante com base em 20 fatores psicológicos, sociais e ambientais.

**Como usar:**
1.  Ajuste os parâmetros na barra lateral esquerda para refletir o perfil do estudante.
2.  Clique no botão "Analisar Nível de Estresse" abaixo.
3.  O resultado da predição será exibido, junto com a probabilidade de cada classe.
"""
)

# --- Botão para realizar a predição ---
if st.button("Analisar Nível de Estresse", type="primary", use_container_width=True):
    if model:
        # --- Preparação dos dados de entrada ---
        # Converte o dicionário de inputs em um DataFrame do Pandas.
        # É crucial que a ordem das colunas seja a mesma usada no treinamento.
        input_df = pd.DataFrame([user_inputs])

        # Garante a ordem correta das colunas
        feature_order = list(feature_explainer.keys())
        input_df = input_df[feature_order]

        # --- Realização da Predição ---
        prediction = model.predict(input_df)
        prediction_proba = model.predict_proba(input_df)

        # Mapeia a saída numérica para um texto descritivo
        stress_levels = {0: "✅ Baixo", 1: "⚠️ Médio", 2: "🔴 Alto"}
        result_text = stress_levels.get(prediction[0], "Desconhecido")

        st.divider()

        # --- Exibição dos Resultados ---
        st.subheader("Resultado da Análise", divider="rainbow")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(label="**Nível de Estresse Previsto**", value=result_text)

        with col2:
            st.write("**Confiança da Predição:**")
            # Formata as probabilidades em um DataFrame para exibição
            proba_df = pd.DataFrame(
                prediction_proba,
                columns=["Baixo", "Médio", "Alto"],
                index=["Probabilidade"],
            ).T
            proba_df.rename(columns={"Probabilidade": "%"}, inplace=True)
            proba_df["%"] = proba_df["%"].apply(lambda x: f"{x:.1%}")
            st.dataframe(proba_df, use_container_width=True)

    else:
        st.error("O modelo não pôde ser carregado. A predição não pode ser realizada.")
