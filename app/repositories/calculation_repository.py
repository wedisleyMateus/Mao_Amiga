from sqlalchemy.orm import Session
from app.schemas.calculation_schema import CalculationResponse
from app.models.calculation_model import Calculation


class CalculationRepositoryBase:
    def __init__(self, db: Session):
        self.db = db


class CalculationRepositoryCreate(CalculationRepositoryBase):
    def create(self, corpo) -> CalculationResponse:
        calculation_obj = Calculation(
            service_id=corpo.service_id,
            client_id=corpo.client,
            value=corpo.service_value,
            squad_value=corpo.square_meter,
            total=corpo.tota
        )
        self.db.add(calculation_obj)
        self.db.commit()
        self.db.refresh(calculation_obj)
        return CalculationResponse.model_validate(calculation_obj)


class CalculationRepositoryCRUD(
    CalculationRepositoryCreate,
):
    pass
