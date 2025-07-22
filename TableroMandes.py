import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import time

# Estilo personalizado con fondo azul claro
st.markdown("""
    <style>
    .stApp {
        background-color: #e6f2ff;
    }
    </style>
""", unsafe_allow_html=True)

# Datos
nombres = [
    "Maite", "Miguel I.", "Katia", "Sebastian", "Walter",
    "Gabriela", "Nemesys", "Miguel G", "Julián", "Deivis x 2",
    "Marcos", "Cristian estupiñan", "Ermes", "Maria judith",
    "Yuli Ramon", "Laura", "Erick"
]

dias_atraso = [40, 10, 30, 5, 0, 15, 45, 20, 37, 7, 12, 22, 8, 16, 25, 14, 33]
plazo_dias = 45
hoy = datetime.now()
fecha_limite = hoy + timedelta(days=plazo_dias)

# Cálculo de progreso (limitado entre 0 y 1)
progreso = [(plazo_dias - d) / plazo_dias for d in dias_atraso]
progreso = [max(0, min(1, p)) for p in progreso]

# DataFrame
df = pd.DataFrame({
    "Nombre": nombres,
    "Días de atraso": dias_atraso,
    "Progreso": progreso
})

# Título
st.title("Mandes")

# Hora y fecha
st.write(f"🕒 Fecha y hora actual: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
st.write(f"📅 Fecha límite para cumplir: {fecha_limite.strftime('%Y-%m-%d')}")

# Gráfico
fig = px.bar(
    df,
    y="Nombre",
    x="Progreso",
    orientation="h",
    color="Progreso",
    color_continuous_scale=["red", "green"],
    range_x=[0, 1],
    text=df["Progreso"].apply(lambda x: f"{int(x*100)} %")
)

fig.update_traces(
    textposition="inside",
    insidetextanchor="middle",
    textfont_color="white"
)
fig.update_layout(
    coloraxis_colorbar=dict(title="Progreso %"),
    yaxis=dict(autorange="reversed"),
    plot_bgcolor="#e6f2ff",  # fondo del gráfico
    paper_bgcolor="#e6f2ff",  # fondo general
    margin=dict(l=150, r=40, t=40, b=40)
)

st.plotly_chart(fig, use_container_width=True)

