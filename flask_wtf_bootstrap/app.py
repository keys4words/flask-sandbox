import os
from datetime import datetime
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField
from wtforms.validators import InputRequired, Email, Length, ValidationError
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
bootstrap = Bootstrap(app)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=3, max=12)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=6)])
    entrydate = DateField('entrydate', format='%Y-%m-%d')
    
    def validate_username(form, field):
        if field.data != 'admin':
            raise ValidationError('You do not have the rights!')



@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    # user = User(username='John Doe', password='Your password', entrydate=datetime.today())

    if form.validate_on_submit():
        # form.populate_obj(user)
        # return f'Form successfully submitted with name: {user.username} and password: {user.password}'
        username = form.username.data
        password = form.password.data
        entrydate = form.entrydate.data
        return f'Form successfully submitted with name: {username} and password: {password} and entrydate: {entrydate}'
    return render_template('index.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)