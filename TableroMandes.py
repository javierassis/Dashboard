import streamlit as st
import json
import os
from datetime import datetime, timedelta

# Lista de personas
personas = [
    "Maite", "Miguel I.", "Katia", "Sebastian", "Walter", "Gabriela", "Nemesys", "Miguel G", "Julián",
    "Deivis 1", "Deivis 2", "Marcos", "Cristian Estupiñan", "Ermes", "Maria Judith", "Yuli Ramon", "Laura", "Erick"
]

# Archivo donde se guarda el progreso
archivo_progreso = "progreso.json"

# Fecha límite para cada persona (puedes personalizar)
fecha_inicio = datetime(2024, 6, 1)
dias_maximos = 45
fecha_limite = fecha_inicio + timedelta(days=dias_maximos)

# Inicializar datos si no existe
if not os.path.exists(archivo_progreso):
    progreso = {persona: {"cumplido": False, "fecha": None} for persona in personas}
    with open(archivo_progreso, "w") as f:
        json.dump(progreso, f)
else:
    with open(archivo_progreso, "r") as f:
        progreso = json.load(f)

# Título
st.title("📊 Tablero de Progreso por Persona")

# Mostrar fecha y hora actual
ahora = datetime.now()
st.write("🕒 Fecha y hora actual:", ahora.strftime("%Y-%m-%d %H:%M:%S"))
st.write("🎯 Fecha límite para cumplir:", fecha_limite.strftime("%Y-%m-%d"))

# Mostrar progreso con barras
for persona in personas:
    datos = progreso.get(persona, {"cumplido": False, "fecha": None})
    cumplido = datos["cumplido"]

    # Días restantes o de atraso
    if datos["fecha"]:
        fecha_cumplimiento = datetime.strptime(datos["fecha"], "%Y-%m-%d %H:%M:%S")
        delta = (fecha_cumplimiento - fecha_inicio).days
        dias_info = f"Cumplido en {delta} días"
    else:
        dias_resto = (fecha_limite - ahora).days
        dias_info = f"⏳ Quedan {dias_resto} días" if dias_resto >= 0 else f"❌ {abs(dias_resto)} días de atraso"

    progreso_barra = 100 if cumplido else 0
    color = "green" if cumplido else "red"

    st.write(f"**{persona}** ({dias_info})")
    st.progress(progreso_barra / 100)


