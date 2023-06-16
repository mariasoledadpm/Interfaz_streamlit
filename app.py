#Importar streamlit
import streamlit as st
#from PIL import Image
import datetime
import requests


#Características básicas

#1 Definir un ícono y título que tendrá la página en la pestaña del navegadorss
st.set_page_config(page_title="SureFly ✈️", page_icon="icono.png", layout="wide")

#2 image para agregar un logo
st.image("surefly.png", width=200)

#3 title para definir el título que ve el usuario al abrir la página
st.title("Viaja relajado, planifica con SureFly ")

import base64

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('fondo1.png')


with st.form(key='params_for_api'):
    #4 Crear columnas para alinear los botones
    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

    # Agregar AEROPUERTO DE ORIGEN en la primera columna
    aeropuerto_origen = col1.selectbox(
        'Código aeropuerto origen',
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
        'Código aeropuerto destino',
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
        '¿Qué día viajas?',
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
        23, 24, 25, 26, 27, 28, 29, 30, 31))

    #Agregar Día de la semana
    dia_de_semana = col4.selectbox(
        '¿Qué día de la semana viajas?',
        ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'))

    #Agregar Mes de viaje
    mes = col5.selectbox(
        '¿Qué mes viajas?',
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))

    # Agregar HORARIO DE SALIDA en cuarta columna
    horario = col6.time_input('Horario de salida', datetime.time(8, 1), step=60 )

    #Agregar AEROLINEA en quinta columna
    aerolinea = col7.selectbox(
        '¿En qué aerolínea viajas?',
        ('United Air Lines Inc.', 'American Airlines Inc.', 'US Airways Inc.', 'Frontier Airlines Inc.', 'JetBlue Airways', 'Skywest Airlines Inc.',
        'Alaska Airlines Inc.', 'Spirit Air Lines', 'Southwest Airlines Co.', 'Delta Air Lines Inc.', 'Atlantic Southeast Airlines',
        'Hawaiian Airlines Inc.', 'American Eagle Airlines Inc.', 'Virgin America'))

    #
    #Schedule time
    scheduled_time = col8.number_input('Scheduled time')

    #Schedule arribal
    scheduled_arrival = col9.number_input('Scheduled arribal')


#Agregar otro espacio vertical
st.markdown("<br>  <br>", unsafe_allow_html=True)

# Agregar botón
submitted = col4.form_submit_button("Enviar Datos")

if submitted:
    #2. Let's build a dictionary containing the parameters for our API...
    params = dict(aeropuerto_origen=aeropuerto_origen,
                aeropuerto_destino=aeropuerto_destino,
                dia=dia,
                mes=mes,
                dia_de_semana=6,
                horario=horario,
                aerolinea=aerolinea,
                scheduled_time=scheduled_time,
                scheduled_arrival=scheduled_arrival)


    #3. Let's call our API using the `requests` package...
    flight_predict_api_url = 'http://127.0.0.1:8200/predict'
    response = requests.get(flight_predict_api_url, params=params)

    #4. Let's retrieve the prediction from the **JSON** returned by the API...
    prediction = response.json()

    pred = prediction['predictions']

    ## Finally, we can display the prediction to the user
    st.header(f'La predicción es: {pred}')