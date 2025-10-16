from decimal import Decimal

from pydantic import BaseModel


class CalculationRequest(BaseModel):
    service_name: str
    client_id: int
    square_meter: Decimal


class CalculationOjb(BaseModel):
    service_id: int
    client_id: int
    service_value: Decimal
    square_meter: Decimal
    total: Decimal

class CalculationResponse(BaseModel):
    service_id: int
    client_id: int
    service_value: Decimal
    square_meter: Decimal
    total: Decimal

    class Config:
        from_attributes = True