from datetime import datetime, date
from pydantic import BaseModel
from ..core.document_type import DocumentType

#TODO: adicionar estados de documento (ativo, expirado, etc)
class DocumentCreate(BaseModel):
    document_type: DocumentType
    end_day: datetime  | None
    file_path: str
    create_date: datetime  | None
    
class DocumentOut(DocumentCreate):
    id: int

    class Config:
        orm_mode = True
