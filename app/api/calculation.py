from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.schemas.calculation_schema import (
    CalculationRequest,
    CalculationResponse

)
from app.services.service import ServiceCalculator, ServiceNotFoundError
from app.infrastructure.conection import get_db
from auth import verify_token
from app.core.logger_config import logger


router = APIRouter(prefix="/calculation", tags=["Services"])


@router.post("/calculation", response_model=CalculationResponse)
def service_calculation(
    data: CalculationRequest,
    db: Session = Depends(get_db),
    user_id: int = Depends(verify_token),
) -> CalculationResponse:
    service = ServiceCalculator(db)
    try:
        result = service.calculate_service_total(data)
        logger.info(f"Service calculation for '{data.name}' completed successfully")
        return result
    except ServiceNotFoundError:
        logger.warning(f"Service {data.name} not found")
        raise HTTPException(status_code=404, detail="Serviço não encontrado")