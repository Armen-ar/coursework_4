import jwt
from flask import request, abort

from project.config import DevelopmentConfig

SECRET = DevelopmentConfig.SECRET_KEY
ALGORITHM = DevelopmentConfig.ALGORITHM


def auth_required(func):
    """
    Метод проверяет авторизацию, наличие токена и его декодирование
    """
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]

        print(token)
        try:
            jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        return func(*args, **kwargs)

    return wrapper
