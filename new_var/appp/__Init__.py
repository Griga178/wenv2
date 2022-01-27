from flask import Flask

# создание экземпляра приложения
app = Flask(__name__) #static_folder="static")
app.debug =  True


from appp import views
