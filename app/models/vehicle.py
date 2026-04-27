from sqlalchemy import Column, Integer, String, Date, Float, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id           = Column(Integer, primary_key=True, index=True)
    vehicle_name = Column(String(100), nullable=False)
    vehicle_number = Column(String(50), unique=True, nullable=False)
    created_at   = Column(DateTime, server_default=func.now())


class VehicleService(Base):
    __tablename__ = "vehicle_services"

    id              = Column(Integer, primary_key=True, index=True)
    vehicle_id      = Column(Integer, nullable=False)
    service_date    = Column(Date, nullable=True)
    liters_filled   = Column(Float, nullable=True)
    fuel_type       = Column(String(20), nullable=True)  # Diesel / Petrol
    created_at      = Column(DateTime, server_default=func.now())