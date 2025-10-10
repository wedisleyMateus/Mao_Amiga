from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.login_schema import (
    LoginRegisterResponse,
    LoginRegisterRequest,
    TokenResponse,
)
from app.core.database import get_db
from app.repositories.login_repository import LoginRepository
from app.logger_config import logger


router = APIRouter(prefix="/login", tags=["login"])


@router.post("", response_model=TokenResponse)
async def login(data: LoginRegisterRequest, db: Session = Depends(get_db)):
    login_in = LoginRepository(db=db)
    result = login_in.get_login(data)
    if result is None:
        raise HTTPException(status_code=404, detail="Login failed")
    logger.info("The login was successful")
    return result


@router.post("/register", response_model=LoginRegisterResponse)
async def login_register(
    data: LoginRegisterRequest, db: Session = Depends(get_db)
) -> LoginRegisterResponse:
    login_repository = LoginRepository(db)
    result = login_repository.get_login(data)
    logger.info("User registered successfully")
    return result
