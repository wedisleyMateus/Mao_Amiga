from pydantic import BaseModel

class TypeServiceSchema(BaseModel):
    name: str
    service_value: float

    class Config:
        from_attributes = True
