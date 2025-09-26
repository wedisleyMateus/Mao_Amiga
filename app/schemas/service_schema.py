from pydantic import BaseModel, field_validator


class TypeServiceSchema(BaseModel):
    id: int
    name: str
    service_value: float

    class Config:
        from_attributes = True


class TypeServiceVerificationSchema(BaseModel):
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
