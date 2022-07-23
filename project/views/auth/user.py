from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
# from project.helpers.decorators import auth_required
from project.setup.api.models import user

user_ns = Namespace('user')


@user_ns.route('/')
class UsersView(Resource):
    @user_ns.marshal_with(user, as_list=True, code=200, description='OK')
    # @auth_required
    def get(self):
        """
        Представление возвращает refresh_token, допуск auth
        """
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')

        return user_service.get_user_by_token(refresh_token=header)

    # @auth_required
    def patch(self):
        """
        Представление обновляет частично фильм по id, допуск auth
        """
        data = request.json
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')

        return user_service.update_user(data, header)


@user_ns.route('/password/')
class UsersView(Resource):
    # @auth_required
    def put(self):
        """
        Представление заменяет старый пароль пользователя на новый по email, допуск auth
        """
        data = request.json
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')

        return user_service.update_password(data, header)
