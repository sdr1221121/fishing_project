from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from ..database import Base
 
class FishingRoutePoint(Base):
    __tablename__ = "fishing_route_points"

    id = Column(Integer, primary_key=True)
    fishing_route_id = Column(Integer, ForeignKey("fishing_routes.id"))

    latitude = Column(Float)
    longitude = Column(Float)
    timestamp = Column(DateTime)

    fishing_route = relationship("FishingRoute", back_populates="fishing_route_points")