from flask_restx import Namespace, Resource

from project.container import genre_service
from project.helpers.decorators import auth_required
from project.setup.api.models import genre
from project.setup.api.parsers import page_parser

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    @genre_ns.expect(page_parser)
    @genre_ns.marshal_with(genre, as_list=True, code=200, description='OK')
    def get(self):
        """
        Возвращает все жанры.
        """
        return genre_service.get_all(**page_parser.parse_args())


@genre_ns.route('/<int:genre_id>/')
class GenreView(Resource):
    @auth_required
    @genre_ns.response(404, 'Not Found')
    @genre_ns.marshal_with(genre, code=200, description='OK')
    def get(self, genre_id: int):
        """
        Возвращает жанр по id.
        """
        return genre_service.get_item(genre_id)