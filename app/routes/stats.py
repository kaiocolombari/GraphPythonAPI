from fastapi import APIRouter
from app.services.stats_service import calculate_stats
from pydantic import BaseModel
from typing import List

router = APIRouter()

class StatsRequest(BaseModel):
    values: List[float]

@router.post("/calculate")
def stats_endpoint(req: StatsRequest):
    """
    Recebe lista de números e retorna estatísticas básicas.
    """
    result = calculate_stats(req.values)
    return result
