from typing import List
from sqlalchemy.orm import Session
from app.repositories.service_repository import ServiceRepositoryCRUD
from app.models.service_model import Service
from app.schemas.service_schema import (
    ServiceRequest,
    ServiceResponse,
    ServiceVerificationSchema
)
from app.core.exceptions.service import (
    ServiceNotFoundError,
    ServiceAlreadyExistsError,
    ServiceListEmptyError,
)


class SrvService:
    def __init__(self, db: Session):
        self.service_repo = ServiceRepositoryCRUD(db)


    def _get_or_raise(self, name: str) -> Service:
        service = self.service_repo.get_by_name(name)
        if not service:
            raise ServiceNotFoundError(service_name=name)
        return service


    def create_service(self, data: ServiceVerificationSchema) -> ServiceResponse:
        existing = self.service_repo.get_by_name(data.name)
        if existing:
            raise ServiceAlreadyExistsError(service_name=data.name)
        created = self.service_repo.create(data)
        return ServiceResponse.model_validate(created)


    def get_all_services(self) -> List[ServiceResponse]:
        list_services_existing = self.service_repo.get_services()
        if not list_services_existing:
            raise ServiceListEmptyError()
        return [ServiceResponse.model_validate(service)
                for service in list_services_existing]


    def get_service(self, name: str) -> ServiceResponse:
        existing = self._get_or_raise(name)
        return ServiceResponse.model_validate(existing)


    def update_service(self, data: ServiceRequest) -> ServiceResponse:
        service = self._get_or_raise(data.name)
        updated = self.service_repo.update(service, data)
        return ServiceResponse.model_validate(updated)


    def delete_service(self, name: str) -> dict[str, str]:
        service = self._get_or_raise(name)
        self.service_repo.delete(service)
        return {"message": "Service deleted"}
