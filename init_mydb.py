# my SQLite DB
import sqlite3

connection = sqlite3.connect('lils.db') #sitebase

with open('lils.sql') as f: #site_schema
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO forms (small_name, full_name) VALUES ('ООО', 'Общество с ограниченной ответственностью')")
cur.execute("INSERT INTO forms (small_name, full_name) VALUES ('ИП', 'Индивидуальный предприниматель')")

cur.execute("INSERT INTO companies (name, inn, form_id) VALUES ('СИТИЛИНК', '7718979307', 1)")
cur.execute("INSERT INTO emploers (name, surname, patronymic) VALUES ('Иванов', 'Петр', 'Иванович')")
#cur.execute("INSERT INTO answers (num, dat) VALUES ('0525', '23.08.2021')")
#cur.execute("INSERT INTO answers_emploers_companies (answers_id, emploer_id, companies_id) VALUES ('1', '1', '1')")

# записываем в БД первые данные (пример)

connection.commit()
connection.close()
