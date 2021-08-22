# my SQLite DB
import sqlite3

connection = sqlite3.connect('lils.db') #sitebase

with open('lils.sql') as f: #site_schema
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

# записываем в БД первые данные (пример)

connection.commit()
connection.close()
