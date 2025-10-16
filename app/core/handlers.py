from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.exceptions.service import (
    ServiceAlreadyExistsError,
    ServiceNotFoundError,
    ServiceListEmptyError
)


def generic_error_handler(request, exc, exception_class, status_code) -> JSONResponse:
    if isinstance(exc, exception_class):
        return JSONResponse(
            status_code=status_code,
            content={"message": exc.message}
        )
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )


def service_already_exists_handler(request, exc):
    return generic_error_handler(request, exc, ServiceAlreadyExistsError, 402)


def service_not_found_handler(request: Request, exc: Exception):
    return generic_error_handler(request, exc, ServiceNotFoundError, 402)


def service_list_handler(request: Request, exc: Exception):
    if isinstance(exc, ServiceListEmptyError):
        return JSONResponse(
            status_code=204,
            content={"detail": exc.message}
        )
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )
