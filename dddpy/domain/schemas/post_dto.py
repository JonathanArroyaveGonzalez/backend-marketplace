from datetime import datetime
import uuid
from sqlalchemy import Column, DateTime, Integer, String, Float
from dddpy.insfrastructure.sqlite.database import Base
from sqlalchemy.orm import relationship


class PostDTO(Base):
    __tablename__ = "Posts"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    category = Column(Integer)
    price = Column(Float)
    description = Column(String)
    stock = Column(Integer)
    status = Column(Integer)
    creation_date = Column(DateTime)
    last_modified_date = Column(DateTime)
    images = relationship("ImageDTO",back_populates="post")
    orders = relationship("OrderDTO",  back_populates="post_order")
    

    def __init__(self, name, category, price, description, stock, status):
        self.id = str(uuid.uuid4())
        self.name = name
        self.category = category
        self.price = float(price)
        self.description = description
        self.stock= stock
        self.status = status
        self.creation_date = datetime.now()
        self.last_modified_date = self.creation_date

    def __str__(self):
        return f'PostDTO(name={self.name}, category={self.category}, price={self.price}, description={self.description}, stock={self.stock}, status={self.status})'

    def editPost(self,price, description, stock, status):
        self.price = float(price)
        self.description = description
        self.stock= stock
        self.status = status
        self.last_modified_date = datetime.now()





        