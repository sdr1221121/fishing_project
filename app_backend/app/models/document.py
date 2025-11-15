from sqlalchemy import Column, DateTime, Integer, String, Date
from ..database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    document_type = Column(String, nullable=False)
    end_day = Column(Date, nullable=True)
    file_path = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=True)