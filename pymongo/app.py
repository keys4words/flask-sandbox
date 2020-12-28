from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from itsdangerous import URLSafeSerializer


app = Flask(__name__)
app.config.from_object('config')

mongo = PyMongo(app)
login_manager = LoginManager(app)
serializer = URLSafeSerializer(app.secret_key)


class Member(UserMixin):
    def __init__(self, member_data):
        self.member_data = member_data

    def get_id(self):
        return self.member_data['session_token']


@login_manager.user_loader
def load_user(session_token):
    members = mongo.db.members
    member_data = members.find_one({'session_token': session_token})
    if member_data:
        return Member(member_data)
    return None

@app.route('/create')
def create():
    members = mongo.db.members
    session_token = serializer.dumps(['Maxim', 'password'])
    members.insert_one({'name': 'Maxim', 'session_token': session_token})
    return '<h1>User created!</h1>'


@app.route('/login')
def login():
    members = mongo.db.members
    member = members.find_one({'name': 'Maxim'})
    maxim = Member(member)

    login_user(maxim)
    return '<h1>You are now logged in!</h1>'


@app.route('/home')
@login_required
def home():
    return f"<h1>The current user is {current_user.member_data['name']}"


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You are now logged out!'



if __name__ == "__main__":
    app.run()