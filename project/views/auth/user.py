from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.helpers.decorators import auth_required
from project.models import UserSchema

user_ns = Namespace('user')


@user_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self):
        """
        Представление возвращает всех пользователей, допуск auth
        """
        users = user_service.get_all()
        response = UserSchema(many=True).dump(users)

        return response, 200

    @auth_required
    def post(self):
        """
        Представление добавляет нового пользователя, допуск auth
        """
        data = request.json
        user = user_service.create(data)

        return f"Пользователь с id {user.id} создан!", 201

    @auth_required
    def put(self, uid):
        """
        Представление обновляет информацию пользователя по id, допуск auth
        """
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    @auth_required
    def patch(self, uid):
        """
        Представление обновляет частично информацию пользователя по id, допуск auth
        """
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update_partical(req_json)
        return "", 204
