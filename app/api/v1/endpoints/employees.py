from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.employee import (
    EmployeeCreate, EmployeeUpdate, EmployeeResponse,
    AttendanceCreate, AttendanceUpdate, AttendanceResponse
)
from app.services.employee_service import (
    create_employee, get_all_employees, get_employee_by_id,
    update_employee, delete_employee,
    mark_attendance, get_all_attendance,
    update_attendance, delete_attendance
)

router = APIRouter()

# ── Employee APIs ─────────────────────────────────────────────
@router.post("/", response_model=EmployeeResponse)
def add_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(db, data)

@router.get("/", response_model=list[EmployeeResponse])
def list_employees(db: Session = Depends(get_db)):
    return get_all_employees(db)

@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    emp = get_employee_by_id(db, employee_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.put("/{employee_id}", response_model=EmployeeResponse)
def edit_employee(employee_id: int, data: EmployeeUpdate, db: Session = Depends(get_db)):
    emp = update_employee(db, employee_id, data)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.delete("/{employee_id}")
def remove_employee(employee_id: int, db: Session = Depends(get_db)):
    emp = delete_employee(db, employee_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}

# ── Attendance APIs ───────────────────────────────────────────
@router.post("/attendance/mark")
def add_attendance(data: AttendanceCreate, db: Session = Depends(get_db)):
    return mark_attendance(db, data)

@router.get("/attendance/all")
def list_attendance(db: Session = Depends(get_db)):
    return get_all_attendance(db)

@router.put("/attendance/{att_id}")
def edit_attendance(att_id: int, data: AttendanceUpdate, db: Session = Depends(get_db)):
    att = update_attendance(db, att_id, data)
    if not att:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return att

@router.delete("/attendance/{att_id}")
def remove_attendance(att_id: int, db: Session = Depends(get_db)):
    att = delete_attendance(db, att_id)
    if not att:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return {"message": "Attendance deleted successfully"}