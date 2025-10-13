import pytest
from decimal import Decimal
from app.repositories.service_repository import ServiceVerificationByName
from app.domain.schemas.service_schema import ServiceCalculationRequest
from app.services.service import ServiceLayer
from app.services.service import ServiceNotFoundError


def test_calculation(mocker):
    data = ServiceCalculationRequest(
        name="Pintura Acrilica", square_meter=Decimal("20")
    )
    mock_db = mocker.Mock()

    mock_service_obj = mocker.Mock()
    mock_service_obj.name = "Pintura Acrilica"
    mock_service_obj.service_value = Decimal("120.5")

    mock_verification = mocker.Mock(spec=ServiceVerificationByName)
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

    mock_verification = mocker.Mock(spec=ServiceVerificationByName)
    mock_verification.service_verification.side_effect = ServiceNotFoundError

    service_layer = ServiceLayer(mock_db)
    service_layer.verification = mock_verification

    with pytest.raises(ServiceNotFoundError):
        service_layer.calculate_service_total(mock_data)
