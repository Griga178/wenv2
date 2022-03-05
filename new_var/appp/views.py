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


@app.route('/information')
def subject_iformation():
    main_query = session.query(Subject).order_by(Subject.name).all()

    return render_template('subject_information.html', main_query = main_query)

@app.route('/model_informations/<int:model_id>')
def model_information(model_id):
    main_query = session.query(Model_char_measure_val).filter_by(model_id = model_id).all()
    linqs_query = session.query(Prototype).filter_by(object_id = model_id).all()
    return render_template('models_info.html', main_query = main_query, linqs_query = linqs_query)

@app.route('/model_set/<int:model_id>')
def model_setting(model_id):
    main_query = session.query(Object).filter_by(id = model_id).all()
    return render_template('model_setting.html', main_query = main_query)

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
        id_of_del = session.query(Prototype).filter_by(id = item_id).one()
        re_func_name = 'proto_table'
    elif table_name == 'Object':
        id_of_del = session.query(Object).filter_by(id = item_id).one()
        re_func_name = 'obj_table'
    elif table_name == 'Subject':
        id_of_del = session.query(Subject).filter_by(id = item_id).one()
        re_func_name = 'subj_table'
    elif table_name == 'Measure':
        id_of_del = session.query(Measure).filter_by(id = item_id).one()
        re_func_name = 'measure_table'
    elif table_name == 'Characteristic':
        id_of_del = session.query(Characteristic).filter_by(id = item_id).one()
        re_func_name = 'chars_table'
    elif table_name == 'Mchmeva':
        id_of_del = session.query(Model_char_measure_val).filter_by(some_id = item_id).one()
        re_func_name = 'mcmv_table'
    elif table_name == 'Groups':
        id_of_del = session.query(Groups).filter_by(id = item_id).one()
        re_func_name = ('index')
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
        producer_link = request.form['producer_link']
        data = Object(name = data2, subject_id = data3, producer_link = producer_link)
        session.add(data)
        session.commit()
    data_list = session.query(Object).all()
    subject_dict = session.query(Subject).all()
    return render_template('objects.html', data_list = data_list, subject_dict = subject_dict)

@app.route('/subjects', methods = ['GET', 'POST'])
def subj_table():
    if request.method == 'POST':
        data2 = request.form['sub_name']
        data = Subject(name = data2)
        session.add(data)
        session.commit()
    data_list = session.query(Subject).all()
    return render_template('subjects.html', data_list = data_list)



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

@app.route('/mcmv', methods = ['GET', 'POST'])
def mcmv_table():
    if request.method == 'POST':
        data2 = request.form['model_id']
        data3 = request.form['char_id']
        data4 = request.form['mes_id']
        data1 = request.form['value']
        data = Model_char_measure_val(model_id = data2, char_id = data3, measure_id = data4, chars_val = data1)
        session.add(data)
        session.commit()
    data_list = session.query(Model_char_measure_val).order_by(Model_char_measure_val.model_id).all()
    model_dict = session.query(Object).all()
    chars_dict = session.query(Characteristic).all()
    measure_dict = session.query(Measure).all()
    return render_template('mcmv.html', data_list = data_list,
    model_dict = model_dict, chars_dict = chars_dict, measure_dict = measure_dict)


def func_for_table(subject_id):
    """ Создаем set, в котором будут:
        сам запрос в sql
        все названия характеристик моделей"""
    model_flaskdict = session.query(Object).filter_by(subject_id = subject_id).all()
    chars_set = set()
    # по id моделей выгружаем характеристики
    for model in model_flaskdict:
        mcmv_flaskdict = session.query(Model_char_measure_val).filter_by(model_id = model.id).all()
        for chars in mcmv_flaskdict:
            name = chars.char_name.name
            chars_set.add(name)
    return model_flaskdict, chars_set

@app.route('/model_compare/<int:subject_ids>', methods = ['GET', 'POST'])
def model_compare_func(subject_ids = 4):
    some_table = func_for_table(subject_ids)
    main_query = session.query(Subject).filter_by(id = subject_ids).all()
    if len(some_table[0]) == 0:
        #url_for('model_compare_func', subject_ids = 4)
        return render_template('subjects.html')
    else:
        return render_template('model_compare.html', data = some_table[0], chars_set = some_table[1], main_query = main_query)

@app.route('/sortded')
def subject_groups():
    return render_template('subjects_group.html')

@app.route('/groups/<int:step><int:group_id>', methods = ['GET', 'POST'])
def chars_group(step, group_id):
    groups_dict = session.query(Groups).all()
    chars_dict = False
    groupp_name = ['']
    if step == 1:
        groupp_name = session.query(Groups).filter_by(id = group_id).all()
        chars_dict = session.query(Groups_measure).filter_by(groups_id = group_id).all()
    if request.method == 'POST':
        if 'add_group' in request.form:
            data = Groups(name = request.form['group_name'])
            session.add(data)
            session.commit()
        else:
            data = Groups_measure(groups_id = request.form['group_id'],
                char_id = request.form['char_id'],
                chars_val_from_to = request.form['chars_val_from_to'],
                chars_val = request.form['chars_val'],
                measure_id = request.form['measure_id'])
            session.add(data)
            session.commit()
        print(request.form)
    return render_template('groups.html', groups_dict = groups_dict, chars_dict = chars_dict, groupp_name = groupp_name)
