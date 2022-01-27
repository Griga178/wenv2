from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sys
from flask_sqlalchemy import SQLAlchemy
from test_bases import *

#static_path = os.path.join(project_root, '../client/static')
#https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-ru
#https://pythonru.com/tag/uroki-po-flask-na-russkom/page/2

#https://habr.com/ru/post/347926/

app = Flask(__name__, template_folder = "test_templates")
#app = Flask(__name__, static_folder = static_path)
app.config['SECRET_KEY'] = 'your secret key'

# База данных - Словари, множества
test_set = {'Компьютер', 'Стул'}
db = SQLAlchemy(app)
#db.create_all()

# Функции
import pickle
file_name = 'comp_info.pkl'
with open(file_name, 'rb') as f:
    pickle_set = pickle.load(f)
    ### НАДО ОТСОРТИРОВАТЬ

def inn_list():
    # создаем список ключей
    key_list = []
    for el in pickle_set:
        key_list.append(el)
    return key_list

def show_list(list_name, amount = 20, cur_page = 0):
    return list_name[cur_page:cur_page + amount]



# Главная страница
@app.route('/', methods = ('GET', 'POST'))
def index():
    list_of_values = []

    if request.method == 'POST':
        values = request.form['values_form']
        list_of_values = values.split(" ")
        print(values)


    return render_template('test_index.html', list_of_values = list_of_values)

@app.route('/tables_pages', methods = ('GET', 'POST'))
def tables_pages():
    list_of_values = []

    if request.method == 'POST':
        values = request.form['values_form']
        list_of_values = values.split(" ")
        print(values)


    return render_template('test_tables.html')
# добавление слова в множество
@app.route('/create', methods = ('GET', 'POST'))
def create():
    if request.method == 'POST':
        word = request.form['title']

        if not word:
            flash('Title is required!')
        else:
            test_set.add(word)

            return redirect(url_for('index'))

    return render_template('test_create.html')


# Страница работы с ПОСТАВЩИКАМИ
@app.route('/companies', methods = ('GET', 'POST'))
def show_companies():
    amoint_of_companies = ""
    posts = []
    comp_key_list = inn_list()

    # Первый вход на страницу
    if request.method == 'GET':
        # вывод первых 10 компаний из общего списка
        amoint_of_companies = len(comp_key_list)
        #posts = show_list(comp_key_list)
        #current_page = 20
    elif request.method == 'POST':
        try:
            # Если задействована форма номера страницы (способ слушать разные формы с 1 страницы)
            list_of_page = request.form['page_number']
            script_number = 1
        except:
            list_of_page = None

        try:
            # Если задействована форма поиска по инн
            form_data = request.form['companies_form']
            script_number = 2
        except:
            form_data = None


        if script_number == 1:
            # Идем по этому сценарию, потому что выбрана соотв. форма
            form_value = int(list_of_page)
            posts = inn_list(form_value, form_value + 10)
        else:
            # поиск ключа в словаре
            try:
                # Список инн
                list_of_values = form_data.split(" ")
                for value in list_of_values:
                    if value in comp_key_list:
                        posts.append(value)
                #posts = [form_data]
            except:
                posts = ['Значение не найдено']


    return render_template('test_companies.html', posts = posts, pickle_set = pickle_set, amoint_of_companies = amoint_of_companies)

@app.route('/working_table', methods = ('GET', 'POST'))
def working_table():
    return render_template('test_working_table.html')

if __name__ == "__main__":
    #app.run(host= '0.0.0.0')
    app.run(debug = True)
