from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from dddpy.application.Services.authService import get_user_by_username_and_role
from dddpy.insfrastructure.Auth.jwt_manage import decode_jwt
from dddpy.insfrastructure.sqlite.database import get_db


class JWTBearer(HTTPBearer):

    async def __call__(self, request: Request, db: Session = Depends(get_db)):
        credentials = await super().__call__(request)
        
        data = decode_jwt(credentials.credentials)
        
        if data:
            #TODO: Cambiar esto a un servicio.
            user = get_user_by_username_and_role(data, db)
            
            if user:
                return user
            else:
                raise HTTPException(status_code=403, detail="Invalid authorization code")
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code")