from typing import List
from fastapi.testclient import TestClient
from app.app import app
from app.model import BMInput
import pytest
import json

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"bmi": "calculator"}


@pytest.mark.parametrize(
    "inputs",
    [
        [
            {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
            {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
            {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
            {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
            {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
        ]
    ],
)
def test_bmi(inputs: List[BMInput]):
    response = client.post("/bmi", data=json.dumps(inputs))
    assert response.status_code == 200
    assert response.json() == [
        {
            "Gender": "Male",
            "HeightCm": 171,
            "WeightKg": 96,
            "bmi": 32.83061454806607,
            "Category": "Moderately obese",
            "Health": "Medium risk",
        },
        {
            "Gender": "Male",
            "HeightCm": 161,
            "WeightKg": 85,
            "bmi": 32.79194475521777,
            "Category": "Moderately obese",
            "Health": "Medium risk",
        },
        {
            "Gender": "Male",
            "HeightCm": 180,
            "WeightKg": 77,
            "bmi": 23.76543209876543,
            "Category": "Normal weight",
            "Health": "Low risk",
        },
        {
            "Gender": "Female",
            "HeightCm": 166,
            "WeightKg": 62,
            "bmi": 22.49963710262738,
            "Category": "Normal weight",
            "Health": "Low risk",
        },
        {
            "Gender": "Female",
            "HeightCm": 150,
            "WeightKg": 70,
            "bmi": 31.11111111111111,
            "Category": "Moderately obese",
            "Health": "Medium risk",
        },
        {
            "Gender": "Female",
            "HeightCm": 167,
            "WeightKg": 82,
            "bmi": 29.402273297715947,
            "Category": "Over weight",
            "Health": "Enhanced risk",
        },
    ]
