from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genre'

    name = Column(String(100), unique=True, nullable=False)


# class GenreSchema(Schema):
#     id = fields.Int()
#     name = fields.Str()


class Director(models.Base):
    __tablename__ = 'director'

    name = Column(String(100), unique=True, nullable=False)


# class DirectorSchema(Schema):
#     id = fields.Int()
#     name = fields.Str()


class Movie(models.Base):
    __tablename__ = 'movie'

    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    trailer = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey("genre.id"), nullable=False)
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey("director.id"), nullable=False)
    director = relationship("Director")


# class MovieSchema(Schema):
#     id = fields.Int()
#     title = fields.Str()
#     description = fields.Str()
#     trailer = fields.Str()
#     year = fields.Int()
#     rating = fields.Float()
#     director = fields.Pluck('DirectorSchema', 'name')
#     genre = fields.Pluck('GenreSchema', 'name')


class User(models.Base):
    __tablename__ = 'user'

    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))
    favorite_genre = Column(Integer, ForeignKey("genre.id"))
    favorite = relationship("Genre")


# class UserSchema(Schema):
#     id = fields.Int()
#     email = fields.Str()
#     password = fields.Str()
#     name = fields.Str()
#     surname = fields.Str()
#     favorite = fields.Pluck('GenreSchema', 'name')
