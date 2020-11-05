from flask import render_template, url_for, redirect
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

@app.route('/layout')
def layout():
    return render_template('layout.html', title='Layout')


@app.route('/child')
def child():
    return render_template('child.html', title='Child')