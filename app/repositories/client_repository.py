from app.models.client_model import Clients
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


class ClientRepository:
    def __init__(self, db: AsyncSession):
        self.db = db


    async def create(self, client: Clients) -> Clients:
        self.db.add(client)
        await self.db.commit()
        await self.db.refresh(client)
        return client


    async def get_by_name(self, name: str) -> Clients:
        result = await self.db.execute(select(Clients).filter(Clients.name == name))
        return result.scalar_one_or_none()


    async def update(self, client: Clients) -> Clients:
        await self.db.commit()
        await self.db.refresh(client)


    async def delete(self, client: Clients) -> Clients:
        await self.db.delete(client)
        await self.db.commit()
