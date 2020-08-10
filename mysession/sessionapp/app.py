import os
from flask import Flask, redirect, render_template, url_for, make_response, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myVerySecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


#### Models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    # pass_hash = db.Column(db.String(128))

    def __init__(self, login, email):
        self.login = login
        self.email = email

    def __repr__(self):
        return f'<User {self.login} with email {self.email}>'


@app.route('/', methods=['GET', 'POST'])
def index():
    content = 'No session'
    if 'username' in session:
        content = session['username']
    return render_template('home.html', content=content)


# @app.route('/setcookie')
# def setcookie():
#     resp = make_response(redirect(url_for('index')))
#     resp.set_cookie('cookie_key', 'cookie_value')
#     return resp


# @app.route('/getcookie')
# def getcookie():
#     cookie_var = request.cookies.get('cookie_key')
#     return '<h2>Cookie: ' + cookie_var + '</h2>'

@app.route('/setsession', methods=['GET', 'POST'])
def setsession():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
        <p><input type=text name=username></p>
        <p><input type=submit value=Login></p>
        </form>
        '''

@app.route('/unsetsession')
def unsetsession():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
