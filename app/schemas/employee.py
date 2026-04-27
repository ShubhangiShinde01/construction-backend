from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from datetime import date as date_type, datetime

# ── Employee Schemas ──────────────────────────────────────────
class EmployeeCreate(BaseModel):
    employee_name   : str
    employee_number : str
    contact         : str

class EmployeeUpdate(BaseModel):
    employee_name   : Optional[str] = None
    employee_number : Optional[str] = None
    contact         : Optional[str] = None

class EmployeeResponse(BaseModel):
    id              : int
    employee_name   : str
    employee_number : str
    contact         : str
    created_at      : Optional[datetime] = None

    class Config:
        from_attributes = True

# ── Attendance Schemas ────────────────────────────────────────
class AttendanceCreate(BaseModel):
    employee_id : int
    date        : date_type
    reason      : Optional[str] = None

class AttendanceUpdate(BaseModel):
    date   : Optional[date_type] = None
    reason : Optional[str]       = None

class AttendanceResponse(BaseModel):
    id            : int
    employee_id   : int
    date          : date_type
    reason        : Optional[str] = None
    employee_name : Optional[str] = None

    class Config:
        from_attributes = True