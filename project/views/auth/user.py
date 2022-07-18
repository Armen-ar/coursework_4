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
    def get(self, email):
        """
        Представление возвращает информацию о пользователе, допуск auth
        """
        user_ = user_service.get_by_email(email)

        return user_, 200

    @auth_required
    def patch(self, uid):
        """
        Представление обновляет частично фильм по id, допуск auth
        """
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update_partical(req_json)
        return "", 204


@user_ns.route('/password/')
class UsersView(Resource):
    @auth_required
    def put(self):
        """
        Представление заменяет старый пароль пользователя на новый по email, допуск auth
        """
        req_json = request.json
        other_password = req_json['old_password']
        password = req_json['new_password']
        email = req_json.get('email')
        user = user_service.password_change(password, other_password, email)
        uid = user.id
        data = {'id': uid, 'password': password}
        user_service.update(data)

        return "", 200
