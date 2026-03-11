from fastapi import APIRouter, Depends,Query
from sqlalchemy.orm import Session 
from ...schemas.document import DocumentCreate, DocumentOut
from ...services.document_service import create_document, get_documents, get_local_documents, filter_documents
from ...database import SessionLocal  
from ...services.notification_service import expire_dates
from typing import Optional


router = APIRouter(prefix="/documents", tags=["Documents"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DocumentOut)
async def add_document(document:DocumentCreate, db: Session = Depends(get_db)):
    return await create_document(db, document)

@router.get("/local", response_model=list[str])
def local_documents_list():
    return get_local_documents()

@router.get("/expired")
def check_expired_documents(db: Session= Depends(get_db)):
    documents = get_documents(db)
    expire_dates(documents)
    return {"message": "Expiration check completed."}

@router.get("/")
def filter_documents(
    vessel_id: Optional[int] = Query(None),
    document_type: Optional[str] = Query(None),
    entity_responsible: Optional[str] = Query(None),
    end_year: Optional[int] = Query(None),
    date1: Optional[int] = Query(None),
    date2: Optional[int] = Query(None),

    db: Session = Depends(get_db),
):
    results = filter_documents(
        db,
        vessel_id=vessel_id,
        document_type=document_type,
        entity_responsible=entity_responsible,
        end_year=end_year,
        date1=date1,
        date2=date2
    )
    return results