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

#st.title("Flight Cancellation", anchor="title")
st.header("👎Addressing Issues", anchor="chap-1")


with st.expander("😕 PASSENGERS"):
    st.write('Travel delays can result in:')

    st.write("🔹*Stress* for business travelers and tourists.")
    st.write(" ")
    st.write("🔹Disruption of itineraries.")
    st.write(" ")
    st.write("🔹Missed connections.")
    st.write(" ")
    st.write("🔹Delayed arrival at destinations.")
    st.write(" ")
    st.write("🔹Additional costs for accommodations due to changes in hotel reservations, planned activities, and ground transportation expenses.")

with st.expander("✈️ AIRLINES"):
    st.write('Impact on airline reputation:')
    st.write(" ")
    st.write("🔹Dissatisfied passengers share negative experiences.")
    st.write(" ")
    st.write('Loss of revenue:')
    st.write("🔹Due to refunds and rescheduling of canceled flights.")
    st.write(" ")
    st.write("Impact on operations and logistics:")
    st.write(" ")
    st.write("🔹Changes in aircraft allocation, crew scheduling, and passenger re-accommodation on other flights.")



st.header("📊 Data", anchor="chap-1")
with st.expander("📁 DATA"):
    st.write("Kaggle +5.8M dataset consisting of 3 tables that contains information about all the flights canceled or delayed at all airports in the United States.")
    url = "https://www.kaggle.com/datasets/usdot/flight-delays"
    st.markdown("Check out this [link](%s) on Kaggle. " % url)

with st.expander("📂 FEATURES"):
    st.write("🔹Origin airport")
    st.write("🔹Destination airport")
    st.write("🔹Day")
    st.write("🔹Day of week")
    st.write("🔹Month")
    st.write("🔹Scheduled arrival")
    st.write("🔹Airline")
    st.write("🔹Duration")

with st.expander("📂 TARGET"):
    st.write("🔹Cancelled")
    st.write("🔹Delay")

st.header("🔎 Technical approach", anchor="chap-1")
with st.expander("🤖 MACHINE LEARNING"):
    st.write("🔹XG Boost Classificator")
    st.write("🔹Decision Tree Classifier")
