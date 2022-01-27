from . import app
from flask import render_template, request, redirect, url_for
from .models import *
from sqlalchemy.orm import sessionmaker
import re

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/', methods = ['GET', 'POST'])
def index():

    return render_template('index.html')
# работа с таблицей прототипами
@app.route('/prototypes', methods = ['GET', 'POST'])
def proto_table():
    if request.method == 'POST':
        data2 = request.form['http_link']
        data3 = request.form['id_object']
        data = Prototype(http_link = data2, object_id = data3)
        session.add(data)
        session.commit()
    data_list = session.query(Prototype).all()
    return render_template('prototypes.html', data_list = data_list)
# Эта функция для удаления элементов по ID во всех таблицах
@app.route('/<int:item_id><table_name>', methods=['GET', 'POST'])
def proto_del(item_id, table_name):
    if table_name == 'Prototype':
        id_of_del = session.query(Prototype).filter_by(id=item_id).one()
        re_func_name = 'proto_table'
    elif table_name == 'Object':
        id_of_del = session.query(Object).filter_by(id=item_id).one()
        re_func_name = 'obj_table'
    elif table_name == 'Subject':
        id_of_del = session.query(Subject).filter_by(id=item_id).one()
        re_func_name = 'subj_table'
    elif table_name == 'Measure':
        id_of_del = session.query(Measure).filter_by(id=item_id).one()
        re_func_name = 'measure_table'
    elif table_name == 'Characteristic':
        id_of_del = session.query(Characteristic).filter_by(id=item_id).one()
        re_func_name = 'chars_table'
    session.delete(id_of_del)
    session.commit()
    return redirect(url_for(re_func_name))

@app.route('/change/<int:item_id>', methods = ['GET', 'POST'])
def proto_change(item_id):
    prot_for_change = session.query(Prototype).filter_by(id = item_id).first()
    obj_table = session.query(Object).all()

    if request.method == 'POST':
        prot_for_change.http_link = request.form['http_link']
        prot_for_change.object_id  = request.form['id_object']
        session.add(prot_for_change)
        session.commit()
        return redirect(url_for('proto_table'))
    else:
        return render_template('change_prot.html', prot_for_change = prot_for_change, obj_table = obj_table)
@app.route('/objects', methods = ['GET', 'POST'])
def obj_table():
    if request.method == 'POST':
        data2 = request.form['obj_name']
        data3 = request.form['id_subject']
        data = Object(name = data2, subject_id = data3)
        session.add(data)
        session.commit()
    data_list = session.query(Object).all()
    return render_template('objects.html', data_list = data_list)

@app.route('/subjects', methods = ['GET', 'POST'])
def subj_table():
    if request.method == 'POST':
        data2 = request.form['sub_name']
        data = Subject(name = data2)
        session.add(data)
        session.commit()
    data_list = session.query(Subject).all()
    return render_template('subjects.html', data_list = data_list)

@app.route('/connections')
def sub_obj_prot():
    data_list = session.query(Prototype).join(Object, Prototype.object_id == Object.id).join(Subject, Object.subject_id == Subject.id).all()
    return render_template('sub_obj_prot.html', data_list = data_list)

@app.route('/measures', methods = ['GET', 'POST'])
def measure_table():
    if request.method == 'POST':
        data2 = request.form['meas_name']
        data = Measure(name = data2)
        session.add(data)
        session.commit()
    data_list = session.query(Measure).all()
    return render_template('measures.html', data_list = data_list)

@app.route('/chars', methods = ['GET', 'POST'])
def chars_table():
    if request.method == 'POST':
        data2 = request.form['char_name']
        data = Characteristic(name = data2)
        session.add(data)
        session.commit()
    data_list = session.query(Characteristic).all()
    return render_template('chars.html', data_list = data_list)
