from flask import render_template, redirect, url_for, abort, jsonify, flash, Blueprint
from flask_login import current_user, login_user, logout_user, login_required

from app import db, login
from forms import RegisterForm, LoginForm
from models import TodoItem, TodoList, Account


routes = Blueprint('routes', __name__)


@login.user_loader
def load_account(id):
    return Account.query.get(int(id))


@routes.route('/')
def home():
    return render_template('home.html')


@routes.route('/lists')
@login_required
def show_list():
    lists = TodoList.query.all()
    return render_template('showlists.html', todolists=lists)


@routes.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.show_list'))

    form = RegisterForm()
    if form.validate_on_submit():
        user = Account(username=form.username.data, email=form.email.data)
        user.set_pass(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Successfully created new account', 'success')
        return redirect(url_for('routes.login'))
    else:
        for error in form.errors:
            flash(form.errors[error][0], 'danger')

    return render_template('register.html', form=form)


@routes.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.show_list'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = Account.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_pass(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('routes.login'))
        login_user(user, remember=True)
        return redirect(url_for('routes.show_list'))
    else:
        for error in form.errors:
            flash(form.errors[error][0], 'danger')

    return render_template('login.html', form=form)


@routes.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('routes.login'))


@routes.route('/addlist')
def add_list():
    new_list = TodoList()
    new_list.name = "New Tod List"
    db.session.add(new_list)
    db.session.commit()
    return redirect(url_for('routes.show_list'))


@routes.route('/list/<listid>')
@login_required
def view_list(listid):
    if listid is None:
        return abort()
    list = TodoList.query.filter_by(id=listid).first()
    if list is None:
        return abort()
    return render_template('viewlist.html', todolist=list)