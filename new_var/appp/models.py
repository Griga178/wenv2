#from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime
#from . import db

# Новый источник
# https://pythonru.com/biblioteki/sqlalchemy-v-flask

import sys
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

# здесь добавим классы

association_table = Table('association', Base.metadata,
    Column('left_id', ForeignKey('systems.id')),
    Column('right_id', ForeignKey('systems.id'))
)

class  System_s(Base):
    __tablename__ = 'systems'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


Base.metadata.create_all(engine)
