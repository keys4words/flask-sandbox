from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length

from models import Account


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username is empty!')])
    password = PasswordField('Password', validators=[DataRequired(message='Password is empty!')])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username is empty!')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(message='Password is empty!')])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


    def validate_username(self, username):
        user = Account.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('This username is registered!')

    def validate_email(self, email):
        user = Account.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This email is registered!')

