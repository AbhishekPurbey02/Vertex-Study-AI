from pydantic import BaseModel

class DocumentUploadResponse(BaseModel):
    filename: str
    content_type: str
    status: str
    extracted_text_preview: str
    extracted_text_length: int
    cleaned_text_preview:str
    cleaned_text_length: int

