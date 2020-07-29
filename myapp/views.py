from flask import url_for, request, send_file, redirect, abort, render_template, flash, make_response, session
from myapp import app, db
from myapp.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from myapp.models import User
from werkzeug.urls import url_parse


# @app.route('/setcookie')
# def setcookie():
#     resp = make_response(redirect(url_for('index')))
#     resp.set_cookie('flask_cookie', 'cookie_value')
#     return resp

# @app.route('/getcookie')
# def getcookie():
#     flask_cookie = request.cookies.get('flask_cookie')
#     return '<h2>Cookie: ' + flask_cookie  + '</h2>'


# @app.route('/setsession', methods=['GET', 'POST'])
# def setsession():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return '''
#         <form action="" method="post">
#         <p><input type=text name=username></p>
#         <p><input type=submit value=login></p>
#         '''

# @app.route('/unsetsession')
# def unsetsession():
#     session.pop('username', None)
#     return redirect(url_for('index'))

# app.secret_key = 'SOME_SECRET_KEY'



@app.route('/')
@app.route('/index')
@login_required
def index():
    # if 'username' in session:
    #     return '<h1>Session %s</h1>'% session['username']
    # return '<h1>No Session'

    # user = {'username': 'Maxim'}
    title = 'My Flask App'

    posts = [
        {'author': {'username': 'Maxim'},
        'body': 'Hello, folks!'},
        {'author': {'username': 'James'},
        'body': 'Dont shake martiny, pal!'},
        {'author': {'username': 'Julie'},
        'body': 'Im crying!'}
    ]

    return render_template('index.html', title=title, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Wrong password or login')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Вход', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Ура, Вы зарегистрированы!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Регистрация', form=form)


""" @app.route('/hello/<name>')
def hello_name(name):
    return f"Hello, {name}"

@app.route('/catalog/<int:item_id>')
def catalog_item(item_id):
    return "Number in catalog: %d" % item_id

@app.route('/versions/<float:version>')
def versions(version):
    return "Version number: %f" % version

@app.route('/path1/')
def path1():
    return "This is path1"

@app.route('/path2')
def path2():
    return "This is path2"

@app.route('/url_for-test')
def url_for_test():
    return url_for('main_page')

@app.route('/login.html')
def send_login():
    return send_file('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return 'POST request with user = %s' % user
    else:
        user = request.args.get('name')
        return 'GET request with user = %s' % user


#redirect(location, statuscode, response)
@app.route('/redirect-to-login-page')
def redirected():
    return redirect(url_for('send_login'))

@app.route('/aborted-page')
def aborted_page():
    abort(401)


@app.errorhandler(404)
def page_not_found(error):
    return "No such page!!!", 404

if __name__ == "__main__":
    with app.test_request_context():
        print(url_for('main_page'))
        print(url_for('path1'))
        print(url_for('path2'))
    app.run(port=8080)


#app.run(host, port, debug, options) """