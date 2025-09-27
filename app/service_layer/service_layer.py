from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.service_repository import ServiceRepository
from app.schemas.service_schema import ServiceSchema


class ServiceLayer:
    def __init__(self, db: Session):
        self.repository = ServiceRepository(db)

    def existence_verification(self, data: ServiceSchema):
        if self.repository.service_verification(data.name):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Serviço já Existente"
            )
        else:
            return self.repository.create_service(data)

    def list_validation(self):
        list_service = self.repository.get_all_service()
        if not list_service:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Lista de Serviço Vazia!!!",
            )
        else:
            return list_service
