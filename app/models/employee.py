from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id           = Column(Integer, primary_key=True, index=True)
    employee_name   = Column(String(100), nullable=False)
    employee_number = Column(String(50), unique=True, nullable=False)
    contact         = Column(String(15), nullable=False)
    created_at      = Column(DateTime, server_default=func.now())


class Attendance(Base):
    __tablename__ = "attendance"

    id          = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, nullable=False)
    date        = Column(Date, nullable=False)
    reason      = Column(String(255), nullable=True)
    created_at  = Column(DateTime, server_default=func.now())