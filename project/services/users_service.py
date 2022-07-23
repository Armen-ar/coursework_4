from project.dao.main import UserDAO
from project.tools.security import generate_password_hash, generate_tokens, approve_refresh_token, get_data_from_token


class UserService:
    def __init__(self, dao: UserDAO):
        """
        Конструктор для всех методов класса
        """
        self.dao = dao

    def get_one(self, id):
        """
        Метод возвращает пользователя по id
        """
        return self.dao.get_by_id(id)

    def get_by_email(self, email):
        """
        Метод возвращает пользователя по логину
        """
        return self.dao.get_user_by_email(email)

    def get_all(self):
        """
        Метод возвращает всех пользователей
        """
        return self.dao.get_all()

    def create(self, user_data):
        """
        Метод создаёт пользователя по email и password
        """
        user_data["password"] = generate_password_hash(user_data["password"])
        self.dao.create(user_data)

    def update_user(self, data: dict, refresh_token):
        """
        Метод обновляет данные пользователя(добавляет имя фамилия и любимый жанр) с хэшированным паролем
        """
        user = self.get_by_email(refresh_token)
        if user:
            self.dao.update(user.email, data)
            return self.get_by_email(refresh_token)

    def check(self, email, password):
        """
        Метод возвращает данные пользователя по паролю
        """
        user = self.get_by_email(email)
        return generate_tokens(user.email, password, user.password)

    def update_token(self, refresh_token):
        """
        Метод по refresh_token обновляет access_token и refresh_token
        """
        return approve_refresh_token(refresh_token)

    def get_user_by_token(self, refresh_token):
        """
        Метод возвращает email пользователя по refresh_token
        """
        data = get_data_from_token(refresh_token)

        if data:
            return self.get_by_email(data.get('email'))

    def update_password(self, data: dict, refresh_token):
        """
        Метод заменяет пароль пользователя
        """
        user = self.get_user_by_token(refresh_token)
        if user:
            self.dao.update(user.email, {"password": generate_password_hash(data.get('password_2'))})
            return self.check(user.email, data.get('password_2'))
