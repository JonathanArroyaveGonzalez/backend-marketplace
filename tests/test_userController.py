# test_userController.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dddpy.insfrastructure.sqlite.database import Base, get_db
from main import app
from dddpy.application.Models.userModel import UserModel

# Configuración de la base de datos de prueba
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear las tablas de la base de datos
Base.metadata.create_all(bind=engine)

# Configurar el cliente de prueba
@pytest.fixture(scope="module")
def client():
    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c

def test_create_user(client):
    user_data = {
        "name": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "phone": "1234567890",
        "password": "Securepassword1"
    }
    response = client.post("/user/createUser", json=user_data)
    assert response.status_code == 200
