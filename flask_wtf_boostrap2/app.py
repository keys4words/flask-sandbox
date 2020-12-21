import os

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(36)


class MyForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    textarea = TextAreaField('Textarea')
    radios = RadioField('Radios', default='option', choices=[('option1', 'Wanna drink?'), ('option2', 'Wanna sleep?')])
    selects = SelectField('Select', choices=[('1', 'Milk'), ('2', 'Beer'), ('3', 'Brendy')])


@app.route('/', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        return render_template('results.html', email=form.email.data, password=form.password.data, textarea=form.textarea.data, radios=form.radios.data, selects=form.selects.data)
    return render_template('form.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)
