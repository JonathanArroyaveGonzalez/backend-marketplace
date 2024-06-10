from datetime import datetime
import uuid
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from dddpy.insfrastructure.sqlite.database import Base

class QualificationDTO(Base):
    __tablename__ = "Qualifications"
    id = Column(String, primary_key=True, index=True)
    order_id = Column(String, ForeignKey('Orders.id'))
    score = Column(Integer)
    comment = Column(String)
    creation_date = Column(DateTime)
    last_modified_date = Column(DateTime)
    order = relationship("OrderDTO", back_populates="qualifications")

    def __init__(self, post_id, score, comment):
            self.id = str(uuid.uuid4())
            self.order_id = post_id
            self.score = score
            self.comment = comment
            self.creation_date = datetime.now()
            self.last_modified_date = datetime.now()