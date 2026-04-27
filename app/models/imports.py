from sqlalchemy import Column, Integer, String, Date, Float, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class ImportEntry(Base):
    __tablename__ = "import_entries"

    id                  = Column(Integer, primary_key=True, index=True)
    date                = Column(Date, nullable=False)
    bill_no             = Column(String(100), nullable=True)
    supplier_name       = Column(String(150), nullable=False)
    material_particulars = Column(String(255), nullable=False)
    quantity            = Column(Float, nullable=False)
    unit                = Column(String(50), nullable=True)
    vehicle_no          = Column(String(50), nullable=True)
    driver_name         = Column(String(100), nullable=True)
    remark              = Column(String(255), nullable=True)
    created_at          = Column(DateTime, server_default=func.now())