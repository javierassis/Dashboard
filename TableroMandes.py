import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Fecha base: hoy
fecha_hoy = datetime(2025, 7, 22)

# Duración del plazo en días
plazo_dias = 45

# Lista de personas con fecha de inicio (ejemplo: hoy para todos)
personas = [
    {'nombre': 'Maite', 'fecha_inicio': fecha_hoy},
    {'nombre': 'Miguel I.', 'fecha_inicio': fecha_hoy},
    {'nombre': 'Katia', 'fecha_inicio': fecha_hoy},
    {'nombre': 'Sebastian', 'fecha_inicio': fecha_hoy},
    {'nombre': 'Walter', 'fecha_inicio': fecha_hoy},
]

# Función para calcular progreso basado en días transcurridos
def calcular_progreso(fecha_inicio, fecha_hoy, plazo_dias):
    dias_transcurridos = (fecha_hoy - fecha_inicio).days
    progreso = min(max(dias_transcurridos / plazo_dias * 100, 0), 100)
    return progreso

# Crear DataFrame con progreso calculado para cada persona
data = []
for p in personas:
    progreso = calcular_progreso(p['fecha_inicio'], fecha_hoy, plazo_dias)
    data.append({'Persona': p['nombre'], 'Progreso': progreso})

df = pd.DataFrame(data)

# Mostrar fecha límite para completar
fecha_limite = fecha_hoy + timedelta(days=plazo_dias)
st.write(f"📅 Fecha límite para cumplir: {fecha_limite.strftime('%Y-%m-%d')}")

# Crear gráfico de barras horizontal con color basado en progreso
fig = px.bar(
    df,
    x='Progreso',
    y='Persona',
    orientation='h',
    color='Progreso',
    color_continuous_scale=['red', 'green'],
    range_color=[0, 100],
    labels={'Progreso': 'Progreso (%)', 'Persona': 'Nombre'}
)

fig.update_layout(coloraxis_colorbar=dict(title="Progreso %"))

st.plotly_chart(fig)


