"""
  This file contains all the database connection definition,
  and all the CRUD for category and question tables.
"""

from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy

DATABASE_NAME = "trivia"
# DATABASE_PATH = "postgres://{}/{}".format('localhost:5432', DATABASE_NAME)
DATABASE_PATH = "postgres://{}:{}@{}/{}".format(
    'postgres', 'postgres', 'localhost:5432', DATABASE_NAME)
DB = SQLAlchemy()


def setup_db(app, database_path=DATABASE_PATH):
    """ Database setup """
    print(database_path)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.app = app
    DB.init_app(app)
    DB.create_all()


# Question


class Question(DB.Model):
    """ Question table definition """
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    category = Column(String)
    difficulty = Column(Integer)

    def __init__(self, question, answer, category, difficulty):
        self.question = question
        self.answer = answer
        self.category = category
        self.difficulty = difficulty

    def insert(self):
        """ Insert data into Question table """
        DB.session.add(self)
        DB.session.commit()

    def update(self):
        """ Update data on Question table"""
        DB.session.commit()

    def delete(self):
        """ Delete data on Question table"""
        DB.session.delete(self)
        DB.session.commit()

    def format(self):
        """ Serialize Question table data for json object """
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'category': self.category,
            'difficulty': self.difficulty
        }


# Category


class Category(DB.Model):
    """ Category table definition """
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    type = Column(String)

    def __init__(self, type):
        self.type = type

    def format(self):
        """ Serialize Category table data for json object """
        return {
            'id': self.id,
            'type': self.type
        }
