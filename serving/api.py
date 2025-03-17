from fastapi import FastAPI, File, UploadFile, HTTPException
import pickle
import pandas as pd

from pydantic import BaseModel
import numpy as np


app = FastAPI()

with open('../artifacts/credit_model.pkl', 'rb') as handle:
    model = pickle.load(handle)

clients = pd.read_csv("../raw_data/test_data.csv", sep=";")

class PredictionData (BaseModel):
    Id: int
    amount: float
    price: float

@app.post("/predict")
async def predict(infos : PredictionData):

    try:
        client=clients[clients.Id==infos.Id].iloc[0,1:].values.tolist()
        client.append(infos.amount)
        montant_final=(1+(infos.price/100))*infos.amount
        client.append(montant_final)
        print(client)
        client=np.array(client).reshape((1,-1))
        prediction = model.predict_proba(client)[0,1]*100
        prediction=np.round(prediction).astype(int)
        prediction_jsonable = prediction.tolist()  
        return prediction_jsonable
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
