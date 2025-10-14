from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.client_schema import ClientCreate, ClientRead
from app.repositories.client_repository import RepositoryCRUD


class ClientNotFound(Exception):
    pass


class ClientService:
    def __init__(self, db: Session):
        self.repository = RepositoryCRUD(db)


    def create_client(self, data: ClientCreate) -> ClientRead:
        existing_client = self.repository.get_by_name(data.name)
        if existing_client:
            raise ClientNotFound()
        create = self.repository.create(data)
        return create


    def get_client(self, name: str) -> ClientRead:
        client = self.repository.get_by_name(name)
        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Client not found"
            )
        return ClientRead.model_validate(client)


    def update_client(self, name: str, data: ClientCreate) -> ClientRead:
        client = self.repository.get_by_name(name)
        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Client not found"
            )
        update = self.repository.update(client, data)
        return update


    def delete_client(self, name: str ) -> dict[str, str]:
        client = self.repository.get_by_name(name)
        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Client not found"
            )
        self.repository.delete(client)
        return {"message": "Client deleted"}
