import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_user import UserManager, UserMixin, SQLAlchemyAdapter, login_required
from flask_mail import Mail


app = Flask(__name__)
app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)
mail = Mail(app)

#################################
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')
    email = db.Column(db.String(255), nullable=False, unique=True)
    confirmed_at = db.Column(db.DateTime())

#################################

db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)

@app.route('/')
def index():
    return 'This is unprotected home page!'


@app.route('/profile')
@login_required
def profile():
    return 'This is protected profile page'


if __name__ == "__main__":
    app.run(debug=True)