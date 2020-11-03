from flask import render_template, request, url_for, session, redirect, g
from runner import app
import model


users = model.get_users()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        message = 'Home Page'
        no_form = True
        return render_template('index.html', message=message, no_form=no_form)
    else:
        login = request.form.get('login')
        email = request.form.get('email')
        password = request.form.get('password')
        user = model.get_user(login)
        message, no_form=model.signup(login, email, password)
        return render_template('index.html', message=message, no_form=no_form)

    # return app.root_path

@app.route('/football', methods=['GET', 'POST'])
def football():
    message = 'Football Page'
    return render_template('football.html', message=message)

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
        g.user = session['login']
    message = 'Dashboard page'
    return render_template('dashboard.html', message=message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        message = 'Have an account? Login!'
        return render_template('login.html', message=message)
    else:
        login = request.form.get('login')
        email = request.form.get('email')
        password = request.form.get('password')
        user = model.get_user(login)

        if user and model.check_psw(login):
            message = f'Dashboard Page'
            return render_template('dashboard.html', message=message, login=user[1])
        else:
            message = f'''There is no user with this login! <a href="{{  url_for('login')  }}>Please, sigup!</a>'''
            return render_template('login.html', message=message)
        

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    pass