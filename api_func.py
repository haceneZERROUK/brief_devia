from fastapi import FastAPI
import numpy as np 
from train_model import make_model_save
from make_pred import make_prediction
import pandas as pd

app = FastAPI()

@app.get('/infos')
def read_root():
    return {"message" : "Hello, welcome on my dashbord!"}

@app.get('/train_model')
def train_model():
    make_model_save()
    print ('training in progress')
    return {"Response":'Training completed.'}

@app.get('/predict/{produit_recu}/{jours_livraison}')
def get_pred(produit_recu: int, jours_livraison: int):
    p1 = [produit_recu, jours_livraison]
    x = np.array([p1])
    prediction = make_prediction(x)
    # prediction = 1
    # print(prediction)
    return {'prediction':prediction}