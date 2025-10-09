from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.login_schema import LoginRegisterResponse, LoginRegisterRequest, TokenResponse
from app.core.database import get_db
from app.repositories.login_repository import LoginRepository


router = APIRouter(prefix="/login", tags=["login"])


@router.post("", response_model=TokenResponse)
async def login(data: LoginRegisterRequest, db: Session = Depends(get_db)):
    login_in = LoginRepository(db=db)
    return login_in.get_login(data)


@router.post("/register", response_model=LoginRegisterResponse)
async def login_register(data: LoginRegisterRequest, db: Session = Depends(get_db) ) -> LoginRegisterResponse:
    login_repository = LoginRepository(db)
    return login_repository.create_register(data)
