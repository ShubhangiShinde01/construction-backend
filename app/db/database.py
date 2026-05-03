# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv
# import os

# load_dotenv()

# DB_SERVER = os.getenv("DB_SERVER")
# DB_NAME   = os.getenv("DB_NAME")
# DB_DRIVER = os.getenv("DB_DRIVER")

# SQLALCHEMY_DATABASE_URL = (
#     f"mssql+pyodbc://@{DB_SERVER}/{DB_NAME}"
#     f"?driver={DB_DRIVER.replace(' ', '+')}"
#     f"&trusted_connection=yes"
# )

# engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



        
# ```

# ---

# ## ✅ Checklist before we start Auth module:
# ```
# ✅ venv activated
# ✅ All packages installed
# ✅ .env file created with DBShindeConstructionCompany
# ✅ database.py updated
# ✅ DBShindeConstructionCompany exists in SSMS
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv
# import os

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")

# print(f"Connecting to: {DATABASE_URL[:50]}...")

# engine = create_engine(DATABASE_URL, echo=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()