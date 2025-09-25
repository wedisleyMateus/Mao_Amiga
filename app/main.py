from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from app.schemas.services import (
    TypeServiceSchema,
    TypeServiceUpdateSchema,
    TypeServiceVerificationSchema,
    TypeServiceCreateSchema,
)
from repositories.type_serveice_repository import (
    create_type_service,
    get_type_service,
    update_type_service,
    delete_type_service,
)
from app.database import get_db

app = FastAPI()


@app.post("/service", response_model=TypeServiceVerificationSchema)
async def create_service(
    service: TypeServiceCreateSchema, db: Session = Depends(get_db)
):
    return create_type_service(service, db)


@app.get("/services/{service_name}", response_model=TypeServiceSchema)
async def get_service(service_name: str, db: Session = Depends(get_db)):
    return get_type_service(service_name, db)


@app.put("/service/{service_id}", response_model=TypeServiceSchema)
async def update_service(
    service_id: int, service: TypeServiceUpdateSchema, db: Session = Depends(get_db)
):
    return update_type_service(service_id, service, db)


@app.delete("/service/{service_id}")
async def delete_service(service_id: int, db: Session = Depends(get_db)):
    return delete_type_service(service_id, db)
