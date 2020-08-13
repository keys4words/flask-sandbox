from flask import render_template, url_for, redirect, Blueprint

from adoption import app, db
from adoption.models import Owner
from adoption.owners.forms import AddOwnerForm

owners_blueprints = Blueprint('owners', __name__,
                                template_folder='templates/owners')


# @app.route('/add_owner', methods=['GET', 'POST'])
@owners_blueprints.route('/add', methods=['GET', 'POST'])
def add_owner():
    form = AddOwnerForm()
    if form.validate_on_submit():
        name = form.name.data
        id_puppy = form.id_puppy.data
        new_owner = Owner(name, id_puppy)

        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('puppies.list_puppies'))
    return render_template('add_owner.html', form=form)
