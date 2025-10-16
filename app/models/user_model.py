from sqlalchemy import Column, String, Integer
from app.infrastructure.conection import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(30), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
