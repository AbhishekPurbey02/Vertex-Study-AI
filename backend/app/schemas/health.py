from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    app: str
    version: str
    environment: str

class DocumentUploadResponse(BaseModel):
    filename: str
    content_type: str
    status: str