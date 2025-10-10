from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from app.models.service_model import Service
from app.schemas.service_schema import ServiceSchema


class BaseService(ABC):
    def __init__(self, db: Session):
        self.db = db

    @abstractmethod
    def query_service(self, data):
        pass


class ServiceBase(BaseService):
    def query_service(self, data):
        return self.db.query(Service).filter(Service.name == data).first()


class CreateService:
    def __init__(self, db: Session):
        self.db = db

    def create_service(self, data):
        type_service = Service(name=data.name, value=data.service_value)
        self.db.add(type_service)
        self.db.commit()
        self.db.refresh(type_service)
        return ServiceSchema.model_validate(type_service)


class GetAllServices:
    def __init__(self, db: Session):
        self.db = db

    def get_all_services(self):
        all_services = self.db.query(Service).all()
        return all_services


class GetService(ServiceBase):

    def get_service(self, service_name):
        service = self.query_service(service_name)
        return service


class UpdateService(ServiceBase):

    def update_service(self, service_name, service):
        get_service = self.query_service(service_name)
        get_service.name = service.name
        get_service.service_value = service.service_value
        self.db.commit()
        self.db.refresh(get_service)
        return get_service


class DeleteService(ServiceBase):

    def delete_service(self, service_name):
        get_service = self.query_service(service_name)
        self.db.delete(get_service)
        self.db.commit()
