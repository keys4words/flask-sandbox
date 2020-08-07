from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#https://flask.palletsprojects.com/en/1.1.x/patterns/packages/
#https://github.com/pallets/flask/tree/1.1.2/examples/tutorial/flaskr


app = Flask(__name__)
app.config.from_object('myapp.config.DevConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from myapp import views, models
