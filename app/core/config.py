from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Construction Management System"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    DB_SERVER: str = os.getenv("DB_SERVER", "SHUBHANGI")
    DB_NAME: str = os.getenv("DB_NAME", "ssms")

settings = Settings()