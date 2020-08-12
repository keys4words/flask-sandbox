from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of Puppy: ')
    submit = SubmitField("Add Puppy")

class DelForm(FlaskForm):
    id = IntegerField('Id of Puppy to delete: ')
    submit = SubmitField("Delete Puppy")

class AddOwnerForm(FlaskForm):
    name = StringField('Name of new Owner: ')
    id_puppy = IntegerField('Id of Puppy: ')
    submit = SubmitField("Add Owner")
