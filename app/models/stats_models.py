from pydantic import BaseModel

class FileUploadResponse(BaseModel):
    filename: str
    size: int
    message: str = "Upload concluído com sucesso"
