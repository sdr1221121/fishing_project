from pydantic import BaseModel

#Locais de pesca
class FishingSpotCreate(BaseModel):
    name: str
    latitude: float
    longitude: float
    description: str | None

    class Config:
        from_attributes = True

class FishingSpotOut(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    description: str | None
    popularity: int

    class Config:
        from_attributes = True