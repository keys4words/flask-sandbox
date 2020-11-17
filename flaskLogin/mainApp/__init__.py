from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'myVerySecretKey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:123@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
manager = LoginManager(app)

from mainApp import models, views

db.create_all()