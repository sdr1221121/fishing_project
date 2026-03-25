from pydantic import BaseModel
from .specie import SpecieOut
class CatchCreate(BaseModel):
    specie:str
    weight:float
    latitude:float
    longitude:float
    captured_method:str
    vessel_id:int | None=None

class CatchOut(CatchCreate):
    id:int
    specie:"SpecieOut"
    
    class Config:
        orm_mode = True