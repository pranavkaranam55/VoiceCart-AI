from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from backend.database import get_analytics_stats
from backend.demand_prediction import predict_demand
from fastapi.middleware.cors import CORSMiddleware
from backend.export_reports import (
    export_csv,
    export_excel,
    export_pdf
)
import shutil

from backend.main import process_order
from backend.database import get_dashboard_stats, get_all_orders

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://voice-cart-ai.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/process-order")
async def process_audio(file: UploadFile = File(...)):

    file_path = f"audio/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = process_order(file_path)

    return result


@app.get("/dashboard")
def get_dashboard():

    return get_dashboard_stats()

@app.get("/orders")
def get_orders():

    return get_all_orders()

@app.get("/analytics")
def get_analytics():

    return get_analytics_stats()

@app.get("/prediction")
def get_prediction():

    return predict_demand()
@app.get("/export/csv")
def download_csv():

    return {
        "file": export_csv()
    }


@app.get("/export/excel")
def download_excel():

    return {
        "file": export_excel()
    }


@app.get("/export/pdf")
def download_pdf():

    return {
        "file": export_pdf()
    }