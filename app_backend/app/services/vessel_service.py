from sqlalchemy.orm import Session
from ..models.vessel import Vessel
from ..schemas.vessel import VesselCreate

def create_vessel(db: Session, vessel: VesselCreate):
    db_vessel = Vessel(**vessel.dict())
    db.add(db_vessel)
    db.commit()
    db.refresh(db_vessel)
    return db_vessel

def get_vessels(db: Session):
    return db.query(Vessel).all()
