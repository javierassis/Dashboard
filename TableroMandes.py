import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os
from datetime import datetime

st.set_page_config(layout="wide")

# Fondo verde esmeralda claro
page_bg_color = """
<style>
body {
    background-color: #C9F5C1 !important;
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# Fecha final
fecha_final = datetime.strptime("2025-09-05", "%Y-%m-%d").date()
fecha_hoy = datetime.today().date()
dias_transcurridos = (fecha_hoy - datetime.strptime("2025-07-21", "%Y-%m-%d").date()).days

# Lista de nombres
nombres = [
    "Maite", "Miguel I.", "Katia", "Sebastian", "Walter", "Gabriela", "Nemesys", "Miguel G",
    "Julián", "Delvis x 2", "Marcos", "estuñán", "Ermes", "maria judith", "Yuli Ramon",
    "Laura", "Erick"
]

# Cargar estado guardado si existe
estado_archivo = "estado_cumplido.json"
if os.path.exists(estado_archivo):
    with open(estado_archivo, "r") as f:
        estado_cumplido = json.load(f)
else:
    estado_cumplido = {nombre: 0 for nombre in nombres}

# Mostrar controles
st.title("🔄 Seguimiento de días cumplidos")
st.write(f"📆 **Días transcurridos:** {dias_transcurridos} | 🗓️ Fecha actual: {fecha_hoy.strftime('%d-%m-%Y')}")

nombre_seleccionado = st.selectbox("Selecciona un nombre para marcar un día cumplido:", nombres)
if st.button("✅ Marcar un día cumplido"):
    if estado_cumplido[nombre_seleccionado] < dias_transcurridos:
        estado_cumplido[nombre_seleccionado] += 1
        with open(estado_archivo, "w") as f:
            json.dump(estado_cumplido, f)
        st.success(f"Se marcó un día cumplido para {nombre_seleccionado}.")
    else:
        st.warning("No puedes marcar más días de los que han transcurrido.")

# Crear DataFrame
df = pd.DataFrame({
    "Nombre": list(estado_cumplido.keys()),
    "Días cumplidos": list(estado_cumplido.values())
})
df["Porcentaje"] = (df["Días cumplidos"] / dias_transcurridos) * 100 if dias_transcurridos > 0 else 0
df["Texto"] = df["Días cumplidos"].astype(str) + " días | " + df["Porcentaje"].round(1).astype(str) + "%"

# Dibujar gráfico de barras horizontales
fig = px.bar(
    df.sort_values("Días cumplidos", ascending=False),
    y="Nombre",
    x="Días cumplidos",
    orientation="h",
    color="Días cumplidos",
    color_continuous_scale="RdYlGn",
    text="Texto",
    labels={"Días cumplidos": "Día actual"}
)

# Estilo de las barras
fig.update_traces(
    textfont_size=16,
    textposition="outside",
    marker_line_color="black",
    marker_line_width=1.5
)

# Ajustes visuales
fig.update_layout(
    plot_bgcolor="#C9F5C1",  # mismo color que el fondo de la página
    paper_bgcolor="#C9F5C1",
    yaxis=dict(tickfont=dict(size=16, family="Arial", color="black")),
    xaxis_title="Días cumplidos",
    yaxis_title="",
    font=dict(size=16),
    margin=dict(l=100, r=50, t=30, b=30),
    coloraxis_colorbar=dict(title="Día actual"),
)

st.plotly_chart(fig, use_container_width=True)
