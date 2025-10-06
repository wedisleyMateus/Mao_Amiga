from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from app.models.service_model import TypeService
from app.schemas.service_schema import ServiceSchema


class VerificationInterface(ABC):
    def __init__(self, db: Session):
        self.db = db

    @abstractmethod
    def service_verification(self, data):
        pass


class ServiceVerificationByName(VerificationInterface):
    def service_verification(self, data):
        return self.db.query(TypeService).filter(TypeService.name == data).first()


class ServiceRepository:
    def __init__(self, db: Session, verification: VerificationInterface):
        self.db = db
        self.verification = verification

    def create_service(self, data):
        type_service = TypeService(name=data.name, service_value=data.service_value)
        self.db.add(type_service)
        self.db.commit()
        self.db.refresh(type_service)
        return ServiceSchema.model_validate(type_service)

    def get_all_service(self):
        all_services = self.db.query(TypeService).all()
        return all_services

    def get_service(self, service_name):
        service = self.verification.service_verification(service_name)
        return service

    def update_service(self, service_name, service):
        get_service = self.verification.service_verification(service_name)
        get_service.name = service.name
        get_service.service_value = service.service_value
        self.db.commit()
        self.db.refresh(get_service)
        return get_service

    def delete_service(self, service_name):
        get_service = self.verification.service_verification(service_name)
        self.db.delete(get_service)
        self.db.commit()
