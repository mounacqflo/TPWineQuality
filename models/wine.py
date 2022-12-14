from pydantic import BaseModel
from typing import Optional


class Wine(BaseModel):
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

    # def __init__(self):
    #     d = {}
    #     d["fixed acidity"] = wine.fixed_acidity
    #     d["volatile acidity"] = wine.volatile_acidity
    #     d["citric acid"] = wine.citric_acid
    #     d["residual sugar"] = wine.residual_sugar
    #     d["chlorides"] = wine.chlorides
    #     d["free sulfur dioxide"] = wine.free_sulfur_dioxide
    #     d["total sulfur dioxide"] = wine.total_sulfur_dioxide
    #     d["density"] = wine.density
    #     d["pH"] = wine.pH
    #     d["sulphates"] = wine.sulphates
    #     d["alcohol"] = wine.alcohol
    #     d["quality"] = wine.quality

# class Wine(BaseModel):
#     wine: dict = {}

#     def __init__(self, fixed_acidity:float, volatile_acidity: float, citric_acid: float, residual_sugar: float, chlorides: float, free_sulfur_dioxide: float, total_sulfur_dioxide: float, density: float, pH: float, sulphates: float, alcohol: float, quality: int = None):
#         wine["fixed acidity"] = fixed_acidity
#         wine["volatile acidity"] = volatile_acidity
#         wine["citric acid"] = citric_acid
#         wine["residual sugar"] = residual_sugar
#         wine["chlorides"] = chlorides
#         wine["free sulfur dioxide"] = free_sulfur_dioxide
#         wine["total sulfur dioxide"] = total_sulfur_dioxide
#         wine["density"] = density
#         wine["pH"] = pH
#         wine["sulphates"] = sulphates
#         wine["alcohol"] = alcohol
#         wine["quality"] = quality