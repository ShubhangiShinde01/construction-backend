from sqlalchemy import Column, Integer, String, Date, Float, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class PetrolPump(Base):
    __tablename__ = "petrol_pumps"

    id        = Column(Integer, primary_key=True, index=True)
    name      = Column(String(100), nullable=False, unique=True)
    address   = Column(String(255), nullable=True)
    created_at = Column(DateTime, server_default=func.now())

class DieselEntry(Base):
    __tablename__ = "diesel_entries"

    id              = Column(Integer, primary_key=True, index=True)
    pump_id         = Column(Integer, nullable=False)
    fuel_type       = Column(String(20), nullable=False)   # Diesel / Petrol
    quantity        = Column(Float, nullable=False)
    vehicle_filled  = Column(String(100), nullable=True)
    date            = Column(Date, nullable=False)
    created_at      = Column(DateTime, server_default=func.now())