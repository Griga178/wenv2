#from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime
#from . import db

# Новый источник
# https://pythonru.com/biblioteki/sqlalchemy-v-flask

#import sys
#from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
# для создания отношений между таблицами
from sqlalchemy.orm import relationship # пока не надо
# для настроек
from sqlalchemy import *

# для определения таблицы и модели
# создание экземпляра declarative_base
Base = declarative_base()

my_base = 'sqlite:///main.db' #appp/
engine = create_engine(f'{my_base}?check_same_thread=False')


class Prototype(Base):
    """Тут хранятся ссылки на товары
        привязаны к своей модели"""
    __tablename__ = 'prototypes'
    id = Column(Integer, primary_key = True)
    http_link = Column(String(255), nullable = False)
    object_id = Column(Integer, ForeignKey('objects.id'))
    object_name = relationship('Object') #, lazy = 'dynamic'

class Object(Base):
    """Тут хранятся известные модели товаров
        с привязкой к названию предмета"""
    __tablename__ = 'objects'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable = False)
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    subject_name = relationship('Subject')
    #prototypes = relationship("Prototype", backref='objects')

class Subject(Base):
    """Тут хранятся названия предметов"""
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable = False)
    #objects = relationship("Object", backref='subjects')

class Measure(Base):
    """ Единицы измерения """
    __tablename__ = 'measures'
    id = Column(Integer, primary_key = True)
    name = Column(String(255), nullable = False)

class Characteristic(Base):
    ''' Характеристики '''
    __tablename__ = 'char_s'
    id = Column(Integer, primary_key = True)
    name = Column(String(255), nullable = False)
    measure_id = Column(Integer, ForeignKey('measures.id'))
    measure_name = relationship('Measure')
Base.metadata.create_all(engine)
