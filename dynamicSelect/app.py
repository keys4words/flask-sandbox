import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'dyn.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'asdlfjaosdfas#$Fsdfa'

db = SQLAlchemy(app)

##########################
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(2))
    name = db.Column(db.String(50))

##########################
class Form(FlaskForm):
    state = SelectField('state', choices=[('CA', 'California'), ('NV', 'Nevada')])
    city = SelectField('city', choices=[()])

##########################
@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()
    form.city.choices = [(city.id, city.name) for city in City.query.filter_by(state='NV').all()]
    if request.method == 'POST':
        city = City.query.filter_by(id=form.city.data).first()
        return f'<h1>State: {form.state.data}, City: {city.name}</h1>'

    return render_template('index.html', form=form)


@app.route('/city/<state>')
def city(state):
    cities = City.query.filter_by(state=state).all()
    cityArray = []
    for city in cities:
        cityObject = {}
        cityObject['id'] = city.id
        cityObject['name'] = city.name
        cityArray.append(cityObject)

    return jsonify({'cities': cityArray})



if __name__ == '__main__':
    app.run(debug=True)