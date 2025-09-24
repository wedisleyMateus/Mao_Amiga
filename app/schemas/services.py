from pydantic import BaseModel


class TypeServiceSchema(BaseModel):
    id: int
    name: str
    service_value: float

    class Config:
        from_attributes = True


class TypeServiceUpdateSchema(BaseModel):
    nome: str
    service_value: float
