import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import json
import os
import requests

# Configuración general
REPO_URL = "https://raw.githubusercontent.com/javierassis/Dashboard/main/estado_cumplido.json"
ARCHIVO_LOCAL = "estado_cumplido.json"
LOCAL = os.path.exists(ARCHIVO_LOCAL)

# --- Estilo de fondo ---
st.markdown("""
    <style>
    .stApp {
        background-color: #e6f2ff;
    }
    </style>
""", unsafe_allow_html=True)

# --- Fechas ---
inicio = datetime(2025, 7, 22)
fecha_limite = datetime(2025, 9, 5)
hoy = datetime.now()
dias_totales = (fecha_limite - inicio).days + 1
dias_transcurridos = max(1, min((hoy - inicio).days + 1, dias_totales))
dias_restantes = (fecha_limite - hoy).days

# --- Lista de personas ---
nombres = [
    "Maite", "Miguel I.", "Katia", "Sebastian", "Walter",
    "Gabriela", "Nemesys", "Miguel G", "Julián", "Deivis x 2",
    "Marcos", "Cristian estupiñan", "Ermes", "Maria judith",
    "Yuli Ramon", "Laura", "Erick"
]

# --- Cargar estado cumplido ---
try:
    if LOCAL:
        with open(ARCHIVO_LOCAL, "r") as f:
            cumplidos = json.load(f)
    else:
        response = requests.get(REPO_URL)
        cumplidos = response.json()
except:
    cumplidos = {}

# --- Interfaz para marcar cumplidos (solo en local) ---
if LOCAL:
    st.sidebar.header("✅ Marcar como cumplido")
    for nombre in nombres:
        if nombre not in cumplidos and dias_transcurridos >= dias_totales:
            if st.sidebar.button(f"Marcar '{nombre}' como cumplido"):
                cumplidos[nombre] = True
                with open(ARCHIVO_LOCAL, "w") as f:
                    json.dump(cumplidos, f)
                st.experimental_rerun()

# --- Crear DataFrame ---
dias_personales = []
colores = []
textos = []

for nombre in nombres:
    if nombre in cumplidos:
        dias = dias_totales
        color = "lightgreen"
        texto = "✅ Cumplido"
    else:
        dias = dias_transcurridos
        color = "lightblue"
        texto = f"{dias} días | {round((dias / dias_totales) * 100)}%"
    dias_personales.append(dias)
    colores.append(color)
    textos.append(texto)

df = pd.DataFrame({
    "Nombre": nombres,
    "Días": dias_personales,
    "Color": colores,
    "Texto": textos
})

# --- Mostrar información ---
st.title("Mandes - Seguimiento de Avance")
st.write(f"📅 Fecha límite: {fecha_limite.strftime('%Y-%m-%d')}")
st.write(f"📆 Hoy: {hoy.strftime('%Y-%m-%d')} | Día {dias_transcurridos} de {dias_totales}")

if dias_restantes > 10:
    st.success(f"🟢 Quedan {dias_restantes} días para cumplir el objetivo.")
elif 5 < dias_restantes <= 10:
    st.warning(f"🟠 Atención: Quedan solo {dias_restantes} días.")
elif 0 < dias_restantes <= 5:
    st.error(f"🔴 ¡Urgente! Quedan solamente {dias_restantes} días.")
else:
    st.error("⛔ La fecha límite ya ha pasado.")

# --- Crear gráfico ---
fig = px.bar(
    df,
    x="Días",
    y="Nombre",
    orientation="h",
    text="Texto",
    color="Color",
    color_discrete_map="identity",
    range_x=[0, dias_totales]
)

fig.update_traces(
    textposition="inside",
    insidetextanchor="start",
    textfont_color="black",
    textfont_size=14
)

fig.update_layout(
    height=700,
    width=950,
    xaxis_title="Días transcurridos",
    yaxis_title="Nombre",
    yaxis=dict(autorange="reversed"),
    plot_bgcolor="#e6f2ff",
    paper_bgcolor="#e6f2ff",
    margin=dict(l=140, r=40, t=30, b=40),
    coloraxis_showscale=False
)

fig.add_vline(
    x=dias_totales,
    line_width=2,
    line_dash="dash",
    line_color="black",
    annotation_text="Meta",
    annotation_position="top right"
)

st.plotly_chart(fig, use_container_width=True)
