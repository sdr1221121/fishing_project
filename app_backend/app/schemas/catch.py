from pydantic import BaseModel

class CatchCreate(BaseModel):
    specie_id:int
    weight:float
    latitude:float
    longitude:float
    captured_method:str
    vessel_id:int | None=None

class CatchOut(CatchCreate):
    id:int
    
    class Config:
        orm_mode = True