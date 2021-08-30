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

def old_get(table_name):
    conn = get_db_connection()
    row_list = conn.execute(table_name).fetchall()
    conn.close()
    if row_list is None:
        print(404)
    else:
        for row in row_list:
            print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} ')

def new_get(table_name):
    conn = get_db_connection()
    row_list = conn.execute(table_name).fetchall()
    conn.close()
    if row_list is None:
        print(404)
    else:
        for row in row_list:
            new_list=[]
            for i in row:
                new_list.append(i)
            print(' '.join(new_list))
            #print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} ')

#get_info('answers')
#get_info('companies')
#get_info('emploers')

#ins = "INSERT INTO answers_emploers_companies (answers_id, emploer_id, companies_id) VALUES (1, 1, 1)"
ins = "SELECT name, small_name FROM companies INNER JOIN forms ON forms.form_id = companies.form;"

ins2 = "SELECT short_form, company_name, answer_number, answer_date, emploer_name, emploer_surname FROM answers INNER JOIN emploers ON emploers.emploer_id = answers.emploer INNER JOIN companies ON companies.company_id = answers.company INNER JOIN forms ON forms.form_id = companies.company_form;"
new_get(ins2)

#get_info('answers_emploers_companies')
