from flask import Flask, redirect, url_for, render_template, request, session, flash, abort
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'something ultimately secret!!!'
app.permanent_session_lifetime = timedelta(minutes=5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


################################
# models
class Users(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


class ToDo(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    task = db.Column('todo_name', db.String(256))

    def __init__(self, task):
        self.task = task


################################
# views

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        email = request.form['email']
        session.permanent = True
        session['user'] = user
        existing_user = Users.query.filter_by(name=user).first()
        if existing_user:
            session['email'] = existing_user.email
        else:
            usr = Users(user, email)
            db.session.add(usr)
            db.session.commit()

        flash('You are logged in!', category='info')
        return redirect(url_for('user'), user=user)
    else:
        if 'user' in session:
            flash('Additional authorization is not needed!', category='danger')
            return redirect(url_for('user'))

        return render_template('login.html')


@app.route('/logout')
def logout():
    user = session['user']
    flash(f'{user.capitalize()}, you have been log out!', category='info')
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route('/user', methods=['POST', 'GET'])
def user():
    if 'user' in session:
        user = session['user']

        if request.method == 'POST':
            todo = request.form['todo']
            session['todo'] = todo
            found_todo = ToDo.query.filter_by()
            flash('Your ToDo was saved!', category='info')
        else:
            if 'todo' in session:
                todo = session['todo']

        return render_template('user.html', user=user, todo=todo)
    else:
        flash('You need login before!', category='danger')
        # abort(401)
        return redirect(url_for('login'))


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html'), 404



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)