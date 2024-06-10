from sqlalchemy.orm import Session

from dddpy.application.Models.orderModel import CreateOrderModel
from dddpy.domain.Enums.orderStatus import orderStatus
from dddpy.domain.schemas.order_dto import OrderDTO
from dddpy.domain.schemas.post_dto import PostDTO
from dddpy.domain.schemas.user_dto import UserDTO
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository

def create_order_service(order:CreateOrderModel, db: Session) -> str:
    post_repository = GenericRepository(db, PostDTO)
    order_repository = GenericRepository(db, OrderDTO)

    post_entity = post_repository.get(order.postId)
    new_order = OrderDTO(user_id=order.userId, post_id=post_entity.id, quantity=order.quantity, total_amount=post_entity.price * order.quantity, status=orderStatus.CREATED)
    response = order_repository.add(new_order)
    return response.id

def get_all_orders_service(db: Session):
    repository = GenericRepository(db, OrderDTO)
    orderList:list[OrderDTO] = repository.get_all()
    for order in orderList:
        order.user_order = map_user_to_order(order.user_id, db)
        order.post_order = map_post_to_order(order.post_id, db)
    return orderList

def get_order_by_id_service(id: str, db: Session) -> OrderDTO:
    repository = GenericRepository(db, OrderDTO)
    order : OrderDTO = repository.get(id)
    order.user_order = map_user_to_order(order.user_id, db)
    order.post_order = map_post_to_order(order.post_id, db)
    return order

def change_order_status_service(id: str, status: orderStatus, db: Session):
    repository = GenericRepository(db, OrderDTO)
    order = repository.get(id)
    order.status = status
    repository.update(order)
    return order

def map_user_to_order(user_id:str, db: Session) -> UserDTO:
    user_repository = GenericRepository(db, UserDTO)
    user = user_repository.get(entity_id=user_id)
    if user:
        user.password = None
    return user

def map_post_to_order(post_id:str, db: Session) -> PostDTO:
    post_repository = GenericRepository(db, PostDTO)
    post = post_repository.get(entity_id=post_id)
    return post