# app/main.py

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from app.classifier import classify_number
from app.fun_fact import get_fun_fact
from app.models import NumberResponse, ErrorResponse

app = FastAPI(title="Number Classification API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/classify-number", response_model=NumberResponse)
def classify_number_api(number: int = Query(..., description="Number to classify")):
    try:
        classification = classify_number(number)
        fun_fact = get_fun_fact(number)
        return {**classification, "number": number, "fun_fact": fun_fact}
    except ValueError:
        return ErrorResponse(number=str(number), error=True)

# Mangum Adapter for AWS Lambda
handler = Mangum(app)
