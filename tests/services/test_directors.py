from unittest.mock import patch

import pytest

from project.dao import DirectorsDAO
from project.exceptions import ItemNotFound
from project.models import Director
from project.services.directors_service import DirectorsService


class TestDirectorsService:

    # @pytest.fixture()
    # @patch('project.dao.DirectorsDAO')
    # def directors_dao_mock(self, dao_mock, director_1, director_1_1, director_1_2):
    #     dao = dao_mock()
    #     # dao.get_by_id.return_value = director_1
    #     # dao.get_all.return_value = [
    #     #     director_1_1,
    #     #     director_1_2
    #     # ]
    #     return dao

    @pytest.fixture()
    def directors_service(self, db):
        return DirectorsService(DirectorsDAO(db.session))

    @pytest.fixture
    def director_1(self, db):
        obj = Director(id=1, name='test_director_1')
        db.session.add(obj)
        db.session.commit()
        return obj

    @pytest.fixture
    def director_1_1(self, db):
        obj = Director(id=2, name='test_director_1_1')
        db.session.add(obj)
        db.session.commit()
        return obj

    @pytest.fixture
    def director_1_2(self, db):
        obj = Director(id=3, name='test_director_1_2')
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_get_director(self, directors_service, director_1_2):
        d = directors_service.get_item(3)
        assert d == director_1_2
        #assert directors_service.get_item(director.id)

    def test_director_not_found(self, directors_service):
        with pytest.raises(ItemNotFound):
            directors_service.get_item(10)

    def test_get_directors_1(self, app, directors_service, director_1, director_1_1):
        app.config['ITEMS_PER_PAGE'] = 2
        directors = directors_service.get_all(page=1)
        assert len(directors) == 2
        assert directors == [director_1, director_1_1]

    def test_get_directors_2(self, app, directors_service, director_1_2):
        app.config['ITEMS_PER_PAGE'] = 2
        directors = directors_service.get_all(page=2)
        assert len(directors) == 1
        assert directors == [director_1_2]

    @pytest.mark.parametrize('page', [1, None], ids=['with page', 'without page'])
    def test_get_directors(self, app, directors_service, page, director_1, director_1_1, director_1_2):
        app.config['ITEMS_PER_PAGE'] = 3
        directors = directors_service.get_all(page=page)
        assert len(directors) == 3
        assert directors == [director_1, director_1_1, director_1_2]
