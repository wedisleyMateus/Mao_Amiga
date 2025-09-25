from typing import Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models import TypeService


def service_verification(service, db: Session):
    return db.query(TypeService).filter(TypeService.name == service.name).first()


def create_type_service(service, db: Session):
    if service_verification(service, db):
        return HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Serviço já Existente"
        )
    else:
        type_service = TypeService(
            name=service.name, service_value=service.service_value
        )
        db.add(type_service)
        db.commit()
        db.refresh(type_service)
        return HTTPException(
            status_code=status.HTTP_201_CREATED,
            detail="Serviço Registrado com Sucesso!",
        )


def get_type_service(service_id, db: Session) -> Optional[int]:
    service = db.query(TypeService).filter(TypeService.id == service_id).first()
    return service


def update_type_service(service_id, service, db: Session):
    get_service = db.query(TypeService).filter(TypeService.id == service_id).first()
    get_service.name = service.name
    get_service.service_value = service.service_value
    db.commit()
    db.refresh(get_service)
    return get_service


def delete_type_service(service_id, db: Session):
    get_service = db.query(TypeService).filter(TypeService.id == service_id).first()
    db.delete(get_service)
    db.commit()
    return {"message": "Item deleted successfully!"}
