#Importar streamlit
import streamlit as st
import datetime
import requests



#Características básicas

#1 Definir un ícono y título que tendrá la página en la pestaña del navegadorss
st.set_page_config(page_title="SureFly ✈️", page_icon="images/icono.png", layout="wide")

#2 image para agregar un logo
st.image("images/surefly.png", width=200)

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


#3 title para definir el título que ve el usuario al abrir la página
#with open('style.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Travel relaxed, plan with SureFly")



with st.form(key='params_for_api'):
    #4 Crear columnas para alinear los botones
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

    # Agregar AEROPUERTO DE ORIGEN en la primera columna
    aeropuerto_origen = col1.selectbox(
        'Origin Airport',
        ('ABE', 'ABI', 'ABQ', 'ABR', 'ABY', 'ACK', 'ACT', 'ACV', 'ACY', 'ADK', 'ADQ', 'AEX', 'AGS', 'AKN',
        'ALB', 'ALO', 'AMA', 'ANC', 'APN', 'ASE', 'ATL', 'ATW', 'AUS', 'AVL', 'AVP', 'AZO', 'BDL', 'BET', 'BFL', 'BGM',
        'BGR', 'BHM', 'BIL', 'BIS', 'BJI', 'BLI', 'BMI', 'BNA', 'BOI', 'BOS', 'BPT', 'BQK', 'BQN', 'BRD', 'BRO', 'BRW',
        'BTM', 'BTR', 'BTV', 'BUF', 'BUR', 'BWI', 'BZN', 'CAE', 'CAK', 'CDC', 'CDV', 'CEC', 'CHA', 'CHO', 'CHS', 'CID',
        'CIU', 'CLD', 'CLE', 'CLL', 'CLT', 'CMH', 'CMI', 'CMX', 'CNY', 'COD', 'COS', 'COU', 'CPR', 'CRP', 'CRW', 'CSG',
        'CVG', 'CWA', 'DAB', 'DAL', 'DAY', 'DBQ', 'DCA', 'DEN', 'DFW', 'DHN', 'DIK', 'DLG', 'DLH', 'DRO', 'DSM', 'DTW',
        'DVL', 'EAU', 'ECP', 'EGE', 'EKO', 'ELM', 'ELP', 'ERI', 'ESC', 'EUG', 'EVV', 'EWN', 'EWR', 'EYW', 'FAI', 'FAR',
        'FAT', 'FAY', 'FCA', 'FLG', 'FLL', 'FNT', 'FSD', 'FSM', 'FWA', 'GCC', 'GCK', 'GEG', 'GFK', 'GGG', 'GJT', 'GNV',
        'GPT', 'GRB', 'GRI', 'GRK', 'GRR', 'GSO', 'GSP', 'GST', 'GTF', 'GTR', 'GUC', 'GUM', 'HDN', 'HIB', 'HLN', 'HNL',
        'HOB', 'HOU', 'HPN', 'HRL', 'HSV', 'HYA', 'HYS', 'IAD', 'IAG', 'IAH', 'ICT', 'IDA', 'ILG', 'ILM', 'IMT', 'IND',
        'INL', 'ISN', 'ISP', 'ITH', 'ITO', 'JAC', 'JAN', 'JAX', 'JFK', 'JLN', 'JMS', 'JNU', 'KOA', 'KTN', 'LAN', 'LAR',
        'LAS', 'LAW', 'LAX', 'LBB', 'LBE', 'LCH', 'LEX', 'LFT', 'LGA', 'LGB', 'LIH', 'LIT', 'LNK', 'LRD', 'LSE', 'LWS',
        'MAF', 'MBS', 'MCI', 'MCO', 'MDT', 'MDW', 'MEI', 'MEM', 'MFE', 'MFR', 'MGM', 'MHK', 'MHT', 'MIA', 'MKE', 'MKG',
        'MLB', 'MLI', 'MLU', 'MMH', 'MOB', 'MOT', 'MQT', 'MRY', 'MSN', 'MSO', 'MSP', 'MSY', 'MTJ', 'MVY', 'MYR', 'OAJ',
        'OAK', 'OGG', 'OKC', 'OMA', 'OME', 'ONT', 'ORD', 'ORF', 'ORH', 'OTH', 'OTZ', 'PAH', 'PBG', 'PBI', 'PDX', 'PHF',
        'PHL', 'PHX', 'PIA', 'PIB', 'PIH', 'PIT', 'PLN', 'PNS', 'PPG', 'PSC', 'PSE', 'PSG', 'PSP', 'PUB', 'PVD', 'PWM',
        'RAP', 'RDD', 'RDM', 'RDU', 'RHI', 'RIC', 'RKS', 'RNO', 'ROA', 'ROC', 'ROW', 'RST', 'RSW', 'SAF', 'SAN', 'SAT',
        'SAV', 'SBA', 'SBN', 'SBP', 'SCC', 'SCE', 'SDF', 'SEA', 'SFO', 'SGF', 'SGU', 'SHV', 'SIT', 'SJC', 'SJT', 'SJU',
        'SLC', 'SMF', 'SMX', 'SNA', 'SPI', 'SPS', 'SRQ', 'STC', 'STL', 'STT', 'STX', 'SUN', 'SUX', 'SWF', 'SYR', 'TLH',
        'TOL', 'TPA', 'TRI', 'TTN', 'TUL', 'TUS', 'TVC', 'TWF', 'TXK', 'TYR', 'TYS', 'UST', 'VEL', 'VLD', 'VPS', 'WRG',
        'WYS', 'XNA', 'YAK', 'YUM'))

    # Agregar AEROPUERTO DE DESTINO en la segunda columna
    aeropuerto_destino = col2.selectbox(
        'Destination Airport',
        ('ABE', 'ABI', 'ABQ', 'ABR', 'ABY', 'ACK', 'ACT', 'ACV', 'ACY', 'ADK', 'ADQ', 'AEX', 'AGS', 'AKN',
        'ALB', 'ALO', 'AMA', 'ANC', 'APN', 'ASE', 'ATL', 'ATW', 'AUS', 'AVL', 'AVP', 'AZO', 'BDL', 'BET', 'BFL', 'BGM',
        'BGR', 'BHM', 'BIL', 'BIS', 'BJI', 'BLI', 'BMI', 'BNA', 'BOI', 'BOS', 'BPT', 'BQK', 'BQN', 'BRD', 'BRO', 'BRW',
        'BTM', 'BTR', 'BTV', 'BUF', 'BUR', 'BWI', 'BZN', 'CAE', 'CAK', 'CDC', 'CDV', 'CEC', 'CHA', 'CHO', 'CHS', 'CID',
        'CIU', 'CLD', 'CLE', 'CLL', 'CLT', 'CMH', 'CMI', 'CMX', 'CNY', 'COD', 'COS', 'COU', 'CPR', 'CRP', 'CRW', 'CSG',
        'CVG', 'CWA', 'DAB', 'DAL', 'DAY', 'DBQ', 'DCA', 'DEN', 'DFW', 'DHN', 'DIK', 'DLG', 'DLH', 'DRO', 'DSM', 'DTW',
        'DVL', 'EAU', 'ECP', 'EGE', 'EKO', 'ELM', 'ELP', 'ERI', 'ESC', 'EUG', 'EVV', 'EWN', 'EWR', 'EYW', 'FAI', 'FAR',
        'FAT', 'FAY', 'FCA', 'FLG', 'FLL', 'FNT', 'FSD', 'FSM', 'FWA', 'GCC', 'GCK', 'GEG', 'GFK', 'GGG', 'GJT', 'GNV',
        'GPT', 'GRB', 'GRI', 'GRK', 'GRR', 'GSO', 'GSP', 'GST', 'GTF', 'GTR', 'GUC', 'GUM', 'HDN', 'HIB', 'HLN', 'HNL',
        'HOB', 'HOU', 'HPN', 'HRL', 'HSV', 'HYA', 'HYS', 'IAD', 'IAG', 'IAH', 'ICT', 'IDA', 'ILG', 'ILM', 'IMT', 'IND',
        'INL', 'ISN', 'ISP', 'ITH', 'ITO', 'JAC', 'JAN', 'JAX', 'JFK', 'JLN', 'JMS', 'JNU', 'KOA', 'KTN', 'LAN', 'LAR',
        'LAS', 'LAW', 'LAX', 'LBB', 'LBE', 'LCH', 'LEX', 'LFT', 'LGA', 'LGB', 'LIH', 'LIT', 'LNK', 'LRD', 'LSE', 'LWS',
        'MAF', 'MBS', 'MCI', 'MCO', 'MDT', 'MDW', 'MEI', 'MEM', 'MFE', 'MFR', 'MGM', 'MHK', 'MHT', 'MIA', 'MKE', 'MKG',
        'MLB', 'MLI', 'MLU', 'MMH', 'MOB', 'MOT', 'MQT', 'MRY', 'MSN', 'MSO', 'MSP', 'MSY', 'MTJ', 'MVY', 'MYR', 'OAJ',
        'OAK', 'OGG', 'OKC', 'OMA', 'OME', 'ONT', 'ORD', 'ORF', 'ORH', 'OTH', 'OTZ', 'PAH', 'PBG', 'PBI', 'PDX', 'PHF',
        'PHL', 'PHX', 'PIA', 'PIB', 'PIH', 'PIT', 'PLN', 'PNS', 'PPG', 'PSC', 'PSE', 'PSG', 'PSP', 'PUB', 'PVD', 'PWM',
        'RAP', 'RDD', 'RDM', 'RDU', 'RHI', 'RIC', 'RKS', 'RNO', 'ROA', 'ROC', 'ROW', 'RST', 'RSW', 'SAF', 'SAN', 'SAT',
        'SAV', 'SBA', 'SBN', 'SBP', 'SCC', 'SCE', 'SDF', 'SEA', 'SFO', 'SGF', 'SGU', 'SHV', 'SIT', 'SJC', 'SJT', 'SJU',
        'SLC', 'SMF', 'SMX', 'SNA', 'SPI', 'SPS', 'SRQ', 'STC', 'STL', 'STT', 'STX', 'SUN', 'SUX', 'SWF', 'SYR', 'TLH',
        'TOL', 'TPA', 'TRI', 'TTN', 'TUL', 'TUS', 'TVC', 'TWF', 'TXK', 'TYR', 'TYS', 'UST', 'VEL', 'VLD', 'VPS', 'WRG',
        'WYS', 'XNA', 'YAK', 'YUM'))

    # Agregar FECHA DE SALIDA en la tercera columna
    #d = col3.date_input("Fecha de salida", datetime.date(2023, 6, 15))

    #Agregar Día de viaje
    dia = col3.selectbox(
        'Day',
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
        23, 24, 25, 26, 27, 28, 29, 30, 31))

    #Agregar Día de la semana
    dia_de_semana = col4.selectbox(
        'Day of week',
        (1, 2, 3, 4, 5, 6, 7))

    #Agregar Mes de viaje
    mes = col5.selectbox(
        'Month',
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))

    # Agregar HORARIO DE SALIDA en cuarta columna
    horario_llegada = col6.time_input('Scheduled arrival', datetime.time(8, 1), step=60 )

    #Agregar AEROLINEA en quinta columna
    aerolinea = col7.selectbox(
        "Airline",
        ('United Air Lines Inc.', 'American Airlines Inc.', 'US Airways Inc.', 'Frontier Airlines Inc.', 'JetBlue Airways', 'Skywest Airlines Inc.',
        'Alaska Airlines Inc.', 'Spirit Air Lines', 'Southwest Airlines Co.', 'Delta Air Lines Inc.', 'Atlantic Southeast Airlines',
        'Hawaiian Airlines Inc.', 'American Eagle Airlines Inc.', 'Virgin America'))

    #
    #Schedule arrival
    scheduled_time = col8.number_input('Scheduled time (min)')


#Agregar otro espacio vertical
st.markdown("<br>  <br>", unsafe_allow_html=True)

# Agregar botón
submitted = col4.form_submit_button("Predict")

if submitted:
    #2. Let's build a dictionary containing the parameters for our API...
    params = dict(aeropuerto_origen=aeropuerto_origen,
                aeropuerto_destino=aeropuerto_destino,
                dia=dia,
                mes=mes,
                dia_de_semana=dia_de_semana,
                horario=horario_llegada,
                aerolinea=aerolinea,
                scheduled_time=scheduled_time,
                scheduled_arrival=horario_llegada)


    #3. Let's call our APIusing the `requests` package...
    flight_predict_api_url ='https://flight-predictor-container-icyevpoxta-uc.a.run.app/predict'
    response = requests.get(flight_predict_api_url, params=params)

    #4. Let's retrieve the prediction from the **JSON** returned by the API...
    response.url
    prediction = response.json()
    prediction
    #pred = prediction['predictions']

    ## Finally, we can display the prediction to the user
    #st.header(f'La predicción es: {pred}')

    #if pred[0] == 1:
    #    st.error('Warning! La probabilidad que tu vuelo sea cancelado es!')
    #else:
    #    st.success('Puedes relajarte, tu vuelo no se cancelará!')
    #    st.balloons()
