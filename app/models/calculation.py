from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.infrastructure.conection import Base

class CalculationRecord(Base):
    __tablename__ = 'calculation_record'
    id = Column(Integer, primary_key=True, autoincrement=True)
    service_id = Column(Integer, ForeignKey('service.id'))
    client_id = Column(Integer, ForeignKey('clients.id'))
    value = Column(Integer, nullable=False)
    squad_value = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)

    client = relationship('Client', backref='calculations')

