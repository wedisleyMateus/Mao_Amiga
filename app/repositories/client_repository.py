from app.domain.models.client_model import Clients
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.logger_config import logger


class ClientRepository:
    def __init__(self, db: AsyncSession):
        self.db = db


    async def create(self, client: Clients) -> Clients:
        logger.info("Starting client creation process")
        self.db.add(client)
        await self.db.commit()
        await self.db.refresh(client)
        logger.info(f"Client {client.name} successfully created")
        return client


    async def get_by_name(self, name: str) -> Clients:
        logger.info("starting the process of finding a client")
        result = await self.db.execute(select(Clients).filter(Clients.name == name))
        logger.info(f"Found client {name} with id {result.scalar()}")
        return result.scalar_one_or_none()


    async def update(self, client: Clients) -> Clients:
        logger.info(f"Starting update process for client id={client.id}")
        await self.db.commit()
        await self.db.refresh(client)
        logger.info(f"Client id={client.id} successfully updated")
        return client


    async def delete(self, client: Clients) -> None:
        logger.info(f"Starting delete process for client id={client.id}")
        await self.db.delete(client)
        await self.db.commit()
        logger.indo("Delete with successfully deleted")

