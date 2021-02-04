from flask import Flask, render_template, request, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signupresult', methods=['POST'])
def signupresult():
    user = request.form['username']
    password = request.form['password']
    return json.dumps({'status': 'ok', 'user': user, 'password': password})


if __name__ == '__main__':
    app.run(debug=True)