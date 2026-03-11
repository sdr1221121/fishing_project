from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Specie(Base):
    __tablename__="species"

    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    classification=Column(String,nullable=True)

    catches=relationship("Catch", back_populates="species")