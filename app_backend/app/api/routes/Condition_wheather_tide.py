from ...services.wheather_service import fetch_wheather
from ...services.tide_service import fetch_tide 
from fastapi import APIRouter
import os


router = APIRouter(prefix="/condition", tags=["Conditions"])

@router.get("/wheather")
def get_wheather():
    return fetch_wheather()

@router.get("/tide")
def get_tide():
    return fetch_tide()

@router.get("/")
def get_conditions(lat:float, lon:float):
    tide_data=fetch_tide(lat, lon)
    wheather_data=fetch_wheather(lat, lon)
    return{
        "Wheather":wheather_data,
        "Tide":tide_data
    }