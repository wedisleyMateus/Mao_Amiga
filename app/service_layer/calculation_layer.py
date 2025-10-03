from decimal import Decimal
from fastapi import HTTPException, status
from app.api.service_api import VerificationWithName
from app.schemas.service_schema import (
    ServiceCalculationSchema,
    ServiceCalculationResponseSchema,
)


def squared_calculation(
    data: ServiceCalculationSchema, verification: VerificationWithName
):
    service = verification.service_verification(data.name)
    if service is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Serviço '{data.name}' não encontrado ",
        )
    else:
        calculation = service.service_value * Decimal(str(data.square_meter))
        return ServiceCalculationResponseSchema(
            name=service.name,
            service_value=service.service_value,
            square_meter=data.square_meter,
            total=calculation,
        )
