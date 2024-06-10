import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from dddpy.insfrastructure.sqlite.database import Base


class ImageDTO(Base):
    __tablename__ = "Images"
    id = Column(String, primary_key=True, index=True)
    url = Column(String)
    post_id = Column(String, ForeignKey("Posts.id"))
    post = relationship("PostDTO", back_populates="images")

    def __init__(self, url, post_id):
        self.url = url
        self.post_id = post_id
        self.id = str(uuid.uuid4())