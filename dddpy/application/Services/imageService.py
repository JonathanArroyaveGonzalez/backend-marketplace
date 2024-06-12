from fastapi import Depends, UploadFile
from sqlalchemy.orm import Session

from dddpy.domain.schemas.image_dto import ImageDTO
from dddpy.insfrastructure.services.storageService import FirebaseStorage
from dddpy.insfrastructure.sqlite.database import get_db
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository


async def upload_image_service(image:UploadFile,idPost: str, db: Session)->str:
    firebase = FirebaseStorage()
    repository = GenericRepository(db, ImageDTO)
    url = await firebase.save(file= image)
    newImage = ImageDTO(url,idPost)
    repository.add(newImage)
    return url