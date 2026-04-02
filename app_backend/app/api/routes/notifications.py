from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...database import SessionLocal
from ...services.notification_service import (
    check_expiring_documents,
    generate_fishing_recommendations,
)

router = APIRouter(prefix="/notification", tags=["Notifications"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.get("/documents/alerts")
def get_document_alerts(db: Session = Depends(get_db)):
    return check_expiring_documents(db)



@router.post("/recommendations")
def get_recommendations(
    weather: dict,
    tides: dict,
    moon_phase: float
):
    return generate_fishing_recommendations(weather, tides, moon_phase)

