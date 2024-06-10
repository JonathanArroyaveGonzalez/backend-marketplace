from abc import ABC, abstractmethod
from fastapi import UploadFile

class AbstractStorage(ABC):

    @abstractmethod
    async def save(self, file: UploadFile):
        pass