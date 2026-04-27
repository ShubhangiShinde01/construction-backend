from sqlalchemy.orm import Session
from app.models.employee import Employee, Attendance
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, AttendanceCreate, AttendanceUpdate

# ── Employee CRUD ─────────────────────────────────────────────
def create_employee(db: Session, data: EmployeeCreate):
    emp = Employee(**data.model_dump())
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp

def get_all_employees(db: Session):
    return db.query(Employee).all()

def get_employee_by_id(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()

def update_employee(db: Session, employee_id: int, data: EmployeeUpdate):
    emp = get_employee_by_id(db, employee_id)
    if not emp:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(emp, key, value)
    db.commit()
    db.refresh(emp)
    return emp

def delete_employee(db: Session, employee_id: int):
    emp = get_employee_by_id(db, employee_id)
    if emp:
        db.delete(emp)
        db.commit()
    return emp

# ── Attendance CRUD ───────────────────────────────────────────
def mark_attendance(db: Session, data: AttendanceCreate):
    att = Attendance(**data.model_dump())
    db.add(att)
    db.commit()
    db.refresh(att)
    return att

def get_all_attendance(db: Session):
    results = (
        db.query(Attendance, Employee.employee_name)
        .join(Employee, Attendance.employee_id == Employee.id)
        .all()
    )
    output = []
    for att, name in results:
        output.append({
            "id"            : att.id,
            "employee_id"   : att.employee_id,
            "date"          : att.date,
            "reason"        : att.reason,
            "employee_name" : name
        })
    return output

def update_attendance(db: Session, att_id: int, data: AttendanceUpdate):
    att = db.query(Attendance).filter(Attendance.id == att_id).first()
    if not att:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(att, key, value)
    db.commit()
    db.refresh(att)
    return att

def delete_attendance(db: Session, att_id: int):
    att = db.query(Attendance).filter(Attendance.id == att_id).first()
    if att:
        db.delete(att)
        db.commit()
    return att