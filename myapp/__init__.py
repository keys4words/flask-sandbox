from flask import Flask

#https://flask.palletsprojects.com/en/1.1.x/patterns/packages/
#https://github.com/pallets/flask/tree/1.1.2/examples/tutorial/flaskr


app = Flask(__name__)
app.config.from_object('myapp.config.DevConfig')

from myapp.views import *
