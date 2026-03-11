from pydantic import BaseModel
from document import DocumentOut
from catch import CatchOut

class VesselCreate(BaseModel):
    name: str
    registration_number: str
    capacity: int | None
    tonnage: int | None


class VesselOut(VesselCreate):
    id: int
    document: list[DocumentOut] | None=[]
    catches: list[CatchOut] | None=[]

    class Config:
        orm_mode = True