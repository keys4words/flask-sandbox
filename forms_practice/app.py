from flask import Flask, render_template, flash, redirect, url_for, session, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myVerySecretKey'

class InfoForm(FlaskForm):
    breed = StringField('What breed are you?', [validators.DataRequired()])
    submit = SubmitField('Submit')


class SignupForm(FlaskForm):
    email = StringField('Enter your email', [validators.Email()])
    name = StringField('Enter your name')
    submit = SubmitField('Sign Up')


@app.route('/', methods=['GET','POST'])
def index():
    breed = False
    form_breed = InfoForm()
    form_signup = SignupForm()

    if form_breed.validate_on_submit():
        breed = form_breed.breed.data
        session['breed'] = form_breed.breed.data
        flash(f'Your breed is {breed}')
        form_breed.breed.data = ''
        return redirect(url_for('index'))
    
    if form_signup.validate_on_submit():
        email = form_signup.email.data
        print(email)
        flash(f'Your email {email} successfully signup!')
        return redirect(url_for('index'))

    return render_template('home.html', form_breed=form_breed, form_signup=form_signup, breed=breed)

if __name__ == "__main__":
    app.run(debug=True)
