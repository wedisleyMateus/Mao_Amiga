from decimal import Decimal
from typing import List
from sqlalchemy.orm import Session
from app.models.service_model import Service
from app.repositories.service_repository import ServiceRepository
from app.schemas.service_schema import (
    ServiceSchema,
    ServiceVerificationSchema,
    ServiceCalculationRequest,
    ServiceCalculationResponse,
)


class ServiceNotFoundError(Exception):
    pass


class ServiceAlreadyExistsError(Exception):
    pass


class ServiceListEmptyError(Exception):
    pass


class ServiceManager:
    def __init__(self, db: Session):
        self.repository = ServiceRepository(db)


    def create_service(self, data: ServiceVerificationSchema) -> ServiceSchema:
        existing = self.repository.get_by_name(data.name)
        if existing:
            raise ServiceAlreadyExistsError()
        service = Service(**data.model_dump())
        created = self.repository.create(service)
        return ServiceSchema.model_validate(created)


    def get_all_services(self) -> List[ServiceSchema]:
        list_services_existing = self.repository.get_services()
        if not list_services_existing:
            raise ServiceListEmptyError()
        return [ServiceSchema.model_validate(service)
                for service in list_services_existing]


    def get_service(self, name: str) -> ServiceSchema:
        existing = self.repository.get_by_name(name)
        if not existing:
            raise ServiceNotFoundError()
        return ServiceSchema.model_validate(existing)


    def update_service(self, data: ServiceSchema) -> ServiceSchema:
        service = self.repository.get_by_name(data.name)
        if not service:
            raise ServiceNotFoundError()
        service.name = data.name
        service.value = data.value
        updated = self.repository.update(service)
        return ServiceSchema.model_validate(updated)


    def delete_service(self, name: str) -> dict[str, str]:
        service = self.repository.get_by_name(name)
        if not service:
            raise ServiceNotFoundError()
        self.repository.delete(service)
        return {"message": "Service deleted"}


class ServiceCalculator:
    def __init__(self, db: Session):
        self.repository = ServiceRepository(db)

    def calculate_service_total(self, data: ServiceCalculationRequest):

        service = self.repository.get_by_name(data.name)
        if not service:
            raise ServiceNotFoundError()
        else:
            calculation = service.value * Decimal(str(data.square_meter))
            return ServiceCalculationResponse(
                name=service.name,
                service_value=service.value,
                square_meter=data.square_meter,
                total=calculation,
            )