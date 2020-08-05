from flask import render_template, request, url_for, send_file, redirect, abort, flash

from myapp import app
from myapp.forms import LoginForm

@app.route('/')
def index():
    posts = [
        {'author':{'username': 'Nicolas'},
        'body': 'shit happens'
        },
        {'author': {'username': 'James Bond'},
         'body': 'From Russia with love'
         },
        {'author': {'username': 'Peter Penn'},
         'body': 'I am always want to be fly'
         }
    ]
    context = {'user': 'Maxim'}
    return render_template('index.html', context=context, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        flash('Login request for user {}, with pass {}, remember me - {}'.format(form.username.data, form.password.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/thankyou', methods=['POST'])
def thank_you():
    username = request.form.get('username')
    password = request.form.get('password')
    remember_me = request.form.get('rememember_me')
    return render_template('thankyou.html', username=username, password=password, remember_me=remember_me)

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['username']
#         psw = request.form['password']
#         return f'POST: User {user} -> {psw}'
#     else:
#         user = request.args.get('username')
#         psw = request.args.get('password')
#         return f'GET: User {user} -> {psw}'

# @app.route('/redirect-to-login-page')
# def redirected():
#     return redirect(url_for('send_login'))

@app.route('/aborted-page')
def aborted_page():
    abort(401)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
