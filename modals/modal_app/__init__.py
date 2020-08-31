from flask import Flask, render_template, flash, request, redirect, url_for, session, jsonify
from modal_app.content_management import Content
from modal_app.db_connect import connection
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import gc
from MySQLdb import escape_string as thwart


TOPIC_DICT = Content()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mySecretKey'


def userinformation():
    try:
        client_name = (session['username'])
        guest = False
    except:
        guest = True
        client_name = 'Guest'

    if not guest:
        try:
            c, conn = connection()
            c.execute("SELECT * FROM users WHERE username = (%s)", (thwart(client_name), ))
            data = c.fetchone()
            settings = data[4]
            tracking = data[5]
            rank = data[6]
        except Exception:
            pass
    else:
        settings = [0, 0]
        tracking = [0, 0]
        rank = [0, 0]
    return client_name, settings, tracking, rank


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to be login first')
            return redirect(url_for('login_page'))
    return wrap


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/dashboard/')
# @login_required
def dashboard():
    try:
        try:
            client_name, settings, tracking, rank = userinformation()
            if len(tracking) < 10:
                tracking = '/some-url/'
            gc.collect()
            if client_name == "Guest":
                flash("Welcome, Guest! Feel free to view content. If you wanna write a post, register first")
            return render_template("dashboard.html", TOPIC_DICT=TOPIC_DICT)
        except Exception as e:
            return(str(e), "Please report error")
    except Exception as e:
        return (str(e), "Please report error")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.route('/slashboard/')
def slashboard():
    try:
        return render_template("dashboard.html", TOPIC_DICT = shamwow)
    except Exception as e:
	    return render_template("500.html", error = str(e))



class RegistrationForm(FlaskForm):
    username = StringField('Username', [Length(min=4, max=20)])
    email = StringField('Email Address', [Length(min=6, max=50)])
    password = PasswordField('New Password', [
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice', [DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', [Length(min=4, max=20)])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField('Login')



@app.route('/login/', methods=["GET","POST"])
def login_page():
    error = ''
    form = LoginForm()
    try:
        c, conn = connection()
        if request.method == "POST":
            data = c.execute("SELECT * FROM users WHERE username = (%s)", (thwart(request.form['username']), ))
            data = c.fetchone()[2]
            if check_password_hash(data ,request.form['password']):
                session['logged_in'] = True
                session['username'] = request.form['username']
                flash("You are now logged in")
                return redirect(url_for("dashboard"))
            else:
                error = "Invalid credentials, try again."
        gc.collect()
        return render_template("login.html", error=error, form=form)

    except Exception as e:
        #flash(e)
        error = "Invalid credentials, try again."
        return render_template("login.html", error = error)  





@app.route('/register/', methods=["GET","POST"])
def register_page():
    try:
        form = RegistrationForm(request.form)
        if request.method == "POST" and form.validate_on_submit():
            username  = form.username.data
            email = form.email.data
            password = generate_password_hash(form.password.data)
            print(password)
            c, conn = connection()

            x = c.execute("SELECT * FROM users WHERE username = (%s)", (thwart(username), ))
            if int(x) > 0:
                flash("That username is already taken, please choose another")
                return render_template("register.html", form=form)
            else:
                c.execute("INSERT INTO users (username, password, email, tracking) VALUES (%s, %s, %s, %s)",
                          (thwart(username), thwart(password), thwart(email), thwart("/introduction-to-python-programming/")))
                
                conn.commit()
                flash("Thanks for registering!")
                c.close()
                conn.close()
                gc.collect()
                session['logged_in'] = True
                session['username'] = username
                return redirect(url_for('dashboard'))
        return render_template("register.html", form=form)
    except Exception as e:
        return(str(e))


@app.route('/logout/')
@login_required
def logout():
    session.clear()
    flash('You have been logged out!')
    gc.collect()
    return redirect(url_for('homepage'))


@app.route('/interactive/')
def interactive():
    return render_template('interactive.html')


@app.route('/background_process', methods=['POST'])
def background_process():
    try:
        lang = request.args.get('proglang')
        if str(lang).lower() == 'python':
            return jsonify(result='You are wise!')
        else:
            return jsonify(result='try again')
    except Exception as e:
        return str(e)