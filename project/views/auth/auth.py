from flask import request
from flask_restx import Namespace, Resource

from project.container import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthsView(Resource):
    def post(self):
        reg_json = request.json

        email = reg_json.get("email", None)
        password = reg_json.get("password", None)

        if None in [email, password]:
            return "", 401

        tokens = auth_service.generate_tokens(email, password)

        return tokens, 201

    def put(self):
        reg_json = request.json
        token = reg_json.get("refresh_token")

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201
