import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd


class Features(BaseModel):
    ph: float | None = None
    Hardness: float | None = None
    Solids: float | None = None
    Chloramines: float | None = None
    Sulfate: float | None = None
    Conductivity: float | None = None
    Organic_carbon: float | None = None
    Trihalomethanes: float | None = None
    Turbidity: float | None = None
    Conductivity: float | None = None


app = FastAPI()
model = joblib.load('water_classifier.pkl')

@app.post('/predict')
def get_predictions(feature: Features):
    feature_dict = dict(feature)
    user_data = pd.DataFrame({k: [v] for k, v in feature_dict.items()})
    result = model.predict(user_data)
    print(result)
    return {
        "result": str(result[0])
    }
