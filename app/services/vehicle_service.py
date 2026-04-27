from sqlalchemy.orm import Session
from app.models.vehicle import Vehicle, VehicleService
from app.schemas.vehicle import (
    VehicleCreate, VehicleUpdate,
    VehicleServiceCreate, VehicleServiceUpdate
)

# ── Vehicle CRUD ──────────────────────────────────────────────
def create_vehicle(db: Session, data: VehicleCreate):
    vehicle = Vehicle(**data.model_dump())
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle

def get_all_vehicles(db: Session):
    return db.query(Vehicle).all()

def get_vehicle_by_id(db: Session, vehicle_id: int):
    return db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()

def update_vehicle(db: Session, vehicle_id: int, data: VehicleUpdate):
    vehicle = get_vehicle_by_id(db, vehicle_id)
    if not vehicle:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(vehicle, key, value)
    db.commit()
    db.refresh(vehicle)
    return vehicle

def delete_vehicle(db: Session, vehicle_id: int):
    vehicle = get_vehicle_by_id(db, vehicle_id)
    if vehicle:
        db.delete(vehicle)
        db.commit()
    return vehicle

# ── Vehicle Service CRUD ──────────────────────────────────────
def create_vehicle_service(db: Session, data: VehicleServiceCreate):
    service = VehicleService(**data.model_dump())
    db.add(service)
    db.commit()
    db.refresh(service)
    return service

def get_all_vehicle_services(db: Session):
    results = (
        db.query(VehicleService, Vehicle.vehicle_name, Vehicle.vehicle_number)
        .join(Vehicle, VehicleService.vehicle_id == Vehicle.id)
        .all()
    )
    output = []
    for svc, name, number in results:
        output.append({
            "id"             : svc.id,
            "vehicle_id"     : svc.vehicle_id,
            "service_date"   : svc.service_date,
            "liters_filled"  : svc.liters_filled,
            "fuel_type"      : svc.fuel_type,
            "vehicle_name"   : name,
            "vehicle_number" : number,
        })
    return output

def get_services_by_vehicle(db: Session, vehicle_id: int):
    return db.query(VehicleService).filter(
        VehicleService.vehicle_id == vehicle_id
    ).all()

def update_vehicle_service(db: Session, service_id: int, data: VehicleServiceUpdate):
    svc = db.query(VehicleService).filter(VehicleService.id == service_id).first()
    if not svc:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(svc, key, value)
    db.commit()
    db.refresh(svc)
    return svc

def delete_vehicle_service(db: Session, service_id: int):
    svc = db.query(VehicleService).filter(VehicleService.id == service_id).first()
    if svc:
        db.delete(svc)
        db.commit()
    return svc