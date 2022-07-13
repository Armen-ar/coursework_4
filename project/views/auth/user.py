from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.models import UserSchema

user_ns = Namespace('user')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        """
        Представление возвращает всех пользователей
        """
        users = user_service.get_all()
        response = UserSchema(many=True).dump(users)

        return response, 200

    def post(self):
        """
        Представление добавляет нового пользователя
        """
        data = request.json
        user = user_service.create(data)

        return f"Пользователь с id {user.id} создан!", 201
