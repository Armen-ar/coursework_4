from flask_restx import abort

from project.dao.main import UserDAO
from project.tools.security import generate_password_hash
from project.tools.security import compare_passwords_hash


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
        return self.dao.get_by_email(email)

    def get_all(self):
        """
        Метод возвращает всех пользователей
        """
        return self.dao.get_all()

    def create(self, user_data):
        """
        Метод добавляет нового пользователя с хэшированным паролем
        """
        user_data["password"] = generate_password_hash(user_data["password"])
        self.dao.create(user_data)

    def update(self, user_data):
        """
        Метод обновления данных пользователя с хэшированным паролем
        """
        user_data["password"] = generate_password_hash(user_data["password"])
        self.dao.update(user_data)
        return user_data

    def update_partical(self, user_data):
        """
        Метод частично обновляет данные пользователя
        """
        self.dao.update_partical(user_data)
        return self.dao

    def password_change(self, password: str, other_password: str, email):
        """
        Метод замены пароля пользователя
        """
        user = self.get_by_email(email)
        user_password = user.password
        new_password = generate_password_hash(password)
        old_password = generate_password_hash(other_password)

        if compare_passwords_hash(old_password, user_password):
            user.password = new_password

            return self.dao.update(user)
        else:
            abort(404)
