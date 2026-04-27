from sqlalchemy.orm import Session
from app.models.exports import ExportEntry
from app.schemas.exports import ExportCreate, ExportUpdate

def create_export(db: Session, data: ExportCreate):
    entry = ExportEntry(**data.model_dump())
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

def get_all_exports(db: Session):
    return db.query(ExportEntry).order_by(ExportEntry.date.desc()).all()

def get_export_by_id(db: Session, export_id: int):
    return db.query(ExportEntry).filter(ExportEntry.id == export_id).first()

def update_export(db: Session, export_id: int, data: ExportUpdate):
    entry = get_export_by_id(db, export_id)
    if not entry:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(entry, key, value)
    db.commit()
    db.refresh(entry)
    return entry

def delete_export(db: Session, export_id: int):
    entry = get_export_by_id(db, export_id)
    if entry:
        db.delete(entry)
        db.commit()
    return entry