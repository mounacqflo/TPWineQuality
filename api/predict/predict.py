from fastapi import APIRouter, status
from models.wine import Wine
from wine_prediction import WinePrediction

predict_router = APIRouter()
wine_prediction = WinePrediction()

@predict_router.post("/api/predict", status_code=status.HTTP_201_CREATED)
async def rate_wine(wine: Wine):
    return wine_prediction.predictWine(wine)

@predict_router.get("/api/predict")
async def get_perfect_wine_characteristics():
    return wine_prediction.getPerfectWine()