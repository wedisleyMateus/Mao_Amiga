from app.models.client_model import Client
from sqlalchemy.orm import Session
from app.core.logger_config import logger
from app.schemas.client_schema import ClientRead


class ClientRepositoryBase:
    def __init__(self, db: Session):
        self.db = db

    def persist(self, entity):
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity


class ClientRepositoryCreate(ClientRepositoryBase):
    def create(self, data) -> ClientRead:
        client = Client(
            name=data.name,
            email=data.email,
            telephone=data.telephone,
            address=data.address
        )
        logger.info("Starting client creation process")
        self.persist(client)
        logger.info(f"Client {client.name} successfully created")
        return ClientRead.model_validate(client)


class ClientRepositoryRetrieveByName(ClientRepositoryBase):
    def get_by_name(self, name: str) -> Client | None:
        logger.info("starting the process of finding a client")
        client = self.db.query(Client).filter(Client.name == name).first()
        logger.info(f"Found client {name} with id {client.id}")
        return client


class ClientRepositoryUpdate(ClientRepositoryBase):
    def update(self, client, data) -> ClientRead:
        client.name = data.name
        client.email = data.email
        client.telephone = data.telephone
        client.address = data.address
        logger.info(f"Starting update process for client id={client.id}")
        self.persist(client)
        logger.info(f"Client id={client.id} successfully updated")
        return ClientRead.model_validate(client)


class ClientRepositoryDelete(ClientRepositoryBase):
    def delete(self, client)-> None:
        logger.info(f"Starting delete process for client id={client.id}")
        self.db.delete(client)
        self.db.commit()
        logger.indo("Delete with successfully deleted")


class ClientRepositoryCRUD(
    ClientRepositoryCreate,
    ClientRepositoryRetrieveByName,
    ClientRepositoryUpdate,
    ClientRepositoryDelete
):
    pass