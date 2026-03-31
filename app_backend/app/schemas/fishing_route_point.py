from pydantic import BaseModel
from datetime import datetime

class FishingRoutePointCreate(BaseModel):
    latitude: float
    longitude: float
    timestamp: datetime

    class Config:
        from_attributes = True

class FishingRoutePointOut(BaseModel):
    id: int
    fishing_route_id: int
    latitude: float
    longitude: float
    timestamp: datetime | None

    class Config:
        from_attributes = True