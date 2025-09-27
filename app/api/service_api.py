from fastapi import Depends, APIRouter, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas.service_schema import (
    ServiceSchema,
    ServiceVerificationSchema,
)
from app.repositories.service_repository import ServiceRepository
from app.service_layer.service_layer import ServiceLayer
from app.core.database import get_db


router = APIRouter(prefix="/services", tags=["Services"])


@router.post(
    "/", response_model=ServiceVerificationSchema, status_code=status.HTTP_201_CREATED
)
async def create_service(
    data: ServiceVerificationSchema, db: Session = Depends(get_db)
) -> ServiceVerificationSchema:
    service = ServiceLayer(db)
    return service.existence_verification(data)


@router.get("/", response_model=List[ServiceSchema])
async def get_services(db: Session = Depends(get_db)) -> List[ServiceSchema]:
    services = ServiceLayer(db)
    return services.list_validation()


@router.get("/{service_name}", response_model=ServiceSchema)
async def get_service(
    service_name: str, db: Session = Depends(get_db)
) -> ServiceSchema:
    services = ServiceRepository(db)
    return services.get_service(service_name)


@router.put("/{service_name}", response_model=ServiceSchema)
async def update_service(
    service_name: str,
    service: ServiceVerificationSchema,
    db: Session = Depends(get_db),
) -> ServiceSchema:
    services = ServiceRepository(db)
    return services.update_service(service_name, service)


@router.delete("/{service_name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_service(service_name: str, db: Session = Depends(get_db)):
    services = ServiceRepository(db)
    return services.delete_service(service_name)
