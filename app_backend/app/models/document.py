from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Date
from ..database import Base
from sqlalchemy.orm import relationship


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    vessel_id=Column(Integer,ForeignKey("vessels.id"), nullable=False)

    document_type = Column(String, nullable=False)
    entity_responsible = Column(String, nullable=False)
    end_day = Column(Date, nullable=True)
    file_path = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=True)

    vessel=relationship("Vessel", back_populates="documents")