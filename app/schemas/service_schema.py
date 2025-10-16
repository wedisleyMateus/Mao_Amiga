from pydantic import BaseModel, field_validator


class ServiceRequest(BaseModel):
    id: int
    name: str
    value: float

class ServiceResponse(BaseModel):
    id: int
    name: str
    value: float

    class Config:
        from_attributes = True


class ServiceVerificationSchema(BaseModel):
    name: str
    value: float

    @field_validator("name", mode="before")
    @classmethod
    def verification_name(cls, v):
        if isinstance(v, int):
            raise ValueError("Valor não Aceito")
        elif isinstance(v, float):
            raise ValueError("Valor não Aceito")
        else:
            return v
