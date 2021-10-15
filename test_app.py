from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sys

#static_path = os.path.join(project_root, '../client/static')

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

def inn_list():
    # создаем список ключей
    key_list = []
    for el in pickle_set:
        key_list.append(el)
    return key_list

print('я выполнен')
a = 10
# Главная страница
@app.route('/', methods = ('GET', 'POST'))
def index():
    my_list = inn_list()
    message = str(len(inn_list()))
    #posts = inn_list()

    if request.method == 'POST':
        word = request.form['index']

        if not word:
            flash('Title is required!')
        else:
            a = 10
            #a += 10
            #posts = inn_list(a)
            # выполнение функции

            #return redirect(url_for('index'))





    return render_template('test_index.html', message = message) #posts = posts,

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

if __name__ == "__main__":
    #app.run(host= '0.0.0.0')
    app.run()
