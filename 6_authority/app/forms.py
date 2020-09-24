from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, InputRequired, Length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=64)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=128)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(min=6, max=120)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=64)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=128)])




