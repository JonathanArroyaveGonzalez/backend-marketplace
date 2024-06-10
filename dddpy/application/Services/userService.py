from dddpy.application.Models.userModel import UserModel
from sqlalchemy.orm import Session

from dddpy.domain.schemas.user_dto import UserDTO
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository

def create_user_service(user:UserModel, db: Session):
        new_user = UserDTO(user.name, user.lastName, user.email, user.phone, user.password)
        repository = GenericRepository(db, UserDTO)
        repository.add(new_user)
        new_user.password = None
        return new_user