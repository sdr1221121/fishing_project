from sqlalchemy import Column, Integer, String
from ..database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    documents_type = Column(String, nullable=False)
    end_day = Column(String, nullable=True)
    file_path = Column(String, nullable=False)
    create_date = Column(String, nullable=True)