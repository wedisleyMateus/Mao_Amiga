from fastapi import FastAPI
from fastapi import Request
from starlette.responses import JSONResponse
from app.core.logger_config import logger
from app.core.handlers.base_handler import generic_error_handler
from app.core.exceptions.client import ClientNotFoundError


def client_not_found_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.warning(f"ClientNotFoundError, path: {request.url.path}")
    return generic_error_handler(request, exc, ClientNotFoundError, 402)

def register_client_handlers(app: FastAPI):
    app.add_exception_handler(ClientNotFoundError, client_not_found_handler)

