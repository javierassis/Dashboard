import streamlit as st
from datetime import datetime, timedelta

# Título
st.title("🏁 Seguimiento de Metas - 45 días")

# Lista de personas
personas = [
    "Maite", "Miguel I.", "Katia", "Sebastian", "Walter",
    "Gabriela", "Nemesys", "Miguel G", "Julián",
    "Deivis 1", "Deivis 2", "Marcos", "Cristian Estupiñan",
    "Ermes", "Maria Judith", "Yuli Ramon", "Laura", "Erick"
]

# Estado inicial (guardar en sesión para mantener)
if "cumplidos" not in st.session_state:
    st.session_state.cumplidos = {persona: False for persona in personas}
if "inicio" not in st.session_state:
    st.session_state.inicio = datetime.today()

# Mostrar lista con checkboxes
st.subheader("✅ Marcar quien ha cumplido:")
for persona in personas:
    st.session_state.cumplidos[persona] = st.checkbox(persona, st.session_state.cumplidos[persona])

# Calcular porcentaje de cumplimiento
total = len(personas)
cumplidos = sum(1 for cumplido in st.session_state.cumplidos.values() if cumplido)
porcentaje = cumplidos / total

# Calcular días transcurridos y ritmo esperado
dias_transcurridos = (datetime.today() - st.session_state.inicio).days
dias_totales = 45
ritmo_esperado = dias_transcurridos / dias_totales

# Elegir color de la barra
if porcentaje >= ritmo_esperado:
    color = "green"
else:
    color = "red"

# Mostrar barra de progreso
st.markdown(f"### Progreso: {cumplidos} de {total} ({porcentaje:.0%})")
st.markdown(
    f"""
    <div style='background-color: lightgray; border-radius: 5px; overflow: hidden;'>
        <div style='width: {porcentaje*100}%; background-color: {color}; padding: 10px; color: white; text-align: center;'>
            {porcentaje:.0%}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Mostrar fecha de inicio y días transcurridos
st.caption(f"📅 Día {dias_transcurridos} de 45")

# Botón para reiniciar
if st.button("🔄 Reiniciar progreso"):
    for persona in personas:
        st.session_state.cumplidos[persona] = False
    st.session_state.inicio = datetime.today()
    st.experimental_rerun()
