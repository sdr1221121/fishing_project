from pydantic import BaseModel

class SpecieCreate(BaseModel):
    name: str
    classification: str | None = None

class SpecieOut(SpecieCreate):
    id: int 

    class config:
        orm_mode = True