# my SQLite DB
import sqlite3

connection = sqlite3.connect('lils.db') #sitebase

with open('lils.sql') as f: #site_schema
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO forms (short_form, long_form) VALUES ('ООО', 'Общество с ограниченной ответственностью')")
cur.execute("INSERT INTO forms (short_form, long_form) VALUES ('ИП', 'Индивидуальный предприниматель')")
cur.execute("INSERT INTO forms (short_form, long_form) VALUES ('ПАО', 'Публичное акционерное общество')")

cur.execute("INSERT INTO companies (company_name, company_inn, company_form) VALUES ('СИТИЛИНК', '7718979307', 1)")
cur.execute("INSERT INTO companies (company_name, company_inn, company_form) VALUES ('ДНС', '7718979308', 1)")
cur.execute("INSERT INTO companies (company_name, company_inn, company_form) VALUES ('Газпром', '7718979309', 3), ('Петров Иван Владимирович', '7718979309234', 2)")
cur.execute("INSERT INTO companies (company_name, company_inn, company_form) VALUES ('Петров Иван Владимирович', '7718979309234', 2)")

cur.execute("INSERT INTO emploers (emploer_name, emploer_surname, emploer_patronymic) VALUES ('Петр', 'Иванов', 'Иванович')")

cur.execute("INSERT INTO answers (answer_number, answer_date, company, emploer) VALUES ('0525', '23.08.2021', 1, 1)")
cur.execute("INSERT INTO answers (answer_number, answer_date, company, emploer) VALUES ('0526', '23.08.2021', 2, 1)")
#cur.execute("INSERT INTO answers (num, dat) VALUES ('0525', '23.08.2021')")
#cur.execute("INSERT INTO answers_emploers_companies (answers_id, emploer_id, companies_id) VALUES ('1', '1', '1')")

# записываем в БД первые данные (пример)

connection.commit()
connection.close()
