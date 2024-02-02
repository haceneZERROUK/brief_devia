import streamlit as st
import numpy as np
from make_pred import make_prediction
import json
import pandas as pd
import plotly.express as px 
import requests



st.set_page_config(page_title='Olist')
st.header('Olist prediction')
st.markdown('using delivery status for predict ')
st.sidebar.header('Prediction')

produit_recu = st.sidebar.text_input('avez-vous reçu votre colis?')
jours_livraison = st.sidebar.text_input('delai de livraison?')
make_pred = st.sidebar.button('prediction button')

if make_pred:
    #CONSTRUIRE L'URL
    url = f'http://localhost:8000/predict/{produit_recu}/{jours_livraison}'

    response = requests.get(url)

    print(response)

    if response.status_code == 200:
        result = response.json()['prediction']
        st.success(f'prediction result: {result}')
    else:
        st.error('Error in prediction request.')
