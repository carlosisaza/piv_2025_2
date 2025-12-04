import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Configuración inicial
st.set_page_config(page_title="Dashboard Churn Telco", layout="wide")
st.title("📊 Dashboard interactivo de Churn (Telco)")


# Cargar datos
df = pd.read_csv('/workspaces/piv_2025_2/src/proyecto_integrador/static/csv/dataset_enriquecido.csv')


# Limpieza básica
df["Churn"] = df["Churn"].str.strip().str.upper()
df["MonthlyCharges"] = pd.to_numeric(df["MonthlyCharges"], errors="coerce")
df["tenure"] = pd.to_numeric(df["tenure"], errors="coerce")

# -----------------------------
# Sidebar: filtros
# -----------------------------
st.sidebar.header("Filtros")
contracts = st.sidebar.multiselect("Contrato", df["Contract"].unique(), default=df["Contract"].unique())
tech_support = st.sidebar.multiselect("Soporte técnico", df["TechSupport"].unique(), default=df["TechSupport"].unique())
internet_service = st.sidebar.multiselect("Servicio de internet", df["InternetService"].unique(), default=df["InternetService"].unique())

tenure_range = st.sidebar.slider("Antigüedad (meses)", int(df["tenure"].min()), int(df["tenure"].max()), (int(df["tenure"].min()), int(df["tenure"].max())))
charge_range = st.sidebar.slider("Cargos mensuales (USD)", float(df["MonthlyCharges"].min()), float(df["MonthlyCharges"].max()), (float(df["MonthlyCharges"].min()), float(df["MonthlyCharges"].max())))

# Aplicar filtros
filtered = df[
    (df["Contract"].isin(contracts)) &
    (df["TechSupport"].isin(tech_support)) &
    (df["InternetService"].isin(internet_service)) &
    (df["tenure"].between(tenure_range[0], tenure_range[1])) &
    (df["MonthlyCharges"].between(charge_range[0], charge_range[1]))
]

# -----------------------------
# KPIs principales
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

churn_rate = (filtered["Churn"] == "YES").mean() * 100
col1.metric("Tasa de churn", f"{churn_rate:.2f}%")

col2.metric("Clientes filtrados", f"{len(filtered):,}")

col3.metric("Cargos mensuales promedio", f"${filtered['MonthlyCharges'].mean():.2f}")

col4.metric("Antigüedad promedio", f"{filtered['tenure'].mean():.0f} meses")

st.divider()

# -----------------------------
# Gráficos interactivos
# -----------------------------
tab1, tab2, tab3 = st.tabs(["Churn por contrato", "Cargos vs antigüedad", "Soporte técnico"])

with tab1:
    st.subheader("Distribución de churn por tipo de contrato")
    fig1 = px.histogram(filtered, x="Contract", color="Churn", barmode="group",
                        title="Churn por contrato")
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.subheader("Relación entre cargos mensuales y antigüedad")
    fig2 = px.scatter(filtered, x="MonthlyCharges", y="tenure", color="Churn",
                      title="Cargos vs antigüedad con churn")
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.subheader("Impacto del soporte técnico en churn")
    fig3 = px.histogram(filtered, x="TechSupport", color="Churn", barmode="group",
                        title="Soporte técnico vs churn")
    st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# Tabla detallada
# -----------------------------
st.subheader("📋 Datos filtrados")
st.dataframe(filtered.head(50))
