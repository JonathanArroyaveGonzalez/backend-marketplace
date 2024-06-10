from datetime import datetime
import uuid

from sqlalchemy import Column, String, ForeignKey, Float, DateTime, Enum, Integer
from sqlalchemy.orm import relationship

from dddpy.domain.Enums.orderStatus import orderStatus
from dddpy.domain.schemas.user_dto import UserDTO
from dddpy.insfrastructure.sqlite.database import Base

class OrderDTO(Base):
    __tablename__ = "Orders"
    id = Column(String, primary_key= True, index=True)
    user_id = Column(String, ForeignKey('Users.id'))
    user_order = relationship("UserDTO", back_populates="orders")
    total_amount = Column(Float)
    creation_date = Column(DateTime)
    last_modified_date = Column(DateTime)
    post_id = Column(String, ForeignKey('Posts.id'))
    post_order = relationship("PostDTO",  back_populates="orders")
    status = Column(Enum(orderStatus))
    quantity = Column(Integer)
    qualifications = relationship("QualificationDTO", back_populates="order")

    def __init__(self, user_id, post_id, total_amount, status, quantity):
        self.user_id = user_id
        self.post_id = post_id
        self.total_amount = total_amount
        self.creation_date = datetime.now()
        self.last_modified_date = datetime.now()
        self.status = status
        self.id = str(uuid.uuid4())
        self.quantity = quantity
