from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_url_get_service():
    api = client.get("/services/Pintura Acrilica")
    assert api.status_code == 200
    assert api.json() == {"id": 1, "name": "Pintura Acrilica", "service_value": 120.5}


def test_url_update():
    api = client.put(
        "/services/Pintura Acrilica",
        json={"name": "Pintura Acrilica", "service_value": 120.5},
    )
    assert api.status_code == 200
    assert api.json() == {"id": 1, "name": "Pintura Acrilica", "service_value": 120.5}
