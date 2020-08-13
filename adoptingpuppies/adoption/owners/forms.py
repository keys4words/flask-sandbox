from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddOwnerForm(FlaskForm):
    name = StringField('Name of new Owner: ')
    id_puppy = IntegerField('Id of Puppy: ')
    submit = SubmitField("Add Owner")
