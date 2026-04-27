from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.diesel import (
    PetrolPumpCreate, PetrolPumpUpdate, PetrolPumpResponse,
    DieselEntryCreate, DieselEntryUpdate
)
from app.services.diesel_service import (
    create_pump, get_all_pumps, get_pump_by_id, update_pump, delete_pump,
    create_entry, get_all_entries, get_entries_by_pump,
    update_entry, delete_entry
)

router = APIRouter()

# ── Petrol Pump APIs ──────────────────────────────────────────
@router.post("/pumps/", response_model=PetrolPumpResponse)
def add_pump(data: PetrolPumpCreate, db: Session = Depends(get_db)):
    return create_pump(db, data)

@router.get("/pumps/", response_model=list[PetrolPumpResponse])
def list_pumps(db: Session = Depends(get_db)):
    return get_all_pumps(db)

@router.put("/pumps/{pump_id}", response_model=PetrolPumpResponse)
def edit_pump(pump_id: int, data: PetrolPumpUpdate, db: Session = Depends(get_db)):
    pump = update_pump(db, pump_id, data)
    if not pump:
        raise HTTPException(status_code=404, detail="Pump not found")
    return pump

@router.delete("/pumps/{pump_id}")
def remove_pump(pump_id: int, db: Session = Depends(get_db)):
    pump = delete_pump(db, pump_id)
    if not pump:
        raise HTTPException(status_code=404, detail="Pump not found")
    return {"message": "Pump deleted successfully"}

# ── Diesel Entry APIs ─────────────────────────────────────────
@router.post("/entries/")
def add_entry(data: DieselEntryCreate, db: Session = Depends(get_db)):
    return create_entry(db, data)

@router.get("/entries/")
def list_entries(db: Session = Depends(get_db)):
    return get_all_entries(db)

@router.get("/entries/pump/{pump_id}")
def list_entries_by_pump(pump_id: int, db: Session = Depends(get_db)):
    return get_entries_by_pump(db, pump_id)

@router.put("/entries/{entry_id}")
def edit_entry(entry_id: int, data: DieselEntryUpdate, db: Session = Depends(get_db)):
    entry = update_entry(db, entry_id, data)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry

@router.delete("/entries/{entry_id}")
def remove_entry(entry_id: int, db: Session = Depends(get_db)):
    entry = delete_entry(db, entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return {"message": "Entry deleted successfully"}