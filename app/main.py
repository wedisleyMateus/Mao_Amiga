from fastapi import FastAPI
from pydantic import BaseModel

class TypeService(BaseModel):
    name: str
    service_value: int

app = FastAPI()


@app.post("/service")
async def service(get_service: TypeService):
    return get_service

