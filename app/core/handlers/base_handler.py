from fastapi import Request
from fastapi.responses import JSONResponse

def generic_error_handler(
        request: Request,
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
