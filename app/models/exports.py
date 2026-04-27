from sqlalchemy import Column, Integer, String, Date, Float, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class ExportEntry(Base):
    __tablename__ = "export_entries"

    id                   = Column(Integer, primary_key=True, index=True)
    date                 = Column(Date, nullable=False)
    bill_no              = Column(String(100), nullable=True)
    party_name_address   = Column(String(255), nullable=False)
    material_particulars = Column(String(255), nullable=False)
    quantity             = Column(Float, nullable=False)
    vehicle_no           = Column(String(50), nullable=True)
    driver_name          = Column(String(100), nullable=True)
    remark               = Column(String(255), nullable=True)
    created_at           = Column(DateTime, server_default=func.now())