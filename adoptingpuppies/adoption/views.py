from flask import render_template, url_for, redirect

from app import app, db
from forms import AddForm, DelForm
from models import Puppy

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_puppy():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_puppy = Puppy(name)

        db.session.add(new_puppy)
        db.session.commit()

        return redirect(url_for('list_puppies'))
    return render_template('add.html', form=form)

@app.route('/list')
def list_puppies():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods=['GET', 'POST'])
def del_puppy():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        puppy = Puppy.query.get(id)
        
        db.session.delete(puppy)
        db.session.commit()

        return redirect(url_for('list_puppies'))
    return render_template('delete.html', form=form)