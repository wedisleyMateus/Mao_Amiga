from sqlalchemy import Column, String, Integer, Numeric
from app.core.database import Base


class Service(Base):
    __tablename__ = "service"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    value = Column(Numeric(10, 2), nullable=False)
