import requests, os
import json
from datetime import date
from typing import List
from ..models.document import Document
from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import extract


#TODO: use firebase keys
FIREBASE_SERVER_KEY =os.getenv("FIREBASE_SERVER_KEY")
FIREBASE_URL = os.getenv("FIREBASE_URL")

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

def generate_alerts(weather: dict, tides: list):
    alerts = []

    wind = weather["wind_speed"]
    temp = weather["temperature"]

    # 🌬️ vento perigoso
    if wind > 12:
        alerts.append("Condições perigosas: vento muito forte")

    # 🌊 maré forte (mudança brusca)
    tide_list = tides.get("data", [])
    if len(tide_list) >= 2:
        
        diff = abs(tide_list[0]["height"] - tide_list[1]["height"])
        if diff > 2:
            alerts.append("Maré com grande variação — correntes fortes")

    # ❄️ água fria
    if temp < 8:
        alerts.append("Temperatura baixa pode afetar a pesca")

    # 🎣 condição ideal (extra útil)
    if wind < 5 and temp > 12:
        alerts.append("Boas condições para pesca")

    return alerts