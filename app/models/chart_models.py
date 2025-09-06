from pydantic import BaseModel
from typing import List, Optional

class ChartRequest(BaseModel):
    x: List
    y: List
    chart_type: str = "line"
    title: Optional[str] = "Meu Gráfico"
    xlabel: Optional[str] = "Eixo X"
    ylabel: Optional[str] = "Eixo Y"

class ChartResponse(BaseModel):
    image_base64: str   
    format: str = "png"
