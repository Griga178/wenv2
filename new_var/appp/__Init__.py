from flask import Flask
#from sqlalchemy import create_engine

# создание экземпляра приложения
app = Flask(__name__)
app.debug =  True


# https://pythonru.com/uroki/15-osnovy-orm-sqlalchemy
# тут про sqlalchemy

from appp import views
