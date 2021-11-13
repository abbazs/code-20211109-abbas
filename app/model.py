from pydantic import BaseModel

class BMInput(BaseModel):
    Gender: str
    HeightCm: float
    WeightKg: float