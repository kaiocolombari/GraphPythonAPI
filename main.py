from fastapi import FastAPI
from app.routes import charts, stats, files

app = FastAPI(title="📊 Graph API", version="1.0.0")

app.include_router(charts.router, prefix="/charts", tags=["Charts"])
app.include_router(stats.router, prefix="/stats", tags=["Statistics"])
app.include_router(files.router, prefix="/files", tags=["Files"])

@app.get("/")
def root():
    return {"message": "Graph API is running 🚀"}
