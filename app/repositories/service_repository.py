from sqlalchemy.orm import Session
from app.models.service_model import TypeService
from app.schemas.service_schema import ServiceSchema


class ServiceRepository:
    def __init__(self, db: Session):
        self.db = db

    def service_verification(self, data):
        return self.db.query(TypeService).filter(TypeService.name == data).first()

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
        service = self.service_verification(service_name)
        return service

    def update_service(self, service_name, service):
        get_service = self.service_verification(service_name)
        get_service.name = service.name
        get_service.service_value = service.service_value
        self.db.commit()
        self.db.refresh(get_service)
        return get_service

    def delete_service(self, service_name):
        get_service = self.service_verification(service_name)
        self.db.delete(get_service)
        self.db.commit()
