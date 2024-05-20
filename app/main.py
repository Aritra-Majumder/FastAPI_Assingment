from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models import BatchRequest, BatchResponse
from app.controllers import add_numbers_batch
from app.utils import get_timestamp
import logging

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/add", response_model=BatchResponse)
async def add_batch(request: BatchRequest):
    try:
        started_at = get_timestamp()
        result = add_numbers_batch(request.payload)
        completed_at = get_timestamp()
        response = BatchResponse(
            batchid=request.batchid,
            payload=request.payload,
            status="complete",
            started_at=started_at,
            completed_at=completed_at,
        )
        return response
    except Exception as e:
        logging.error(f"Error processing batch {request.batchid}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
