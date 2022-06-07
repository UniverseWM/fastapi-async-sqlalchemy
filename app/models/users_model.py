from core.configs import Settings
from sqlalchemy import Boolean, Column, Integer, String


class UserModel(Settings.DBBaseModel):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False, unique=True)
    password: str = Column(String(256), nullable=False)
    active: bool = Column(Boolean, default=True)
