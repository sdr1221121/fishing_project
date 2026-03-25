from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from ...services.catch_service import get_all_catches, create_new_catch
from ...services.report_service import generate_catch_report
from ...database import SessionLocal  
from fastapi.responses import Response
from ...schemas.catch import CatchCreate, CatchOut



router= APIRouter(prefix="/catch",tags=["Catches"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=CatchOut)
async def add_cartches(catch: CatchCreate, db: Session = Depends(get_db)):
    return await create_new_catch(db, catch)

@router.get("/", response_model=list[CatchOut])
def fecth_all_catches(db: Session = Depends(get_db)):
    return get_all_catches(db)

@router.get("/report")
def download_report(db:Session=Depends(get_db)):
    catches=get_all_catches(db)
    pdf=generate_catch_report(catches)

    return Response(content=pdf,
                    media_type="application/pdf",
                    headers={
                        "Content-Disposition":"attachement; filename=catch_report.pdf"
                    })