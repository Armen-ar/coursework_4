from typing import Optional, List

from sqlalchemy import desc
from werkzeug.exceptions import NotFound

from project.dao.base import BaseDAO, T
from project.models import Genre, Director, Movie, User


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all_order_by(self, page: Optional[int] = None, filter=None) -> List[T]:
        stmt = self._db_session.query(self.__model__)
        if filter:
            stmt = stmt.order_by(desc(self.__model__.year))
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()


class UserDAO(BaseDAO[User]):
    __model__ = User

    def get_user_by_email(self, email):
        """
        Метод возвращает данные пользователя по email
        """
        stmt = self._db_session.query(self.__model__).filter(self.__model__.email == email).one()

        return stmt

    def create(self, user_data):
        """
        Метод создаёт пользователя по email и password
        """
        entity = self.__model__(**user_data)

        self._db_session.add(entity)
        self._db_session.commit()

    def update(self, email, user_data):
        """
        Метод обновляет данные пользователя по email
        """
        self._db_session.query(self.__model__).filter(self.__model__.email == email).update(user_data)
        self._db_session.commit()
