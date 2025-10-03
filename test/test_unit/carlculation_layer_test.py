from decimal import Decimal
from app.repositories.service_repository import VerificationWithName
from app.schemas.service_schema import ServiceCalculationSchema
from app.service_layer.calculation_layer import squared_calculation


def test_calculation(mocker):
    data = ServiceCalculationSchema(name="Pintura Acrilica", square_meter=20)

    mock_service_obj = mocker.Mock()
    mock_service_obj.name = "Pintura Acrilica"
    mock_service_obj.service_value = Decimal("120.5")

    mock_verification = mocker.Mock(spec=VerificationWithName)
    mock_verification.service_verification.return_value = mock_service_obj

    resultado = squared_calculation(data, mock_verification)
    assert resultado.name == "Pintura Acrilica"
    assert resultado.service_value == 120.5
    assert resultado.total == 2410.0
