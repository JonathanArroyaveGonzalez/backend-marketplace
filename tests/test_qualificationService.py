# test_qualificationService.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dddpy.insfrastructure.sqlite.database import Base, get_db
from dddpy.application.Services.qualificationService import create_qualification_service
from dddpy.application.Models.qualificationModel import CreateQualificationModel
from dddpy.domain.schemas.qualification_dto import QualificationDTO
from dddpy.domain.schemas.order_dto import OrderDTO

# Configuración de la base de datos de prueba
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear las tablas de la base de datos
Base.metadata.create_all(bind=engine)

# Configurar la base de datos de prueba
@pytest.fixture(scope="module")
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
                db.close()

def test_create_qualification_service(db: Session):
    # Crear una orden de prueba
    order = OrderDTO(user_id="1", post_id="1", quantity=1, total_amount=100.0, status="CREATED")
    db.add(order)
    db.commit()
        
    # Datos de calificación de prueba
    qualification_data = CreateQualificationModel(
                orderId=order.id,
        score=5,
        comment="Excellent service!"
    )
        
    # Crear la calificación
    qualification_id = create_qualification_service(qualification_data, db)
        
    # Verificar que la calificación se haya creado correctamente
    assert qualification_id is not None
    qualification = db.query(QualificationDTO).filter(QualificationDTO.id == qualification_id).first()
    assert qualification is not None
    assert qualification.order_id == qualification_data.orderId
    assert qualification.score == qualification_data.score
    assert qualification.comment == qualification_data.comment