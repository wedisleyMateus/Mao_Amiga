from decimal import Decimal
from sqlalchemy.orm import Session
from app.repositories.service_repository import (
    ServiceRepository,
    ServiceVerificationByName,
)
from app.schemas.service_schema import (
    ServiceSchema,
    ServiceCalculationRequest,
    ServiceCalculationResponse,
)


class ServiceNotFoundError(Exception):
    """Erro quando o serviço não é encontrado"""

    pass


class ServiceAlreadyExistsError(Exception):
    """Erro quando o serviço já existe no sistema"""

    pass


class ServiceListEmptyError(Exception):
    """Erro quando a lista de serviços está vazia"""

    pass


class ServiceLayer:
    def __init__(self, db: Session):
        self.verification = ServiceVerificationByName(db)
        self.repository = ServiceRepository(db, self.verification)

    def existence_verification(self, data: ServiceSchema):
        if self.verification.service_verification(data.name):
            raise ServiceAlreadyExistsError()
        else:
            return self.repository.create_service(data)

    def list_validation(self):
        list_service = self.repository.get_all_service()
        if not list_service:
            raise ServiceListEmptyError()
        else:
            return list_service

    def calculate_service_total(self, data: ServiceCalculationRequest):
        """
        Calcula o valor total do serviço por metro quadrado

        Args:
            data(ServiceCalculationSchema): Contem os dados de entrada:
            - 'name' = Nome do serviço e
            - 'square_meter' = valor do metro quadrado

        Raises:
            ServiceNotFoundError: serviço não for encontrado

        Returns:
            ServiceCalculationResponseSchema: Objeto com todas as informações
            do serviço e incluindo o total do serviço
        """
        service = self.verification.service_verification(data.name)
        if service is None:
            raise ServiceNotFoundError()
        else:
            calculation = service.service_value * Decimal(str(data.square_meter))
            return ServiceCalculationResponse(
                name=service.name,
                service_value=service.service_value,
                square_meter=data.square_meter,
                total=calculation,
            )
