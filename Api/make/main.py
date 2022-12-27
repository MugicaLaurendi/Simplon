from typing import Union
import pickle
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

model = pickle.load(open("pipline.pkl","rb"))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/model/")
def prediction(
    size: Union[int, None] = None,
    total_bill: Union[int, None] = None,
    sex: Union[str, None] = None,
    smoker: Union[str, None] = None,
    day: Union[str, None] = None,
    time: Union[str, None] = None,
    ):
    X = pd.DataFrame({"size":[size],"total_bill":[total_bill],"sex":[sex],"smoker":[smoker],"day":[day],"time":[time]})
    prediction = model.predict(X)[0]

    return {"Prediction": prediction}

@app.get("/bob/{value}")
def read_bob(value):
    return {str(value) : value}
