import pytest
from app.api.service_api import (
    create_service,
    get_services,
    get_service,
    update_service,
    delete_service,
)
from fastapi import HTTPException
from app.schemas import ServiceVerificationSchema
from app.repositories.service_repository import VerificationWithName


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


@pytest.mark.asyncio
async def test_get_service_all(mocker):
    data_list = [
        {"id": 1, "name": "Pintura Acrilica", "service_value": 120.2},
        {"id": 2, "name": "Pintura Normal", "service_value": 40},
    ]

    mock_db = mocker.Mock()
    mock_service_layer = mocker.Mock()
    mock_service_layer.list_validation.return_value = data_list

    mocker.patch("app.api.service_api.ServiceLayer", return_value=mock_service_layer)

    resultado = await get_services(mock_db)
    assert resultado == [
        {"id": 1, "name": "Pintura Acrilica", "service_value": 120.2},
        {"id": 2, "name": "Pintura Normal", "service_value": 40},
    ]
    mock_service_layer.list_validation.assert_called_once()


@pytest.mark.asyncio
async def test_get_service(mocker):
    service_name = "Pintura Acrilica"
    data = {"id": 1, "name": service_name, "service_value": 120.2}

    mock_db = mocker.Mock()
    mock_verification = mocker.Mock(spec=VerificationWithName)
    mock_service = mocker.Mock()

    mocker.patch(
        "app.api.service_api.VerificationWithName", return_value=mock_verification
    )
    mocker.patch("app.api.service_api.ServiceRepository", return_value=mock_service)

    mock_service.get_service.return_value = data

    resultado = await get_service(service_name, mock_db)
    assert resultado == data


@pytest.mark.asyncio
async def test_update_service(mocker):
    service_name = "Pintura Acrilica"
    data = ServiceVerificationSchema(name="Pintura Acrilica", service_value=120.3)

    mock_db = mocker.Mock()
    mock_verification = mocker.Mock(spec=VerificationWithName)

    mock_service = mocker.Mock()
    mock_service.update_service.return_value = data

    mocker.patch(
        "app.api.service_api.VerificationWithName", return_value=mock_verification
    )
    mocker.patch("app.api.service_api.ServiceRepository", return_value=mock_service)

    resultado = await update_service(service_name, data, mock_db)
    assert resultado == data


@pytest.mark.asyncio
async def test_delete_service(mocker):
    service_name = "Pintura Normal"

    mock_db = mocker.Mock()
    mock_verification = mocker.Mock(spec=VerificationWithName)

    mock_service = mocker.Mock()
    mock_service.delete_service.side_effect = HTTPException(
        status_code=204, detail="Serviço deletado com sucesso"
    )

    mocker.patch(
        "app.api.service_api.VerificationWithName", return_value=mock_verification
    )
    mocker.patch("app.api.service_api.ServiceRepository", return_value=mock_service)

    with pytest.raises(HTTPException) as excecao:
        await delete_service(service_name, mock_db)

    assert excecao.value.status_code == 204
    assert excecao.value.detail == "Serviço deletado com sucesso"
