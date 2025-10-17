from pydantic import BaseModel
from decimal import Decimal


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


class ClientBudgetResponse(BaseModel):
    service_id: int
    client_id: int
    value: Decimal
    squad_value: Decimal
    total: Decimal

    class Config:
        from_attributes = True