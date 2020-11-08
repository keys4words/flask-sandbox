from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'something ultimately secret!!!'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        session.permanent = True
        session['user'] = user
        flash('You are logged in!', category='info')
        return redirect(url_for('user'))
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


@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return render_template('user.html', user=user)
    else:
        flash('You need login before!', category='danger')
        return redirect(url_for('login'))



if __name__ == "__main__":
    app.run(debug=True)