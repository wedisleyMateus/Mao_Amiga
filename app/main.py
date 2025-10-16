from fastapi import FastAPI
from app.api import client_api, user_api, service_api, calculation_api
from app.core.handlers import (
    service_already_exists_handler,
    service_list_handler,
    service_not_found_handler
)
from app.core.exceptions.service import (
    ServiceAlreadyExistsError,
    ServiceNotFoundError,
    ServiceListEmptyError
)

app = FastAPI()

app.add_exception_handler(ServiceAlreadyExistsError, service_already_exists_handler)
app.add_exception_handler(ServiceNotFoundError, service_not_found_handler)
app.add_exception_handler(ServiceListEmptyError, service_list_handler)

app.include_router(service_api.router)
app.include_router(client_api.router)
app.include_router(user_api.router)
app.include_router(calculation_api.router)
