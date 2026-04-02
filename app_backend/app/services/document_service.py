import os
from sqlalchemy.orm import Session
from ..models.document import Document
from datetime import date, datetime
from typing import Optional
from sqlalchemy import extract, and_
from fastapi import UploadFile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST_DIR = os.path.join(BASE_DIR, 'uploaded_documents/')

os.makedirs(DEST_DIR, exist_ok=True)

async def create_document(
    db: Session,
    file: UploadFile,
    document_type: str,
    entity_responsible: str,
    end_day: Optional[date] = None
):
    file_bytes = await file.read()

    db_document = Document(
        document_type=document_type,
        entity_responsible=entity_responsible,
        end_day=end_day,
        file_name=file.filename,
        file_data=file_bytes,
        create_date=datetime.utcnow()
    )

    db.add(db_document)
    db.commit()
    db.refresh(db_document)

    return db_document



def get_local_documents():
    document = []
    for file_name in os.listdir(DEST_DIR):
        file_path = os.path.join(DEST_DIR, file_name)
        if os.path.isfile(file_path):
            document.append(file_path)
    return document

# ✅ FILTROS (corrigidos)
def filter_documents(
    db: Session,
    vessel_id: Optional[int] = None,
    document_type: Optional[str] = None,
    entity_responsible: Optional[str] = None,
    end_day: Optional[int] = None,   # ano
    date1: Optional[date] = None,
    date2: Optional[date] = None
):
    query = db.query(Document)

    if vessel_id is not None:
        query = query.filter(Document.vessel_id == vessel_id)

    if document_type is not None:
        query = query.filter(Document.document_type == document_type)

    if entity_responsible is not None:
        query = query.filter(Document.entity_responsible == entity_responsible)

    if end_day is not None:
        query = query.filter(extract("year", Document.end_day) == end_day)

    if date1 is not None and date2 is not None:
        query = query.filter(
            and_(Document.end_day >= date1, Document.end_day <= date2)
        )

    return query.all()