from pydantic import BaseModel
from typing import Optional
from datetime import date as date_type, datetime

class PetrolPumpCreate(BaseModel):
    name    : str
    address : Optional[str] = None

class PetrolPumpUpdate(BaseModel):
    name    : Optional[str] = None
    address : Optional[str] = None

class PetrolPumpResponse(BaseModel):
    id      : int
    name    : str
    address : Optional[str] = None

    class Config:
        from_attributes = True

class DieselEntryCreate(BaseModel):
    pump_id        : int
    fuel_type      : str
    quantity       : float
    vehicle_filled : Optional[str]       = None
    date           : date_type

class DieselEntryUpdate(BaseModel):
    fuel_type      : Optional[str]       = None
    quantity       : Optional[float]     = None
    vehicle_filled : Optional[str]       = None
    date           : Optional[date_type] = None

class DieselEntryResponse(BaseModel):
    id             : int
    pump_id        : int
    pump_name      : Optional[str]       = None
    fuel_type      : str
    quantity       : float
    vehicle_filled : Optional[str]       = None
    date           : date_type

    class Config:
        from_attributes = True