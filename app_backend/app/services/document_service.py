import os
from ..schemas.document import DocumentCreate
from shutil import copyfile
from sqlalchemy.orm import Session
from ..models.document import Document
from datetime import date
from typing import List,Optional
from sqlalchemy import extract


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

async def save_document(document: DocumentCreate):
    print(f"Salvando documento do tipo {document.document_type}, com fim em {document.end_day}, no caminho {document.file_path}, criado em {document.create_date}")
    try:
         # separate extension
        _, ext = os.path.splitext(document.file_path)
        ext = ext.lower() or ".pdf"  

        file_name = f"{document.document_type}_{document.end_day or 'no_end_date'}"

        copyfile(document.file_path, os.path.join(DEST_DIR, file_name + ext))
        print(f"Documento salvo em {os.path.join(DEST_DIR, file_name + ext)}")
    except FileNotFoundError:
        print(f"Erro: O arquivo {document.file_path} não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao salvar o documento: {e}")
        return None

def get_local_documents():
    document = []
    for file_name in os.listdir(DEST_DIR):
        file_path = os.path.join(DEST_DIR, file_name)
        if os.path.isfile(file_path):
            document.append(file_path)
    return document

def filter_documents(
        db:Session,
        vessel_id:Optional[int]=None,
        document_type:Optional[str]=None,
        entity_responsible:Optional[str]=None,
        end_year:Optional[int]=None,
        date1:Optional[int]=None,
        date2:Optional[int]=None

):
    query=db.query(Document)

    if vessel_id is not None:
        query= query.filter(Document.vessel_id==vessel_id)

    if document_type is not None:
        query= query.filter(Document.document_type==document_type)

    if entity_responsible is not None:
        query= query.filter(Document.entity_responsible==entity_responsible)

    if end_year is not None:
      query= query.filter(extract("year",Document.end_year)==end_year)

    if (date1 and date2) is not None:
      query= query.filter(Document.end_day> date1 and Document.end_day<date2)

    results= query.all()

    return results