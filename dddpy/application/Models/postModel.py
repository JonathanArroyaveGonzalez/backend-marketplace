from fastapi import File, UploadFile
from pydantic import BaseModel
from sqlalchemy import Double
from dddpy.application.Models.entityModel import EntityModel


class PostModel(BaseModel, EntityModel):
    name:str
    category:int
    price:float
    description:str
    stock:int
    status:int

class CreatePostModel(BaseModel):
    name:str
    category:int
    price: float
    description:str
    stock:int
    status:int