from fastapi import FastAPI
from app.api import client_api, user_api, service_api, calculation_api
from app.core.handlers.service_handler import register_service_handlers
from app.core.handlers.client_handler import register_client_handlers

app = FastAPI()

register_service_handlers(app)
register_client_handlers(app)

app.include_router(service_api.router)
app.include_router(client_api.router)
app.include_router(user_api.router)
app.include_router(calculation_api.router)
