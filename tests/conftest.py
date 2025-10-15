import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, String, Integer, Numeric
from starlette.testclient import TestClient

from app.infrastructure.conection import get_db
from app.main import app

DATABASE_TEST_URL = "sqlite+pysqlite:///:memory:"

engine = create_engine(DATABASE_TEST_URL, connect_args={"check_same_thread": False})
connection = engine.connect()
TestingSessionLocal = sessionmaker(bind=connection, autoflush=False, autocommit=False)
Base = declarative_base()


class Service(Base):
    __tablename__ = "type_service"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    service_value = Column(Numeric(10, 2), nullable=False)


@pytest.fixture(scope="session", autouse=True)
def criando_test_db():
    Base.metadata.create_all(bind=connection)
    yield
    Base.metadata.drop_all(bind=connection)
    connection.close()


@pytest.fixture
def db():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def override_get_db(db):
    def override():
        yield db

    app.dependency_overrides[get_db] = override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()
