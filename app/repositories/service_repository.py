from sqlalchemy.future import select
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.service_model import Service


class ServiceRepository:
    def __init__(self, db: AsyncSession):
        self.db = db


    async def create(self, service: Service) -> Service:
        self.db.add(service)
        await self.db.commit()
        await self.db.refresh(service)
        return service


    async def get_by_name(self, name: str) -> Service:
        result = await self.db.execute(select(Service).filter(Service.name == name))
        return result.scalar_one_or_none()


    async def get_services(self) -> List[Service]:
        result = await self.db.execute(select(Service))
        services = list(result.scalars().all())
        return services


    async def update(self, service: Service) -> Service:
        self.db.add(service)
        await self.db.commit()
        await self.db.refresh(service)
        return service


    async def delete(self, service: Service) -> Service:
        await self.db.delete(service)
        await self.db.commit()
