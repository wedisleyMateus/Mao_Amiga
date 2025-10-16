from fastapi import Depends, APIRouter, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas.service_schema import (
    ServiceRequest,
    ServiceResponse,
    ServiceVerificationSchema,
)
from app.services.service import SrvService
from app.infrastructure.conection import get_db
from auth import verify_token
from app.core.logger_config import logger

router = APIRouter(prefix="/v1/services", tags=["Services"])


@router.post(
    "/create", response_model=ServiceResponse, status_code=status.HTTP_201_CREATED
)
def create_service(
    data: ServiceVerificationSchema,
    db: Session = Depends(get_db),
    user_id: int = Depends(verify_token),
) -> ServiceResponse:
    service = SrvService(db)
    result = service.create_service(data)
    logger.info(f"Service {data.name} successfully registered by user {user_id}")
    return result


@router.get("/", response_model=List[ServiceResponse])
def get_services(
    db: Session = Depends(get_db), user_id: int = Depends(verify_token)
) -> List[ServiceResponse]:
    services = SrvService(db)
    result = services.get_all_services()
    logger.info(f"List found with values by user {user_id}")
    return result


@router.get("/{service_name}", response_model=ServiceResponse)
def get_service(
    service_name: str,
    db: Session = Depends(get_db),
    user_id: int = Depends(verify_token),
) -> ServiceResponse:
    service = SrvService(db)
    result = service.get_service(service_name)
    logger.info(f"Service '{service_name}' retrieved successfully by user {user_id}")
    return result


@router.put("/{service_name}", response_model=ServiceResponse)
def update_service(
    service_name: str,
    data: ServiceRequest,
    db: Session = Depends(get_db),
    user_id: int = Depends(verify_token),
) -> ServiceResponse:
    service = SrvService(db)
    result = service.update_service(data)
    logger.info(f"Service '{service_name}' updated successfully by user {user_id}")
    return result


@router.delete("/{service_name}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service(
    service_name: str,
    db: Session = Depends(get_db),
    user_id: int = Depends(verify_token),
):
    service = SrvService(db)
    result = service.delete_service(service_name)
    logger.info(f"Service '{service_name}' deleted successfully by user {user_id}")
    return result
