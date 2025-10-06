from sqlalchemy import Column, String, Integer
from app.core.database import Base


class Clients(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    telephone = Column(String(30), nullable=False)
    address = Column(String(200), nullable=True)
