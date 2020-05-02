import os
from sqlalchemy import Column, String, Integer, DateTime
from flask_sqlalchemy import SQLAlchemy
import json


db = SQLAlchemy()

if os.getenv('ENV') == 'prod':
    database_path = os.getenv('DATABASE_URL')

if os.getenv('ENV') == 'dev':
    database_name = "castingAgency"
    database_path = "postgres://{}/{}".format('localhost:5432', database_name)

print(os.getenv('ENV'))
'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Movies(db.Model):

    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    releaseDate = Column(DateTime)

    # CRUD
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # json
    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "releaseDate": self.releaseDate
        }


class Actors(db.Model):

    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

    # CRUD
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # json
    def format(self):
        return {
            "id": self.id,
            "title": self.name,
            "age": self.age,
            "gender": self.gender
        }
