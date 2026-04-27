from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class Site(Base):
    __tablename__ = "sites"

    id         = Column(Integer, primary_key=True, index=True)
    site_name  = Column(String(150), nullable=False)
    location   = Column(String(255), nullable=True)
    created_at = Column(DateTime, server_default=func.now())

class SiteImage(Base):
    __tablename__ = "site_images"

    id         = Column(Integer, primary_key=True, index=True)
    site_id    = Column(Integer, nullable=False)
    image_path = Column(String(500), nullable=False)
    created_at = Column(DateTime, server_default=func.now())