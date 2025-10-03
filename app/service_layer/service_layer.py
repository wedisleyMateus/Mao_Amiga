from fastapi import HTTPException, status
from decimal import Decimal
from sqlalchemy.orm import Session
from app.repositories.service_repository import ServiceRepository, VerificationWithName
from app.schemas.service_schema import (
    ServiceSchema,
    ServiceCalculationSchema,
    ServiceCalculationResponseSchema,
)


class ServiceLayer:
    def __init__(self, db: Session):
        self.verification = VerificationWithName(db)
        self.repository = ServiceRepository(db, self.verification)

    def existence_verification(self, data: ServiceSchema):
        if self.verification.service_verification(data.name):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Serviço já Existente"
            )
        else:
            return self.repository.create_service(data)

    def list_validation(self):
        list_service = self.repository.get_all_service()
        if not list_service:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Lista de Serviço Vazia!!!",
            )
        else:
            return list_service

    def calculate_service_total(self, data: ServiceCalculationSchema):
        """
        Calcula o valor total do serviço por metro quadrado

        Args:
            data(ServiceCalculationSchema): Contem os dados de entrada:
            - 'name' = Nome do serviço e
            - 'square_meter' = valor do metro quadrado

        Raises:
            HTTPException: 404 se o serviço não for encontrado

        Returns:
            ServiceCalculationResponseSchema: Objeto com todas as informações
            do serviço,incluindo o total do serviço
        """
        service = self.verification.service_verification(data.name)
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
