


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles
# from app.core.config import settings
# from app.db.database import engine, Base
# from app.models.user import User
# from app.api.v1.endpoints import auth,employees,vehicles,diesel
# # from app.api.v1.endpoints import auth, employees, vehicles, diesel, imports, exports, sites
# from app.models.employee import Employee, Attendance
# from app.models.vehicle import Vehicle, VehicleService
# Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title=settings.PROJECT_NAME,
#     version=settings.VERSION,
#     openapi_url="/openapi.json",   # ← this was missing
#     docs_url="/docs",
#     redoc_url="/redoc",
# )

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# app.include_router(auth.router,      prefix=f"{settings.API_V1_STR}/auth",      tags=["Auth"])
# app.include_router(employees.router, prefix=f"{settings.API_V1_STR}/employees", tags=["Employees"])
# app.include_router(vehicles.router,  prefix=f"{settings.API_V1_STR}/vehicles",  tags=["Vehicles"])
# # app.include_router(diesel.router,    prefix=f"{settings.API_V1_STR}/diesel",    tags=["Diesel"])
# # app.include_router(imports.router,   prefix=f"{settings.API_V1_STR}/imports",   tags=["Imports"])
# # app.include_router(exports.router,   prefix=f"{settings.API_V1_STR}/exports",   tags=["Exports"])
# # app.include_router(sites.router,     prefix=f"{settings.API_V1_STR}/sites",     tags=["Sites"])

# @app.get("/")
# def root():
#     return {"message": "Construction Management System API Running ✅"}


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from app.core.config import settings
from app.db.database import engine, Base

# Models
from app.models.user import User
from app.models.employee import Employee, Attendance
from app.models.vehicle import Vehicle, VehicleService
from app.models.diesel import PetrolPump, DieselEntry
from app.models.imports import ImportEntry
from app.models.exports import ExportEntry
from app.models.sites import Site, SiteImage

# Routers
from app.api.v1.endpoints import (
    auth, employees, vehicles, diesel, imports, exports, sites
)

# ✅ Create tables (safe)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ✅ CORS (keep open for mobile)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ FIX: ensure uploads folder exists (IMPORTANT for Render)
if not os.path.exists("uploads"):
    os.makedirs("uploads")

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# ✅ ROUTES
app.include_router(auth.router,      prefix=f"{settings.API_V1_STR}/auth",      tags=["Auth"])
app.include_router(employees.router, prefix=f"{settings.API_V1_STR}/employees", tags=["Employees"])
app.include_router(vehicles.router,  prefix=f"{settings.API_V1_STR}/vehicles",  tags=["Vehicles"])
app.include_router(diesel.router,    prefix=f"{settings.API_V1_STR}/diesel",    tags=["Diesel"])
app.include_router(imports.router,   prefix=f"{settings.API_V1_STR}/imports",   tags=["Imports"])
app.include_router(exports.router,   prefix=f"{settings.API_V1_STR}/exports",   tags=["Exports"])
app.include_router(sites.router,     prefix=f"{settings.API_V1_STR}/sites",     tags=["Sites"])

# ✅ ROOT
@app.get("/")
def root():
    return {"message": "Construction Management System API Running ✅"}


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles
# from app.core.config import settings
# from app.db.database import engine, Base

# # Models
# from app.models.user import User
# from app.models.employee import Employee, Attendance
# from app.models.vehicle import Vehicle, VehicleService
# from app.models.diesel import PetrolPump, DieselEntry
# from app.models.imports import ImportEntry
# from app.models.exports import ExportEntry
# from app.models.sites import Site, SiteImage

# # Routers
# from app.api.v1.endpoints import (
#     auth, employees, vehicles, diesel, imports, exports, sites
# )

# Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title=settings.PROJECT_NAME,
#     version=settings.VERSION,
#     openapi_url="/openapi.json",
#     docs_url="/docs",
#     redoc_url="/redoc",
# )

# app.add_middleware(
#     CORSMiddleware,
#     #allow_origins=["http://localhost:3000"],
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# app.include_router(auth.router,      prefix=f"{settings.API_V1_STR}/auth",      tags=["Auth"])
# app.include_router(employees.router, prefix=f"{settings.API_V1_STR}/employees", tags=["Employees"])
# app.include_router(vehicles.router,  prefix=f"{settings.API_V1_STR}/vehicles",  tags=["Vehicles"])
# app.include_router(diesel.router,    prefix=f"{settings.API_V1_STR}/diesel",    tags=["Diesel"])
# app.include_router(imports.router,   prefix=f"{settings.API_V1_STR}/imports",   tags=["Imports"])
# app.include_router(exports.router,   prefix=f"{settings.API_V1_STR}/exports",   tags=["Exports"])
# app.include_router(sites.router,     prefix=f"{settings.API_V1_STR}/sites",     tags=["Sites"])

# @app.get("/")
# def root():
#     return {"message": "Construction Management System API Running ✅"}