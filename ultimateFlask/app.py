from flask import Flask, jsonify, request, url_for, redirect, session, render_template, g
import sqlite3


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'asldmfa4u@$#52342j421nk-21o31'


def connect_db():
    sql = sqlite3.connect('my.db')
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


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
    db = get_db()
    cursor = db.execute('select * from users')
    results = cursor.fetchall()
    return render_template('home.html', name=name, display=False, \
        myList=['one', 'two', 'three', 'four'], myDict=[{'name': 'Jowe'}, {'name': 'Jeremy'}],\
        results=results)


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

        db = get_db()
        db.execute('insert into users (name, location) values (?, ?)', [name, location])
        db.commit()

        # return f"<h1>Hello {name}! You are from {location}</h1>"
        return redirect(url_for('home', name=name))


@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()
    name = data['name']
    location = data['location']
    randomList = data['randomList']
    return jsonify({'result': 'Success!', 'name': name, 'location': location, 'randomElement': randomList[1]})


@app.route('/viewresults')
def viewresults():
    db = get_db()
    cursor = db.execute('select id, name, location from users')
    results = cursor.fetchall()
    return '<h1>The ID - {}, name: {}, location: {}</h1>'.format(results[0]['id'], results[0]['name'], results[0]['location'])



if __name__ == "__main__":
    app.run()