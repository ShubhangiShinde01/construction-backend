from pydantic import BaseModel
from typing import Optional
from datetime import date as date_type

class ExportCreate(BaseModel):
    date                 : date_type
    bill_no              : Optional[str]   = None
    party_name_address   : str
    material_particulars : str
    quantity             : float
    vehicle_no           : Optional[str]   = None
    driver_name          : Optional[str]   = None
    remark               : Optional[str]   = None

class ExportUpdate(BaseModel):
    date                 : Optional[date_type] = None
    bill_no              : Optional[str]       = None
    party_name_address   : Optional[str]       = None
    material_particulars : Optional[str]       = None
    quantity             : Optional[float]     = None
    vehicle_no           : Optional[str]       = None
    driver_name          : Optional[str]       = None
    remark               : Optional[str]       = None

class ExportResponse(BaseModel):
    id                   : int
    date                 : date_type
    bill_no              : Optional[str]   = None
    party_name_address   : str
    material_particulars : str
    quantity             : float
    vehicle_no           : Optional[str]   = None
    driver_name          : Optional[str]   = None
    remark               : Optional[str]   = None

    class Config:
        from_attributes = True