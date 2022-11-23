from fastapi import FastAPI, status
from models.wine import Wine

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Wine Quality Prediction"}

@app.post("/api/predict", status_code=status.HTTP_201_CREATED)
async def rate_wine(wine: Wine):
    quality = 9.2
    return {"Quality": quality}

@app.get("/api/predict")
async def get_perfect_wine_characteristics():
    perfect_wine: Wine
    return perfect_wine

@app.get("/api/model")
async def get_serialized_model():
    return None

@app.get("/api/model/description")
async def get_model_description():
    return {"description": "params"}

@app.put("/api/model")
async def add_wine(wine: Wine):
    return {"message": "wine added"}

@app.post("/api/model/retrain")
async def retrain_model():
    return {"message": "model retrained"}


"""
    if item_id not in items:
        raise HTTPException HTTPException(status_code=404, detail="Item not found")
"""