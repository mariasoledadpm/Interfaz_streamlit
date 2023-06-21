#Importar streamlit
import streamlit as st
import datetime
import requests



#Características básicas

#1 Definir un ícono y título que tendrá la página en la pestaña del navegadorss
st.set_page_config(page_title="SureFly ✈️", page_icon="images/icono.png", layout="wide")

#2 image para agregar un logo
st.image("images/surefly_sin_fondo.png", width=200)

page_bg_img = """
<style>
[data-testid='stAppViewContainer'] {
background-image: url("https://images.unsplash.com/photo-1514542124776-b1401b7dd173?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&dl=shea-rouda-RL2xSO3vFmQ-unsplash.jpg");
background-size: cover;
}

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}

[data-testid="stToolbar"]{
right: 2rem;
}

[data-testid="stSidebar"] {
background-image: url("https://images.unsplash.com/photo-1514542124776-b1401b7dd173?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&dl=shea-rouda-RL2xSO3vFmQ-unsplash.jpg");
background-position:cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Cancelación de vuelos", anchor="title")
st.header("Problemas", anchor="chap-1")


with st.expander("😕 PASAJEROS"):
    st.write('Retrasos en los planes de viaje pueden generar:')

    st.write("▶️*Estrés* en viajeros de negocios y turistas.")
    st.write(" ")
    st.write("▶️Interrupción en itinerarios.")
    st.write(" ")
    st.write("▶️Pérdida de conexiones.")
    st.write(" ")
    st.write("▶️Demora en la llegada a destinos.")
    st.write(" ")
    st.write("▶️Costos adicionales en alojamiento por cambios en reservas de hoteles, actividades planificadas y gastos de transporte terrestre.")

with st.expander("✈️ AEROLÍNEAS"):
    st.write('Impacto en la reputación de la aerolínea:')
    st.write(" ")
    st.write("▶️Pasajeros insatisfechos comparten experiencias negativas.")
    st.write(" ")
    st.write('Pérdida de ingresos:')
    st.write("▶️Por reembolsos y reprogramación de vuelos cancelados.")
    st.write(" ")
    st.write("Impacto en operaciones y logística:")
    st.write(" ")
    st.write("▶️Cambios en asignación de aeronaves, tripulación y reacomodación de pasajeros en otros vuelos.")



st.header("Data", anchor="chap-1")
with st.expander("DATA"):
    st.write(" ")

with st.expander(":sunglasses: MEJORAS"):
    st.write("▶️Agregar variable 'Clima' aumentaría el valor de la predicción,")
    st.write("ya que se consideraría las situaciones adversas que puede enfrentar un vuelo.")
