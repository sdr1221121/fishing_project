from fastapi import APIRouter, Depends,Query
from sqlalchemy.orm import Session 
from ...schemas.document import DocumentCreate, DocumentOut
from ...services.notification_service import get_expired_documents, get_valid_documents
from ...database import SessionLocal  
from ...services.notification_service import expire_dates


router = APIRouter(prefix="/notification", tags=["Documents"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/expired")
def get_expired_documents(db:Session=Depends(get_db)):
    return get_expired_documents(db)

@router.get("/valid")
def get_valid_documents(db: Session= Depends(get_db)):
    return get_valid_documents(db)