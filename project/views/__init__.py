from project.views.auth.auth import auth_ns
from project.views.auth.user import user_ns
from project.views.main.directors import director_ns
from project.views.main.genres import genre_ns
from project.views.main.movies import movie_ns


__all__ = [
    'auth_ns',
    'genre_ns',
    'user_ns',
    'director_ns',
    'movie_ns',
]







