import sqlite3

# Подключение к БД SQLite (требуется закрытие!)
def get_db_connection(name):
    conn = sqlite3.connect(name)
    conn.row_factory = sqlite3.Row
    return conn

# Вывод всего содержимого таблицы
def all_post(table_name):
    conn = get_db_connection('lils.db')
    post = conn.execute(f'SELECT * FROM {table_name};').fetchall()
    conn.close()
    if post is None:
        abort(404)
    else:
        list_of_lists = []
        for row in post:
            list = []
            for el in row:
                list.append(el)
            list_of_lists.append(list)
    return list_of_lists
