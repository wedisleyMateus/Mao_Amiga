from sqlalchemy.orm import Session
from app.models.login_model import Login
from app.schemas.login_schema import LoginRegisterResponse, TokenResponse
from auth import hashed_password, verify_password, creat_access_token


class LoginRepository:
    def __init__(self, db: Session):
        self.db = db


    def create_register(self, data):
        hash_pw = hashed_password(data.password)
        account = Login(username=data.username, password=hash_pw)
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)
        return LoginRegisterResponse.model_validate(account)


    def get_login(self, data):
        account = self.db.query(Login).filter(Login.username == data.username).first()
        verify_password(data.password, account.password)

        token = creat_access_token({"sub": account.username})
        return TokenResponse(access_token=token, token_type="bearer")

