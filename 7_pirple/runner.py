import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import timedelta


app = Flask(__name__)
app.config['SECRET_KEY'] = 'myVerySecretKey'
app.permanent_session_lifetime = timedelta(minutes=5)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'todo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


from views import *
from models import seed_db


if __name__ == "__main__":
    app.run(port=5000, debug=True)
    # seed_db(db)
