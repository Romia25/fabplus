from flask_appbuilder import Model
from sqlalchemy import INTEGER, Column, Integer, String
from .. import db
# from config import SQLALCHEMY_BINDS


class Line(Model):
    __tablename__ = 'line'
    __bind_key__ = 'DB1'  # Specify the binding key for this model
    id = Column(INTEGER, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def insert_intoLine(name, age):
        el_line = Line(name, age)
        db.session.add(el_line)
        db.session.commit()

# class Line(Model):
#     __bind_key__ = 'DB2'  # Specify the binding key for this model
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     age = Column(Integer)

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @staticmethod
#     def insert_intoLine(name, age):
#         el_line = Line(name, age)
#         db.session.add(el_line)
#         db.session.commit()

# class Line(Model):
#     # __bind_key__ = 'DB1'  # Specify the binding key for this model
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     age = Column(Integer)

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @staticmethod
#     def insert_intoLine(name, age):
#         el_line = Line(name, age)
#         db.session.add(el_line)
#         db.session.commit()
