
import pickle
import pandas as pd
import numpy as np

df = pd.read_csv('data/training_dataset.csv')

def make_prediction(x):


    #charger le modele à partir d'un fichier pickle
    with open ('main_model.pkl', 'rb') as fichier_modele:
        loaded_model = pickle.load(fichier_modele)

    x = pd.DataFrame({'produit_recu': [df['produit_recu']],
                        'temps_livraison': df['temps_livraison']})
    # print('ma data est ça',data)
#faire la prédiction
    prediction_out = loaded_model.predict(x)
    # prediction_out = 1
    return prediction_out