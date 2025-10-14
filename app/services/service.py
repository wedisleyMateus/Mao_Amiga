from decimal import Decimal
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.service_model import Service
from app.repositories.service_repository import ServiceRepository
from app.schemas import (
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
    def __init__(self, db: AsyncSession):
        self.repository = ServiceRepository(db)


    async def create_service(self, data: ServiceVerificationSchema) -> ServiceSchema:
        existing = await self.repository.get_by_name(data.name)
        if existing:
            raise ServiceAlreadyExistsError()
        service = Service(**data.model_dump())
        created = await self.repository.create(service)
        return ServiceSchema.model_validate(created)


    async def get_all_services(self) -> List[ServiceSchema]:
        list_services_existing = await self.repository.get_services()
        if not list_services_existing:
            raise ServiceListEmptyError()
        return [ServiceSchema.model_validate(service)
                for service in list_services_existing]


    async def get_service(self, name: str) -> ServiceSchema:
        existing = await self.repository.get_by_name(name)
        if not existing:
            raise ServiceNotFoundError()
        return ServiceSchema.model_validate(existing)


    async def update_service(self, data: ServiceSchema) -> ServiceSchema:
        service = await self.repository.get_by_name(data.name)
        if not service:
            raise ServiceNotFoundError()
        service.name = data.name
        service.value = data.value
        updated = await self.repository.update(service)
        return ServiceSchema.model_validate(updated)


    async def delete_service(self, name: str) -> ServiceSchema:
        service = await self.repository.get_by_name(name)
        if not service:
            raise ServiceNotFoundError()
        delete = await self.repository.delete(service)
        return ServiceSchema.model_validate(delete)


class ServiceCalculator:
    def __init__(self, db: AsyncSession):
        self.repository = ServiceRepository(db)

    async def calculate_service_total(self, data: ServiceCalculationRequest):

        service = await self.repository.get_by_name(data.name)
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