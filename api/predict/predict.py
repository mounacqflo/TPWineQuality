from fastapi import APIRouter, status
from models.wine import Wine

predict_router = APIRouter()

@predict_router.post("/api/predict", status_code=status.HTTP_201_CREATED)
async def rate_wine(wine: Wine):
    quality = 9.2
    return {"Quality": quality}

@predict_router.get("/api/predict")
async def get_perfect_wine_characteristics():
    perfect_wine: Wine
    return perfect_wine