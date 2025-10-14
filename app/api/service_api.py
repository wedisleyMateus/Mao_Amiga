from fastapi import Depends, APIRouter, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.schemas.service_schema import (
    ServiceSchema,
    ServiceVerificationSchema,
    ServiceCalculationRequest,
    ServiceCalculationResponse,
)
from app.services.service import (
    ServiceManager,
    ServiceCalculator,
    ServiceNotFoundError,
    ServiceAlreadyExistsError,
    ServiceListEmptyError
)
from app.infrastructure.conection import get_db
from auth import verify_token
from app.core.logger_config import logger

router = APIRouter(prefix="/v1/services", tags=["Services"])


@router.post(
    "/", response_model=ServiceSchema, status_code=status.HTTP_201_CREATED
)
def create_service(
    data: ServiceVerificationSchema,
    db: Session = Depends(get_db),
    user_id: int = Depends(verify_token),
) -> ServiceSchema:
    try:
        service = ServiceManager(db)
        result = service.create_service(data)
        logger.info(f"Service {data.name} successfully registered by user {user_id}")
        return result
    except ServiceAlreadyExistsError:
        logger.warning(f"Service {data.name} already exists")
        raise HTTPException(status_code=409, detail="Serviço já Existente")


@router.get("/", response_model=List[ServiceSchema])
def get_services(
    db: Session = Depends(get_db), user_id: int = Depends(verify_token)
) -> List[ServiceSchema]:
    try:
        services = ServiceManager(db)
        result = services.get_all_services()
        logger.info(f"List found with values by user {user_id}")
        return result
    except ServiceListEmptyError:
        logger.warning("The list is currently empty")
        raise HTTPException(status_code=404, detail="Service list is empty")


@router.get("/{service_name}", response_model=ServiceSchema)
def get_service(
    service_name: str,
    db: Session = Depends(get_db),
    user_id: int = Depends(verify_token),
) -> ServiceSchema:
    service = ServiceManager(db)
    result = service.get_service(service_name)
    logger.info(f"Service '{service_name}' retrieved successfully by user {user_id}")
    return result


@router.put("/{service_name}", response_model=ServiceSchema)
def update_service(
    service_name: str,
    data: ServiceSchema,
    db: Session = Depends(get_db),
    user_id: int = Depends(verify_token),
) -> ServiceSchema:
    service = ServiceManager(db)
    result = service.update_service(data)
    logger.info(f"Service '{service_name}' updated successfully by user {user_id}")
    return result


@router.delete("/{service_name}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service(
    service_name: str,
    db: Session = Depends(get_db),
    user_id: int = Depends(verify_token),
):
    service = ServiceManager(db)
    result = service.delete_service(service_name)
    logger.info(f"Service '{service_name}' deleted successfully by user {user_id}")
    return result


@router.post("/calculation", response_model=ServiceCalculationResponse)
def service_calculation(
    data: ServiceCalculationRequest,
    db: Session = Depends(get_db),
    user_id: int = Depends(verify_token),
) -> ServiceCalculationResponse:
    service = ServiceCalculator(db)
    try:
        result = service.calculate_service_total(data)
        logger.info(f"Service calculation for '{data.name}' completed successfully")
        return result
    except ServiceNotFoundError:
        logger.warning(f"Service {data.name} not found")
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
