from ...services.wheather_service import fetch_wheather
from ...services.tide_service import fetch_tide 
from ...services.notification_service import generate_fishing_recommendations
from fastapi import APIRouter

router = APIRouter(prefix="/condition", tags=["Conditions"])

@router.get("/wheather")
def get_wheather(latitude: float, longitude: float):
    return fetch_wheather(latitude, longitude)

@router.get("/tide")
def get_tide(latitude: float, longitude: float):
    return fetch_tide(latitude, longitude)

@router.get("/")
def get_conditions(latitude: float, longitude: float):
    tide_data = fetch_tide(latitude, longitude)
    wheather_data = fetch_wheather(latitude, longitude)
    alerts = generate_fishing_recommendations(wheather_data, tide_data)

    return {
        "Wheather": wheather_data,
        "Tide": tide_data,
        "alerts": alerts
    }