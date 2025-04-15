import logging
from fastapi import FastAPI
from joblib import load
import os
from pathlib import Path
from .schemas import IrisFeatures

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Загрузка модели при старте
model_path = os.path.join(Path(__file__).parent.parent, "iris_model.joblib")
model = load(model_path)
logger.info("Model loaded successfully")

@app.get("/health")
async def health_check():
    logger.info("Health check passed")
    return {"status": "OK"}

@app.post("/predict")
async def predict(features: IrisFeatures):
    try:
        data = [[
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width
        ]]
        prediction = model.predict(data).tolist()
        logger.info(f"Prediction successful: {prediction}")
        return {"prediction": prediction[0]}
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return {"error": str(e)}