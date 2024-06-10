from pydantic import BaseModel


class EditPostModel(BaseModel):
    id: str
    price:float
    description:str
    stock:int
    status:int
