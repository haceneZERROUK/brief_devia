import streamlit as st
import pandas as pd
import requests

df = pd.read_csv('data/training_dataset.csv')

st.set_page_config(page_title='Olist')
st.header('Olist training model')
st.markdown('Train model to make predictions ')
st.sidebar.header('Train model')


launch_training = st.sidebar.button('training')
if launch_training:

    # print('welcome')
    url = f'http://localhost:8000/train_model'

    #Envoyer la requête à FastAPI
    response = requests.get(url)

    #vérigier si la requête à réussi (statut 200)
    if response.status_code == 200:

        st.success(f'Model training message')
    else:
        st.error('Error in prediction resquest.')


else:
    url = f'http://127.0.0.1:8000/infos'

    #Envoyer la requête à FastAPI
    response = requests.get(url)

    #vérigier si la requête à réussi (statut 200)
    if response.status_code == 200:
        st.success(f'API welcome message')
    else:
        st.error('Error in prediction resquest.')


