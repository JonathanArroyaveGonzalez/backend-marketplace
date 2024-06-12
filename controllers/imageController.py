from fastapi import APIRouter, Depends, UploadFile, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from dddpy.application.Models.userModel import UserModel
from dddpy.application.Services.imageService import upload_image_service
from dddpy.domain.schemas.image_dto import ImageDTO
from dddpy.insfrastructure.Auth.jwt_depends import JWTBearer
from dddpy.insfrastructure.services.storageService import FirebaseStorage
from dddpy.insfrastructure.sqlite.database import get_db
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository

#Nueva adicion
from fastapi import File, Form, UploadFile

image_router = APIRouter(prefix="/image",tags=["image"])
@image_router.post(
        "/uploadImage"
        )
async def upload_image(image: UploadFile = File(...), idPost: str = Form(...), db: Session = Depends(get_db)):

        return await upload_image_service(image, idPost, db)