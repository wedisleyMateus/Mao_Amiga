from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.service_models import TypeService


def service_verification(service, db: Session):
    return db.query(TypeService).filter(TypeService.name == service.name).first()


def get_service_name(service_name, db: Session):
    while True:
        try:
            if int(service_name):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail="Valor não aceito"
                )
        except ValueError:
            try:
                if float(service_name):
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Valor não aceito",
                    )
            except ValueError:
                break
    return db.query(TypeService).filter(TypeService.name == service_name).first()


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


def get_all_service(db: Session):
    all_services = db.query(TypeService).all()
    if all_services is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Lista de Serviço Vazia!!!"
        )
    else:
        return all_services


def get_type_service(service_name, db: Session):
    service = get_service_name(service_name, db)
    if service is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Serviço Inexistente"
        )
    else:
        return service


def update_type_service(service_name, service, db: Session):
    get_service = get_service_name(service_name, db)
    get_service.name = service.name
    get_service.service_value = service.service_value
    db.commit()
    db.refresh(get_service)
    return get_service


def delete_type_service(service_name, db: Session):
    get_service = get_service_name(service_name, db)
    db.delete(get_service)
    db.commit()
    return {"message": "Item deleted successfully!"}
