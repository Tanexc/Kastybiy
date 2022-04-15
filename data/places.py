import datetime
import sqlalchemy
from sqlalchemy import orm
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Place(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "places"

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    category = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    adress = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    mapPath = sqlalchemy.Column(sqlalchemy.String, nullable=True)
