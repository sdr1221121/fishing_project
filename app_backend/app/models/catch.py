from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from ..database import Base
from sqlalchemy.orm import composite
from .coordinate import Coordinate
from .specie import Specie
from sqlalchemy.orm import relationship

class Catch(Base):
    __tablename__ ="catches"

    id=Column(Integer,primary_key=True,index=True)

    specie_id=Column(Integer,ForeignKey("species.id"),nullable=True)

    weight=Column(Float,nullable=False)

    latitude=Column(Float,nullable=False)
    longitude=Column(Float,nullable=False)

    captured_method=Column(String,nullable=False)

    vessel_id=Column(Integer,ForeignKey("vessels.id"),nullable=True)

    specie=relationship("Specie", back_populates="catches")
    cooordinate=composite(Coordinate,latitude,longitude)