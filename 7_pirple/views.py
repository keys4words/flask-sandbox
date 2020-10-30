from flask import render_template, request
from demo import app
import model


def check_user(username, password):
    user = model.get_user(username)
    if user:
        print(user)
        return (username == user[1]) and (password == user[2])
    else:
        return False


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        message = 'Home Page'
        return render_template('index.html', message=message)
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = model.get_user(username)
        if username == user[1]:
            if password == user[2]:
                message = f'You are logged in, {username}!'
                return render_template('dashboard.html', message=message)
            else:
                message = f'User with this login already exists!'
        else:
            message = 'You need authorize before loggin'
            return render_template('index.html', message=message)

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
    message = 'Dashboard page'
    return render_template('dashboard.html', message=message)