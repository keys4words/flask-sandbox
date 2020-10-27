from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        username = request.form['username']
        password = request.form['password']
        if username == 'Maxim' and password == 'test':
            message = 'Maxim logged in successfully'
        else:
            message = 'You need authorize before loggin'
        return render_template('index.html', message=message)

    # return app.root_path

@app.route('/football', methods=['GET'])
def football():
    return render_template('football.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run(port=5000, debug=True)
