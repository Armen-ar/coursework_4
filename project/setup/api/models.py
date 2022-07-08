from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})


director: Model = api.model('Режиссёр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Квентин Тарантино'),
})


movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Йеллоустоун'),
    'description': fields.String(required=True, max_length=100, example='Владелец ранчо пытается сохранить землю ....'),
    'trailer': fields.String(required=True, max_length=100, example='https://www.youtube.com/watch?v=UKei_d0cbP4'),
    'year': fields.Integer(required=True, example=2018),
    'rating': fields.Float(required=True, example=8.6),
    'genre_id': fields.Integer(required=True, example=17),
    'director_id': fields.Integer(required=True, example=1),
})


# user: Model = api.model('Пользователь', {
#     'imail': fields.String(required=True, max_length=100, example=1),
#     'password': fields.String(required=True, max_length=100, example='!1234Agmr'),
#     'name': fields.String(required=True, max_length=100, example='John'),
#     'surname': fields.String(required=True, max_length=100, example='Taylor'),
#     'favorite_genre': fields.Integer(required=True, example=1),
# })
