from fastapi import APIRouter
from app.models.chart_models import ChartRequest
from app.services.chart_service import generate_chart

router = APIRouter()

@router.post("/generate")
def generate_chart_endpoint(req: ChartRequest):
    """
    Recebe dados e retorna gráfico em base64.
    """
    img_base64 = generate_chart(req)
    return {"image_base64": img_base64}
