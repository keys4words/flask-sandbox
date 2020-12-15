
import os

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Length, AnyOf, Email


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['WTF_CSRF_TIME_LIMIT'] = 3600

#############################
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('Username is required!'), AnyOf(values=['maxim', 'admin'], message='Only maxim or admin allowed!')])
    password = PasswordField('password', validators=[InputRequired('Password is required!'), Length(min=4, max=6, message='Password must be from 4 to 6 symbols length')])
    age = IntegerField('age', default=28)
    email = StringField('email', validators=[Email()])
    remember_me = BooleanField('Remember me')

class User:
    def __init__(self, username, password, age, email, remember_me):
        self.username = username
        self.password = password
        self.age = age
        self.email = email
        self.remember_me = remember_me

#############################

@app.route('/', methods=['GET', 'POST'])
def index():
    default_user = User('John Doe', '', 30, 'j.doe@mail.com', True)

    form = LoginForm(obj=default_user)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return f'Form submitted with username: {username} and password: {password}'
    return render_template('index.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)