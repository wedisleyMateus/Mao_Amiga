import pytest
from app.api.service_api import create_service
from app.schemas.service_schema import ServiceVerificationSchema


@pytest.mark.asyncio
async def test_create_service(mocker):
    mock_data = ServiceVerificationSchema(name="Salve jorge", service_value=120.2)

    mock_db = mocker.Mock()

    mock_service_layer = mocker.Mock()
    mock_service_layer.existence_verification.return_value = mock_data

    mocker.patch("app.api.service_api.ServiceLayer", return_value=mock_service_layer)

    resultado = await create_service(mock_data, mock_db)
    assert resultado.name == "Salve jorge"
