import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Lista completa de personas
nombres = [
    "Maite", "Miguel I.", "Katia", "Sebastian", "Walter", 
    "Gabriela", "Nemesys", "Miguel G", "Julián", "Deivis x 2",
    "Marcos", "Cristian estupiñan", "Ermes", "Maria judith", 
    "Yuli Ramon", "Laura", "Erick"
]

# Aquí defines los días de atraso o tiempo usado para cada persona (ejemplo)
dias_atraso = [40, 10, 30, 5, 0, 15, 45, 20, 37, 7, 12, 22, 8, 16, 25, 14, 33]

# Parámetros
plazo_dias = 45
hoy = datetime(2025, 7, 22)
fecha_limite = hoy + timedelta(days=plazo_dias)

# Calcular progreso (1 = a tiempo, 0 = límite, menos 0 = atraso)
progreso = [(plazo_dias - d) / plazo_dias for d in dias_atraso]
progreso = [max(0, min(1, p)) for p in progreso]  # limitar entre 0 y 1

df = pd.DataFrame({
    "Nombre": nombres,
    "Días de atraso": dias_atraso,
    "Progreso": progreso
})

# Mostrar título y fechas
st.title("Mandes")
st.write(f"🕒 Fecha y hora actual: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
st.write(f"📅 Fecha límite para cumplir: {fecha_limite.strftime('%Y-%m-%d')}")

# Crear gráfico de barras horizontal con colores de progreso (rojo a verde)
fig = px.bar(
    df,
    y="Nombre",
    x="Progreso",
    orientation="h",
    color="Progreso",
    color_continuous_scale=["red", "green"],
    range_x=[0, 1],
    text=df["Días de atraso"].apply(lambda x: f"{x} días de atraso")
)

fig.update_traces(textposition="inside", insidetextanchor="middle", textfont_color="white")
fig.update_layout(
    coloraxis_colorbar=dict(title="Progreso %"),
    yaxis=dict(autorange="reversed"),
    plot_bgcolor="white",
    paper_bgcolor="white",
    margin=dict(l=150, r=40, t=40, b=40)
)

st.plotly_chart(fig, use_container_width=True)


