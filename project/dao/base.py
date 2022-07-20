from typing import Generic, List, Optional, TypeVar

from flask import current_app
from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm import scoped_session
from werkzeug.exceptions import NotFound

from project.models import User
from project.setup.db.models import Base

T = TypeVar('T', bound=Base)


class BaseDAO(Generic[T]):
    __model__ = Base

    def __init__(self, db_session: scoped_session) -> None:
        """
        Конструктор для всех методов класса
        """
        self._db_session = db_session

    @property
    def _items_per_page(self) -> int:
        """
        Метод выводит на каждой странице столько записей, сколько задано в BaseConfig
        """
        return current_app.config['ITEMS_PER_PAGE']

    def get_by_id(self, id: int) -> Optional[T]:
        """
        Метод возвращает сущность по id
        """
        return self._db_session.query(self.__model__).get(id)

    def get_all(self, page: Optional[int] = None) -> List[T]:
        """
        Метод возвращает все сущности по видам постранично
        """
        stmt: BaseQuery = self._db_session.query(self.__model__)
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()

    def get_by_email(self, email):
        """
        Метод возвращает пользователя по email
        """
        return self._db_session.query(self.__model__).filter(self.__model__.email == email).one()

    def create(self, user_data):
        """
        Метод добавляет нового пользователя
        """
        entity = self.__model__(**user_data)

        self._db_session.add(entity)
        self._db_session.commit()

    def update(self, user: User):
        """
        Метод переписывает пароль пользователя
        """
        self._db_session.add(user)
        self._db_session.commit()

    def update_partical(self, user_data):
        """
        Метод обновляет частично данные пользователя
        """
        user = self.get_by_id(user_data.get("id"))
        if "name" in user_data:
            user.name = user_data.get("name")
        if "surname" in user_data:
            user.surname = user_data.get("surname")
        if "favorite_genre" in user_data:
            user.favorite_genre = user_data.get("favorite_genre")

        self._db_session.add(user)
        self._db_session.commit()
