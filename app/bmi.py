from typing import TypedDict


class Classification(TypedDict):
    Category: str
    Health: str


def classify(bmi: float) -> Classification:
    if bmi <= 18.4:
        return Classification(Category="Under weight", Health="Malnutrition risk")
    elif bmi >= 18.5 and bmi <= 24.9:
        return Classification(Category="Normal weight", Health="Low risk")
    elif bmi >= 25 and bmi <= 29.9:
        return Classification(Category="Over weight", Health="Enhanced risk")
    elif bmi >= 30 and bmi <= 34.9:
        return Classification(Category="Moderately obese", Health="Medium risk")
    elif bmi >= 35 and bmi <= 39.9:
        return Classification(Category="Severely obese", Health="High risk")
    else:
        return Classification(Category="Very severely obese", Health="Very high risk")
