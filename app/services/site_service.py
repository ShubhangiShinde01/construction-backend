from sqlalchemy.orm import Session
from app.models.sites import Site, SiteImage
from app.schemas.sites import SiteCreate, SiteUpdate
import os, shutil
from fastapi import UploadFile

UPLOAD_DIR = "uploads/site_images"

def create_site(db: Session, data: SiteCreate):
    site = Site(**data.model_dump())
    db.add(site)
    db.commit()
    db.refresh(site)
    return site

def get_all_sites(db: Session):
    return db.query(Site).all()

def get_site_by_id(db: Session, site_id: int):
    return db.query(Site).filter(Site.id == site_id).first()

def update_site(db: Session, site_id: int, data: SiteUpdate):
    site = get_site_by_id(db, site_id)
    if not site:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(site, key, value)
    db.commit()
    db.refresh(site)
    return site

def delete_site(db: Session, site_id: int):
    site = get_site_by_id(db, site_id)
    if site:
        db.delete(site)
        db.commit()
    return site

def upload_site_image(db: Session, site_id: int, file: UploadFile):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = f"{UPLOAD_DIR}/{site_id}_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    image = SiteImage(site_id=site_id, image_path=file_path)
    db.add(image)
    db.commit()
    db.refresh(image)
    return image

def get_images_by_site(db: Session, site_id: int):
    return db.query(SiteImage).filter(SiteImage.site_id == site_id).all()

def delete_site_image(db: Session, image_id: int):
    image = db.query(SiteImage).filter(SiteImage.id == image_id).first()
    if image:
        if os.path.exists(image.image_path):
            os.remove(image.image_path)
        db.delete(image)
        db.commit()
    return image