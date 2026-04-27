from sqlalchemy.orm import Session
from app.models.diesel import PetrolPump, DieselEntry
from app.schemas.diesel import (
    PetrolPumpCreate, PetrolPumpUpdate,
    DieselEntryCreate, DieselEntryUpdate
)

# ── Petrol Pump CRUD ──────────────────────────────────────────
def create_pump(db: Session, data: PetrolPumpCreate):
    pump = PetrolPump(**data.model_dump())
    db.add(pump)
    db.commit()
    db.refresh(pump)
    return pump

def get_all_pumps(db: Session):
    return db.query(PetrolPump).all()

def get_pump_by_id(db: Session, pump_id: int):
    return db.query(PetrolPump).filter(PetrolPump.id == pump_id).first()

def update_pump(db: Session, pump_id: int, data: PetrolPumpUpdate):
    pump = get_pump_by_id(db, pump_id)
    if not pump:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(pump, key, value)
    db.commit()
    db.refresh(pump)
    return pump

def delete_pump(db: Session, pump_id: int):
    pump = get_pump_by_id(db, pump_id)
    if pump:
        db.delete(pump)
        db.commit()
    return pump

# ── Diesel Entry CRUD ─────────────────────────────────────────
def create_entry(db: Session, data: DieselEntryCreate):
    entry = DieselEntry(**data.model_dump())
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

def get_all_entries(db: Session):
    results = (
        db.query(DieselEntry, PetrolPump.name)
        .join(PetrolPump, DieselEntry.pump_id == PetrolPump.id)
        .all()
    )
    output = []
    for entry, pump_name in results:
        output.append({
            "id"             : entry.id,
            "pump_id"        : entry.pump_id,
            "pump_name"      : pump_name,
            "fuel_type"      : entry.fuel_type,
            "quantity"       : entry.quantity,
            "vehicle_filled" : entry.vehicle_filled,
            "date"           : entry.date,
        })
    return output

def get_entries_by_pump(db: Session, pump_id: int):
    results = (
        db.query(DieselEntry, PetrolPump.name)
        .join(PetrolPump, DieselEntry.pump_id == PetrolPump.id)
        .filter(DieselEntry.pump_id == pump_id)
        .all()
    )
    output = []
    for entry, pump_name in results:
        output.append({
            "id"             : entry.id,
            "pump_id"        : entry.pump_id,
            "pump_name"      : pump_name,
            "fuel_type"      : entry.fuel_type,
            "quantity"       : entry.quantity,
            "vehicle_filled" : entry.vehicle_filled,
            "date"           : entry.date,
        })
    return output

def update_entry(db: Session, entry_id: int, data: DieselEntryUpdate):
    entry = db.query(DieselEntry).filter(DieselEntry.id == entry_id).first()
    if not entry:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(entry, key, value)
    db.commit()
    db.refresh(entry)
    return entry

def delete_entry(db: Session, entry_id: int):
    entry = db.query(DieselEntry).filter(DieselEntry.id == entry_id).first()
    if entry:
        db.delete(entry)
        db.commit()
    return entry