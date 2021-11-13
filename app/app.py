from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from app.model import BMInput
from typing import List
import pandas as pd
from app.bmi import classify

app = FastAPI()


@app.get("/")
async def index():
    return {"bmi": "calculator", "by": "code-20211109-abbas"}


@app.post("/bmi")
async def calculate_bmi(bminput: List[BMInput]):
    try:
        df = pd.DataFrame(jsonable_encoder(bminput))
        df = df.assign(bmi=df.WeightKg / (pow(df.HeightCm / 100, 2)))
        df[["Category", "Health"]] = df.apply(
            lambda x: classify(x.bmi), axis=1, result_type="expand"
        )
        return df.to_dict(orient="records")
    except:
        return {"status": "error"}
