from fastapi import APIRouter, status
from models.wine import Wine

model_router = APIRouter()

@model_router.get("/api/model")
async def get_serialized_model():
    return {"test": None}

@model_router.get("/api/model/description")
async def get_model_description():
    return {"description": "params"}

@model_router.put("/api/model")
async def add_wine(wine: Wine):
    return {"message": "wine added"}

@model_router.post("/api/model/retrain", status_code=status.HTTP_201_CREATED)
async def retrain_model():
    return {"message": "model retrained"}