#from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime
#from . import db

# Новый источник
# https://pythonru.com/biblioteki/sqlalchemy-v-flask

import sys
from sqlalchemy import Column, ForeignKey, Integer, String
# для определения таблицы и модели
from sqlalchemy.ext.declarative import declarative_base
# для создания отношений между таблицами
from sqlalchemy.orm import relationship # пока не надо
# для настроек
from sqlalchemy import create_engine
# создание экземпляра declarative_base
Base = declarative_base()

my_base = 'sqlite:///appp/main.db'
engine = create_engine(f'{my_base}?check_same_thread=False')

# здесь добавим классы
# мы создаем класс Book наследуя его из класса Base.
'''
class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    genre = Column(String(250))

# создает экземпляр create_engine в конце файла
#engine = create_engine('sqlite:///appp/my_collection.db')

#Base.metadata.create_all(engine)
'''

class  System_s(Base):
    __tablename__ = 'systems'
    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)

Base.metadata.create_all(engine)
