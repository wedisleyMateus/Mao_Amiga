from sqlalchemy.orm import Session
from app.schemas.calculation_schema import CalculationResponse
from app.models.calculation_model import Calculation


class CalculationRepositoryBase:
    def __init__(self, db: Session):
        self.db = db


class CalculationRepositoryCreate(CalculationRepositoryBase):
    def create(self, new_calculation) -> CalculationResponse:
        calculation_entity = Calculation(
            service_id=new_calculation.service_id,
            client_id=new_calculation.client_id,
            value=new_calculation.service_value,
            squad_value=new_calculation.square_meter,
            total=new_calculation.total
        )
        self.db.add(calculation_entity)
        self.db.commit()
        self.db.refresh(calculation_entity)
        return CalculationResponse.model_validate(calculation_entity )


class CalculationRepositoryCRUD(
    CalculationRepositoryCreate,
):
    pass
