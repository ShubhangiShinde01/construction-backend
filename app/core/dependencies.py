# # from fastapi import Depends, HTTPException, status
# # from fastapi.security import OAuth2PasswordBearer
# # from sqlalchemy.orm import Session
# # from app.db.database import get_db
# # from app.services.auth_service import decode_token, get_user_by_username
# # from jose import JWTError

# # oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

# # def get_current_user(
# #     token: str = Depends(oauth2_scheme),
# #     db:    Session = Depends(get_db)
# # ):
# #     credentials_exception = HTTPException(
# #         status_code = status.HTTP_401_UNAUTHORIZED,
# #         detail      = "Could not validate credentials",
# #         headers     = {"WWW-Authenticate": "Bearer"},
# #     )
# #     try:
# #         payload  = decode_token(token)
# #         username = payload.get("sub")
# #         if username is None:
# #             raise credentials_exception
# #     except JWTError:
# #         raise credentials_exception

# #     user = get_user_by_username(db, username)
# #     if user is None:
# #         raise credentials_exception
# #     return user

# # def admin_only(current_user=Depends(get_current_user)):
# #     if current_user.role != "admin":
# #         raise HTTPException(
# #             status_code = status.HTTP_403_FORBIDDEN,
# #             detail      = "Admin access required"
# #         )
# #     return current_user

# from fastapi import Depends, HTTPException, status, Header
# from sqlalchemy.orm import Session
# from app.db.database import get_db
# from app.services.auth_service import decode_token, get_user_by_username
# from jose import JWTError
# from typing import Optional

# def get_current_user(
#     authorization: Optional[str] = Header(None),
#     db: Session = Depends(get_db)
# ):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials"
#     )
#     if not authorization or not authorization.startswith("Bearer "):
#         raise credentials_exception
    
#     token = authorization.split(" ")[1]
    
#     try:
#         payload  = decode_token(token)
#         username = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception

#     user = get_user_by_username(db, username)
#     if user is None:
#         raise credentials_exception
#     return user

# def admin_only(current_user=Depends(get_current_user)):
#     if current_user.role != "admin":
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Admin access required"
#         )
#     return current_user
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User

# No auth validation - returns dummy admin user
def get_current_user(db: Session = Depends(get_db)):
    return db.query(User).filter(User.role == "admin").first()

def admin_only(db: Session = Depends(get_db)):
    return db.query(User).filter(User.role == "admin").first()