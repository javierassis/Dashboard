import streamlit as st
import datetime
import plotly.graph_objects as go
import json

st.set_page_config(layout="wide")

nombres = ["Maite", "Miguel I.", "Katia", "Walter", "Gabriela", "Nemesys",
           "Miguel G", "Julián", "Marcos", "Ermes", "Maria judith", "Yuli Ramon",
           "Laura", "Erick", "Sebastian", "Deivis x 2", "ian estupiñan"]

fecha_objetivo = datetime.datetime(2024, 9, 5)
fecha_actual = datetime.datetime.now()
dias_restantes = (fecha_objetivo - fecha_actual).days
progreso = (1 - dias_restantes / 45) * 100
progreso = max(0, min(progreso, 100))  # Limita el progreso entre 0 y 100

with open("estado_cumplido.json", "r", encoding="utf-8") as f:
    estado_cumplido = json.load(f)

fig = go.Figure()

for nombre in nombres:
    cumplido = estado_cumplido.get(nombre, {}).get("cumplido", False)

    if cumplido:
        dias = 45
        texto = "✅ Cumplido"
        color = "lightgreen"
    else:
        dias = 45 - dias_restantes
        texto = f"{dias} días | {progreso:.0f}%"
        color = "skyblue"

    fig.add_trace(go.Bar(
        y=[nombre],
        x=[dias],
        orientation='h',
        name=nombre,
        marker=dict(color=color),
        hovertemplate=f"<b>{nombre}</b><br>{texto}<extra></extra>",
        text=[texto],
        textposition='inside'
    ))

fig.update_layout(
    title="Progreso por Persona hacia el 5 de septiembre",
    xaxis_title="Días",
    yaxis_title="",
    xaxis=dict(range=[0, 45]),
    barmode='stack',
    height=800,
    margin=dict(l=200, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)
