from decimal import Decimal
from sqlalchemy.orm import Session
from app.repositories.service_repository import RepositoryCRUD
from app.repositories.calculation_repository import RepositoryCreate
from app.schemas.calculation_schema import CalculationRequest, CalculationOjb
from app.services.service import ServiceNotFoundError


class ServiceCalculator:
    def __init__(self, db: Session):
        self.repository = RepositoryCRUD(db)
        self.repository_calc = RepositoryCreate(db)
        self.db = db

    def calculate_service_total(self, data: CalculationRequest):
        service = self.repository.get_by_name(data.name)

        if not service:
            raise ServiceNotFoundError()


        total = service.value * Decimal(str(data.square_meter))

        corpo =  CalculationOjb(
            service_id=service.id,
            client_id=data.client_idt,
            service_value=service.value,
            square_meter=data.square_meter,
            total=total,
        )
        result = self.repository_calc.create(corpo)
        return result

