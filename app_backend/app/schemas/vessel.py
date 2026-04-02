from pydantic import BaseModel

class VesselCreate(BaseModel):
    name: str
    registration_number: str
    capacity: int | None
    tonnage: float | None


class VesselOut(VesselCreate):
    id: int

    class Config:
        orm_mode = True