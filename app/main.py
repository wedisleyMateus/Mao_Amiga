from fastapi import FastAPI
from app.api import client_api, user_api, service_api, calculation_api

app = FastAPI()

app.include_router(service_api.router)
app.include_router(client_api.router)
app.include_router(user_api.router)
app.include_router(calculation_api.router)
