import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error
import pickle

def make_model_save():
    # Importer le dataframe Olist
    olist_df = pd.read_csv("data/training_dataset.csv")

    # Définir la variable cible et les caractéristiques
    X = olist_df[['produit_recu', 'temps_livraison']]
    y = olist_df[['score']]  

    # Séparer les données d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)

    # Créer et entraîner le modèle
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Sauvegarder le modèle
    with open('main_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)

    # Tester le modèle
    predictions = model.predict(X_test)
    Mae = mean_absolute_error(y_test, predictions)
    print(f"Mae: {Mae}")
