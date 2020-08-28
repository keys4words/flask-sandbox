from flask import Flask, render_template, flash, request, redirect, url_for
from modal_app.content_management import Content
from modal_app.db_connect import connection
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash



TOPIC_DICT = Content()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mySecretKey'

@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html", TOPIC_DICT=TOPIC_DICT)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.route('/slashboard/')
def slashboard():
    try:
        return render_template("dashboard.html", TOPIC_DICT = shamwow)
    except Exception as e:
	    return render_template("500.html", error = str(e))


@app.route('/login/', methods=["GET","POST"])
def login_page():
    error = ''
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('dashboard'))
            else:
                error = "Invalid credentials. Try Again."
        return render_template("login.html", error = error)
    except Exception as e:
        # flash(e)
        return render_template("login.html", error = error)


class RegistrationForm(FlaskForm):
    username = StringField('Username', [Length(min=4, max=20)])
    email = StringField('Email Address', [Length(min=6, max=50)])
    password = PasswordField('New Password', [
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice', [DataRequired()])


@app.route('/register/', methods=["GET","POST"])
def register_page():
    try:
        form = RegistrationForm(request.form)

        if request.method == "POST" and form.validate_on_submit():
            username  = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt((str(form.password.data)))
            c, conn = connection()

            x = c.execute("SELECT * FROM users WHERE username = (%s)",
                          (thwart(username)))

            if int(x) > 0:
                flash("That username is already taken, please choose another")
                return render_template('register.html', form=form)

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
    except Exception as e:
        return(str(e))
