from typing import Optional, List
from project.dao import MoviesDAO
from project.exceptions import ItemNotFound
from project.models import Movie


class MoviesService:
    def __init__(self, dao: MoviesDAO) -> None:
        self.dao = dao

    def get_item(self, id: int) -> Movie:
        """
        Метод возвращает фильм по id
        """
        if movie := self.dao.get_by_id(id):
            return movie
        raise ItemNotFound(f'Movie with id={id} not exists.')

    def get_all(self, filter=None, page: Optional[int] = None) -> List[Movie]:
        """
        Метод возвращает все фильмы, приоритет новые
        """
        return self.dao.get_all_order_by(page=page, filter=filter)
