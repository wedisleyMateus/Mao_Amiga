from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Clients
from app.schemas import ClientCreate, ClientRead
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
        create = await self.repository.create(client)
        return ClientRead.model_validate(create)


    async def get_client(self, name: str) -> ClientRead:
        client = await self.repository.get_by_name(name)
        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Client not found"
            )
        return ClientRead.model_validate(client)


    async def update_client(self, name: str, data: ClientCreate) -> ClientRead:
        client = await self.repository.get_by_name(name)
        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Client not found"
            )
        client.name = data.name
        client.email = data.email
        client.telephone = data.telephone
        client.address = data.address
        update = await self.repository.update(client)
        return ClientRead.model_validate(update)


    async def delete_client(self, name: str ) -> ClientRead:
        client = await self.repository.get_by_name(name)
        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Client not found"
            )
        delete = await self.repository.delete(client)
        return ClientRead.model_validate(delete)
