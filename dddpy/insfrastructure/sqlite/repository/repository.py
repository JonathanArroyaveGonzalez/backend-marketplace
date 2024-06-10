#infrastructure/repository_generic.py
from sqlalchemy.orm import Session, selectinload
from typing import List, Type, TypeVar, Generic

from dddpy.domain.schemas.image_dto import ImageDTO

T = TypeVar('T')

class GenericRepository(Generic[T]):
    def __init__(self, db_session: Session, model: Type[T]):
        self.db_session = db_session
        self.model = model

    def add(self, entity: T) -> T:
        self.db_session.add(entity)
        self.db_session.commit()
        self.db_session.refresh(entity)
        return entity

    def get(self, entity_id: str) -> T:
        return self.db_session.query(self.model).filter_by(id=entity_id).first()

    def get_all(self) -> list[T]:
        return self.db_session.query(self.model).all()

    def update(self, entity: T) -> T:
        self.db_session.commit()
        self.db_session.refresh(entity)
        return entity

    def delete(self, entity: T):
        self.db_session.delete(entity)
        self.db_session.commit()

    def get_by_filter(self, **filters) -> List[T]:
        return self.db_session.query(self.model).filter_by(**filters).all()

    def get_all_with_images(self, db: Session) -> List[T]:
        # Realiza una consulta que incluye las imágenes relacionadas usando selectinload
        query = db.query(self.model).options(selectinload(self.model.images))
        return query.all()


