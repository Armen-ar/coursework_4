from flask_restx import Namespace, Resource
from project.container import movie_service
from project.setup.api.models import movie

from project.setup.api.parsers import page_parser

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    @movie_ns.expect(page_parser)
    @movie_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Возвращает все фильмы, в приоритете новые фильмы.
        """
        return movie_service.get_all(**page_parser.parse_args())


@movie_ns.route('/<int:movie_id>/')
class MovieView(Resource):
    @movie_ns.response(404, 'Not Found')
    @movie_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self, movie_id: int):
        """
        Возвращает фильм по id.
        """
        return movie_service.get_item(movie_id)
