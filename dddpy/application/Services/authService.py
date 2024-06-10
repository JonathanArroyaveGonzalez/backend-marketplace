from fastapi import Depends
from sqlalchemy.orm import Session
from dddpy.application.Models.loginDataModel import UserLogin
from dddpy.application.Models.userModel import UserModel
from dddpy.domain.schemas.user_dto import UserDTO
from dddpy.insfrastructure.Auth.jwt_manage import encode_jwt
from dddpy.insfrastructure.services.encryptService import check_password
from dddpy.insfrastructure.sqlite.database import get_db


def validate_password(db_user: UserDTO, user:UserLogin):
    if check_password(user.password, db_user.password):
            
        token = get_token(UserModel(**db_user.__dict__).__dict__)

        return token
    else:
        return None
    
def get_token(data: dict):
    return encode_jwt(data)


def get_user_by_username_and_role(data: dict, db: Session = Depends(get_db)):
    user = db.query(UserDTO).filter(UserDTO.email == data["email"]).first()
    return user