from pathlib import Path
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.document import Document
from app.services.text_service import clean_text
from app.schemas.document import DocumentUploadResponse
from app.services.pdf_service import extract_text_from_pdf
from app.services.text_service import clean_text, chunk_text


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],

)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/upload", response_model=DocumentUploadResponse)
async def upload_document(
    file:UploadFile = File(...),
    db: Session = Depends(get_db),
    ):
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
    cleaned_text = clean_text(extracted_text)
    chunks = chunk_text(cleaned_text)
    document = Document(
        filename=file.filename,
        file_path=str(file_path),
        content_type=file.content_type,
        status="uploaded",
        extracted_text_length=len(extracted_text),
        cleaned_text_length=len(cleaned_text),
        chunk_count=len(chunks),
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return DocumentUploadResponse(

        filename=file.filename,
        content_type = file.content_type,
        status='uploaded',
        extracted_text_preview=extracted_text[:500],
        extracted_text_length=len(extracted_text),
        cleaned_text_preview=cleaned_text[:500],
        cleaned_text_length=len(cleaned_text),
        chunk_count=len(chunks),
        chunk_preview=chunks[0] if chunks else "",
    )