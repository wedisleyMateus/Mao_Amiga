from decimal import Decimal
from sqlalchemy.orm import Session
from app.repositories.service_repository import ServiceRepositoryCRUD
from app.repositories.calculation_repository import CalculationRepositoryCRUD
from app.schemas.calculation_schema import CalculationRequest, CalculationCreate
from app.services.service import ServiceNotFoundError


class ServiceCalculator:
    def __init__(self, db: Session):
        self.service_repo = ServiceRepositoryCRUD(db)
        self.calculation_repo = CalculationRepositoryCRUD(db)
        self.db = db

    def calculate_service_total(self, data: CalculationRequest):
        service = self.service_repo.get_by_name(data.name)

        if not service:
            raise ServiceNotFoundError()


        total = service.value * Decimal(str(data.square_meter))

        new_calculation =  CalculationCreate(
            service_id=service.id,
            client_id=data.client_idt,
            service_value=service.value,
            square_meter=data.square_meter,
            total=total,
        )
        result = self.calculation_repo.create(new_calculation)
        return result

