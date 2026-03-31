from sqlalchemy import Column, Integer, DateTime,ForeignKey
from ..database import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class FishingRoute(Base):
    __tablename__ = "fishing_routes"

    id = Column(Integer, primary_key=True)
    vessel_id=Column(Integer,ForeignKey("vessels.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    fishing_route_points = relationship("FishingRoutePoint", back_populates="fishing_route")