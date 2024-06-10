from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from dddpy.application.Models.editPostModel import EditPostModel
from dddpy.application.Models.postModel import CreatePostModel
from dddpy.application.Models.userModel import UserModel
from dddpy.application.Services.postService import create_post_service, edit_post_service, get_postById_service, get_posts_service, get_posts_with_images_service
from dddpy.domain.schemas.post_dto import PostDTO
from dddpy.insfrastructure.Auth.jwt_depends import JWTBearer
from dddpy.insfrastructure.sqlite.database import get_db
from typing import Optional


post_router = APIRouter(prefix="/post",tags=["post"])
@post_router.post(
        "/createPost"
        )
async def create_post(post:CreatePostModel,db:Session = Depends(get_db), authorized: UserModel = Depends(JWTBearer())):
        return create_post_service(post,db)


@post_router.get(
     "/getPosts"
        )
async def get_posts(db:Session = Depends(get_db)):
        return get_posts_service(db)


@post_router.get(
     "/getPostById"
        )
async def get_postById( id: str,db:Session = Depends(get_db)):
        return get_postById_service(id,db)

"""""
@post_router.get("/posts-with-images")
def get_posts_with_images(
    db: Session = Depends(get_db)):
    posts = get_posts_with_images_service(db)
    return posts
    """
@post_router.get("/posts-with-images")
def get_posts_with_images(
    db: Session = Depends(get_db),
    limit: int = Query(10, ge=1),     # Default limit: 10 posts per page
    skip: int = Query(0, ge=0)        # Default skip: Start from the first post
):
    posts, total = get_posts_with_images_service(db, limit, skip)
    return {"registros": posts, "totalRegistros": total}


@post_router.put(
     "/editPost"
        )
async def edit_post( editPost: EditPostModel ,db:Session = Depends(get_db), authorized: UserModel = Depends(JWTBearer())):
        return edit_post_service(editPost, db)

