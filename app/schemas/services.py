from pydantic import BaseModel

class TypeService(BaseModel):
    name: str
    service_value: int
