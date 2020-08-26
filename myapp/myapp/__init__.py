from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#https://flask.palletsprojects.com/en/1.1.x/patterns/packages/
#https://github.com/pallets/flask/tree/1.1.2/examples/tutorial/flaskr


app = Flask(__name__)
app.config.from_object('config.DevConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import views, models
