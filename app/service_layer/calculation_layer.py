from decimal import Decimal
from app.api.service_api import VerificationWithName
from app.schemas.service_schema import (
    ServiceCalculationSchema,
    ServiceCalculationResponseSchema,
)


def squared_calculation(
    data: ServiceCalculationSchema, verification: VerificationWithName
):
    service = verification.service_verification(data.name)

    calculation = service.service_value * Decimal(str(data.square_meter))
    return ServiceCalculationResponseSchema(
        name=service.name,
        service_value=service.service_value,
        square_meter=data.square_meter,
        total=calculation,
    )
