from io import BytesIO
import os
from fastapi import UploadFile
from environment.env import firebase

from dddpy.application.abstract.abstractStorage import AbstractStorage

class FirebaseStorage(AbstractStorage):

    def __init__(self):
        self.storage = firebase.storage()

    async def save(self, file: UploadFile):
        # Crear un nombre de archivo único
        filename = f"{os.urandom(16).hex()}-{file.filename}"

        # Leer el archivo en la memoria
        file_bytes = await file.read()

        # Subir el archivo a Firebase Storage
        self.storage.child(filename).put(file_bytes)

        # Devolver la URL de la imagen
        return self.storage.child(filename).get_url(None)