from sqlalchemy.orm import Session
from sqlalchemy.future import select
from app.models.login_model import Login
from app.schemas.login_schema import LoginRegisterResponse, TokenResponse
from auth import hashed_password, verify_password, creat_access_token
from app.core.logger_config import logger


class LoginRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_register(self, data):
        logger.info("Starting to create a new login")
        hash_pw = hashed_password(data.password)
        account = Login(username=data.username, password=hash_pw)
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)
        logger.info("Login created successfully")
        return LoginRegisterResponse.model_validate(account)

    def get_login(self, data):
        logger.info(f"Trying to authenticate user '{data.username}'")
        query = select(Login).where(Login.username == data.username)
        result = self.db.execute(query)
        account = result.scalar_one_or_none()
        verify_password(data.password, account.password)

        token = creat_access_token({"sub": account.username})
        logger.info("Access token generated successfully")
        return TokenResponse(access_token=token, token_type="bearer")
