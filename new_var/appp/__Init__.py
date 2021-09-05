from flask import Flask

# создание экземпляра приложения
app = Flask(__name__)
app.debug =  True


from appp import views
