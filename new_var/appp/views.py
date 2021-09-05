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

# Эта функция позволит создать новую элемент и сохранить его в базе данных.
@app.route('/new', methods=['GET', 'POST'])
def newSys():
    if request.method == 'POST':
        newSys = System_s(name = request.form['name'])
        session.add(newSys)
        session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('newSys.html')

# Эта функция для удаления элементов
@app.route('/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteSys(item_id):
    sysToDelete = session.query(System_s).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(sysToDelete)
        session.commit()
        return redirect(url_for('index', item_id = item_id))
    else:
        return render_template('deleteSys.html', system_s = sysToDelete)

# Функция создающяя связи между элементами
@app.route('/<int:item_id>/consist_of/', methods=['GET', 'POST'])
def sys_consists(item_id):
    # тут все элементы этой системой
    #sys_elements = session.query
    pass
