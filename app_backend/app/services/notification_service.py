import requests
import json
from datetime import date
from typing import List
from app.models.document import Document

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
