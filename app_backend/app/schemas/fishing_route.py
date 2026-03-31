from pydantic import BaseModel
from datetime import datetime
from typing import List
from .fishing_route_point import FishingRoutePointOut

class FishingRouteCreate(BaseModel):
    vessel_id: int
    name:str

    class Config:
        from_attributes = True


class FishingRouteOut(BaseModel):
    id: int
    vessel_id: int
    name:str    
    created_at: datetime
    fishing_route_points: List[FishingRoutePointOut]

    class Config:
        from_attributes = True