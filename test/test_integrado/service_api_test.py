def test_url_create_service(override_get_db):
    api = override_get_db.post(
        "/services", json={"name": "Pintura Acrilica", "service_value": 120.5}
    )
    assert api.status_code == 201


def test_url_get_service(override_get_db):
    api = override_get_db.get("/services/Pintura Acrilica")
    assert api.status_code == 200
    assert api.json() == {"id": 1, "name": "Pintura Acrilica", "service_value": 120.5}


def test_url_update(override_get_db):
    api = override_get_db.put(
        "/services/Pintura Acrilica",
        json={"name": "Pintura Acrilica", "service_value": 120.20},
    )
    assert api.status_code == 200
    assert api.json() == {"id": 1, "name": "Pintura Acrilica", "service_value": 120.2}
