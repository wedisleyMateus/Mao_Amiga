from fastapi import FastAPI
from .api import service_api

app = FastAPI()

app.include_router(service_api.router)
