from flask import Flask, jsonify, request, url_for, redirect, session, render_template

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'asldmfa4u@$#52342j421nk-21o31'

# @app.route('/', defaults={'name': 'John Dow'})
# @app.route('/<string:name>')
# def index(name):
#     return f'<h1>Hello, {name}</h1>'

@app.route('/')
def index():
    session.pop('name', None)
    return '<h1>Index Page</h1>'

@app.route('/home', methods=['GET', 'POST'], defaults={'name': 'John Doe'})
@app.route('/home/<string:name>', methods=['GET', 'POST'])
def home(name):
    session['name'] = name
    return render_template('home.html', name=name, display=False, myList=['one', 'two', 'three', 'four'], myDict=[{'name': 'Jowe'}, {'name': 'Jeremy'}])


@app.route('/json')
def json():
    if 'name' in session:
        name = session['name']
    else:
        name = 'Not in session'
    return jsonify({'key': 'value', 'key2': [213, 99, 9], 'name': name})


@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return f'<h1>Query Page for {name} with location in {location}</h1>'


# @app.route('/theform')
# def theform():
#     return '''<form method="POST" action="/process">
#                 <input type="text" name="name">
#                 <input type="text" name="location">
#                 <input type="submit" value="Submit">
#               </form>'''


# @app.route('/process', methods=['POST'])
# def process():
#     name = request.form['name']
#     location = request.form['location']
#     return f"<h1>Hello {name}! You are from {location}</h1>"


@app.route('/theform', methods=['GET', 'POST'])
def theform():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        location = request.form['location']
        # return f"<h1>Hello {name}! You are from {location}</h1>"
        return redirect(url_for('home', name=name))


@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()
    name = data['name']
    location = data['location']
    randomList = data['randomList']
    return jsonify({'result': 'Success!', 'name': name, 'location': location, 'randomElement': randomList[1]})



if __name__ == "__main__":
    app.run()