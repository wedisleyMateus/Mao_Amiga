from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.core.logger_config import logger
from app.core.exceptions.client import ClientNotFoundError

def generic_client_error_handler(
        request,
        exc,
        exception_class,
        status_code
) -> JSONResponse:
    if isinstance(exc, exception_class):
        return JSONResponse(
            status_code=status_code,
            content={"message": exc.message}
        )
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )

def client_not_found_handler(request, exc):
    logger.warning(f"ClientNotFoundError, path: {request.url.path}")
    return generic_client_error_handler(request, exc, ClientNotFoundError, 402)

def register_client_handlers(app: FastAPI):
    app.add_exception_handler(ClientNotFoundError, client_not_found_handler)

