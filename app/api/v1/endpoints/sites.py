from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.sites import SiteCreate, SiteUpdate, SiteResponse
from app.services.site_service import (
    create_site, get_all_sites, get_site_by_id,
    update_site, delete_site,
    upload_site_image, get_images_by_site, delete_site_image
)

router = APIRouter()

@router.post("/", response_model=SiteResponse)
def add_site(data: SiteCreate, db: Session = Depends(get_db)):
    return create_site(db, data)

@router.get("/", response_model=list[SiteResponse])
def list_sites(db: Session = Depends(get_db)):
    return get_all_sites(db)

@router.get("/{site_id}", response_model=SiteResponse)
def get_site(site_id: int, db: Session = Depends(get_db)):
    site = get_site_by_id(db, site_id)
    if not site:
        raise HTTPException(status_code=404, detail="Site not found")
    return site

@router.put("/{site_id}", response_model=SiteResponse)
def edit_site(site_id: int, data: SiteUpdate, db: Session = Depends(get_db)):
    site = update_site(db, site_id, data)
    if not site:
        raise HTTPException(status_code=404, detail="Site not found")
    return site

@router.delete("/{site_id}")
def remove_site(site_id: int, db: Session = Depends(get_db)):
    site = delete_site(db, site_id)
    if not site:
        raise HTTPException(status_code=404, detail="Site not found")
    return {"message": "Site deleted successfully"}

@router.post("/{site_id}/upload")
def upload_image(site_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    return upload_site_image(db, site_id, file)

@router.get("/{site_id}/images")
def list_images(site_id: int, db: Session = Depends(get_db)):
    return get_images_by_site(db, site_id)

@router.delete("/images/{image_id}")
def remove_image(image_id: int, db: Session = Depends(get_db)):
    image = delete_site_image(db, image_id)
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    return {"message": "Image deleted successfully"}