from flask_sqlalchemy import SQLAlchemy
from test_app import db

class Prototypes(db.Model):
    ''' Таблица содержащая конкретные прототипы и ссылки на них
        + связь с экземляром прототипа, "его описанием"
        прим.: (1, citilink/macbook0123.html, 1)'''
    __tablename__ = 'prototypes'
    id = db.Column(db.Integer(), primary_key=True)
    link = db.Column(db.String(255), nullable=False)
    object_id = db.Column(db.Integer(), db.ForeignKey('objects.id'))

    def __repr__(self):
	       return f'{self.id}:{self.link[:10]}'

class Objects(db.Model):
    ''' Таблица содержащая принадлежность прототипа к объекту
        + его принадлежность к категории (ноутбук)
        прим.: (1, 'macbookpro a1226', 1)'''
    __tablename__ = 'objects'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    prototypes_of = db.relationship('Prototypes', backref='object')
    subject_id = db.Column(db.Integer(), db.ForeignKey('subjects.id'))

    def __repr__(self):
	       return "<{}:{}>".format(self.id,  self.title[:10])

class Subjects(db.Model):
    ''' Таблица содержащая принадлежность предмета к категории
        прим.: (1, 'Ноутбук')'''
    __tablename__ = 'subjects'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    subject_of = db.relationship('Objects', backref='subject')

    def __repr__(self):
	       return "<{}:{}>".format(self.id,  self.title[:10])

#db.create_all()
