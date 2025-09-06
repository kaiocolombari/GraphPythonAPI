from pydantic import BaseModel
from typing import List, Optional

class StatsRequest(BaseModel):
    values: List[float]

class StatsResponse(BaseModel):
    mean: float
    median: float
    min: float
    max: float
    stdev: float
