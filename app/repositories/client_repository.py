from app.models.client_model import Clients
from sqlalchemy.orm import Session
from app.core.logger_config import logger
from app.schemas.client_schema import ClientRead


class RepositoryBase:
    def __init__(self, db: Session):
        self.db = db

    def _save(self, obj):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj


class RepositoryCreate(RepositoryBase):
    def create(self, data) -> ClientRead:
        client = Clients(
            name=data.name,
            email=data.email,
            telephone=data.telephone,
            address=data.address
        )
        logger.info("Starting client creation process")
        self._save(client)
        logger.info(f"Client {client.name} successfully created")
        return ClientRead.model_validate(client)


class RepositoryRetrieveByName(RepositoryBase):
    def get_by_name(self, name: str) -> Clients | None:
        logger.info("starting the process of finding a client")
        client = self.db.query(Clients).filter(Clients.name == name).first()
        logger.info(f"Found client {name} with id {client.id}")
        return client


class RepositoryUpdate(RepositoryBase):
    def update(self, client, data) -> ClientRead:
        client.name = data.name
        client.email = data.email
        client.telephone = data.telephone
        client.address = data.address
        logger.info(f"Starting update process for client id={client.id}")
        self._save(client)
        logger.info(f"Client id={client.id} successfully updated")
        return ClientRead.model_validate(client)


class RepositoryDelete(RepositoryBase):
    def delete(self, client)-> None:
        logger.info(f"Starting delete process for client id={client.id}")
        self.db.delete(client)
        self.db.commit()
        logger.indo("Delete with successfully deleted")


class RepositoryCRUD(
    RepositoryCreate,
    RepositoryRetrieveByName,
    RepositoryUpdate,
    RepositoryDelete
):
    pass