import streamlit as st
import duckdb
import plotly.express as px
import os
from dotenv import load_dotenv


# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================

st.set_page_config(
    page_title="Dashboard do Arroz",
    page_icon="🌾",
    layout="wide"
)


# =========================
# CARREGAR VARIÁVEIS DO .ENV
# =========================

load_dotenv()

DB_PATH = os.getenv("banco_dados")

if DB_PATH is None:
    st.error("A variável DB_PATH não foi encontrada no arquivo .env.")
    st.stop()


# =========================
# CONEXÃO COM DUCKDB
# =========================

con = duckdb.connect(
    DB_PATH,
    read_only=True
)


# =========================
# TÍTULO
# =========================

st.title("🌾 Dashboard do Mercado de Arroz")

st.write(
    "Acompanhamento de preços, dólar, diesel e indicadores do mercado."
)


# =========================
# BARRA LATERAL
# =========================

st.sidebar.header("🔎 Filtros")


# Filtro de estado
estado = st.sidebar.selectbox(
    "Estado",
    [
        "Todos",
        "Rio Grande do Sul",
        "Santa Catarina",
        "Paraná"
    ]
)


# Filtro de período
periodo = st.sidebar.selectbox(
    "Período",
    [
        "Últimos 30 dias",
        "Últimos 90 dias",
        "Último ano",
        "Todo o período"
    ]
)


# Filtro de produto
produto = st.sidebar.selectbox(
    "Produto",
    [
        "Arroz",
        "Dólar",
        "Diesel"
    ]
)


# Mostrar filtros selecionados
st.write("Estado selecionado:", estado)
st.write("Período selecionado:", periodo)
st.write("Produto selecionado:", produto)


# =========================
# DADOS - CEPEA
# =========================

query = """
SELECT
    date,
    valor_BRL,
    valor_US
FROM cepea_stagging
ORDER BY date
"""

df_cepea = con.execute(query).fetchdf()


# =========================
# GRÁFICO
# =========================

st.subheader("Evolução do preço")

fig = px.line(
    df_cepea,
    x="date",
    y="valor_BRL",
    markers=True,
    title="Preço do arroz - CEPEA"
)

fig.update_layout(
    xaxis_title="Data",
    yaxis_title="Preço (R$)",
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
