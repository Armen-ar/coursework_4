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
#
# Если нужно заменить port, тогда и в документе 'main.0041c12b.chunk.js'
# нужно будет заменить 'localhost:5000' на '127.0.0.1:25000'
# debug=True
# port=25000
