from fastapi import FastAPI
from api.model.model import model_router
from api.predict.predict import predict_router

app = FastAPI()

app.include_router(model_router)
app.include_router(predict_router)

@app.get("/")
async def root():
    return {"message": "Wine Quality Prediction"}

"""
    if item_id not in items:
        raise HTTPException HTTPException(status_code=404, detail="Item not found")
"""

# configurer le port