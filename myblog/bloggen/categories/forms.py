from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class CategoryForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired()])
    desc = StringField('Description')
    submit = SubmitField('Create Category')