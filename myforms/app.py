from flask import Flask, render_template, flash, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myVerySecretKey'

class InfoForm(FlaskForm):
    breed = StringField('What breed are you?')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET','POST'])
def index():
    breed = False
    form = InfoForm()
    if form.validate_on_submit():
        breed = form.breed.data
        session['breed'] = form.breed.data
        flash(f'{breed}')
        form.breed.data = ''
        return redirect(url_for('index'))
    return render_template('home.html', form=form, breed=breed)

if __name__ == "__main__":
    app.run(debug=True)
