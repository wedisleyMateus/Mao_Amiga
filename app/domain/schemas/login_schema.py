from pydantic import BaseModel


class LoginRegisterRequest(BaseModel):
    username: str
    password: str


class LoginRegisterResponse(BaseModel):
    username: str

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
