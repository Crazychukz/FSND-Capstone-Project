import os
from sqlalchemy import Column, String, Integer, Table, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import json
from flask_migrate import Migrate

DATABASE_URL = os.environ.get('DATABASE_URL')

db = SQLAlchemy()
Base = declarative_base()


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    migrate = Migrate(app, db)


casts = db.Table('casts',
                 Column('movie_id', Integer, ForeignKey('movie.id')),
                 Column('actor_id', Integer, ForeignKey('actor.id'))
                 )


class Movie(db.Model):
    __tablename__ = 'movie'

    id = Column(Integer(), primary_key=True)
    title = Column(String(200), unique=True)
    release_date = Column(db.Date, nullable=False)
    genres = db.Column(db.String(500), nullable=True)
    casts = db.relationship('Actor', secondary=casts, backref=db.backref('movie_casts', lazy='dynamic'))
    '''
    short() short form representation of the Movie model
    '''

    def short(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'casts': [i.short() for i in self.casts]
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a model into a database
        the model must exist in the database
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a model into a database
        the model must exist in the database
    '''

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())


class Actor(db.Model):
    __tablename__ = 'actor'
    id = Column(Integer(), primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=True)
    age = Column(Integer, nullable=True)

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())
