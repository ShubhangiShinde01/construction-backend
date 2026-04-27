from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.vehicle import (
    VehicleCreate, VehicleUpdate, VehicleResponse,
    VehicleServiceCreate, VehicleServiceUpdate, VehicleServiceResponse
)
from app.services.vehicle_service import (
    create_vehicle, get_all_vehicles, get_vehicle_by_id,
    update_vehicle, delete_vehicle,
    create_vehicle_service, get_all_vehicle_services,
    get_services_by_vehicle, update_vehicle_service,
    delete_vehicle_service
)

router = APIRouter()

# ── Vehicle APIs ──────────────────────────────────────────────
@router.post("/", response_model=VehicleResponse)
def add_vehicle(data: VehicleCreate, db: Session = Depends(get_db)):
    return create_vehicle(db, data)

@router.get("/", response_model=list[VehicleResponse])
def list_vehicles(db: Session = Depends(get_db)):
    return get_all_vehicles(db)

@router.get("/{vehicle_id}", response_model=VehicleResponse)
def get_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = get_vehicle_by_id(db, vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.put("/{vehicle_id}", response_model=VehicleResponse)
def edit_vehicle(vehicle_id: int, data: VehicleUpdate, db: Session = Depends(get_db)):
    vehicle = update_vehicle(db, vehicle_id, data)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.delete("/{vehicle_id}")
def remove_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = delete_vehicle(db, vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return {"message": "Vehicle deleted successfully"}

# ── Vehicle Service APIs ──────────────────────────────────────
@router.post("/service/add")
def add_service(data: VehicleServiceCreate, db: Session = Depends(get_db)):
    return create_vehicle_service(db, data)

@router.get("/service/all")
def list_all_services(db: Session = Depends(get_db)):
    return get_all_vehicle_services(db)

@router.get("/service/vehicle/{vehicle_id}")
def list_services_by_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    return get_services_by_vehicle(db, vehicle_id)

@router.put("/service/{service_id}")
def edit_service(service_id: int, data: VehicleServiceUpdate, db: Session = Depends(get_db)):
    svc = update_vehicle_service(db, service_id, data)
    if not svc:
        raise HTTPException(status_code=404, detail="Service record not found")
    return svc

@router.delete("/service/{service_id}")
def remove_service(service_id: int, db: Session = Depends(get_db)):
    svc = delete_vehicle_service(db, service_id)
    if not svc:
        raise HTTPException(status_code=404, detail="Service record not found")
    return {"message": "Service record deleted successfully"}