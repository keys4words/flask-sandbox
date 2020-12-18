
import os

from collections import namedtuple

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, Form, FormField, FieldList
from wtforms.validators import InputRequired, Length, AnyOf, Email


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['WTF_CSRF_TIME_LIMIT'] = 3600

#############################
class PhoneForm(Form):
    country_code = IntegerField('country code')
    area_code = IntegerField('area code')
    number = StringField('number')


class YearForm(Form):
    year = IntegerField('year')
    total = IntegerField('total')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('Username is required!'), AnyOf(values=['maxim', 'admin'], message='Only maxim or admin allowed!')])
    password = PasswordField('password', validators=[InputRequired('Password is required!'), Length(min=4, max=6, message='Password must be from 4 to 6 symbols length')])
    age = IntegerField('age', default=28)
    email = StringField('email', validators=[Email()])
    remember_me = BooleanField('Remember me')
    home_phone = FormField(PhoneForm)
    mobile_phone = FormField(PhoneForm)
    years = FieldList(FormField(YearForm))


class NameForm(LoginForm):
    first_name = StringField('first name')
    last_name = StringField('last name')


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

    group = namedtuple('Group', ['year', 'total'])
    g1 = group(2005, 1000)
    g2 = group(2007, 2000)
    g3 = group(2009, 17000)

    years = {'years': [g1, g2, g3]}

    form = NameForm(obj=default_user, data=years)
    
    del form.mobile_phone

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        output = '<h1>'
        for el in form.years:
            output += 'Year: {}<br>'.format(el.year.data)
            output += 'Total: {}<br>'.format(el.total.data)
        output += '</h1>'

        return output
        # return f'Form submitted with username: {username} and password: {password}'
    return render_template('index.html', form=form)


@app.route('/dynamic', methods=['GET', 'POST'])
def dynamic():
    class DynamicForm(FlaskForm):
        pass

    DynamicForm.name = StringField('name')
    names = ['first_name', 'middle_name', 'last_name']
    for el in names:
        setattr(DynamicForm, el, StringField(el))

    form = DynamicForm()

    if form.validate_on_submit():

        return f'Dynamic form submitted with name: {form.name.data}'

    return render_template('dynamic.html', form=form, names=names)



if __name__ == "__main__":
    app.run(debug=True)