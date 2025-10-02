import pytest
from app.api.service_api import create_service
from fastapi import HTTPException
from app.schemas.service_schema import ServiceVerificationSchema


@pytest.mark.asyncio
async def test_create_service(mocker):
    data = ServiceVerificationSchema(name="Pintura Acrilica", service_value=120.2)
    mock_db = mocker.Mock()

    mock_service_layer = mocker.Mock()
    mock_service_layer.existence_verification.return_value = data

    mocker.patch("app.api.service_api.ServiceLayer", return_value=mock_service_layer)

    resultado = await create_service(data, mock_db)
    assert resultado.name == "Pintura Acrilica"
    assert resultado.service_value == 120.2
    mock_service_layer.existence_verification.assert_called_once()


@pytest.mark.asyncio
async def test_create_service_existing(mocker):
    data = mocker.Mock()
    mock_db = mocker.Mock()

    mock_service_layer = mocker.Mock()
    mock_service_layer.existence_verification.side_effect = HTTPException(
        status_code=409, detail="Serviço já existente"
    )

    mocker.patch("app.api.service_api.ServiceLayer", return_value=mock_service_layer)

    with pytest.raises(HTTPException) as excecao:
        await create_service(data, mock_db)

    assert excecao.value.status_code == 409
    assert excecao.value.detail == "Serviço já existente"
