from sqlalchemy.orm import Session
from app.models.service_model import Service
from app.core.logger_config import logger
from app.schemas.service_schema import ServiceSchema


class RepositoryBase:
    def __init__(self, db: Session):
        self.db = db


class RepositoryCreate(RepositoryBase):
    def create(self, data) -> ServiceSchema:
        service = Service(name=data.name, value=data.value)
        self.db.add(service)
        self.db.commit()
        (self.db.refresh(service))
        logger.info(f"Service '{service.name}' created successfully.")
        return ServiceSchema.model_validate(service)


class RepositoryRetrieveByName(RepositoryBase):
    def get_by_name(self, name: str) -> Service | None:
        logger.info(f"Querying service by name: '{name}'")
        service = self.db.query(Service).filter(Service.name == name).first()
        logger.info(f"Service '{name}' found.")
        return service


class RepositoryRetrieveAll(RepositoryBase):
    def get_services(self):
        logger.info("Fetching all services...")
        services = self.db.query(Service).all()
        logger.info(f"{len(services)} services found.")
        return services


class RepositoryUpdate(RepositoryBase):
    def update(self, service, data) -> ServiceSchema:
        service.name = data.name
        service.value = data.value
        logger.info(f"Updating service: '{service.name}'...")
        self.db.add(service)
        self.db.commit()
        self.db.refresh(service)
        logger.info(f"Service '{service.name}' updated successfully.")
        return service


class RepositoryDelete(RepositoryBase):
    def delete(self, service: Service) -> None:
        logger.info(f"Deleting service: '{service.name}'...")
        self.db.delete(service)
        self.db.commit()
        logger.info(f"Service '{service.name}' deleted successfully.")


class RepositoryCRUD(
    RepositoryCreate,
    RepositoryRetrieveByName,
    RepositoryRetrieveAll,
    RepositoryUpdate,
    RepositoryDelete
):
    pass
