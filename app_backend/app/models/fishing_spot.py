from sqlalchemy import Column, Integer, String, Float
from ..database import Base

class FishingSpot(Base):
    __tablename__ = "fishing_spots"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    description = Column(String, nullable=True)
    popularity = Column(Integer, default=0)