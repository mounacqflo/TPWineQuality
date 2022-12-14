from fastapi import APIRouter, status
from models.wine import Wine
from fastapi.responses import FileResponse
from wine_prediction import WinePrediction
import wget

model_router = APIRouter()

wine_prediction = WinePrediction()

@model_router.get("/api/model")
async def get_serialized_model():
    #wget.download('./rf.joblib')
    return FileResponse(path= 'rf.joblib', filename= 'rf.joblib', media_type='joblib')
    #return FileResponse('rf.joblib')

@model_router.get("/api/model/description")
async def get_model_description():
    return {"description": "params"}

# ok
@model_router.put("/api/model")
async def add_wine(wine: Wine):
    return wine_prediction.addWine(wine)

# ok
@model_router.post("/api/model/retrain", status_code=status.HTTP_201_CREATED)
async def retrain_model():
    return wine_prediction.retrain()