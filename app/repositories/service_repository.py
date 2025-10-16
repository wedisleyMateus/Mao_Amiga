from typing import List
from sqlalchemy.orm import Session
from app.models.service_model import Service
from app.core.logger_config import logger
from app.schemas.service_schema import ServiceSchema


class ServiceRepositoryBase:
    def __init__(self, db: Session):
        self.db = db

    def persist(self, entity):
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity


class ServiceRepositoryCreate(ServiceRepositoryBase):
    def create(self, data) -> ServiceSchema:
        service = Service(name=data.name, value=data.value)
        self.persist(service)
        logger.info(f"Service '{service.name}' created successfully.")
        return ServiceSchema.model_validate(service)


class ServiceRepositoryRetrieveByName(ServiceRepositoryBase):
    def get_by_name(self, name: str) -> Service | None:
        logger.info(f"Querying service by name: '{name}'")
        service = self.db.query(Service).filter(Service.name == name).first()
        logger.info(f"Service '{name}' found.")
        return service


class ServiceRepositoryRetrieveAll(ServiceRepositoryBase):
    def get_services(self) -> List[Service]:
        logger.info("Fetching all services...")
        services = self.db.query(Service).all()
        logger.info(f"{len(services)} services found.")
        return services


class ServiceRepositoryUpdate(ServiceRepositoryBase):
    def update(self, service, data) -> ServiceSchema:
        service.name = data.name
        service.value = data.value
        logger.info(f"Updating service: '{service.name}'...")
        self.persist(service)
        logger.info(f"Service '{service.name}' updated suc  cessfully.")
        return service


class ServiceRepositoryDelete(ServiceRepositoryBase):
    def delete(self, service: Service) -> None:
        logger.info(f"Deleting service: '{service.name}'...")
        self.db.delete(service)
        self.db.commit()
        logger.info(f"Service '{service.name}' deleted successfully.")


class ServiceRepositoryCRUD(
    ServiceRepositoryCreate,
    ServiceRepositoryRetrieveByName,
    ServiceRepositoryRetrieveAll,
    ServiceRepositoryUpdate,
    ServiceRepositoryDelete
):
    pass
