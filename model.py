import os
from sqlalchemy import Column, String, Integer, create_engine, DateTime
from flask_sqlalchemy import SQLAlchemy
import json


db = SQLAlchemy()
database_name = "castingAgency"

# setup for local mode.
# database_path = "postgres://{}/{}".format('localhost:5432', database_name)
# database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))
# database_filename = "castingAgency.db"
# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_path=database_path


'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://znjwtsmkzfozca:59bcec5b00859bcf407466a555657eb712b260d8d06b512f9420532a13043d2c@ec2-34-234-228-127.compute-1.amazonaws.com:5432/d2mulmshfgth62"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

# Schema


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
