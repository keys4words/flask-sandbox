from flask import Flask, render_template, session, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'newSecretKey1'


class SimpleForm(FlaskForm):
    submit = SubmitField('Signup')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        flash('Button was clicked!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
