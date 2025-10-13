from fastapi import Depends, APIRouter, status, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.schemas.service_schema import (
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

router = APIRouter(prefix="/services", tags=["Services"])


@router.post(
    "/", response_model=ServiceSchema, status_code=status.HTTP_201_CREATED
)
async def create_service(
    data: ServiceVerificationSchema,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(verify_token),
) -> ServiceSchema:
    try:
        service = ServiceManager(db)
        result = await service.create_service(data)
        logger.info(f"Service {data.name} successfully registered by user {user_id}")
        return result
    except ServiceAlreadyExistsError:
        logger.warning(f"Service {data.name} already exists")
        raise HTTPException(status_code=409, detail="Serviço já Existente")


@router.get("/", response_model=List[ServiceSchema])
async def get_services(
    db: AsyncSession = Depends(get_db), user_id: int = Depends(verify_token)
) -> List[ServiceSchema]:
    try:
        services = ServiceManager(db)
        result = await services.get_all_services()
        logger.info(f"List found with values by user {user_id}")
        return result
    except ServiceListEmptyError:
        logger.warning("The list is currently empty")
        raise HTTPException(status_code=404, detail="Service list is empty")


@router.get("/{service_name}", response_model=ServiceSchema)
async def get_service(
    service_name: str,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(verify_token),
) -> ServiceSchema:
    service = ServiceManager(db)
    result = await service.get_service(service_name)
    logger.info(f"Service '{service_name}' retrieved successfully by user {user_id}")
    return result


@router.put("/{service_name}", response_model=ServiceSchema)
async def update_service(
    service_name: str,
    data: ServiceSchema,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(verify_token),
) -> ServiceSchema:
    service = ServiceManager(db)
    result = await service.update_service(data)
    logger.info(f"Service '{service_name}' updated successfully by user {user_id}")
    return result


@router.delete("/{service_name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_service(
    service_name: str,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(verify_token),
):
    service = ServiceManager(db)
    result = await service.delete_service(service_name)
    logger.info(f"Service '{service_name}' deleted successfully by user {user_id}")
    return result


@router.post("/calculation", response_model=ServiceCalculationResponse)
async def service_calculation(
    data: ServiceCalculationRequest,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(verify_token),
) -> ServiceCalculationResponse:
    service = ServiceCalculator(db)
    try:
        result = await service.calculate_service_total(data)
        logger.info(f"Service calculation for '{data.name}' completed successfully")
        return result
    except ServiceNotFoundError:
        logger.warning(f"Service {data.name} not found")
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
