from fastapi import Depends, APIRouter, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas.service_schema import (
    TypeServiceSchema,
    TypeServiceVerificationSchema,
)
from app.repositories.service_repository import (
    create_type_service,
    get_type_service,
    update_type_service,
    delete_type_service,
    get_all_service,
)
from app.core.database import get_db


router = APIRouter(prefix="/services", tags=["Services"])


@router.post("/", response_model=TypeServiceSchema, status_code=status.HTTP_201_CREATED)
async def create_service(
    service: TypeServiceVerificationSchema, db: Session = Depends(get_db)
) -> TypeServiceSchema:
    return create_type_service(service, db)


@router.get("/", response_model=List[TypeServiceSchema])
async def get_services(db: Session = Depends(get_db)) -> List[TypeServiceSchema]:
    return get_all_service(db)


@router.get("/{service_name}", response_model=TypeServiceSchema)
async def get_service(
    service_name: str, db: Session = Depends(get_db)
) -> TypeServiceSchema:
    return get_type_service(service_name, db)


@router.put("/{service_name}", response_model=TypeServiceSchema)
async def update_service(
    service_name: str,
    service: TypeServiceVerificationSchema,
    db: Session = Depends(get_db),
) -> TypeServiceSchema:
    return update_type_service(service_name, service, db)


@router.delete("/{service_name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_service(service_name: str, db: Session = Depends(get_db)):
    return delete_type_service(service_name, db)
