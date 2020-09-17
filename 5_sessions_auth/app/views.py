from flask import render_template, url_for, redirect, flash, redirect, flash, url_for, make_response, request, session
from app.forms import LoginForm
from app import app
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

# @app.route('/setcookie')
# def setcookie():
#     resp = make_response(redirect(url_for('index')))
#     resp.set_cookie('flask_key', 'flask_value')
#     return resp


# @app.route('/getcookie')
# def getcookie():
#     flask_key = request.cookies.get('flask_key')
#     return '<h1>Data from cookie: ' + flask_key + '</h1>'


# @app.route('/setsession', methods=['GET', 'POST'])
# def setsession():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return '''
#     <form action="" method='POST'>
#     <p><input type=text name=username></p>
#     <p><input type=submit value=Login></p>
#     '''

# @app.route('/unsetsession')
# def unsetsession():
#     session.pop('username', None)
#     return redirect(url_for('index'))


@app.route('/')
@login_required
def index():
    if 'username' in session:
        return f"<h1>Session: {session['username']}"
    return "<h1>Session: No Data"

    # user = {'username': 'James'}
    title = 'Home page'

    posts = [
        {
            'author': {'username': 'Peter'},
            'body': 'Hello'
        },
        {
            'author': {'username': 'Mike'},
            'body': 'Hello from Mike'
        },
        {
            'author': {'username': 'James'},
            'body': 'Hello from James'
        },
    ]


    # return render_template('index.html', title=title, user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Wrong login or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash(f'Welcome, {form.username.data}! Remember me = {form.remember_me.data}')
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Login page', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))