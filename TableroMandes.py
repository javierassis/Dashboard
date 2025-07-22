import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Fondo claro
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
progreso_real = max(0, min(1, dias_transcurridos / dias_totales))
dias_restantes = (fecha_limite - hoy).days

# Lista de personas
nombres = [
    "Maite", "Miguel I.", "Katia", "Sebastian", "Walter",
    "Gabriela", "Nemesys", "Miguel G", "Julián", "Deivis x 2",
    "Marcos", "Cristian estupiñan", "Ermes", "Maria judith",
    "Yuli Ramon", "Laura", "Erick"
]

# DataFrame con visual mínimo para que la barra se vea
df = pd.DataFrame({
    "Nombre": nombres,
    "Progreso": [progreso_real] * len(nombres),
    "Visual": [max(progreso_real, 0.02)] * len(nombres),  # mínimo 2% visible
    "Porcentaje": [f"{int(progreso_real * 100)} %" for _ in nombres]
})

# Encabezados
st.title("Mandes")
st.write(f"🕒 Fecha y hora actual: {hoy.strftime('%Y-%m-%d %H:%M:%S')}")
st.write(f"📅 Fecha límite para cumplir: {fecha_limite.strftime('%Y-%m-%d')}")

# Alerta por días restantes
if dias_restantes > 10:
    st.success(f"🟢 Quedan {dias_restantes} días para cumplir el objetivo.")
elif 5 < dias_restantes <= 10:
    st.warning(f"🟠 Atención: Quedan solo {dias_restantes} días.")
elif 0 < dias_restantes <= 5:
    st.error(f"🔴 ¡Urgente! Quedan solamente {dias_restantes} días.")
else:
    st.error("⛔ La fecha límite ya ha pasado.")

# Gráfico
fig = px.bar(
    df,
    y="Nombre",
    x="Visual",  # se asegura que haya al menos un 2%
    orientation="h",
    color="Progreso",
    text="Porcentaje",
    range_x=[0, 1],
    color_continuous_scale=["red", "orange", "green"]
)

fig.update_traces(
    textposition="inside",
    insidetextanchor="start",
    textfont_color="black"
)

fig.update_layout(
    coloraxis_colorbar=dict(title="Progreso %"),
    yaxis=dict(autorange="reversed"),
    plot_bgcolor="#e6f2ff",
    paper_bgcolor="#e6f2ff",
    margin=dict(l=150, r=40, t=40, b=40)
)

st.plotly_chart(fig, use_container_width=True)

