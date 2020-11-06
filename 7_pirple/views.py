from flask import render_template, request, url_for, session, redirect, g
from runner import app
import model

login = ''
users = model.get_users()


@app.before_request
def before_request():
    g.users = None
    if 'login' in session:
        g.users = session['login']


@app.route('/', methods=['GET'])
def home():
    if 'login' in session:
        # g.users = session['login']
        message = 'Welcome, ' + session['login']
        return render_template('dashboard.html', message=message, user=session['login'])
    return render_template('index.html', message='Login or signup!')
    # return app.root_path

# @app.route('/football', methods=['POST'])
# def football():
#     message = 'Football Page'
#     return render_template('football.html', message=message)

@app.route('/about', methods=['GET'])
def about():
    message = 'About page'
    return render_template('about.html', message=message)

@app.route('/privacy', methods=['GET'])
def privacy():
    message = 'Privacy Policy Page'
    return render_template('privacy.html', message=message)

@app.route('/terms', methods=['GET'])
def terms():
    message = 'Terms of Use page'
    return render_template('terms.html', message=message)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'login' in session:
        message = 'Dashboard page'
        return render_template('dashboard.html', message=message, user=session['login'])
    else:
        message = 'You need to authorize before'
        return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('login', None)
        login = request.form.get('login')
        psw = request.form.get('password')
        if model.check_psw(login, psw):
            session['login'] = request.form.get('login')
            return redirect(url_for('home'))
    return render_template('login.html', message='Login page')


@app.route('/getsession')
def getsession():
    if 'login' in session:
        return session['login']
    return redirect(url_for('login'))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('login', None)
    return redirect(url_for('home'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        message = 'Signup Page'
        return render_template('signup.html', message=message)
    else:
        login = request.form.get('login')
        email = request.form.get('email')
        password = request.form.get('password')
        msg = model.signup(login, email, password)
        return render_template('signup.html', message=msg)