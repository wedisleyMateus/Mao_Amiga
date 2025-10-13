from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.domain.models.service_model import Service
from app.core.logger_config import logger


class ServiceRepository:
    def __init__(self, db: AsyncSession):
        self.db = db


    async def create(self, service: Service) -> Service:
        logger.info(f"Creating a new service: '{service.name}'")
        self.db.add(service)
        await self.db.commit()
        await self.db.refresh(service)
        logger.info(f"Service '{service.name}' created successfully.")
        return service


    async def get_by_name(self, name: str) -> Service:
        logger.info(f"Querying service by name: '{name}'")
        result = await self.db.execute(select(Service).filter(Service.name == name))
        logger.info(f"Service '{name}' found.")
        return result.scalar_one_or_none()


    async def get_services(self) -> Sequence[Service]:
        logger.info("Fetching all services...")
        result = await self.db.execute(select(Service))
        services = result.scalars().all()
        logger.info(f"{len(services)} services found.")
        return services

    async def update(self, service: Service) -> Service:
        logger.info(f"Updating service: '{service.name}'...")
        self.db.add(service)
        await self.db.commit()
        await self.db.refresh(service)
        logger.info(f"Service '{service.name}' updated successfully.")
        return service

    async def delete(self, service: Service) -> None:
        logger.info(f"Deleting service: '{service.name}'...")
        await self.db.delete(service)
        await self.db.commit()
        logger.info(f"Service '{service.name}' deleted successfully.")
