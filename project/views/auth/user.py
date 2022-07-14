from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.helpers.decorators import auth_required
from project.setup.api.models import user

user_ns = Namespace('user')


@user_ns.route('/')
class UsersView(Resource):
    @user_ns.marshal_with(user, as_list=True, code=200, description='OK')
    @auth_required
    def get(self):
        """
        Представление возвращает информацию о пользователе, допуск auth
        """
        users = user_service.get_all()

        return users, 200

    @auth_required
    def patch(self, uid):
        """Представление обновляет частично фильм по id, допуск auth"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update_partical(req_json)
        return "", 204


@user_ns.route('/*password')
class UsersView(Resource):
    @auth_required
    def put(self, uid):
        """Представление заменяет старый пароль пользователя на новый по id, допуск auth"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return "", 204
