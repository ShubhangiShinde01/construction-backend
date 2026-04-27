from pydantic import BaseModel
from typing import Optional
from datetime import date as date_type, datetime

# ── Vehicle Schemas ───────────────────────────────────────────
class VehicleCreate(BaseModel):
    vehicle_name   : str
    vehicle_number : str

class VehicleUpdate(BaseModel):
    vehicle_name   : Optional[str] = None
    vehicle_number : Optional[str] = None

class VehicleResponse(BaseModel):
    id             : int
    vehicle_name   : str
    vehicle_number : str
    created_at     : Optional[datetime] = None

    class Config:
        from_attributes = True

# ── Vehicle Service Schemas ───────────────────────────────────
class VehicleServiceCreate(BaseModel):
    vehicle_id    : int
    service_date  : Optional[date_type] = None
    liters_filled : Optional[float]     = None
    fuel_type     : Optional[str]       = None

class VehicleServiceUpdate(BaseModel):
    service_date  : Optional[date_type] = None
    liters_filled : Optional[float]     = None
    fuel_type     : Optional[str]       = None

class VehicleServiceResponse(BaseModel):
    id             : int
    vehicle_id     : int
    service_date   : Optional[date_type] = None
    liters_filled  : Optional[float]     = None
    fuel_type      : Optional[str]       = None
    vehicle_name   : Optional[str]       = None
    vehicle_number : Optional[str]       = None

    class Config:
        from_attributes = True