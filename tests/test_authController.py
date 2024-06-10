import bcrypt
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dddpy.insfrastructure.services.encryptService import encrypt_password
from main import app  # Asumiendo que `app` está definido en `main.py`
from controllers.authController import auth_router
from dddpy.domain.schemas.user_dto import UserDTO
from dddpy.insfrastructure.sqlite.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Para pruebas con archivo de BD
# SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"  # Para pruebas en memoria

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# Dependency override
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session():
    db = TestingSessionLocal()
    yield db
    db.close()


def test_login_invalid_credentials(db_session):
    response = client.post("/auth/login", json={"email": "john@example.com", "password": "wrong_password"})
    
    assert response.status_code == 401
    assert response.json() == {"message": "Invalid credentials"}

def test_login_user_not_exist(db_session):
    response = client.post("/auth/login", json={"email": "nonexistent@example.com", "password": "any_password"})
    
    assert response.status_code == 401
    assert response.json() == {"message": "User does not exist"}
