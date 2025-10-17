from sqlalchemy import Column, String, Integer
from app.infrastructure.conection import Base

class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    telephone = Column(String(30), nullable=False)
    address = Column(String(200), nullable=True)
