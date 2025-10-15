from tests.conftest import Service


def test_create_user(db):
    create_service = Service(name="Pintura Acrilica", service_value=120.20)
    db.add(create_service)
    db.commit()

    assert create_service.id == 1
    assert create_service.name == "Pintura Acrilica"
    assert float(create_service.service_value) == 120.20


def test_get_service(db):
    service = db.query(Service).filter_by(name="Pintura Acrilica").first()
    assert service.name == "Pintura Acrilica"


def test_get_all(db):
    service_1 = Service(name="Pintura Acentinado", service_value=120.20)
    service_2 = Service(name="Pintura Normal", service_value=60)
    db.add(service_1)
    db.add(service_2)
    db.commit()

    service_all = db.query(Service).all()
    assert len(service_all) == 3
    assert service_all[2].name == "Pintura Normal"


def test_delete(db):
    service = Service(name="Pintura Acrilica", service_value=120.20)
    db.add(service)
    db.commit()

    assert service.id == 4
    assert service.name == "Pintura Acrilica"
    assert float(service.service_value) == 120.20

    db.delete(service)
    db.commit()
