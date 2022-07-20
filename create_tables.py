from project.config import DevelopmentConfig
from project.server import create_app
from project.setup.db import db

if __name__ == '__main__':
    with create_app(DevelopmentConfig).app_context():
        """
        Создаёт таблицы
        """
        db.create_all()
