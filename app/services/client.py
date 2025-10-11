from sqlalchemy.ext.asyncio import AsyncSession
from app.models.client_model import Clients
from app.schemas.client_schema import ClientCreate, ClientRead
from app.repositories.client_repository import ClientRepository


class ClientNotFound(Exception):
    pass


class ClientService:
    def __init__(self, db: AsyncSession):
        self.repository = ClientRepository(db)


    async def create_client(self, data: ClientCreate) -> ClientRead:
        existing_client =  await self.repository.get_by_name(data.name)
        if existing_client:
            raise ClientNotFound()
        client = Clients(**data.model_dump())
        create = self.repository.create(client)
        return ClientRead.model_validate(create)
