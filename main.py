from flask import Flask, render_template, request, url_for
from db_func import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

main_select = 'SELECT answer_number, answer_date, emploer_name, emploer_surname, short_form, company_name FROM answers INNER JOIN emploers ON emploers.emploer_id = answers.emploer INNER JOIN companies ON companies.company_id = answers.company INNER JOIN forms ON forms.form_id = companies.company_form;'

@app.route('/')
def index():
    conn = get_db_connection('lils.db')
    posts = conn.execute(main_select).fetchall()
    conn.close()
    return render_template('main.html', posts=posts)

#на этой странице выводятся таблицы по сссылке
@app.route('/<table_name>')
def new_post(table_name):
    posts = all_post(table_name)
    return render_template('new_post.html', posts=posts)


if __name__ == "__main__":
    #app.run(host= '0.0.0.0')
    app.run()
