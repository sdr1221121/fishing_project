import requests
import os
import json
from datetime import date
from typing import List
from sqlalchemy.orm import Session

from ..models.document import Document

FIREBASE_SERVER_KEY = os.getenv("FIREBASE_SERVER_KEY")
FIREBASE_URL = os.getenv("FIREBASE_URL")


def send_notification(token: str, title: str, message: str):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"key={FIREBASE_SERVER_KEY}"
    }

    body = {
        "to": token,
        "notification": {
            "title": title,
            "body": message
        },
        "priority": "high"
    }

    response = requests.post(FIREBASE_URL, headers=headers, data=json.dumps(body))
    return response.json()


def check_expiring_documents(db: Session):
    today = date.today()

    documents = db.query(Document)\
        .filter(Document.end_day.isnot(None))\
        .all()

    alerts = []

    for doc in documents:
        if doc.end_day < today:
            alerts.append({
                "document_id": doc.id,
                "message": f"Documento expirado: {doc.document_type.value}"
            })

            if doc.device_token:
                send_notification(
                    token=doc.device_token,
                    title="Documento Expirado",
                    message=f"O documento {doc.document_type.value} expirou."
                )

        elif (doc.end_day - today).days <= 30:
            alerts.append({
                "document_id": doc.id,
                "message": f"Documento a expirar: {doc.document_type}"
            })

    return alerts


def generate_fishing_recommendations(weather: dict, tides: dict):
    recommendations = []

    wind = weather.get("wind_speed", 0)
    temp = weather.get("temperature", 0)

    if wind > 12:
        recommendations.append("Vento forte — condições desfavoráveis")

    elif wind < 5:
        recommendations.append("Vento fraco — boas condições")

    if temp > 12:
        recommendations.append("Temperatura favorável à atividade piscatória")

    elif temp < 8:
        recommendations.append("Temperatura baixa — atividade reduzida")

    tide_data = tides.get("data", [])

    if len(tide_data) >= 2:
        diff = abs(tide_data[0]["height"] - tide_data[1]["height"])

        if diff > 2:
            recommendations.append("Correntes fortes devido a grande variação de maré")

        else:
            recommendations.append("Maré estável — condições normais")

    return recommendations

