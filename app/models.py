from pydantic import BaseModel
from typing import List
from datetime import datetime

class BatchRequest(BaseModel):
    batchid: str
    payload: List[List[int]]

class BatchResponse(BaseModel):
    batchid: str
    payload: List[List[int]]
    status: str
    started_at: datetime
    completed_at: datetime
