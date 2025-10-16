from sqlalchemy import Column, ForeignKey, Integer, Numeric

from app.infrastructure.conection import Base

class CalculationRecord(Base):
    __tablename__ = 'calculation_record'
    id = Column(Integer, primary_key=True, autoincrement=True)
    service_id = Column(Integer, ForeignKey('service.id'))
    client_id = Column(Integer, ForeignKey('clients.id'))
    value = Column(Numeric(10, 2), nullable=False)
    squad_value = Column(Numeric(10, 2), nullable=False)
    total = Column(Numeric(10, 2), nullable=False)

    client = relationship('Clients', backref='calculations')

