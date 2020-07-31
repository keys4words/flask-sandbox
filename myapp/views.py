from flask import render_template, request, url_for, send_file
from myapp import app

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/login.html')
def send_login():
    return send_file('login.html')


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
