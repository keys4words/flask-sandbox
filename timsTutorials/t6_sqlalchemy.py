import os
from flask import Flask, redirect, url_for, render_template, request, session, flash, abort
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'something ultimately secret!!!'
app.permanent_session_lifetime = timedelta(minutes=5)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'user.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


################################
# models
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Text)
    email = db.Column('email', db.String(100))
    todos = db.relationship('ToDo', backref='todo', lazy='dynamic')

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User: {self.name} with email: {self.email}>'


class ToDo(db.Model):
    __tablename__ = 'todo'
    id = db.Column('todo_id', db.Integer, primary_key=True)
    task = db.Column('todo_name', db.Text)
    priority = db.Column('priority', db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, task, priority, user_id):
        self.task = task
        self.priority = priority
        self.user_id = user_id

    def __repr__(self):
        return f'{self.task}'


def seed_db(db):
    james = Users('James Bond', 'j.bond@yahoo.com')
    tyson = Users('Mike Tyson', 'boxing@gmail.com')
    data_users = [james, tyson]
    db.session.add_all(data_users)
    db.session.commit()
    
    james_todo1 = ToDo('Sex with blond', 'high', james.id)
    james_todo2 = ToDo('Kill the spy', 'high', james.id)
    tyson_todo1 = ToDo('first round', 'middle', tyson.id)
    tyson_todo2 = ToDo('second round', 'middle', tyson.id)
    tyson_todo3 = ToDo('third round', 'low', tyson.id)
    
    data_todos = [james_todo1, james_todo2, tyson_todo1, tyson_todo2, tyson_todo3]
    db.session.add_all(data_todos)
    db.session.commit()

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
            flash('New user added!', category='info')

        flash('You are logged in!', category='info')
        return redirect(url_for('user', user=user))
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
            if 'todo' in request.form:
                task_from_form = request.form['todo']
                priority_from_form = request.form['priority']
                user_from_db = Users.query.filter_by(name=user).first()
                new_todo = ToDo(task_from_form, priority_from_form, user_from_db.id)
                db.session.add(new_todo)
                db.session.commit()
                flash('Your ToDo was added!', category='info')
            else:
                get_todo_id = [el for el in request.form.keys()][0][-1]
                delete_todo = ToDo.query.filter_by(id=get_todo_id).first()
                db.session.delete(delete_todo)
                db.session.commit()
                flash('Your ToDo was removed!')
        
        todos = Users.query.filter_by(name=user).first().todos
        return render_template('user.html', user=user, todos=enumerate(todos))
    else:
        flash('You need login before!', category='danger')
        # abort(401)
        return redirect(url_for('login'))


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html'), 404



if __name__ == "__main__":
    # db.create_all()
    # seed_db(db)
    app.run(debug=True)