from sqlalchemy.orm import Session
from app.schemas.calculation_schema import CalculationResponse
from app.models.calculation import CalculationRecord


class RepositoryBase:
    def __init__(self, db: Session):
        self.db = db


class RepositoryCreate(RepositoryBase):
    def create(self, corpo):
        calculation_obj = CalculationRecord(
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
