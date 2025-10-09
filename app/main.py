from fastapi import FastAPI
from app.api import service_api, client_api, login_api

app = FastAPI()

app.include_router(service_api.router)
app.include_router(client_api.router)
app.include_router(login_api.router)
