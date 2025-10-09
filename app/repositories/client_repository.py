from sqlalchemy.orm import Session
from app.models.client_model import Clients
from app.schemas.client_schema import ClientRead


class ClientRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_client(self, data):
        client = Clients(
            name=data.name,
            email=data.email,
            telephone=data.telephone,
            address=data.address,
        )
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return ClientRead.model_validate(client)

    def get_client(self, client_name):
        client = self.db.query(Clients).filter(Clients.name == client_name).first()
        return client

    def update_client(self, client, client_data):
        client = self.db.query(Clients).filter(Clients.name == client).first()
        client.email = client_data.email
        client.telephone = client_data.telephone
        client.address = client_data.address
        self.db.commit()
        self.db.refresh(client)
        return client

    def detete_client(self, client_name):
        client = self.db.query(Clients).filter(Clients.name == client_name).first()
        self.db.delete(client)
        self.db.commit()
