from pydantic import BaseModel
from typing import Optional
from datetime import date as date_type, datetime

class ImportCreate(BaseModel):
    date                 : date_type
    bill_no              : Optional[str]   = None
    supplier_name        : str
    material_particulars : str
    quantity             : float
    unit                 : Optional[str]   = None
    vehicle_no           : Optional[str]   = None
    driver_name          : Optional[str]   = None
    remark               : Optional[str]   = None

class ImportUpdate(BaseModel):
    date                 : Optional[date_type] = None
    bill_no              : Optional[str]       = None
    supplier_name        : Optional[str]       = None
    material_particulars : Optional[str]       = None
    quantity             : Optional[float]     = None
    unit                 : Optional[str]       = None
    vehicle_no           : Optional[str]       = None
    driver_name          : Optional[str]       = None
    remark               : Optional[str]       = None

class ImportResponse(BaseModel):
    id                   : int
    date                 : date_type
    bill_no              : Optional[str]   = None
    supplier_name        : str
    material_particulars : str
    quantity             : float
    unit                 : Optional[str]   = None
    vehicle_no           : Optional[str]   = None
    driver_name          : Optional[str]   = None
    remark               : Optional[str]   = None

    class Config:
        from_attributes = True