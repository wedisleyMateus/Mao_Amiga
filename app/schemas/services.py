from pydantic import BaseModel


class TypeServiceSchema(BaseModel):
    id: int
    name: str
    service_value: float

    class Config:
        from_attributes = True


class TypeServiceVerificationSchema(BaseModel):
    detail: str


class TypeServiceCreateSchema(BaseModel):
    name: str
    service_value: float


class TypeServiceUpdateSchema(BaseModel):
    name: str
    service_value: float
