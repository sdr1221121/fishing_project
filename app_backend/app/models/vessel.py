from sqlalchemy import Column, Integer, String,Float
from ..database import Base
from sqlalchemy.orm import relationship


class Vessel(Base):
    __tablename__ = "vessels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    registration_number = Column(String, unique=True, nullable=False)
    capacity = Column(Integer, nullable=True)
    tonnage = Column(Float, nullable=True)

    documents = relationship("Document", back_populates="vessel", cascade="all, delete")