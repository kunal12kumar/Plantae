from fastapi import APIRouter, UploadFile, File
from services.disease_model import predict_disease

router = APIRouter()

@router.post("/predict-disease")
async def predict_disease_route(file: UploadFile = File(...)):
    img_bytes = await file.read()
    return predict_disease(img_bytes)
