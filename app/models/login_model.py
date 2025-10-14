from sqlalchemy import Column, String, Integer
from app.infrastructure.conection import Base


class Login(Base):
    __tablename__ = "login"
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(30), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
