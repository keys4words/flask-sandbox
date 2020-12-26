import os

from urllib.parse import urlparse, urljoin

from flask import Flask, render_template, request, session, redirect
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user, fresh_login_required
from flask_sqlalchemy import SQLAlchemy

from itsdangerous import URLSafeTimedSerializer, SignatureExpired

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(36)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'fl2.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['TIME_TO_EXPIRE'] = 3600

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

serializer = URLSafeTimedSerializer(app.secret_key)

###############################
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(50))
    session_token = db.Column(db.String(100), unique=True)

    def get_id(self):
        return self.session_token


@login_manager.user_loader
def load_user(session_token):
    user = User.query.filter_by(session_token=session_token).first()
    try:
        serializer.loads(session_token, max_age=60)
    except SignatureExpired:
        user.session_token = None
        db.session.commit()
        return None

    return user


def create_user():
    user = User(username='Mike', password='test', session_token=serializer.dumps(['Mike', 'test']))
    db.session.add(user)
    db.session.commit()


def update_token():
    mike = User.query.filter_by(username='Mike').first()
    mike.password = 'new-test'
    mike.session_token = serializer.dumps(['Mike', 'new-test'])
    db.session.commit()

##############################

@app.route('/')
def index():
    user = User.query.filter_by(username='Mike').first()
    session_token = serializer.dumps(['Mike', 'test'])
    user.session_token = session_token
    db.session.commit()
    
    login_user(user, remember=True)
    return 'You are now logged in!'
    

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return '<h1>You are logged out!</h1>'


@app.route('/home')
@login_required
def home():
    return 'The current user is ' + current_user.username

#################################

if __name__ == "__main__":
    app.run(debug=True)
