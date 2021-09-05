#from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# импортируем классы Book и Base из файла database_setup.py
from models import System_s, Base, engine

#engine = create_engine('sqlite:///main.db')
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
editedBook = session.query(System_s).filter_by(id=1).one()
print(editedBook.id, editedBook.name)
# рЕДАКТИРОВАНИЕ UPDATE
#editedBook.author = "Дэн Бейдер"
#session.add(editedBook)
#session.commit()
