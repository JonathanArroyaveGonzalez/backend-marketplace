import os
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from dddpy.insfrastructure.sqlite.database import Base, engine
from controllers.userController import user_router
from controllers.authController import auth_router
from controllers.postController import post_router
from controllers.imageController import image_router
from controllers.orderController import order_router
from controllers.qualificationController import qualification_router

app = FastAPI(
    title="Marketplace API",
    debug=True
)

# Configuración de CORS
origins = [
    "*",  # Permite solicitudes de cualquier origen
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind= engine)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(post_router)
app.include_router(image_router)
app.include_router(order_router)
app.include_router(qualification_router)


@app.get(
        "/healthCheck",
        status_code=status.HTTP_200_OK
        )
async def healthCheck():
    '''app is already working!'''
    return {"message": "All works!"}

@app.get("/")
def read_root():
    image_path = os.path.join("resources", "images", "codesnakes.png")
    return FileResponse(image_path)



             

    
