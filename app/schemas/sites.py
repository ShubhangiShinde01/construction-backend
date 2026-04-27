from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class SiteCreate(BaseModel):
    site_name : str
    location  : Optional[str] = None

class SiteUpdate(BaseModel):
    site_name : Optional[str] = None
    location  : Optional[str] = None

class SiteImageResponse(BaseModel):
    id         : int
    site_id    : int
    image_path : str

    class Config:
        from_attributes = True

class SiteResponse(BaseModel):
    id        : int
    site_name : str
    location  : Optional[str] = None
    images    : Optional[List[SiteImageResponse]] = []

    class Config:
        from_attributes = True