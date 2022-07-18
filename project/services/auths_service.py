import calendar
import datetime

import jwt
from flask import current_app
from flask_restx import abort

from project.services.users_service import UserService
from project.tools.security import compare_passwords_hash


class AuthsService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        """
        Метод, который генерирует access_token и refresh_token, получая email и пароль пользователя
        с проверкой is_refresh (создание новых токенов, а не перегенерация refresh_token)
        """
        user = self.user_service.get_by_email(email)

        if user is None:
            raise abort(404)

        if not is_refresh:
            if not compare_passwords_hash(user.password, password):
                abort(400)

        data = {
            "email": user.email,
            "password": user.password
        }
        # 15 min for access_token
        min15 = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config['TOKEN_EXPIRE_MINUTES'])
        data["exp"] = calendar.timegm(min15.timetuple())
        access_token = jwt.encode(data, key=current_app.config['SECRET_KEY'],
                                  algorithm=current_app.config['ALGORITHM'])

        # 130 days for refresh_token
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=current_app.config['TOKEN_EXPIRE_DAYS'])
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, key=current_app.config['SECRET_KEY'],
                                   algorithm=current_app.config['ALGORITHM'])

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        """
        Метод получает информацию о пользователе, извлекает значение 'email' и по refresh_token,
        который получил в методе generate_tokens вызывает этот же метод и передаёт туда только
        email и получает новую пару токенов
        """
        data = jwt.decode(jwt=refresh_token, key=current_app.config['SECRET_KEY'],
                          algorithms=[current_app.config['ALGORITHM']])
        email = data.get("email")

        return self.generate_tokens(email, None, is_refresh=True)
