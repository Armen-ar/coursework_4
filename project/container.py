from project.dao.main import DirectorsDAO, MoviesDAO, UserDAO, GenresDAO
from project.services import GenresService, DirectorsService, MoviesService, UserService, AuthsService

from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
movie_dao = MoviesDAO(db.session)
user_dao = UserDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
movie_service = MoviesService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthsService(user_service=user_service)
