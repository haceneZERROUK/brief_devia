import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/training_dataset.csv")
df_a = pd.read_csv('data/orders_dataset.csv')
df_b = pd.read_csv('data/customers_dataset.csv')
df_c = df_a.merge(df_b, on='customer_id', how='left')
df_paiement = pd.read_csv('data/order_payments_dataset.csv')


# df_final = df.merge(df_a, on='order_id', how= 'left' ).merge(df_b, on='customer_id', how='left')
df_c = df_a.merge(df_b, on='customer_id', how='left')
df_final = df.merge(df_c, on='order_id', how='left')
df_final= df_final.merge(df_paiement, on='order_id', how='left')

#table pour les CA par note

df_final_recu = df_final[df_final['produit_recu'] != 0]
df_final_recu_trie = df_final_recu.groupby('review_score')['payment_value'].sum()
df_final_recu_trie = pd.DataFrame(df_final_recu_trie).reset_index()
df_final_recu_trie = df_final_recu_trie.rename(columns={'payment_value': 'somme_paiement'})
print(df_final_recu_trie.head())

st.set_page_config(page_title='Olist_dataset')
st.header('Comparison - Olist Dataset')
st.markdown('Explore the variables to understand the relationship between data.')
st.sidebar.header('variable comparison')

options = st.sidebar.radio('Select infos',
                           options=['temps de livraison par état',
                                    'score par temps de livraison',
                                    'Methode de paiement',
                                    'CA par note'])

if  options == 'temps de livraison par état':
    st.markdown('option1')
elif  options == 'score par temps de livraison':
    st.markdown('option2')
elif options =='Methode de paiement':
    st.markdown('option3')
elif options == 'CA par note':
    st.markdown('option4')

if options == 'temps de livraison par état':
    plot = df_group = df_final.groupby('customer_state')['temps_livraison'].mean().reset_index()
    plot = px.histogram(
    df_group,
    x='customer_state',
    y='temps_livraison',
    labels={'customer_state'},
    title='Moyenne des temps de livraison par état du client',
    color='customer_state',
   )
    plot.update_layout(
    xaxis_title='Etat du client',
    yaxis_title='livraison moyenne'
)
    plot.update_traces(marker_color='blue')
    st.plotly_chart(plot)

elif options == 'score par temps de livraison':
    plot = sns.boxplot(
               y="temps_livraison",
               x="score",
               data = df_final,
               showfliers=False,
               palette='magma')
    st.pyplot(plt)

elif options == 'Methode de paiement':
    df_paiement_trie = df_paiement.groupby('payment_type')['payment_type'].count()

    plot, ax = plt.subplots()
    ax.pie(
        df_paiement_trie,
        labels=df_paiement_trie,
        autopct='%1.1f%%',
        colors=sns.color_palette('pastel')
        )
    st.pyplot(plt)

elif options == 'CA par note':
    plot = sns.barplot(x='review_score',
                       y='somme_paiement', 
                       data=df_final_recu_trie, 
                       palette='magma')
    st.pyplot(plt)