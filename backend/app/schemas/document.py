from pydantic import BaseModel

class DocumentUploadResponse(BaseModel):
    filename: str
    content_type: str
    status: str