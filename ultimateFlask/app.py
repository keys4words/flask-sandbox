from flask import Flask, jsonify, request

app = Flask(__name__)

# @app.route('/', defaults={'name': 'John Dow'})
# @app.route('/<string:name>')
# def index(name):
#     return f'<h1>Hello, {name}</h1>'

@app.route('/')
def index():
    return '<h1>Index Page</h1>'


@app.route('/home', methods=['GET', 'POST'])
def home():
    return 'Home Page'

@app.route('/json')
def json():
    return jsonify({'key': 'value', 'key2': [213, 99, 9]})

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return f'<h1>Query Page for {name} with location in {location}</h1>'

@app.route('/theform')
def theform():
    return '''<form method="POST" action="/process">
                <input type="text" name="name">
                <input type="text" name="location">
                <input type="submit" value="Submit">
              </form>'''


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    return f"<h1>Hello {name}! You are from {location}</h1>"



if __name__ == "__main__":
    app.run(debug=True)