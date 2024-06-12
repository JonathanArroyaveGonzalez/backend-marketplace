from typing import List
from fastapi import File, UploadFile
from pydantic import BaseModel
from sqlalchemy import Double
from dddpy.application.Models.entityModel import EntityModel
from dddpy.domain.schemas.order_dto import OrderDTO
from dddpy.domain.schemas.post_dto import PostDTO


class PostModel(BaseModel, EntityModel):
    createdUser: str
    name:str
    category:int
    price:float
    description:str
    stock:int
    status:int

class CreatePostModel(BaseModel):
    createdUser: str
    name:str
    category:int
    price: float
    description:str
    stock:int
    status:int

class PostOrdersModel(EntityModel):
    createdUser: str
    name:str
    category:int
    price: float
    description:str
    stock:int
    status:int
    orders: List[OrderDTO]
    
    def __init__(self, post :PostDTO, orders: List[OrderDTO]):
        self.created_User = post.user_id
        self.id = post.id
        self.name = post.name
        self.category = post.category
        self.price = post.price
        self.description = post.description
        self.stock = post.stock
        self.status = post.status
        self.creationDate = post.creation_date
        self.orders = orders