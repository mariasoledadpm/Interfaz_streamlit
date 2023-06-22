#Importar streamlit
import streamlit as st
import datetime
import requests
from PIL import Image


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

st.title("❓ Don't you know where to look for your data?")

url = "https://www.google.com/travel/flights"
#st.write("check out this [link](%s)" % url)
st.markdown("Check out this [link](%s) on Google Flights " % url)

image = Image.open('images/ayuda_info.png')
st.image(image, width=1300, caption="User interface legend")

st.subheader("User interface legend")
st.write("🔹Black: Origin Airport")
st.write("🔹Red: Destination Airport")
st.write("🔹Yellow: Day, day of week, month")
st.write("🔹Turquoise: Arrival")
st.write("🔹Purple: Airline")
st.write("🔹Green: Duration (min)")
