from flask import Blueprint, render_template

part2 = Blueprint('part2', __name__, static_folder="static", template_folder="templates")

@part2.route('/index')
def index():
    return render_template('index.html')