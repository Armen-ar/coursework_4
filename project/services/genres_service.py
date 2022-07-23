from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Genre


class GenresService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, id: int) -> Genre:
        """
        Метод возвращает жанр по id
        """
        if genre := self.dao.get_by_id(id):
            return genre
        raise ItemNotFound(f'Genre with id={id} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Genre]:
        """
        Метод возвращает всех жанры
        """
        return self.dao.get_all(page)
