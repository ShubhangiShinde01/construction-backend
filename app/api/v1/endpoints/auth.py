# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from app.db.database import get_db
# from app.schemas.user import UserCreate, UserLogin, UserResponse, TokenResponse
# from app.services.auth_service import (
#     create_user, get_user_by_username,
#     verify_password, create_access_token,
#     get_all_users, delete_user
# )
# from app.core.dependencies import get_current_user, admin_only

# router = APIRouter()

# # ── Register (Admin only) ─────────────────────────────────────
# @router.post("/register", response_model=UserResponse)
# def register(
#     user: UserCreate,
#     db: Session = Depends(get_db),
#     _: dict = Depends(admin_only)
# ):
#     if get_user_by_username(db, user.username):
#         raise HTTPException(status_code=400, detail="Username already exists")
#     return create_user(db, user)

# # ── Login ─────────────────────────────────────────────────────
# @router.post("/login", response_model=TokenResponse)
# def login(user: UserLogin, db: Session = Depends(get_db)):
#     db_user = get_user_by_username(db, user.username)
#     if not db_user or not verify_password(user.password, db_user.password):
#         raise HTTPException(status_code=401, detail="Invalid username or password")

#     token = create_access_token({"sub": db_user.username, "role": db_user.role})
#     return {
#         "access_token" : token,
#         "token_type"   : "bearer",
#         "role"         : db_user.role,
#         "full_name"    : db_user.full_name
#     }

# # ── Get all users (Admin only) ────────────────────────────────
# @router.get("/users", response_model=list[UserResponse])
# def list_users(
#     db: Session = Depends(get_db),
#     _: dict = Depends(admin_only)
# ):
#     return get_all_users(db)

# # ── Delete user (Admin only) ──────────────────────────────────
# @router.delete("/users/{user_id}")
# def remove_user(
#     user_id: int,
#     db: Session = Depends(get_db),
#     _: dict = Depends(admin_only)
# ):
#     user = delete_user(db, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return {"message": "User deleted successfully"}

# # ── Get current logged-in user ────────────────────────────────
# @router.get("/me", response_model=UserResponse)
# def get_me(current_user=Depends(get_current_user)):
#     return current_user

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user import UserCreate, UserLogin, UserResponse, TokenResponse
from app.services.auth_service import (
    create_user, get_user_by_username,
    verify_password, create_access_token,
    get_all_users, delete_user
)

router = APIRouter()

# ── Login ─────────────────────────────────────────────────────
@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token({"sub": db_user.username, "role": db_user.role})
    return {
        "access_token" : token,
        "token_type"   : "bearer",
        "role"         : db_user.role,
        "full_name"    : db_user.full_name
    }

# ── Register ──────────────────────────────────────────────────
@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    return create_user(db, user)

# ── Get all users ─────────────────────────────────────────────
@router.get("/users", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return get_all_users(db)

# ── Delete user ───────────────────────────────────────────────
@router.delete("/users/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

# ── Get all users ─────────────────────────────────────────────
@router.get("/me", response_model=UserResponse)
def get_me(db: Session = Depends(get_db)):
    return get_all_users(db)[0]