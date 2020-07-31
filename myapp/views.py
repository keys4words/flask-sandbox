from flask import render_template, request, url_for, send_file, redirect, abort
from myapp import app

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/login.html')
def send_login():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        psw = request.form['password']
        return f'POST: User {user} -> {psw}'
    else:
        user = request.args.get('username')
        psw = request.args.get('password')
        return f'GET: User {user} -> {psw}'

@app.route('/redirect-to-login-page')
def redirected():
    return redirect(url_for('send_login'))

@app.route('/aborted-page')
def aborted_page():
    abort(401)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
