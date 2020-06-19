from flask import Flask, url_for, request, send_file, redirect, abort

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def main_page():
    return 'Hey, Max!'

@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello, {name}"

@app.route('/catalog/<int:item_id>')
def catalog_item(item_id):
    return "Number in catalog: %d" % item_id

@app.route('/versions/<float:version>')
def versions(version):
    return "Version number: %f" % version

@app.route('/path1/')
def path1():
    return "This is path1"

@app.route('/path2')
def path2():
    return "This is path2"

@app.route('/url_for-test')
def url_for_test():
    return url_for('main_page')

@app.route('/login.html')
def send_login():
    return send_file('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return 'POST request with user = %s' % user
    else:
        user = request.args.get('name')
        return 'GET request with user = %s' % user


#redirect(location, statuscode, response)
@app.route('/redirect-to-login-page')
def redirected():
    return redirect(url_for('send_login'))

@app.route('/aborted-page')
def aborted_page():
    abort(401)
    this_is_never_executed()


@app.errorhandler(404)
def page_not_found(error):
    return "No such page!!!", 404

if __name__ == "__main__":
    with app.test_request_context():
        print(url_for('main_page'))
        print(url_for('path1'))
        print(url_for('path2'))
    app.run(port=8080)


#app.run(host, port, debug, options)