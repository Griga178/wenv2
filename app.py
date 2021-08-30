import os
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, send_from_directory
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename


# https://flask-russian-docs.readthedocs.io/ru/latest/patterns/fileuploads.html
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xlsx'])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def get_db_connection(name):
    conn = sqlite3.connect(name)
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection('database.db')
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/new')
def new():
    conn = get_db_connection('lils.db')
    posts = conn.execute('SELECT answer_number, answer_date, emploer_name, emploer_surname, short_form, company_name FROM answers INNER JOIN emploers ON emploers.emploer_id = answers.emploer INNER JOIN companies ON companies.company_id = answers.company INNER JOIN forms ON forms.form_id = companies.company_form;').fetchall()
    conn.close()
    return render_template('new.html', posts=posts)

# Главная страница
@app.route('/')
def index():
    conn = get_db_connection('database.db')
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

def all_post(table_name):
    conn = get_db_connection('lils.db')
    post = conn.execute(f'SELECT * FROM {table_name};').fetchall()
    if post is None:
        abort(404)
    return post




# вывод строки из бд по post_id
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection('database.db')
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')




def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=('GET', 'POST'))
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return render_template('index.html')
            return redirect(url_for('upload_file',
                                    filename=filename))
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection('database.db')
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection('database.db')
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

if __name__ == "__main__":
    #app.run(host= '0.0.0.0')
    app.run()
