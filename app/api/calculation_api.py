
from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.calculation_schema import (
    CalculationRequest,
    CalculationResponse

)
from app.services.service import ServiceNotFoundError
from app.services.calculation import SrvCalculation
from app.infrastructure.conection import get_db
from auth import verify_token
from app.core.logger_config import logger


router = APIRouter(prefix="/calculation", tags=["Services"])


@router.post("", response_model=CalculationResponse)
def create_calculation(
    data: CalculationRequest,
    db: Session = Depends(get_db),
    user_id: int = Depends(verify_token),
) -> CalculationResponse:
    service = SrvCalculation(db)
    try:
        result = service.calculate_service_total(data)
        logger.info(
            f"Calculation for '{data.service_name}' completed successfully"
        )
        return result
    except ServiceNotFoundError:
        logger.warning(f"Service {data.service_name} not found")
        raise HTTPException(status_code=404, detail="Service not found")


@router.delete("/{calculation_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_calculation(
        calculation_id: int,
        db: Session = Depends(get_db),
        _user_id: int = Depends(verify_token)
):
    calc = SrvCalculation(db)
    calc.delete_calculation(calculation_id)