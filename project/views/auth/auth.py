from flask import request
from flask_restx import Namespace, Resource

from project.container import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthsView(Resource):
    def post_register(self):
        """
        Метод создаёт пользователя в системе
        """
        reg_json = request.json

        email = reg_json.get("email", None)
        password = reg_json.get("password", None)

        if None in [email, password]:
            return "", 401

        return "", 201


@auth_ns.route('/login')
class AuthsView(Resource):
    def post_login(self):
        """
        Метод проверяет аутентификацию пользователя в системе
        """
        reg_json = request.json

        email = reg_json.get("email", None)
        password = reg_json.get("password", None)

        if None in [email, password]:
            return "", 401

        tokens = auth_service.generate_tokens(email, password)

        return tokens, 201

    def put(self):
        """
        Метод проверяет валидность refresh_token и создаёт пару новых
        """
        reg_json = request.json
        token = reg_json.get("refresh_token")

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201
