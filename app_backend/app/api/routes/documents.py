from fastapi import APIRouter, Depends, Query, UploadFile, File, Form, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, date
from ...schemas.document import DocumentOut
from ...database import SessionLocal
from ...models.document import Document
from ...services.document_service import filter_documents, get_local_documents


router = APIRouter(prefix="/documents", tags=["Documents"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=DocumentOut)
async def add_document(
    file: UploadFile = File(...),
    document_type: str = Form(...),
    entity_responsible: str = Form(...),
    end_day: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    file_bytes = await file.read()

    db_document = Document(
        document_type=document_type,
        entity_responsible=entity_responsible,
        end_day=date.fromisoformat(end_day) if end_day else None,
        file_name=file.filename,
        file_data=file_bytes,
        create_date=datetime.utcnow()
    )

    db.add(db_document)
    db.commit()
    db.refresh(db_document)

    return db_document


@router.get("/", response_model=list[DocumentOut])
def get_filtered_documents(
    vessel_id: Optional[int] = Query(None),
    document_type: Optional[str] = Query(None),
    entity_responsible: Optional[str] = Query(None),
    end_day: Optional[int] = Query(None),
    date1: Optional[date] = Query(None),
    date2: Optional[date] = Query(None),
    db: Session = Depends(get_db),
):
    return filter_documents(
        db,
        vessel_id=vessel_id,
        document_type=document_type,
        entity_responsible=entity_responsible,
        end_day=end_day,
        date1=date1,
        date2=date2
    )


@router.get("/{doc_id}/download")
def download_document(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()

    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    return Response(
        content=doc.file_data,
        media_type="application/octet-stream",
        headers={
            "Content-Disposition": f'attachment; filename="{doc.file_name}"'
        }
    )

@router.get("/local", response_model=list[str])
def local_documents_list():
    return get_local_documents()