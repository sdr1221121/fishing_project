from datetime import datetime, date
from pydantic import BaseModel
from typing import Optional


class DocumentBase(BaseModel):
    document_type: str
    entity_responsible: str
    end_day: Optional[date] = None


class DocumentCreate(DocumentBase):
    pass


class DocumentOut(DocumentBase):
    id: int
    file_name: str
    create_date: Optional[datetime] = None
    

    class Config:
        orm_mode = True 