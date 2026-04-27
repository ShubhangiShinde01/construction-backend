from sqlalchemy.orm import Session
from app.models.imports import ImportEntry
from app.schemas.imports import ImportCreate, ImportUpdate


def create_import(db: Session, data: ImportCreate):
    entry = ImportEntry(**data.model_dump())
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

def get_all_imports(db: Session):
    return db.query(ImportEntry).order_by(ImportEntry.date.desc()).all()

def get_import_by_id(db: Session, import_id: int):
    return db.query(ImportEntry).filter(ImportEntry.id == import_id).first()

def update_import(db: Session, import_id: int, data: ImportUpdate):
    entry = get_import_by_id(db, import_id)
    if not entry:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(entry, key, value)
    db.commit()
    db.refresh(entry)
    return entry

def delete_import(db: Session, import_id: int):
    entry = get_import_by_id(db, import_id)
    if entry:
        db.delete(entry)
        db.commit()
    return entry