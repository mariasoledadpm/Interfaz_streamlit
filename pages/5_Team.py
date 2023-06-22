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

st.title("SureFly team☕", anchor="title")
st.header("Batch 1249, Le Wagon", anchor="chap-1")
st.subheader("Data Science", anchor="sub-1")

with st.expander("TEAM"):

    c1,c2,c3 = st.columns(3)
    with c1:
        image1 = Image.open("images/diego2.png")
        st.image(image1, caption="Diego García-Huidobro")
        st.markdown(
            """
            <div style="display: flex; justify-content: center;">
                <img src="https://storage.googleapis.com/taxifare_mariasoledadpm/Untitled.png" alt="Imagen" width="200"/>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c2:
        image2 = Image.open("images/sole2.png")
        st.image(image2, caption="María Soledad Peña")
        st.markdown(
            """
            <div style="display: flex; justify-content: center;">
                <img src="https://storage.googleapis.com/taxifare_mariasoledadpm/Sole.png" alt="Imagen" width="200"/>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c3:
        image3 = Image.open("images/nacho.jpeg")
        st.image(image3, caption="Ignacio Lambardi")
        st.markdown(
            """
            <div style="display: flex; justify-content: center;">
                <img src="https://storage.googleapis.com/taxifare_mariasoledadpm/Nacho.png" alt="Imagen" width="200"/>
            </div>
            """,
            unsafe_allow_html=True
        )
