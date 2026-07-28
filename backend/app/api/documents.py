from pathlib import Path
from fastapi import APIRouter, File, HTTPException, UploadFile
from app.schemas.document import DocumentUploadResponse
from app.services.pdf_service import extract_text_from_pdf

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],

)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/upload", response_model=DocumentUploadResponse)
async def upload_document(file:UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )
    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:
        content =  await file.read()
        buffer.write(content)
    
    extracted_text = extract_text_from_pdf(file_path)

    return DocumentUploadResponse(
        filename=file.filename,
        content_type = file.content_type,
        status='uploaded',
        extracted_text_preview=extracted_text[:500],
        extracted_text_length=len(extracted_text),
    )