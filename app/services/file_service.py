import os
import pandas as pd
from tempfile import NamedTemporaryFile
from app.models.stats_models import FileUploadResponse

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_uploaded_file(file_bytes: bytes, filename: str) -> FileUploadResponse:
    file_path = os.path.join(UPLOAD_DIR, filename)
    with open(file_path, "wb") as f:
        f.write(file_bytes)

    return FileUploadResponse(
        filename=filename,
        size=len(file_bytes),
        message="Upload concluído com sucesso"
    )

def read_csv(file_path: str) -> pd.DataFrame:
    """
    Lê um CSV e retorna um DataFrame.
    """
    return pd.read_csv(file_path)

def create_temp_file(file_bytes: bytes, suffix=".csv") -> str:
    """
    Cria arquivo temporário e retorna caminho.
    """
    temp_file = NamedTemporaryFile(delete=False, suffix=suffix)
    temp_file.write(file_bytes)
    temp_file.close()
    return temp_file.name