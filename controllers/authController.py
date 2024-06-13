from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from dddpy.application.Models.loginDataModel import UserLogin
from dddpy.application.Services.authService import validate_password
from dddpy.domain.schemas.user_dto import UserDTO
from dddpy.insfrastructure.sqlite.database import get_db
from sqlalchemy.orm import Session



auth_router = APIRouter(prefix="/auth",tags=["auth"])
@auth_router.post("/login")
def login(user: UserLogin, db:Session = Depends(get_db)):
    db_user = db.query(UserDTO).filter(UserDTO.email == user.email).first()

    if db_user:
        token = validate_password(db_user, user)
        
        if token:
            user_data = {
                "id" : db_user.id,
                "name":db_user.name,
                "email": db_user.email,
                "lastName": db_user.lastName,
                "phone": db_user.phone,
                "token": token
            }
            return JSONResponse(content=user_data, status_code=200)
        else:
            return JSONResponse(content={"message": "Invalid credentials"}, status_code=401)
        
    else:
        return JSONResponse(content={"message": "User does not exist"}, status_code=401)