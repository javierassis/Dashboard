import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Datos ejemplo
nombres = ['Walter', 'Sebastian', 'Katia', 'Miguel I.', 'Maite']
hoy = datetime(2025, 7, 22)
fecha_limite = hoy + timedelta(days=45)  # 45 días desde hoy

# Supongamos que 'progreso' es % completado, donde 1 = 100% completado
# Por ejemplo, valores entre 0 y 1
progresos = [0.8, 0.4, 0.2, 0.6, 0.1]

df = pd.DataFrame({
    'Nombre': nombres,
    'Progreso': progresos
})

st.title("Mandes")
st.write(f"📅 Fecha límite para cumplir: {fecha_limite.strftime('%Y-%m-%d')}")

fig = px.bar(
    df,
    y='Nombre',
    x='Progreso',
    orientation='h',
    color='Progreso',
    color_continuous_scale=['red', 'green'],  # rojo=0, verde=1
    range_x=[0, 1],
    labels={'Progreso': 'Progreso (%)', 'Nombre': 'Nombre'},
    text=df['Progreso'].apply(lambda x: f"{int(x*100)}%")
)

fig.update_traces(textposition='inside', insidetextanchor='middle')
fig.update_layout(
    coloraxis_colorbar=dict(title="Progreso %"),
    yaxis=dict(autorange="reversed"),  # Para que el primer nombre esté arriba
    plot_bgcolor='white',  # Fondo blanco
    paper_bgcolor='white',
    margin=dict(l=100, r=40, t=40, b=40)
)

st.plotly_chart(fig, use_container_width=True)


