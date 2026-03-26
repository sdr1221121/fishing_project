from ...services.wheather_service import fetch_wheather
from ...services.tide_service import fetch_tide 
from fastapi import APIRouter


router = APIRouter(prefix="/condition", tags=["Conditions"])

@router.get("/wheather")
def get_wheather():
    return fetch_wheather()

@router.get("/tide")
def get_tide():
    return fetch_tide()
