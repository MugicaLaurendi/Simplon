from typing import Union
import pickle
import numpy as np
from fastapi import FastAPI

app = FastAPI()

model = pickle.load(open('lr_red_wine.pkl', 'rb'))

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/lr_red_wine")
def read_lr_red_wine(alcohol: float, sulphates: float, citric_acid: float):

    X = np.array([[alcohol,sulphates,citric_acid]])
    prediction = model.predict(X)[0]
    prediction = float(prediction)

    return {"Wine quality": prediction}
