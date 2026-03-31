import xml.etree.ElementTree as ET
from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..models.fishing_routes import FishingRoute
from ..models.fishing_route_point import FishingRoutePoint

def generate_gpx(route):
    gpx = '<?xml version="1.0" encoding="UTF-8"?>\n'
    gpx += '<gpx version="1.1" creator="PescaApp">\n'
    gpx += '<trk><name>Fishing Route</name><trkseg>\n'

    for point in route.fishing_route_points:
        gpx += f'<trkpt lat="{point.latitude}" lon="{point.longitude}">'
        gpx += f'<time>{point.timestamp.isoformat()}</time>'
        gpx += '</trkpt>\n'

    gpx += '</trkseg></trk>\n</gpx>'

    return gpx


def import_gpx(file_content: bytes, db: Session, vessel_id: int = None):

    # 📥 parse XML
    try:
        root = ET.fromstring(file_content)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid GPX file")

    # 🔎 extrair pontos (compatível com qualquer GPX)
    points = root.findall(".//trkpt")

    if not points:
        raise HTTPException(status_code=400, detail="No track points found")

    # 🆕 criar nova rota automaticamente
    fishing_route = FishingRoute(vessel_id=vessel_id)
    db.add(fishing_route)
    db.commit()
    db.refresh(fishing_route)

    # 💾 guardar pontos
    route_points = []

    for pt in points:
        lat = float(pt.attrib["lat"])
        lon = float(pt.attrib["lon"])

        time_elem = pt.find("time")
        timestamp = None

        if time_elem is not None and time_elem.text:
            try:
                timestamp = datetime.fromisoformat(
                    time_elem.text.replace("Z", "+00:00")
                )
            except ValueError:
                timestamp = None

        route_points.append(
            FishingRoutePoint(
                fishing_route_id=fishing_route.id,
                latitude=lat,
                longitude=lon,
                timestamp=timestamp
            )
        )

    db.add_all(route_points)
    db.commit()

    return {
        "message": "GPX imported and route created successfully",
        "fishing_route_id": fishing_route.id,
        "points_imported": len(route_points)
    }