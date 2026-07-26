from pathlib import Path
from fastapi import APIRouter, File, HTTPException, UploadFile
from app.schemas.document import DocumnetUploadResponse

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],

)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/upload", response_model=DocumnetUploadResponse)
async def upload_document(file:UploadFile = File(...)):
    if file.content_type != "applicable/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )
    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:
        content =  await file.read()
        buffer.write(content)

    return DocumnetUploadResponse(
        filename=file.filename,
        content_type = file.content_type,
        status='uploaded',
    )