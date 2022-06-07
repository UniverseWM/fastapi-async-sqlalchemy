from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://admin:admin@localhost:5432/fastapi"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
