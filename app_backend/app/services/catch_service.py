from sqlalchemy.orm import Session
from ..models.catch import Catch
from ..schemas.catch import CatchCreate

def create_catch(db:Session, catch:CatchCreate):
    db_catch=Catch(**catch.dict())
    db.add(db_catch)
    db.commit()
    db.refresh(db_catch)
    return db_catch

def get_all_catches(db:Session):
    return db.query(Catch).all()