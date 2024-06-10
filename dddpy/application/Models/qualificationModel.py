from pydantic import BaseModel
from dddpy.application.Models.entityModel import EntityModel


class QualificationModel(EntityModel, BaseModel):
    rate: int
    comment: str

class CreateQualificationModel(BaseModel):
    orderId: str
    score: int
    comment: str