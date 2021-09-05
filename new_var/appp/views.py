from . import app
from flask import render_template, request, redirect, url_for
from .models import Base, System_s, engine
from sqlalchemy.orm import sessionmaker

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def index():
    info = session.query(System_s).all()

    return render_template('index.html', list = info)

# Эта функция позволит создать новую книгу и сохранить ее в базе данных.
@app.route('/new', methods=['GET', 'POST'])
def newSys():
    if request.method == 'POST':
        newSys = System_s(name = request.form['name'])
        session.add(newSys)
        session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('newSys.html')
