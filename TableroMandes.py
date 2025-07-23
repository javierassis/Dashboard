import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Estilo de fondo y fuente en negrilla para los nombres
st.markdown("""
    <style>
    .stApp {
        background-color: #d2f8d2; /* Verde esmeralda claro */
    }
    .yaxis .tick text {
        font-weight: bold !important;
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
progreso_porcentaje = round((dias_transcurridos / dias_totales) * 100)

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
    "Días": [dias_transcurridos] * len(nombres),
    "Meta": [dias_totales] * len(nombres),
    "Porcentaje": [progreso_porcentaje] * len(nombres),
    "Texto": [f"{dias_transcurridos} días | {progreso_porcentaje}%" for _ in nombres]
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

# Crear gráfico con barra base y barra de progreso
fig = go.Figure()

# Barra de meta (gris claro)
fig.add_trace(go.Bar(
    x=df["Meta"],
    y=df["Nombre"],
    orientation='h',
    marker=dict(color="#f0f0f0"),
    showlegend=False,
    hoverinfo='skip'
))

# Barra de progreso (color)
fig.add_trace(go.Bar(
    x=df["Días"],
    y=df["Nombre"],
    orientation='h',
    text=df["Texto"],
    marker=dict(color=df["Días"], colorscale="RdYlGn_r"),
    textposition="inside",
    insidetextanchor="start",
    textfont=dict(color="black", size=16),  # Tamaño del texto ampliado
    name="Progreso"
))

# Línea de meta
fig.add_shape(
    type="line",
    x0=dias_totales,
    y0=-0.5,
    x1=dias_totales,
    y1=len(nombres)-0.5,
    line=dict(color="black", dash="dash"),
)

fig.add_annotation(
    x=dias_totales,
    y=-1,
    text="🎯 Meta",
    showarrow=False,
    font=dict(size=12, color="black"),
)

# Configuración del gráfico
fig.update_layout(
    height=700,
    width=950,
    xaxis_title="Días transcurridos",
    yaxis_title="Nombre",
    yaxis=dict(autorange="reversed", tickfont=dict(size=12, family="Arial", color="black", weight="bold")),
    plot_bgcolor="#d2f8d2",
    paper_bgcolor="#d2f8d2",
    margin=dict(l=140, r=40, t=30, b=40),
    coloraxis_colorbar=dict(title="Día actual"),
    barmode='overlay'
)

# Mostrar gráfico
st.plotly_chart(fig, use_container_width=True)
