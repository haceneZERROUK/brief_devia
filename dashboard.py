import pandas as pd
import streamlit as st

df = pd.read_csv('data/training_dataset.csv')

st.set_page_config(page_title='Olist')
st.header('Olist satisfaction customers machine learning project')
st.markdown('Assessing the significant variables affecting customer satisfaction in the Olist database. ')
st.markdown('Use this dashboard to understand the data and to make predictions')
st.markdown('')
st.image('img.png')