from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from ...schemas.document import DocumentCreate, DocumentOut
from ...services.document_service import create_document, get_documents, get_local_documents, delete_document
from ...database import SessionLocal  
from ...services.notification_service import expire_dates

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

@router.get("/", response_model=list[DocumentOut])
def documents_list(db: Session= Depends(get_db)):
    return get_documents(db)

@router.get("/local", response_model=list[str])
def local_documents_list():
    return get_local_documents()

@router.get("/expired")
def check_expired_documents(db: Session= Depends(get_db)):
    documents = get_documents(db)
    expire_dates(documents)
    return {"message": "Expiration check completed."}

@router.delete("/{document_id}")
def delete_document_endpoint(document_id: int, db: Session = Depends(get_db)):
    success = delete_document(db, document_id)
    if not success:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"message": "Document deleted successfully"}