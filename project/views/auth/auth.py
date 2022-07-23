from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthsView(Resource):
    @auth_ns.marshal_with(user, as_list=True, code=200, description='OK')
    def post(self):
        """
        Представление получает email и password, создаёт пользователя в системе
        """
        req_json = request.json

        email = req_json.get("email")
        password = req_json.get("password")

        if None in [email, password]:
            return "", 401

        user_service.create(req_json)

        return 201


@auth_ns.route('/login/')
class AuthView(Resource):
    @auth_ns.response(404, 'Not Found')
    def post(self):
        """
        Представление получает email и password, генерирует токены
        """
        data = request.json
        if data.get('email') and data.get('password'):
            return user_service.check(data.get('email'), data.get('password')), 201
        else:
            return "", 401

    @auth_ns.response(404, 'Not Found')
    def put(self):
        """
        Представление проверяет валидность refresh_token и создаёт пару новых токенов
        """
        data = request.json
        if data.get('access_token') and data.get('refresh_token'):
            return user_service.update_token(data.get('refresh_token')), 201
        else:
            return "", 401
