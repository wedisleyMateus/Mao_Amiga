from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.logger_config import logger
from app.core.exceptions.service import (
    ServiceAlreadyExistsError,
    ServiceNotFoundError,
    ServiceListEmptyError
)


def generic_service_error_handler(
        request,
        exc,
        exception_class,
        status_code
) -> JSONResponse:
    if isinstance(exc, exception_class):
        return JSONResponse(
            status_code=status_code,
            content={"message": exc.message_suffix}
        )
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )


def service_already_exists_handler(request, exc):
    logger.warning(f"ServiceAlreadyExistsError, path: {request.url.path}")
    return generic_service_error_handler(
        request, exc, ServiceAlreadyExistsError, 402
    )


def service_not_found_handler(request: Request, exc: Exception):
    logger.warning(f"ServiceNotFoundError, path: {request.url.path}")
    return generic_service_error_handler(
        request, exc, ServiceNotFoundError, 402
    )


def service_list_handler(request: Request, exc: Exception):
    if isinstance(exc, ServiceListEmptyError):
        logger.warning(f"ServiceListEmptyError, path: {request.url.path}")
        return JSONResponse(
            status_code=204,
            content={"detail": exc.message}
        )
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )

def register_service_handlers(app: FastAPI):
    app.add_exception_handler(
        ServiceAlreadyExistsError, service_already_exists_handler
    )
    app.add_exception_handler(ServiceNotFoundError, service_not_found_handler)
    app.add_exception_handler(ServiceListEmptyError, service_list_handler)
