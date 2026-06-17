import ipaddress
from pathlib import Path

import geoip2.database
import geoip2.errors
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="IP 地理位置查询")

DB_PATH = Path(__file__).parent / "GeoLite2-City.mmdb"


class IPResponse(BaseModel):
    ip: str
    country: str | None
    country_code: str | None
    city: str | None
    latitude: float | None
    longitude: float | None
    timezone: str | None
    postal_code: str | None


@app.get("/api/v1/ip/query", response_model=IPResponse)
def query_ip(ip: str):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        raise HTTPException(status_code=400, detail="IP 地址不合法")

    if not DB_PATH.exists():
        raise HTTPException(
            status_code=500,
            detail=f"离线数据库未找到，请将 GeoLite2-City.mmdb 放置于 {DB_PATH}",
        )

    try:
        with geoip2.database.Reader(str(DB_PATH)) as reader:
            record = reader.city(ip)
    except geoip2.errors.AddressNotFoundError:
        raise HTTPException(status_code=404, detail="未找到该 IP 的地理信息")

    return IPResponse(
        ip=ip,
        country=record.country.name,
        country_code=record.country.iso_code,
        city=record.city.name,
        latitude=record.location.latitude,
        longitude=record.location.longitude,
        timezone=record.location.time_zone,
        postal_code=record.postal.code,
    )
