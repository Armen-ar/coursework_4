from project.config import DevelopmentConfig
from project.models import Genre, Director, Movie, User
from project.server import create_app, db

app = create_app(DevelopmentConfig)


@app.shell_context_processor
def shell():
    """
    Метод возвращает модели сущностей
    """
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director,
        "Movie": Movie,
        "User": User,
    }


if __name__ == '__main__':
    app.run(
        host="localhost",
        debug=True
    )


# host="localhost",
# debug=True
# port=25000
