import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import DevConfig

app = Flask(__name__)

app.config.from_object(DevConfig())

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

import views

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('path1'))
        print(url_for('path2'))
    app.run()