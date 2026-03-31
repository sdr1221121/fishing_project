from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException

from ..models.fishing_routes import FishingRoute
from ..models.fishing_route_point import FishingRoutePoint


def create_route(db: Session, vessel_id: int):
    fishing_route = FishingRoute(vessel_id=vessel_id)

    db.add(fishing_route)
    db.commit()
    db.refresh(fishing_route)

    return fishing_route


def get_route_by_id(db: Session, fishing_route_id: int):
    fishing_route = (
        db.query(FishingRoute)
        .options(joinedload(FishingRoute.fishing_route_points))
        .filter(FishingRoute.id == fishing_route_id)
        .first()
    )

    if not fishing_route:
        raise HTTPException(status_code=404, detail="Route not found")

    return fishing_route


def get_all_routes(db: Session):
    return (
        db.query(FishingRoute)
        .options(joinedload(FishingRoute.fishing_route_points))
        .all()
    )


def add_point_to_route(db: Session, fishing_route_id: int, latitude: float, longitude: float):
    fishing_route = db.query(FishingRoute).filter(FishingRoute.id == fishing_route_id).first()

    if not fishing_route:
        raise HTTPException(status_code=404, detail="Route not found")

    point = FishingRoutePoint(
        fishing_route_id=fishing_route_id,
        latitude=latitude,
        longitude=longitude
    )

    db.add(point)
    db.commit()

    return point