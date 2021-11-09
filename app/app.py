import pandas as pd
from bmi import classify
import json

def process(inp: str):
    with open(inp, "r") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    df = df.assign(bmi=df.WeightKg/(df.HeightCm/100))
    df = df.apply(lambda x: classify(x.bmi), axis=1, result_type="expand")
