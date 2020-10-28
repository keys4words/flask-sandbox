from flask import render_template, url_for, redirect, flash, request
from app.forms import LoginForm
from app import app

@app.route('/')
def index():
    user = {'username': 'James'}
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


    return render_template('index.html', title=title, user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        remember_me = request.form.get('remember_me')
        flash(f'Welcome, {form.username.data}! Your password={form.password.data}, Remember me = {remember_me}')
        # flash(f'Welcome, {form.username.data}! Remember me = {form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login page', form=form)