from fastapi import APIRouter, Depends,Query
from sqlalchemy.orm import Session 
from ...services.catch_service import get_all_catches
from ...database import SessionLocal  

route= APIRouter(prefix="/catch",tags=["Catches"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@route.get("/")
def get_all_catches(db: Session = Depends(get_db)):
    get_all_catches(db)
