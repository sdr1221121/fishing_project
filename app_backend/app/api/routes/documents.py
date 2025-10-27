from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from ...schemas.document import DocumentCreate, DocumentOut
from ...services.document_service import create_document, get_documents, get_local_documents
from ...database import SessionLocal  

router = APIRouter(prefix="/documents", tags=["Documents"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DocumentOut)
def add_document(document:DocumentCreate, db: Session = Depends(get_db)):
    return create_document(db, document)

@router.get("/", response_model=list[DocumentOut])
def documents_list(db: Session= Depends(get_db)):
    return get_documents(db)

@router.get("/local", response_model=list[str])
def local_documents_list():
    return get_local_documents()