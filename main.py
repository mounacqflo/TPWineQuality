from fastapi import FastAPI
import uvicorn
from api.model.model import model_router
from api.predict.predict import predict_router

# configure port
PORT = 8000

app = FastAPI()

app.include_router(model_router)
app.include_router(predict_router)

@app.get("/")
async def root():
    return {"message": "Wine Quality Prediction"}

if __name__ == '__main__':
    uvicorn.run(app, port=PORT)