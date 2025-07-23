from fastapi import FastAPI
from pydantic import BaseModel
import joblib 
import os

app=FastAPI()
model_path=os.path.join(os.path.dirname(__file__),"model.pkl")
model=joblib.load(model_path)
class InputData(BaseModel):
    features:list[float]
@app.post("/predict")
def predict(data:InputData):
    prediction=model.predict([data.features])
    return {"predictions":int(prediction[0])}