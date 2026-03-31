from sqlalchemy.orm import Session
from ..models.catch import Catch
from ..models.coordinate import Coordinate
from ..schemas.catch import CatchCreate
from ..models.specie import Specie


async def create_new_catch(db:Session, catch:CatchCreate):

    specie = None
    my_vessel_id=None

    if catch.specie:
        specie = db.query(Specie).filter(Specie.name == catch.specie).first()

    if not specie:
        specie=create_new_specie(db, catch.specie)

    if catch.vessel_id:
        my_vessel_id=catch.vessel_id
        
#TODO: take off vessel id as null
    db_catch = Catch(
        specie_id=specie.id,
        weight=catch.weight,
        latitude=catch.latitude,
        longitude=catch.longitude,
        captured_method=catch.captured_method,
        vessel_id=my_vessel_id,
        cooordinate=Coordinate(catch.latitude, catch.longitude)
    )
    db.add(db_catch)
    db.commit()
    db.refresh(db_catch)
    return db_catch

def get_all_catches(db:Session):
    return db.query(Catch).all()

def create_new_specie(db:Session,specie_name:str,classification=None):
    db_specie = Specie(
        name=specie_name,
        classification=classification  
    )
    db.add(db_specie)
    db.commit()
    db.refresh(db_specie)
    return db_specie