from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# создание экземпляра приложения
app = Flask(__name__)
app.debug =  True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config ['SQALCHEMY_TRACK_MODIFICATIONS'] = False # скоро пропадет
db = SQLAlchemy(app)

class  System_s(db.Model):
    __tablename__ = 'systems'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    def __repr__(self):
	       #return "<{}:{}>".format(self.id,  self.title[:10])
           return f'<{self.id}:{self.name[:10]}>'

# https://pythonru.com/uroki/15-osnovy-orm-sqlalchemy
# тут про sqlalchemy
from appp import views
