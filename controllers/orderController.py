from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dddpy.application.Models.orderModel import CreateOrderModel, UpdateOrderStatusModel
from dddpy.application.Models.userModel import UserModel
from dddpy.application.Services.orderService import change_order_status_service, create_order_service, get_all_orders_service, get_order_by_id_service, get_order_by_user_service
from dddpy.domain.Enums.orderStatus import orderStatus
from dddpy.insfrastructure.Auth.jwt_depends import JWTBearer
from dddpy.insfrastructure.sqlite.database import get_db

order_router = APIRouter(prefix="/order",tags=["order"])
@order_router.post(
        "/createOrder"
        )
async def create_order(order: CreateOrderModel, db: Session = Depends(get_db), authorized: UserModel = Depends(JWTBearer())) -> str:
    return create_order_service(order, db)

@order_router.get(
        "/getAllOrders"
        )
async def get_all_orders(db: Session = Depends(get_db), authorized: UserModel = Depends(JWTBearer())):
    return get_all_orders_service(db)

@order_router.get(
    "/getOrderById"
)
async def get_order_by_id(id: str, db: Session = Depends(get_db), authorized: UserModel = Depends(JWTBearer())):
    return get_order_by_id_service(id, db)

@order_router.put(
    "/updateOrderStatus"
)
async def change_order_status(model: UpdateOrderStatusModel, db: Session = Depends(get_db), authorized: UserModel = Depends(JWTBearer())):
    return change_order_status_service(model.orderId, model.status, db)
    
@order_router.get(
    "/getOrderByUser"
)
async def get_order_by_user(user_id: str, db: Session = Depends(get_db)):
    return get_order_by_user_service(user_id, db)