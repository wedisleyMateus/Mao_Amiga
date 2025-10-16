from typing import List
from sqlalchemy.orm import Session
from app.repositories.service_repository import RepositoryCRUD
from app.models.service_model import Service
from app.schemas.service_schema import (
    ServiceSchema,
    ServiceVerificationSchema
)


class ServiceNotFoundError(Exception):
    pass


class ServiceAlreadyExistsError(Exception):
    pass


class ServiceListEmptyError(Exception):
    pass


class ServiceManager:
    def __init__(self, db: Session):
        self.repository = RepositoryCRUD(db)


    def _get_or_raise(self, name: str) -> Service:
        service = self.repository.get_by_name(name)
        if not service:
            raise ServiceNotFoundError()
        return service


    def create_service(self, data: ServiceVerificationSchema) -> ServiceSchema:
        existing = self.repository.get_by_name(data.name)
        if existing:
            raise ServiceAlreadyExistsError()
        created = self.repository.create(data)
        return created


    def get_all_services(self) -> List[ServiceSchema]:
        list_services_existing = self.repository.get_services()
        if not list_services_existing:
            raise ServiceListEmptyError()
        return [ServiceSchema.model_validate(service)
                for service in list_services_existing]


    def get_service(self, name: str) -> ServiceSchema:
        existing = self._get_or_raise(name)
        return ServiceSchema.model_validate(existing)


    def update_service(self, data: ServiceSchema) -> ServiceSchema:
        service = self._get_or_raise(data.name)
        updated = self.repository.update(service, data)
        return updated


    def delete_service(self, name: str) -> dict[str, str]:
        service = self._get_or_raise(name)
        self.repository.delete(service)
        return {"message": "Service deleted"}
