from pydantic import BaseModel
from typing import Optional

class Wine(BaseModel):
    """
    Create a Wine model based on wine informations stored in the CSV file except the Id field.
    """

    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float
    quality: Optional[float]