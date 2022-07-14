from project.config import DevelopmentConfig
from project.dao.main import UserDAO
from project.tools.security import generate_password_hash
from project.tools.security import compare_passwords_hash

PWD_HASH_SALT = DevelopmentConfig.PWD_HASH_SALT
PWD_HASH_ITERATIONS = DevelopmentConfig.PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, id):
        """
        Метод возвращает пользователя по id
        """
        return self.dao.get_by_id(id)

    def get_by_email(self, email):
        """
        Метод возвращает пользователя по имени
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
        user_data["password"] = self.generate_password(user_data["password"])
        self.dao.create(user_data)

    def update(self, user_data):
        """
        Метод обновления данных пользователя с хэшированным паролем
        """
        user_data["password"] = self.generate_password(user_data["password"])
        self.dao.update(user_data)
        return self.dao

    def update_partical(self, user_data):
        """
        Метод частично обновляет данные пользователя
        """
        self.dao.update_partical(user_data)
        return self.dao

    def generate_password(self, password):
        """
        Метод хеширование пароля
        """
        return generate_password_hash(password)

    def compare_passwords(self, password_hash, other_password) -> bool:
        """
        Метод сравнения password_hash и other_password
        """
        return compare_passwords_hash(password_hash, other_password)
