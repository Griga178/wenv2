# for db
import sqlite3
def get_db_connection():
    conn = sqlite3.connect('lils.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(): # все строки из таблицы
    conn = get_db_connection()
    post = conn.execute(f'SELECT * FROM posts').fetchall()
    conn.close()
    if post is None:
        abort(404)
    return post

ins = "INSERT INTO posts (title, content) VALUES ('second Post', 'Content for the 2 post')"

def ins_db(insa): # вставка в бд
    conn = sqlite3.connect('lils.db')
    conn.execute(insa)
    conn.commit()
    conn.close()


#ins_db(ins)
print(f'id,      date,           data,')
for row in get_post():
    print(f'{row[0]}, {row[1]}, {row[2]},')
