from dddpy.application.Models.qualificationModel import CreateQualificationModel
from sqlalchemy.orm import Session

from dddpy.domain.schemas.order_dto import OrderDTO
from dddpy.domain.schemas.qualification_dto import QualificationDTO
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository

def create_qualification_service(qualification: CreateQualificationModel,db:Session):
    repository = GenericRepository(db, QualificationDTO)
    order_repository = GenericRepository(db, OrderDTO)
    order_entity = order_repository.get(qualification.orderId)
    new_qualification = QualificationDTO(order_entity.id, qualification.score, qualification.comment)
    repository.add(new_qualification)
    return new_qualification.id