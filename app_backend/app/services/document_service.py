import os
from ..core.documents_type import DocumentType
from ..schemas.document import DocumentCreate
from shutil import copyfile
from sqlalchemy.orm import Session
from ..models.document import Document


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST_DIR = os.path.join(BASE_DIR, 'uploaded_documents/')

os.makedirs(DEST_DIR, exist_ok=True)

def create_document(db: Session, document: DocumentCreate):
    db_document=Document(**document.dict())
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    save_document(db_document.documents_type, document)
    return db_document

def save_document(doc_type: str, document: DocumentCreate):
    print(f"Salvando documento do tipo {doc_type}, com fim em {document.end_day}, no caminho {document.file_path}, criado em {document.create_date}")
    try:
         # separate extension
        _, ext = os.path.splitext(document.file_path)
        ext = ext.lower() or ".pdf"  

        file_name = f"{doc_type.value}_{document.end_day or 'no_end_date'}"

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