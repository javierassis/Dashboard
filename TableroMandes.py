import streamlit as st
import json
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(layout="wide")
st.title("📊 Tablero de Seguimiento")

# Paso 1: Cargar archivo estado_cumplido.json
try:
    with open("estado_cumplido.json", "r", encoding="utf-8") as f:
        estado_actual = json.load(f)
    st.write("📁 Datos cargados desde estado_cumplido.json:", estado_actual)
except FileNotFoundError:
    st.error("❌ No se encontró el archivo estado_cumplido.json.")
    estado_actual = {}
except json.JSONDecodeError:
    st.error("❌ Error al leer el archivo JSON. Verifica su formato.")
    estado_actual = {}

# Puedes incluir aquí la lógica que uses para generar el dataframe `df`
# Aquí va un ejemplo mínimo de cómo continuar luego con los datos

# Ejemplo: DataFrame de ejemplo con nombres
nombres = ["Maite", "Miguel I.", "Katia", "Walter", "Gabriela", "Nemesys",
           "Miguel G", "Julián", "Marcos", "Ermes", "Maria judith", "Yuli Ramon",
           "Laura", "Erick", "Sebastian", "Deivis x 2", "ian estupiñan"]

datos = []
fecha_inicio = datetime(2024, 6, 1)
fecha_hoy = datetime.now()
dias_transcurridos = (fecha_hoy - fecha_inicio).days

for nombre in nombres:
    cumplido = estado_actual.get(nombre, {}).get("cumplido", False)
    estado = "Cumplido" if cumplido else f"{dias_transcurridos} días | {int((dias_transcurridos / 45) * 100)}%"
    datos.append({"Nombre": nombre, "Estado": estado, "Días": dias_transcurridos if not cumplido else 45})

df = pd.DataFrame(datos)

# Colores según cumplimiento
df["Color"] = df["Estado"].apply(lambda x: "✅ Cumplido" in x)

# Gráfico
fig = px.bar(
    df,
    x="Días",
    y="Nombre",
    orientation="h",
    text="Estado",
    color="Color",
    color_discrete_map={True: "lightgreen", False: "lightblue"},
    height=700
)

fig.update_layout(
    xaxis_title="Días transcurridos",
    yaxis_title="",
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)
