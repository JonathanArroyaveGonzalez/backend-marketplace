from pydantic import BaseModel
from dddpy.application.Models.entityModel import EntityModel
from dddpy.domain.Enums.orderStatus import orderStatus

class OrderModel(EntityModel, BaseModel):
    status: orderStatus
    userId: str
    postId: str

class CreateOrderModel(BaseModel):
    quantity: int
    userId: str
    postId: str

class UpdateOrderStatusModel(BaseModel):
    status: orderStatus
    orderId: str