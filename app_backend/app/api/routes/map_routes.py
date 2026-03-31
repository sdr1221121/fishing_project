from fastapi import UploadFile, File, APIRouter, Depends, Query
from typing import Optional
from sqlalchemy.orm import Session
from fastapi.responses import Response
from ...database import SessionLocal  
from ...models.fishing_spot import FishingSpot
from ...services.gpx_service import generate_gpx, import_gpx
from ...services.fishing_spot_service import create_fishing_spot, fetch_fishing_spots
from ...schemas.fishing_route import FishingRouteCreate, FishingRouteOut
from ...schemas.fishing_route_point import FishingRoutePointCreate
from ...schemas.fishing_spot import FishingSpotCreate, FishingSpotOut
from ...services.fishing_route_service import (
    create_route,
    get_route_by_id,
    get_all_routes,
    add_point_to_route
)
import xml.etree.ElementTree as ET


router = APIRouter(prefix="/map", tags=["Map & Routes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------
# SPOTS
# -------------------------
@router.get("/spots")
def get_fishing_spots(
    db: Session=Depends(get_db),
    name: Optional[str] = Query(None),
    min_popularity: Optional[int] = Query(None),
    max_popularity: Optional[int] = Query(None),
    lat: Optional[float] = Query(None),
    lon: Optional[float] = Query(None),
    radius: Optional[float] = Query(None)
    ):
    results = fetch_fishing_spots(
        db,
        name=name,
        min_popularity=min_popularity,
        max_popularity=max_popularity,
        lat=lat,
        lon=lon,
        radius=radius
    )
    return results

@router.post("/spots",response_model=FishingSpotOut)
def create_fishing_spots(data:FishingSpotCreate,db:Session=Depends(get_db)):
    return create_fishing_spot(db,data.name,data.latitude,data.longitude,data.description)

# -------------------------
# ROUTES
# -------------------------
@router.post("/routes", response_model=FishingRouteOut)
def create_route_endpoint(data: FishingRouteCreate, db: Session = Depends(get_db)):
    return create_route(db, data.vessel_id , data.name)


@router.get("/routes", response_model=list[FishingRouteOut])
def get_routes_endpoint(db: Session = Depends(get_db)):
    return get_all_routes(db)


@router.get("/routes/{fishing_route_id}", response_model=FishingRouteOut)
def get_route_endpoint(route_id: int, db: Session = Depends(get_db)):
    return get_route_by_id(db, route_id)

# -------------------------
# POINTS
# -------------------------
@router.post("/routes/{fishing_route_id}/points")
def add_point_endpoint(
    fishing_route_id: int,
    data: FishingRoutePointCreate,
    db: Session = Depends(get_db)
):
    add_point_to_route(db, fishing_route_id, data.latitude, data.longitude)
    return {"message": "Ponto adicionado"}

# -------------------------
# GPX EXPORT
# -------------------------

@router.get("/routes/{route_id}/gpx")
def export_gpx(fishing_route_id : int, db: Session = Depends(get_db)):

    fishing_route = get_route_by_id(db, fishing_route_id )

    gpx_data = generate_gpx(fishing_route)

    return Response(
        content=gpx_data,
        media_type="application/gpx+xml",
        headers={
            "Content-Disposition": f"attachment; filename=route_{fishing_route_id}.gpx"
        }
    )

# -------------------------
# GPX IMPORT
# -------------------------
@router.post("/routes/{fishing_route_id }/import-gpx")
async def import_gpx_endpoint(
    fishing_route_id : int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    content = await file.read()
    return import_gpx(content, fishing_route_id , db)

