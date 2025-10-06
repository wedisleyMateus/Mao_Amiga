from pydantic import BaseModel


class ClientCreate(BaseModel):
    name: str
    email: str
    telephone: str
    address: str


class ClientRead(BaseModel):
    id: int
    name: str
    email: str
    telephone: str
    address: str

    class Config:
        from_attributes = True
