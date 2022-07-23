from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Director


class DirectorsService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, id: int) -> Director:
        """
        Метод возвращает режиссёра по id
        """
        if director := self.dao.get_by_id(id):
            return director
        raise ItemNotFound(f'Director with id={id} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Director]:
        """
        Метод возвращает всех режиссёров
        """
        return self.dao.get_all(page)
