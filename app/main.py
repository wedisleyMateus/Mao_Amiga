from fastapi import FastAPI
from schemas.services import TypeService

app = FastAPI()


@app.post("/service")
async def service(post_service: TypeService):
    return post_service
