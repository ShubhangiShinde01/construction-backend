from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.imports import ImportCreate, ImportUpdate, ImportResponse
from app.services.import_service import (
    create_import, get_all_imports,
    get_import_by_id, update_import, delete_import
)

router = APIRouter()

@router.post("/", response_model=ImportResponse)
def add_import(data: ImportCreate, db: Session = Depends(get_db)):
    return create_import(db, data)

@router.get("/", response_model=list[ImportResponse])
def list_imports(db: Session = Depends(get_db)):
    return get_all_imports(db)

@router.get("/{import_id}", response_model=ImportResponse)
def get_import(import_id: int, db: Session = Depends(get_db)):
    entry = get_import_by_id(db, import_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Import record not found")
    return entry

@router.put("/{import_id}", response_model=ImportResponse)
def edit_import(import_id: int, data: ImportUpdate, db: Session = Depends(get_db)):
    entry = update_import(db, import_id, data)
    if not entry:
        raise HTTPException(status_code=404, detail="Import record not found")
    return entry

@router.delete("/{import_id}")
def remove_import(import_id: int, db: Session = Depends(get_db)):
    entry = delete_import(db, import_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Import record not found")
    return {"message": "Import record deleted successfully"}