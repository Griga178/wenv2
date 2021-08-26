# for db
import sqlite3
def get_db_connection():
    conn = sqlite3.connect('lils.db')
    conn.row_factory = sqlite3.Row
    return conn

ins = "INSERT INTO answers (title, content) VALUES ('second Post', 'Content for the 2 post')"

def ins_db(insa): # вставка в бд
    conn = sqlite3.connect('lils.db')
    conn.execute(insa)
    conn.commit()
    conn.close()

def get_info(table_name):
    conn = get_db_connection()
    row_list = conn.execute(f'SELECT * FROM {table_name}').fetchall()
    conn.close()
    if row_list is None:
        print(404)
    else:
        print(f'{table_name}')
        for row in row_list:
            print(f'{row[0]},   {row[1]},   {row[2]}')

def new_get(table_name):
    conn = get_db_connection()
    row_list = conn.execute(table_name).fetchall()
    conn.close()
    if row_list is None:
        print(404)
    else:
        for row in row_list:
            print(f'{row[0]},   {row[1]}')

#get_info('answers')
#get_info('companies')
#get_info('emploers')

#ins = "INSERT INTO answers_emploers_companies (answers_id, emploer_id, companies_id) VALUES (1, 1, 1)"
ins = "SELECT name, small_name FROM companies INNER JOIN forms ON forms.id = companies.form_id;"
new_get(ins)

#get_info('answers_emploers_companies')
