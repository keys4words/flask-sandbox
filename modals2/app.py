from flask import Flask, render_template, jsonify, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from random import randint
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myVerySecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'modals2.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    email = db.Column(db.String(60))
    random = db.Column(db.Integer)


class PopupForm(FlaskForm):
    name = StringField('Enter your login', validators=[DataRequired()])
    email = StringField('Enter your email', validators=[DataRequired()])
    submit = SubmitField('Popup')


@app.route('/')
def index():
    members = Member.query.all()
    return render_template('index.html', members=members)

@app.route('/update', methods=['POST'])
def update():
    member = Member.query.filter_by(id=request.form['id']).first()
    member.name = request.form['name']
    member.email = request.form['email']
    member.random = randint(1, 10000)

    db.session.commit()
    # member = Member.query.filter_by(id=request.form['id']).first()
    return jsonify({'result': 'success', 'member_num': member.random})


@app.route('/popup', methods=['GET', 'POST'])
def popup():
    form = PopupForm()
    if form.validate_on_submit():
        # member = Member()
        name = form.name.data
        email = form.email.data
        print(name, email)
        return jsonify(status='ok')
    return render_template('popup.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)