from sqlalchemy import Column, Integer, String
from ..database import Base

class Vessel(Base):
    __tablename__ = "vessels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    registration_number = Column(String, unique=True, nullable=False)
    capacity = Column(Integer, nullable=True)
    tonnage = Column(Integer, nullable=True)
