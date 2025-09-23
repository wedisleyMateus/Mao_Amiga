from sqlalchemy import Column, String, Integer, Numeric
from .database import Base

class TypeService(Base):
    __tablename__ = "type_service"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    service_value = Column(Numeric(10, 2), nullable=False)

