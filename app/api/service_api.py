from fastapi import Depends, APIRouter, status, HTTPException
from typing import List
import logging
from sqlalchemy.orm import Session
from app.schemas.service_schema import (
    ServiceSchema,
    ServiceVerificationSchema,
    ServiceCalculationRequest,
    ServiceCalculationResponse,
)
from app.repositories.service_repository import (
    ServiceRepository,
    ServiceVerificationByName,
)
from app.service_layer.service_layer import (
    ServiceLayer,
    ServiceNotFoundError,
    ServiceAlreadyExistsError,
    ServiceListEmptyError,
)
from app.core.database import get_db
from auth import verify_token


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/services", tags=["Services"])


@router.post(
    "/", response_model=ServiceVerificationSchema, status_code=status.HTTP_201_CREATED
)
async def create_service(
    data: ServiceVerificationSchema,
    db: Session = Depends(get_db),
    user_id: int = Depends(verify_token)
) -> ServiceVerificationSchema:
    try:
        service = ServiceLayer(db)
        return service.existence_verification(data)
    except ServiceAlreadyExistsError:
        logger.warning(f"Service {data.name} already exists")
        raise HTTPException(status_code=409, detail="Serviço já Existente")


@router.get("/", response_model=List[ServiceSchema])
async def get_services(
        db: Session = Depends(get_db),
        user_id: int = Depends(verify_token)
) -> List[ServiceSchema]:
    try:
        services = ServiceLayer(db)
        return services.list_validation()
    except ServiceListEmptyError:
        raise HTTPException(status_code=404, detail="Service list is empty")


@router.get("/{service_name}", response_model=ServiceSchema)
async def get_service(
    service_name: str,
    db: Session = Depends(get_db),
    user_id: int = Depends(verify_token)
) -> ServiceSchema:
    verification = ServiceVerificationByName(db)
    services = ServiceRepository(db, verification)
    return services.get_service(service_name)


@router.put("/{service_name}", response_model=ServiceSchema)
async def update_service(
    service_name: str,
    service: ServiceVerificationSchema,
    db: Session = Depends(get_db),
    user_id: int = Depends(verify_token)
) -> ServiceSchema:
    verification = ServiceVerificationByName(db)
    services = ServiceRepository(db, verification)
    return services.update_service(service_name, service)


@router.delete("/{service_name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_service(
        service_name: str,
        db: Session = Depends(get_db),
        user_id: int = Depends(verify_token)
):
    verification = ServiceVerificationByName(db)
    services = ServiceRepository(db, verification)
    return services.delete_service(service_name)


@router.post("/calculation", response_model=ServiceCalculationResponse)
async def service_calculation(
    data: ServiceCalculationRequest,
    db: Session = Depends(get_db),
    user_id: int = Depends(verify_token)
) -> ServiceCalculationResponse:
    service = ServiceLayer(db)
    try:
        return service.calculate_service_total(data)
    except ServiceNotFoundError:
        logger.warning(f"Service {data.name} not found")
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
