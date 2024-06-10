# test_orderService.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dddpy.insfrastructure.sqlite.database import Base, get_db
from dddpy.application.Services.orderService import create_order_service, get_all_orders_service, get_order_by_id_service
from dddpy.application.Models.orderModel import CreateOrderModel
from dddpy.domain.schemas.order_dto import OrderDTO
from dddpy.domain.schemas.post_dto import PostDTO
from dddpy.domain.schemas.user_dto import UserDTO
from dddpy.domain.Enums.orderStatus import orderStatus

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

def test_create_order_service(db: Session):
    # Crear usuario y post de prueba
    user = UserDTO(name="Test", lastName="User", email="testuser@example.com", phone="32344444", password="Admin1234")
    post = PostDTO(name="Test Post", category=1, price=100.0, description="A test post", stock=10, status=1)
    db.add(user)
    db.add(post)
    db.commit()
    
    order_data = CreateOrderModel(
        userId=user.id,
        postId=post.id,
        quantity=2
    )
    order_id = create_order_service(order_data, db)
    assert order_id is not None

def test_get_all_orders_service(db: Session):
    orders = get_all_orders_service(db)
    assert len(orders) > 0
    order = orders[0]
    assert order.user_order is not None
    assert order.post_order is not None

def test_get_order_by_id_service(db: Session):
    order = db.query(OrderDTO).first()
    retrieved_order = get_order_by_id_service(order.id, db)
    assert retrieved_order is not None
    assert retrieved_order.id == order.id
    assert retrieved_order.user_order is not None
    assert retrieved_order.post_order is not None
