from sqlalchemy.orm import Session
from app.models.client_model import Client
from app.schemas.client_schema import ClientCreate, ClientRead
from app.repositories.client_repository import ClientRepositoryCRUD
from app.core.exceptions.client import ClientNotFoundError


class SrvClient:
    def __init__(self, db: Session):
        self.client_repo = ClientRepositoryCRUD(db)


    def _get_or_raise(self, name: str) -> Client:
        client = self.client_repo.get_by_name(name)
        if not client:
            raise ClientNotFoundError(name=name)
        return client


    def create_client(self, data: ClientCreate) -> ClientRead:
        self.client_repo.get_by_name(data.name)
        create = self.client_repo.create(data)
        return ClientRead.model_validate(create)


    def get_client(self, name: str) -> ClientRead:
        client = self._get_or_raise(name)
        return ClientRead.model_validate(client)


    def update_client(self, name: str, data: ClientCreate) -> ClientRead:
        client = self._get_or_raise(name)
        update = self.client_repo.update(client, data)
        return ClientRead.model_validate(update)


    def delete_client(self, name: str ) -> None:
        client = self._get_or_raise(name)
        self.client_repo.delete(client)
        return None
