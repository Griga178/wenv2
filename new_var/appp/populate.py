from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# импортируем классы Book и Base из файла database_setup.py
from models import Book, Base

engine = create_engine('sqlite:///my_collection.db')
# Свяжим engine с метаданными класса Base,
# чтобы декларативы могли получить доступ через экземпляр DBSession
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# Экземпляр DBSession() отвечает за все обращения к базе данных
# и представляет «промежуточную зону» для всех объектов,
# загруженных в объект сессии базы данных.
session = DBSession()

'''
# добавление данных (INSERT)
bookOne = Book(title="Чистый Python", author="Дэн Бейде", genre="компьютерная литература")
session.add(bookOne)
session.commit()
'''

'''
# SELECT чтение данных из таблицы
a = session.query(Book).all()
for i in a:
    print(i.title)
b = session.query(Book).first()
print(b.title)
'''
# Поиск с фильтром
editedBook = session.query(Book).filter_by(id=1).one()
print(editedBook.title, editedBook.author)
# рЕДАКТИРОВАНИЕ UPDATE
editedBook.author = "Дэн Бейдер"
session.add(editedBook)
session.commit()
