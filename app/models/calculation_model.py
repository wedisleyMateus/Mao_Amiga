from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

from app.infrastructure.conection import Base

class Calculation(Base):
    __tablename__ = 'calculation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    service_id = Column(Integer, ForeignKey('service.id'))
    client_id = Column(Integer, ForeignKey('client.id'))
    value = Column(Numeric(10, 2), nullable=False)
    squad_value = Column(Numeric(10, 2), nullable=False)
    total = Column(Numeric(10, 2), nullable=False)

    client = relationship('Client', backref='calculations')
    service = relationship('Service', backref='calculations')

