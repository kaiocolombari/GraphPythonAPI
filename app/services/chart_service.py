import matplotlib.pyplot as plt
import io
import base64
from app.models.chart_models import ChartRequest

def generate_chart(req: ChartRequest) -> str:
    fig, ax = plt.subplots()

    if req.chart_type == "line":
        ax.plot(req.x, req.y, marker="o")
    elif req.chart_type == "column":
        ax.bar(req.x, req.y)
    elif req.chart_type == "bar":
        ax.barh(req.x, req.y)
    elif req.chart_type == "scatter":
        ax.scatter(req.x, req.y)
    elif req.chart_type == "area":
        ax.fill_between(req.x, req.y, alpha=0.4)
        ax.plot(req.x, req.y, color="black")
    elif req.chart_type == "pie":
        ax.pie(req.y, labels=req.x, autopct="%1.1f%%")
        ax.axis("equal")

    if req.chart_type != "pie":
        ax.set_title(req.title)
        ax.set_xlabel(req.xlabel)
        ax.set_ylabel(req.ylabel)

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()
    return img_base64
