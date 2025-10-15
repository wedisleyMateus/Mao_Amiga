from decimal import Decimal

from pydantic import BaseModel


class CalculationRequest(BaseModel):
    name: int
    client: int
    square_meter: Decimal


class CalculationResponse(BaseModel):
    name: int
    client: int
    service_value: Decimal
    square_meter: Decimal
    total: Decimal

    class Config:
        from_attributes = True