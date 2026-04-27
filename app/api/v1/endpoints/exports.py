from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.exports import ExportCreate, ExportUpdate, ExportResponse
from app.services.export_service import (
    create_export, get_all_exports,
    get_export_by_id, update_export, delete_export
)

router = APIRouter()

@router.post("/", response_model=ExportResponse)
def add_export(data: ExportCreate, db: Session = Depends(get_db)):
    return create_export(db, data)

@router.get("/", response_model=list[ExportResponse])
def list_exports(db: Session = Depends(get_db)):
    return get_all_exports(db)

@router.get("/{export_id}", response_model=ExportResponse)
def get_export(export_id: int, db: Session = Depends(get_db)):
    entry = get_export_by_id(db, export_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Export record not found")
    return entry

@router.put("/{export_id}", response_model=ExportResponse)
def edit_export(export_id: int, data: ExportUpdate, db: Session = Depends(get_db)):
    entry = update_export(db, export_id, data)
    if not entry:
        raise HTTPException(status_code=404, detail="Export record not found")
    return entry

@router.delete("/{export_id}")
def remove_export(export_id: int, db: Session = Depends(get_db)):
    entry = delete_export(db, export_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Export record not found")
    return {"message": "Export record deleted successfully"}