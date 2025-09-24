from typing import Optional
from sqlalchemy.orm import Session

from app.models import TypeService


def create_type_service(service, db: Session):
    type_service = TypeService(name=service.name, service_value=service.service_value)
    db.add(type_service)
    db.commit()
    db.refresh(type_service)
    return type_service

def get_type_service(service_id, db: Session) -> Optional[int]:
    service = db.query(TypeService).filter(TypeService.id==service_id).first()
    return service

def update_type_service(service_id, service, db: Session):
    get_service = db.query(TypeService).filter(TypeService.id==service_id).first()
    get_service.name = service.name
    get_service.service_value = service.service_value
    db.commit()
    db.refresh(get_service)
    return get_service


