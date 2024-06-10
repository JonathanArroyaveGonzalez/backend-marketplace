from typing import List
from pydantic import BaseModel

from dddpy.application.Models.entityModel import EntityModel
from dddpy.application.Models.qualificationModel import QualificationModel
from dddpy.domain.schemas.image_dto import ImageDTO
from dddpy.domain.schemas.post_dto import PostDTO
from dddpy.domain.schemas.qualification_dto import QualificationDTO


class PostDetailResponseModel(EntityModel):
    name:str
    category:int
    price:float
    description:str
    stock:int
    status:int
    qualifications: List[QualificationDTO]
    images: List[ImageDTO]

    def __init__(self, post :PostDTO, qualifications: List[QualificationDTO], images :List[ImageDTO]):
        self.id = post.id
        self.name = post.name
        self.category = post.category
        self.price = post.price
        self.description = post.description
        self.stock = post.stock
        self.status = post.status
        self.creationDate = post.creation_date
        self.qualifications = qualifications
        self.images = images
        



    