from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from ...schemas.vessel import VesselCreate, VesselOut
from ...services.vessel_service import create_vessel, get_vessels
from ...database import SessionLocal  

router = APIRouter(prefix="/vessels", tags=["Vessels"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=VesselOut)
def add_vessel(vessel: VesselCreate, db: Session = Depends(get_db)):
    return create_vessel(db, vessel)

@router.get("/", response_model=list[VesselOut])
def list_vessels(db: Session = Depends(get_db)):
    return get_vessels(db)
