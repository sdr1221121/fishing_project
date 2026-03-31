from sqlalchemy.orm import Session
from typing import Optional, List
from ..models.fishing_spot import FishingSpot
from sqlalchemy import and_
import math

TOLERANCE = 0.0003
RADIUS_METERS = 30

# Distância (Haversine)
def distance_meters(lat1, lon1, lat2, lon2):
    R = 6371000

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

def create_fishing_spot(
    db: Session,
    name: str,
    latitude: float,
    longitude: float,
    description: Optional[str] = None
):
    nearby_spots = db.query(FishingSpot).filter(
        and_(
            FishingSpot.latitude.between(latitude - TOLERANCE, latitude + TOLERANCE),
            FishingSpot.longitude.between(longitude - TOLERANCE, longitude + TOLERANCE)
        )
    ).all()

    for fishing_spot in nearby_spots:
        if distance_meters(latitude, longitude, fishing_spot.latitude, fishing_spot.longitude) <= RADIUS_METERS:
            fishing_spot.popularity += 1
            db.commit()
            db.refresh(fishing_spot)
            return fishing_spot

    new_spot = FishingSpot(
        name=name,
        latitude=latitude,
        longitude=longitude,
        description=description,
        popularity=1
    )

    db.add(new_spot)
    db.commit()
    db.refresh(new_spot)

    return new_spot

def decrease_spot_popularity(db: Session, fishing_spot_id: int):
    fishing_spot = db.query(FishingSpot).filter(FishingSpot.id == fishing_spot_id).first()

    if not fishing_spot:
        return None

    if fishing_spot.popularity > 1:
        fishing_spot.popularity -= 1
        db.commit()
        db.refresh(fishing_spot)
        return fishing_spot
    else:
        db.delete(fishing_spot)
        db.commit()
        return {"message": "Spot removed"}

def fetch_fishing_spots(
    db: Session,
    name: Optional[str] = None,
    min_popularity: Optional[int] = None,
    max_popularity: Optional[int] = None,
    lat: Optional[float] = None,
    lon: Optional[float] = None,
    radius: Optional[float] = None
) -> List[FishingSpot]:

    query = db.query(FishingSpot)

    if name:
        query = query.filter(FishingSpot.name.ilike(f"%{name}%"))

    if min_popularity is not None:
        query = query.filter(FishingSpot.popularity >= min_popularity)

    if max_popularity is not None:
        query = query.filter(FishingSpot.popularity <= max_popularity)

    fishing_spots = query.all()

    if lat is not None and lon is not None and radius is not None:
        filtered_spots = []
        for spot in fishing_spots:
            dist = distance_meters(lat, lon, spot.latitude, spot.longitude)
            if dist <= radius:
                filtered_spots.append(spot)
        return filtered_spots

    return fishing_spots