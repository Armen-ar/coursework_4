from flask import request
from flask_restx import Namespace, Resource

from project.container import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthsView(Resource):
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
class AuthsView(Resource):
    def post(self):
        """
        Представление получает email и password, генерирует токены
        """
        req_json = request.json

        email = req_json.get("email")
        password = req_json.get("password")

        if None in [email, password]:
            return "", 401

        token = auth_service.generate_tokens(email, password)

        return token, 201

    def put(self):
        """
        Представление проверяет валидность refresh_token и создаёт пару новых токенов
        """
        req_json = request.cookies
        token = req_json.get("RefreshToken")

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201
