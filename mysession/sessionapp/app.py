import os
from flask import Flask, redirect, render_template, url_for, make_response, request, session, flash

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, current_user, login_user

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myVerySecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)
login = LoginManager(app)



#### Forms
class LoginForm(FlaskForm):
    login = StringField('Enter your login', validators=[DataRequired()])
    password = PasswordField('Enter your password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')


#### Models
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), index=True, unique=True)
    pass_hash = db.Column(db.String(128))

    def __init__(self, login, password):
        self.login = login
        self.pass_hash = self.set_pass(password)

    def set_pass(self, password):
        self.pass_hash = generate_password_hash(password)

    def check_pass(self, password):
        return check_password_hash(self.pass_hash, password)

    def __repr__(self):
        return f'<User {self.login}>'

#### Views
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

# @app.route('/setsession', methods=['GET', 'POST'])
# def setsession():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return '''
#         <form action="" method="post">
#         <p><input type=text name=username></p>
#         <p><input type=submit value=Login></p>
#         </form>
#         '''

# @app.route('/unsetsession')
# def unsetsession():
#     session.pop('username', None)
#     return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm(csrf_enabled=True)
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user is None or not user.check_pass(form.password.data):
            flash('Incorrect login or password!')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash(f'Hello, {form.login}')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
