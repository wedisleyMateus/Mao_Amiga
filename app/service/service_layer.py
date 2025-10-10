from decimal import Decimal
from sqlalchemy.orm import Session
from app.repositories.service_repository import (
    ServiceBase,
    CreateService,
    GetAllServices,
)
from app.schemas.service_schema import (
    ServiceSchema,
    ServiceCalculationRequest,
    ServiceCalculationResponse,
)


class ServiceNotFoundError(Exception):
    pass


class ServiceAlreadyExistsError(Exception):
    pass


class ServiceListEmptyError(Exception):
    pass


class  ServiceCreator:
    def __init__(self, db: Session):
        self.verification = ServiceBase(db)
        self.repository = CreateService(db)

    def existence_verification(self, data: ServiceSchema):
        if self.verification.query_service(data.name):
            raise ServiceAlreadyExistsError()
        else:
            return self.repository.create_service(data)


class ServiceLister:
    def __init__(self, db: Session):
        self.repository = GetAllServices(db)


    def list_verification(self):
        list_service = self.repository.get_all_services()
        if not list_service:
            raise ServiceNotFoundError()
        else:
            return list_service


class ServiceCalculator:
    def __init__(self, db: Session):
        self.verification = ServiceBase(db)
        self.repository = CreateService(db)

    def calculate_service_total(self, data: ServiceCalculationRequest):

        service = self.verification.query_service(data.name)
        if service is None:
            raise ServiceNotFoundError()
        else:
            calculation = service.service_value * Decimal(str(data.square_meter))
            return ServiceCalculationResponse(
                name=service.name,
                service_value=service.service_value,
                square_meter=data.square_meter,
                total=calculation,
            )
