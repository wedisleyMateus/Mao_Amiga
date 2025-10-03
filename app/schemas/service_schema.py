from pydantic import BaseModel, field_validator


class ServiceSchema(BaseModel):
    id: int
    name: str
    service_value: float

    class Config:
        from_attributes = True


class ServiceVerificationSchema(BaseModel):
    name: str
    service_value: float

    @field_validator("name", mode="before")
    @classmethod
    def verification_name(cls, v):
        if isinstance(v, int):
            raise ValueError("Valor não Aceito")
        elif isinstance(v, float):
            raise ValueError("Valor não Aceito")
        else:
            return v


class ServiceCalculationSchema(BaseModel):
    name: str
    square_meter: float


class ServiceCalculationResponseSchema(BaseModel):
    name: str
    service_value: float
    square_meter: float
    total: float
