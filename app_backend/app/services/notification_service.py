import requests
import json
from datetime import date
from typing import List
from ..models.document import Document
from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import extract


#TODO: use firebase keys
FIREBASE_SERVER_KEY = ""
FIREBASE_URL = ""

def expire_dates(document: List[Document]):
    today = date.today()
    for doc in document:
        if doc.end_day < today:
            print(f"Documento {doc.document_type.value} expirado em {doc.end_day}")
            send_notification(
                token_dispositivo=doc.device_token,
                titulo="Documento Expirado",
                mensagem=f"O documento {doc.document_type.value} expirou em {doc.end_day}."
            )

def send_notification(token_dispositivo: str, titulo: str, mensagem: str):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"key={FIREBASE_SERVER_KEY}"
    }

    body = {
        "to": token_dispositivo,  
        "notification": {
            "title": titulo,
            "body": mensagem
        },
        "priority": "high"
    }

    response = requests.post(FIREBASE_URL, headers=headers, data=json.dumps(body))
    return response.json()

def get_expired_documents(db:Session):
    query=db.query(Document)
    today=date.today
    expired_documents=query.filter(Document.end_day.isnot(None), Document.end_day < today).all
    return expired_documents or ["VAZIO"]

def get_valid_documents(db:Session):
    query=db.query(Document)
    today=date.today
    valid_documents=query.filter(Document.end_day>today).all
    return valid_documents or ["VAZIO"]