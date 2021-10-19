from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sys

#static_path = os.path.join(project_root, '../client/static')
#https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-ru
#https://pythonru.com/tag/uroki-po-flask-na-russkom/page/2

#https://habr.com/ru/post/347926/

app = Flask(__name__)
#app = Flask(__name__, static_folder = static_path)
app.config['SECRET_KEY'] = 'your secret key'

# База данных - Словари, множества
test_set = {'Компьютер', 'Стул'}

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

    if request.method == 'GET':
        posts = inn_list()

    if request.method == 'POST':
        inn_value = request.form['INN']

        if not inn_value:
            flash('Title is required!')
        else:
            print(inn_value)

            try:
                posts = pickle_set[inn_value]
            except:
                posts = ['Значение не найдено']

            return render_template('test_index.html', posts = posts)

    return render_template('test_index.html', posts = posts[0:10]) #,

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
    # Первый вход на страницу
    if request.method == 'GET':
        # вывод первых 10 компаний из общего списка
        posts = inn_list()
        current_page = 20

    elif request.method == 'POST':
        try:
            # Если задействована форма номера страницы
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
            form_value = int(list_of_page)
            posts = inn_list(form_value, form_value + 10)
        else:
            # поиск ключа в словаре
            try:
                posts = pickle_set[form_data]
            except:
                posts = ['Значение не найдено']


    return render_template('test_companies.html', posts = posts)


if __name__ == "__main__":
    #app.run(host= '0.0.0.0')
    app.run(debug = True)
