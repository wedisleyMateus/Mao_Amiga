from fastapi import FastAPI
from app.api import client_api, login_api, service_api, calculation

app = FastAPI()

app.include_router(service_api.router)
app.include_router(client_api.router)
app.include_router(login_api.router)
app.include_router(calculation.router)
