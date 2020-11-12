from flask import render_template, request, url_for, session, redirect, flash
from runner import app, db
from models import Users, ToDo


@app.route('/')
def home():
    return render_template('index.html', message='Home page')

# @app.route('/football', methods=['POST'])
# def football():
#     message = 'Football Page'
#     return render_template('football.html', message=message)

@app.route('/about')
def about():
    message = 'About page'
    return render_template('about.html', message=message)

@app.route('/privacy')
def privacy():
    message = 'Privacy Policy Page'
    return render_template('privacy.html', message=message)

@app.route('/terms')
def terms():
    message = 'Terms of Use page'
    return render_template('terms.html', message=message)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        message = 'Signup Page'
        return render_template('signup.html', message=message)
    else:
        login = request.form.get('login')
        email = request.form.get('email')
        password = request.form.get('password')

        session.permanent = True
        session['login'] = login
        existing_user = Users.query.filter_by(login=login).first()
        if existing_user:
            flash('User with such login already exists!', category='danger')
            return render_template('signup.html', message='Signup Page')
        else:
            usr = Users(login, email, password)
            db.session.add(usr)
            db.session.commit()
            flash(f'User {login} was successfully signup!', category='info')
            return redirect(url_for('dashboard', user=login))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        session.permanent = True
        session['login'] = login
        existing_user = Users.query.filter_by(login=login).first()
        if existing_user:
            if existing_user.password == password:
                flash('You are logged in!', category='info')
                return redirect(url_for('dashboard', user=login))
            else:
                flash('Wrong password', category='danger')
                return render_template('login.html', message='Login page')
        else:
            flash('There is no user with such login! Signup first!', category='danger')
            return render_template('signup.html', message='Signup Page')
    else:
        if 'login' in session:
            flash('Additional authorization is not needed!', category='danger')
            return redirect(url_for('dashboard', user=session['login']))
        else:
            return render_template('login.html', message='Login page')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'login' in session:
        login = session['login']
        if request.method == 'POST':
            if 'todo' in request.form:
                task_from_form = request.form['todo']
                priority_from_form = request.form['priority']
                user_from_db = Users.query.filter_by(login=login).first()
                new_todo = ToDo(task_from_form, priority_from_form, user_from_db.id)
                db.session.add(new_todo)
                db.session.commit()
                flash('Your ToDo was added!', category='info')
            else:
                get_todo_id = [el for el in request.form.keys()][0][-1]
                delete_todo = ToDo.query.get(get_todo_id)
                db.session.delete(delete_todo)
                db.session.commit()
                flash('Your ToDo was removed!')
        
        todos = Users.query.filter_by(login=login).first().todos
        return render_template('dashboard.html', user=login, todos=enumerate(todos))
    else:
        flash('You need login before!', category='danger')
        # abort(401)
        return redirect(url_for('login', message='Login page'))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    login = session['login']
    flash(f'{login.capitalize()}, you have been log out!', category='info')
    session.pop('login', None)
    return redirect(url_for('login', message='Login page'))

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html'), 404

