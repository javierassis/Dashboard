import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Estilo de fondo
st.markdown("""
    <style>
    .stApp {
        background-color: #e6f2ff;
    }
    </style>
""", unsafe_allow_html=True)

# Fechas
inicio = datetime(2025, 7, 22)
fecha_limite = datetime(2025, 9, 5)
hoy = datetime.now()
dias_totales = (fecha_limite - inicio).days + 1
dias_transcurridos = (hoy - inicio).days + 1
dias_transcurridos = max(1, min(dias_transcurridos, dias_totales))  # Mantener entre 1 y 45
dias_restantes = (fecha_limite - hoy).days

# Lista de personas
nombres = [
    "Maite", "Miguel I.", "Katia", "Sebastian", "Walter",
    "Gabriela", "Nemesys", "Miguel G", "Julián", "Deivis x 2",
    "Marcos", "Cristian estupiñan", "Ermes", "Maria judith",
    "Yuli Ramon", "Laura", "Erick"
]

# Crear DataFrame
df = pd.DataFrame({
    "Nombre": nombres,
    "Día actual": [dias_transcurridos] * len(nombres),
    "Texto": [f"Día {dias_transcurridos}" for _ in nombres]
})

# Título
st.title("Mandes")

# Fecha límite
st.write(f"📅 Fecha límite para cumplir: {fecha_limite.strftime('%Y-%m-%d')}")

# Alerta días restantes
if dias_restantes > 10:
    st.success(f"🟢 Quedan {dias_restantes} días para cumplir el objetivo.")
elif 5 < dias_restantes <= 10:
    st.warning(f"🟠 Atención: Quedan solo {dias_restantes} días.")
elif 0 < dias_restantes <= 5:
    st.error(f"🔴 ¡Urgente! Quedan solamente {dias_restantes} días.")
else:
    st.error("⛔ La fecha límite ya ha pasado.")

# Crear gráfico
fig = px.bar(
    df,
    y="Nombre",
    x="Día actual",
    orientation="h",
    text="Texto",
    color="Día actual",
    color_continuous_scale="RdYlGn_r",  # verde (día 1) → rojo (día 45)
    range_x=[1, dias_totales],
)

# Ajustes visuales
fig.update_traces(
    textposition="inside",
    insidetextanchor="start",
    textfont_color="black"
)

fig.update_layout(
    coloraxis_colorbar=dict(title="Día actual"),
    yaxis=dict(autorange="reversed"),
    xaxis_title="Días transcurridos",
    plot_bgcolor="#e6f2ff",
    paper_bgcolor="#e6f2ff",
    margin=dict(l=150, r=40, t=40, b=40)
)

# Mostrar gráfico
st.plotly_chart(fig, use_container_width=True)

