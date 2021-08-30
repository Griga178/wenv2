#new_app

# Функция выводит выбранную таблицу целиком
def get_db_connection(name):
    conn = sqlite3.connect(name)
    conn.row_factory = sqlite3.Row
    return conn

def all_post(table_name):
    conn = get_db_connection('lils.db')
    post = conn.execute(f'SELECT * FROM {table_name};').fetchall()
    if post is None:
        abort(404)
    return post
