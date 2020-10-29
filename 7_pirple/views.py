from flask import render_template, request
from demo import app

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        message = 'Home Page'
        return render_template('index.html', message=message)
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'Maxim' and password == 'test':
            message = model.show_position(username)
            return render_template('football.html', message=message)
        else:
            message = 'You need authorize before loggin'
            return render_template('index.html', message=message)

    # return app.root_path

@app.route('/football', methods=['GET', 'POST'])
def football():
    message = 'Football Page'
    return render_template('football.html', message=message)

@app.route('/about', methods=['GET'])
def about():
    message = 'About page'
    return render_template('about.html', message=message)

@app.route('/privacy', methods=['GET'])
def privacy():
    message = 'Privacy Policy Page'
    return render_template('privacy.html', message=message)

@app.route('/terms', methods=['GET'])
def terms():
    message = 'Terms of Use page'
    return render_template('terms.html', message=message)