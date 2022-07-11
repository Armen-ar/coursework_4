from typing import Generic, List, Optional, TypeVar

from flask import current_app
from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm import scoped_session
from werkzeug.exceptions import NotFound
from project.setup.db.models import Base

T = TypeVar('T', bound=Base)


class BaseDAO(Generic[T]):
    __model__ = Base

    def __init__(self, db_session: scoped_session) -> None:
        self._db_session = db_session

    @property
    def _items_per_page(self) -> int:
        return current_app.config['ITEMS_PER_PAGE']

    def get_by_id(self, id: int) -> Optional[T]:
        """Метод возвращает сущность по id"""
        return self._db_session.query(self.__model__).get(id)

    def get_all(self, page: Optional[int] = None) -> List[T]:
        """Метод возвращает все сущности по видам"""
        stmt: BaseQuery = self._db_session.query(self.__model__)
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()

    def get_by_username(self, username):
        """Метод возвращает пользователя по имени"""
        return self._db_session.query(self.__model__).filter(self.__model__.username == username).one()

    def create(self, user_data):
        """Метод добавляет нового пользователя"""
        entity = self.__model__(**user_data)

        self._db_session.add(entity)
        self._db_session.commit()
        return entity

    def update(self, user_data):
        """Метод обновляет данные пользователя по id"""
        uid = user_data.get("id")
        user = self.get_by_id(uid)

        user.imail = user_data.get("imail")
        user.password = user_data.get("password")
        user.name = user_data.get("name")
        user.surname = user_data.get("surname")
        user.favorite = user_data.get("favorite")

        self._db_session.add(user)
        self._db_session.commit()
