from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hello! This is a main page</h1>"

@app.route('/<name>')
def user(name):
    return f'Hello, {name}'

@app.route('/admin')
def admin():
    # return redirect(url_for('home'))
    return redirect(url_for('user', name='Admin'))



if __name__ == "__main__":
    app.run(debug=True)