import jwt
from flask import request, abort, current_app


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
            jwt.decode(token, key=current_app.config['SECRET_KEY'],
                       algorithms=current_app.config['ALGORITHM'])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        req_json = request.json
        email = req_json.get('email')

        return func(*args, **kwargs, email=email)

    return wrapper
