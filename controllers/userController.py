from fastapi import APIRouter, Depends

from dddpy.application.Models.userModel import UserModel
from dddpy.application.Services.userService import create_user_service
from dddpy.domain.schemas.user_dto import UserDTO
from dddpy.insfrastructure.sqlite.database import get_db
from sqlalchemy.orm import Session

from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository


user_router = APIRouter(prefix="/user",tags=["user"])

@user_router.post(
        "/createUser"
        )
async def create_user(user:UserModel, db: Session = Depends(get_db)):
        return create_user_service(user, db)
        