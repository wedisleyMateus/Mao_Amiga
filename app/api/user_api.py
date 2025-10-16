from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.login_schema import (
    LoginRegisterResponse,
    LoginRegisterRequest,
    TokenResponse,
)
from app.infrastructure.conection import get_db
from app.repositories.user_repository import UserRepositoryCRUD
from app.core.logger_config import logger


router = APIRouter(prefix="/login", tags=["login"])


@router.post("", response_model=TokenResponse)
def login(data: LoginRegisterRequest, db: Session = Depends(get_db)):
    login_in = UserRepositoryCRUD(db)
    result = login_in.get_by_name(data)
    if result is None:
        raise HTTPException(status_code=404, detail="Login failed")
    logger.info("The login was successful")
    return result


@router.post("/register", response_model=LoginRegisterResponse)
def login_register(
    data: LoginRegisterRequest, db: Session = Depends(get_db)
) -> LoginRegisterResponse:
    login_repository = UserRepositoryCRUD(db)
    result = login_repository.create(data)
    logger.info("User registered successfully")
    return result
