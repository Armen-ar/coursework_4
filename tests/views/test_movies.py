import pytest

from project.models import Movie, Director, Genre


class TestMoviesView:
    @pytest.fixture
    def movie(self, db):
        d = Director(name='AAA')
        g = Genre(name='B')
        obj = Movie(title="test_title", description="test_description",
                    trailer="test_trailer", year=1, rating=1, genre_id=1, director_id=1)
        db.session.add(d)
        db.session.add(g)
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_many(self, client, movie):
        response = client.get("/movies/")
        assert response.status_code == 200
        assert response.json == [{"id": movie.id, "title": movie.title, "description": movie.description,
                                  "trailer": movie.trailer, "year": movie.year, "rating": movie.rating,
                                  "genre": {'id': movie.genre.id, 'name': movie.genre.name},
                                  "director": {'id': movie.director.id, 'name': movie.director.name}}]

    def test_movie_pages(self, client, movie):
        response = client.get("/movies/?page=1")
        assert response.status_code == 200
        assert len(response.json) == 1

        response = client.get("/movies/?page=2")
        assert response.status_code == 200
        assert len(response.json) == 0

    def test_movie(self, client, movie):
        response = client.get("/movies/1/")
        assert response.status_code == 200
        assert response.json == {"id": movie.id, "title": movie.title, "description": movie.description,
                                 "trailer": movie.trailer, "year": movie.year, "rating": movie.rating,
                                 "genre": {'id': movie.genre.id, 'name': movie.genre.name},
                                 "director": {'id': movie.director.id, 'name': movie.director.name}}

    def test_movie_not_found(self, client, movie):
        response = client.get("/movies/2/")
        assert response.status_code == 404
