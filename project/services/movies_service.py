from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Movie


class MoviesService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, id: int) -> Movie:
        """
        Метод возвращает фильм по id
        """
        if movie := self.dao.get_by_id(id):
            return movie
        raise ItemNotFound(f'Movie with id={id} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Movie]:
        """
        Метод возвращает все фильмы
        """
        return self.dao.get_all(page=page)
