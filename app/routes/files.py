from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Recebe CSV/Excel e retorna mensagem de sucesso.
    """
    contents = await file.read()
    return {"filename": file.filename, "size": len(contents)}
