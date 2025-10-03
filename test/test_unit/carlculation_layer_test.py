import pytest
from decimal import Decimal
from fastapi import HTTPException, status
from app.repositories.service_repository import VerificationWithName
from app.schemas.service_schema import ServiceCalculationSchema
from app.service_layer.service_layer import ServiceLayer


def test_calculation(mocker):
    data = ServiceCalculationSchema(name="Pintura Acrilica", square_meter=Decimal("20"))
    mock_db = mocker.Mock()

    mock_service_obj = mocker.Mock()
    mock_service_obj.name = "Pintura Acrilica"
    mock_service_obj.service_value = Decimal("120.5")

    mock_verification = mocker.Mock(spec=VerificationWithName)
    mock_verification.service_verification.return_value = mock_service_obj

    service_layer = ServiceLayer(mock_db)
    service_layer.verification = mock_verification

    resultado = service_layer.calculate_service_total(data)
    assert resultado.name == "Pintura Acrilica"
    assert resultado.service_value == 120.5
    assert resultado.total == 2410.0


def test_calculation_exception(mocker):
    mock_data = mocker.Mock()
    mock_data.name = ""

    mock_db = mocker.Mock()

    mock_verification = mocker.Mock(spec=VerificationWithName)
    mock_verification.service_verification.side_effect = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Serviço '{mock_data.name}' não encontrado",
    )

    service_layer = ServiceLayer(mock_db)
    service_layer.verification = mock_verification

    with pytest.raises(HTTPException) as excecao:
        service_layer.calculate_service_total(mock_data)

    assert excecao.value.status_code == status.HTTP_404_NOT_FOUND
    assert excecao.value.detail == "Serviço '' não encontrado"
