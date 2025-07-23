import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Estilo personalizado
st.markdown("""
    <style>
    .stApp {
        background-color: #ccf2cc; /* Verde esmeralda claro */
    }
    .css-1d391kg {
        padding: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Fechas
inicio = datetime(2025, 7, 22)
fecha_limite = datetime(2025, 9, 5)
hoy = datetime.now()
dias_totales = (fecha_limite - inicio).days + 1
dias_transcurridos = (hoy - inicio).days + 1
dias_transcurridos = max(1, min(dias_transcurridos, dias_totales))
dias_restantes = (fecha_limite - hoy).days

# Lista de personas
nombres = [
    "Maite", "Miguel I.", "Katia", "Sebastian", "Walter",
    "Gabriela", "Nemesys", "Miguel G", "Julián", "Deivis x 2",
    "Marcos", "Cristian estupiñan", "Ermes", "Maria judith",
    "Yuli Ramon", "Laura", "Erick"
]

# Porcentaje de avance
progreso_porcentaje = round((dias_transcurridos / dias_totales) * 100)

# Crear DataFrame
df = pd.DataFrame({
    "Nombre": [f"<b>{n}</b>" for n in nombres],  # Nombres en negrita con HTML
    "Días": [dias_transcurridos] * len(nombres),
    "Porcentaje": [progreso_porcentaje] * len(nombres),
    "Texto": [f"<b style='font-size:16px'>{dias_transcurridos} días | {progreso_porcentaje}%</b>" for _ in nombres]
})

# Título
st.title("Mandes")

# Fecha límite
st.write(f"📅 Fecha límite para cumplir: {fecha_limite.strftime('%Y-%m-%d')}")

# Mensaje de progreso
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
    x="Días",
    y="Nombre",
    orientation="h",
    text="Texto",
    color="Días",
    color_continuous_scale="RdYlGn_r",
    range_x=[0, dias_totales]
)

# Estilo gráfico
fig.update_traces(
    textposition="inside",
    insidetextanchor="start",
    textfont_color="black",
    hovertemplate='%{y}: %{x} días'
)

fig.update_layout(
    autosize=True,
    height=60 * len(nombres),  # Se ajusta dinámicamente según número de personas
    xaxis_title="Días transcurridos",
    yaxis_title="Nombre",
    yaxis=dict(autorange="reversed", tickfont=dict(size=13)),
    plot_bgcolor="#ccf2cc",
    paper_bgcolor="#ccf2cc",
    margin=dict(l=20, r=20, t=30, b=20),
    coloraxis_colorbar=dict(title="Día actual")
)

# Mostrar gráfico con ajuste automático
st.plotly_chart(fig, use_container_width=True)
