import os
from ..core.document_type import DocumentType
from ..schemas.document import DocumentCreate
from shutil import copyfile
from sqlalchemy.orm import Session
from ..models.document import Document
from datetime import date
from typing import List

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST_DIR = os.path.join(BASE_DIR, 'uploaded_documents/')

os.makedirs(DEST_DIR, exist_ok=True)

async def create_document(db: Session, document: DocumentCreate):
    db_document=Document(**document.dict())
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    await save_document(document)
    return db_document

#TODO: doc type enum
async def save_document(document: DocumentCreate):
    print(f"Salvando documento do tipo {document.document_type}, com fim em {document.end_day}, no caminho {document.file_path}, criado em {document.create_date}")
    try:
         # separate extension
        _, ext = os.path.splitext(document.file_path)
        ext = ext.lower() or ".pdf"  

        file_name = f"{document.document_type.value}_{document.end_day or 'no_end_date'}"

        copyfile(document.file_path, os.path.join(DEST_DIR, file_name + ext))
        print(f"Documento salvo em {os.path.join(DEST_DIR, file_name + ext)}")
    except FileNotFoundError:
        print(f"Erro: O arquivo {document.file_path} não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao salvar o documento: {e}")
        return None

def get_documents(db: Session):
    return db.query(Document).all()

def get_local_documents():
    document = []
    for file_name in os.listdir(DEST_DIR):
        file_path = os.path.join(DEST_DIR, file_name)
        if os.path.isfile(file_path):
            document.append(file_path)
    return document

def expire_dates(document: List[Document]):
    today = date.today()
    for doc in document:
        if doc.end_day < today:
            print(f"Documento {doc.document_type.value} expirado em {doc.end_day}")