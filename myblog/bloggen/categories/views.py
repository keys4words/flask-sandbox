from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import current_user, login_required
from bloggen import db
from bloggen.models import Postcategory
from bloggen.categories.forms import CategoryForm


category = Blueprint('category', __name__)

@category.route('/categories', methods=['GET', 'POST'])
def list_cats():
    all_cats = Postcategory.query.all()
    return render_template('categories.html', all_cats=all_cats)
    