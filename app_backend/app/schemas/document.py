from pydantic import BaseModel
from ..core.documents_type import DocumentType

class DocumentCreate(BaseModel):
    documents_type: str
    end_day: str | None
    file_path: str
    create_date: str | None
    
class DocumentOut(DocumentCreate):
    id: int

    class Config:
        orm_mode = True
